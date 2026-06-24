
from groq import Groq
import os
import re
import sqlite3
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

GROQ_MODEL = os.getenv("GROQ_MODEL")

db_path = Path(__file__).parent / "db.sqlite"

client_sql = Groq(api_key=os.getenv("GROQ_API_KEY"))

sql_prompt = """
You are an expert in understanding the database schema and generating SQL queries for a natural language question asked
pertaining to the data you have. The schema is provided in the schema tags.

<schema>

table: product

fields:
product_link - string (hyperlink to product)
title - string (name of the product)
brand - string (brand of the product)
price - integer (price of the product in Indian Rupees)
discount - float (discount on the product. 10 percent discount is represented as 0.1, 20 percent as 0.2, and such.)
avg_rating - float (average rating of the product. Range 0-5, 5 is the highest.)
total_ratings - integer (total number of ratings for the product)

</schema>

Make sure whenever you try to search for the brand name, the name can be in any case.
So, make sure to use LIKE and LOWER() for brand matching.
Never use ILIKE.

Create a single SQL query for the question provided.

The query should:
1. Always use SELECT *
2. Include LIMIT 10 unless the user explicitly asks for more results.

Just the SQL query is needed, nothing more.

Always provide the SQL in between the <SQL></SQL> tags.
"""

comprehension_prompt = """
You are an expert in understanding the context of the question and replying based on the data provided.

You will be given:

QUESTION:
A user question.

DATA:
The result obtained from the database.

Rules:

1. Use ONLY the provided data.
2. Do not hallucinate.
3. Do not say "Based on the data".
4. If data is empty, say:
   "No matching products were found."

When products are present, return them in the format:

1. Product Title
   Price: Rs. XXXX
   Discount: XX%
   Rating: X.X
   Link: URL

One product per line.
"""


def generate_sql_query(question):
    chat_completion = client_sql.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": sql_prompt,
            },
            {
                "role": "user",
                "content": question,
            }
        ],
        model=GROQ_MODEL,
        temperature=0.2,
        max_tokens=512
    )

    return chat_completion.choices[0].message.content


def run_query(query):
    """
    Execute SQL query and return a DataFrame.
    """

    if not query.strip().upper().startswith("SELECT"):
        return None

    with sqlite3.connect(db_path) as conn:
        df = pd.read_sql_query(query, conn)

    return df


def data_comprehension(question, context):
    """
    Convert structured SQL output into a user-friendly response.
    """

    chat_completion = client_sql.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": comprehension_prompt,
            },
            {
                "role": "user",
                "content": f"QUESTION: {question}\n\nDATA: {context}",
            }
        ],
        model=GROQ_MODEL,
        temperature=0.2,
        max_tokens=1000
    )

    return chat_completion.choices[0].message.content


def sql_chain(question):

    sql_response = generate_sql_query(question)

    pattern = r"<SQL>(.*?)</SQL>"
    matches = re.findall(pattern, sql_response, re.DOTALL)

    if len(matches) == 0:
        return "Sorry, the system could not generate a SQL query."

    generated_query = matches[0].strip()

    print("\nGenerated SQL:")
    print(generated_query)

    response = run_query(generated_query)

    if response is None:
        return "Sorry, there was a problem executing the SQL query."

    if response.empty:
        return "No matching products were found."

    # IMPORTANT FIX:
    # Limit rows before sending to Groq
    response = response.head(5)

    context = response.to_dict(orient="records")

    print("\nRows sent to LLM:", len(context))

    answer = data_comprehension(question, context)

    return answer


if __name__ == "__main__":

    question = "Show top 3 shoes in descending order of rating"

    answer = sql_chain(question)

    print("\nAnswer:")
    print(answer)
