class Route:
    def __init__(self, name):
        self.name = name


def router(query):

    query = query.lower()

    faq_keywords = [
        "return",
        "refund",
        "track",
        "delivery",
        "payment",
        "cash",
        "exchange",
        "policy",
        "order",
        "defective"
    ]

    sql_keywords = [
        "shoe",
        "shoes",
        "nike",
        "puma",
        "adidas",
        "product",
        "price",
        "discount",
        "rating",
        "sale",
        "buy"
    ]

    chat_keywords = [
        "hello",
        "hi",
        "hey",
        "how are you",
        "who are you",
        "thank you",
        "thanks",
        "good morning",
        "good evening"
    ]

    if any(keyword in query for keyword in faq_keywords):
        return Route("faq")

    if any(keyword in query for keyword in sql_keywords):
        return Route("sql")

    if any(keyword in query for keyword in chat_keywords):
        return Route("chat")

    return None