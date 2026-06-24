from semantic_router import Route, RouteLayer
from semantic_router.encoders import HuggingFaceEncoder

encoder = HuggingFaceEncoder(
    name="sentence-transformers/all-MiniLM-L6-v2"
)

faq = Route(
    name='faq',
    utterances=[
        "What is the return policy of the products?",
        "Do I get discount with the HDFC credit card?",
        "How can I track my order?",
        "What payment methods are accepted?",
        "How long does it take to process a refund?",
        "What is your policy on defective products?",
        "Can I return a product?",
    ]
)

sql = Route(
    name='sql',
    utterances=[
        "I want to buy nike shoes that have 50% discount.",
        "Are there any shoes under Rs. 3000?",
        "Do you have formal shoes in size 9?",
        "Are there any Puma shoes on sale?",
        "What is the price of puma running shoes?",
        "Show me top rated shoes",
        "Show me shoes under 5000",
        "List Adidas shoes",
    ]
)

chat = Route(
    name='chat',
    utterances=[
        "Hello",
        "Hi",
        "Hey",
        "How are you?",
        "Who are you?",
        "What can you do?",
        "Good morning",
        "Good evening",
        "Thank you",
        "Thanks",
        "Nice to meet you"
    ]
)

router = RouteLayer(
    routes=[faq, sql, chat],
    encoder=encoder
)

if __name__ == "__main__":
    print(router("What is your policy on defective products?").name)
    print(router("Show me Puma shoes under 5000").name)
    print(router("How are you?").name)