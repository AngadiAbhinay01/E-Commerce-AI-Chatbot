import streamlit as st
from pathlib import Path

from faq import ingest_faq_data, faq_chain
from sql import sql_chain
from router import router

faqs_path = Path(__file__).parent / "resources" / "faq_data.csv"

try:
    ingest_faq_data(faqs_path)
except Exception as e:
    print("FAQ Ingestion Error:", e)


def ask(query):

    try:

        route_obj = router(query)

        if route_obj is None:
            return (
                "I can help you with product searches, pricing, discounts, "
                "orders, returns, refunds, and payment-related questions."
            )

        route = route_obj.name

        print(f"Detected Route: {route}")

        if route == "faq":
            return faq_chain(query)

        elif route == "sql":
            return sql_chain(query)

        elif route == "chat":
            return (
                "Hello! 👋 I am your E-commerce Assistant. "
                "I can help you find products, compare prices, "
                "check discounts, and answer store-related FAQs."
            )

        return (
            "I can help with product searches and e-commerce FAQs."
        )

    except Exception as e:
        print("Routing Error:", e)
        return (
            "Sorry, I encountered an error while processing your request."
        )


st.title("🛒 E-commerce Bot")

query = st.chat_input("Write your query")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if query:

    with st.chat_message("user"):
        st.markdown(query)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    response = ask(query)

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )