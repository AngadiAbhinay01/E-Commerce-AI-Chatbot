import os
from pathlib import Path

import chromadb
from chromadb.utils import embedding_functions
from groq import Groq
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL")

if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY not found. Check your .env file or Streamlit secrets."
    )

groq_client = Groq(
    api_key=GROQ_API_KEY
)

faqs_path = Path(__file__).parent / "resources" / "faq_data.csv"

ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

chroma_client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection_name_faq = "faqs"


def ingest_faq_data(path):

    existing_collections = [
        c.name for c in chroma_client.list_collections()
    ]

    if collection_name_faq not in existing_collections:

        print("Ingesting FAQ data into ChromaDB...")

        collection = chroma_client.create_collection(
            name=collection_name_faq,
            embedding_function=ef
        )

        df = pd.read_csv(path)

        docs = df["question"].tolist()

        metadata = [
            {"answer": ans}
            for ans in df["answer"].tolist()
        ]

        ids = [
            f"id_{i}"
            for i in range(len(docs))
        ]

        collection.add(
            documents=docs,
            metadatas=metadata,
            ids=ids
        )

        print(
            f"FAQ Data successfully ingested into collection: "
            f"{collection_name_faq}"
        )

    else:
        print(
            f"Collection '{collection_name_faq}' already exists"
        )


def get_relevant_qa(query):

    collection = chroma_client.get_collection(
        name=collection_name_faq,
        embedding_function=ef
    )

    result = collection.query(
        query_texts=[query],
        n_results=2
    )

    return result


def generate_answer(query, context):

    prompt = f"""
Given the following context and question, generate an answer based only on the context.

If the answer is not found in the context, reply exactly:

I don't know

CONTEXT:
{context}

QUESTION:
{query}
"""

    completion = groq_client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return completion.choices[0].message.content


def faq_chain(query):

    result = get_relevant_qa(query)

    context = "\n".join(
        item.get("answer", "")
        for item in result["metadatas"][0]
    )

    answer = generate_answer(query, context)

    return answer


if __name__ == "__main__":

    ingest_faq_data(faqs_path)

    query = "Do you take cash as a payment option?"

    answer = faq_chain(query)

    print(answer)