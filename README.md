# 🛒 E-Commerce AI Chatbot

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![LangChain](https://img.shields.io/badge/LangChain-LLM-green)
![SQLite](https://img.shields.io/badge/SQLite-Database-orange)
![Gemini](https://img.shields.io/badge/Google-Gemini-red)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-success)

An AI-powered **E-Commerce Shopping Assistant** that helps users search, explore, and discover products from Flipkart through natural language conversations.

The system combines **Web Scraping**, **SQLite Database**, **LLM-powered Query Understanding**, and **Conversational AI** to provide an intelligent shopping experience.

---

# 📌 Project Overview

Traditional e-commerce platforms require users to manually browse thousands of products.

This project builds an intelligent chatbot that allows users to interact using natural language queries such as:

* "Show me laptops under ₹50,000"
* "Recommend the best gaming phone"
* "Find wireless headphones with good ratings"
* "Suggest budget smart TVs"

The chatbot understands user intent, retrieves relevant products from the database, and generates conversational responses.

---

## 🚀 Features

* AI-powered conversational shopping assistant
* Product search using natural language
* Web scraping of Flipkart product data
* SQLite-based product database
* Intelligent product recommendations
* Context-aware chatbot responses
* Fast product retrieval using SQL queries
* Scalable architecture for large product catalogs
* Modular code structure for future enhancements

---

## 🎯 Problem Statement

Customers often struggle to find relevant products due to:

* Large product catalogs
* Complex filtering options
* Time-consuming manual searches
* Difficulty comparing products

This system solves the problem by allowing users to search products using natural language and receive personalized recommendations.

Example:

> User: "Show me the best smartphones under ₹20,000"

The chatbot:

1. Understands the intent
2. Extracts product requirements
3. Queries the product database
4. Returns relevant products
5. Generates a conversational response

---

## 🏗 System Architecture

```text
                 Flipkart Website
                         │
                         ▼
                 Web Scraping Layer
                         │
                         ▼
                    CSV Dataset
                         │
                         ▼
               SQLite Product Database
                         │
                         ▼
                  LangChain Agent
                         │
          ┌──────────────┴──────────────┐
          ▼                             ▼
      Gemini LLM                  SQL Query Tool
          │                             │
          └──────────────┬──────────────┘
                         ▼
                 Chatbot Response
                         │
                         ▼
                    User Interface
```

---

## 📂 Project Workflow

### Step 1: Data Collection

Product information is scraped from Flipkart including:

* Product Name
* Price
* Rating
* Number of Reviews
* Product Description
* Product Link
* Category Information

The extracted data is stored in CSV format.

---

### Step 2: Database Creation

The scraped CSV data is loaded into SQLite.

The database stores structured product information for fast retrieval.

Example Table:

| Column              |
| ------------------- |
| product_name        |
| product_price       |
| product_rating      |
| product_reviews     |
| product_description |
| product_link        |

---

### Step 3: Natural Language Understanding

The chatbot receives user queries such as:

```text
Recommend a gaming laptop under ₹60,000
```

The LLM interprets:

* Product Type → Laptop
* Budget → ₹60,000
* Use Case → Gaming

---

### Step 4: SQL Query Generation

The chatbot converts user intent into SQL queries.

Example:

```sql
SELECT *
FROM product
WHERE price <= 60000
AND product_name LIKE '%gaming%'
```

---

### Step 5: Response Generation

The retrieved products are passed to the LLM, which generates a conversational response with recommendations and explanations.

---

## 📊 Dataset Description

The dataset is collected through web scraping from Flipkart product listings.

### 🔹 Features

| Feature             | Description       |
| ------------------- | ----------------- |
| product_name        | Name of product   |
| product_price       | Product price     |
| product_rating      | Customer rating   |
| product_reviews     | Number of reviews |
| product_description | Product details   |
| product_link        | Product URL       |
| category            | Product category  |

---

## 🤖 AI Components

### Large Language Model (LLM)

Used for:

* Understanding user intent
* Extracting product constraints
* Generating SQL queries
* Producing conversational responses

### LangChain

Used for:

* Agent orchestration
* Tool integration
* Database interaction
* Prompt management

### SQLite

Used for:

* Structured product storage
* Fast product retrieval
* Query execution

---

## 📈 Example User Queries

```text
Show me laptops under ₹50,000
```

```text
Suggest the best smartphones for photography
```

```text
Recommend gaming headphones
```

```text
Find Bluetooth speakers with ratings above 4 stars
```

```text
Show me budget smartwatches
```

---

## 📂 Project Structure

```text
Flipkart-Ecommerce-Chatbot/
│
├── data/
│   ├── flipkart_product_data.csv
│
├── web_scraping/
│   ├── flipkart_data_extraction.ipynb
│   ├── csv_to_sqlite.py
│
├── database/
│   ├── db.sqlite
│
├── chatbot/
│   ├── app.py
│   ├── prompts.py
│   ├── database_utils.py
│
├── requirements.txt
│
└── README.md
```

---

## Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/Flipkart-Ecommerce-Chatbot.git

cd Flipkart-Ecommerce-Chatbot
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key
```

---

### 5️⃣ Run Web Scraping

```bash
jupyter notebook
```

Open:

```text
flipkart_data_extraction.ipynb
```

---

### 6️⃣ Load Data into SQLite

```bash
python csv_to_sqlite.py
```

---

### 7️⃣ Run the Chatbot

```bash
streamlit run app.py
```

---

## 🛠 Tech Stack

### Programming

* Python

### Data Collection

* Selenium
* BeautifulSoup
* Requests

### Database

* SQLite

### AI & LLM

* Google Gemini
* LangChain

### Data Processing

* Pandas
* NumPy

### Frontend

* Streamlit

### Development

* Jupyter Notebook

---

## 💡 Key Learnings

* Building end-to-end Generative AI applications
* Web scraping real-world e-commerce data
* Database creation and management using SQLite
* Prompt engineering for conversational systems
* LangChain agent development
* LLM-powered SQL generation
* Conversational product recommendation systems
* Integration of AI with structured databases

---

## 🔮 Future Enhancements

* Real-time Flipkart data updates
* RAG-based product retrieval
* Product comparison feature
* Personalized recommendations
* User authentication
* Shopping cart integration
* Multi-language support
* Voice-enabled shopping assistant
* FastAPI backend deployment
* Cloud deployment on AWS/GCP/Azure

---

## 👨‍💻 Author

**Abhinay Angadi**

📧 Email: [angadiabhinay2001@gmail.com](mailto:angadiabhinay2001@gmail.com)

💼 LinkedIn: https://linkedin.com/in/abhinay-angadi-541004159

💻 GitHub: https://github.com/AngadiAbhinay01

---

## ⭐ If You Found This Project Helpful

If you found this project useful or learned something from it, please consider giving it a ⭐ on GitHub.

Your support helps improve the project and motivates future development.

---

**Built with Python, LangChain, Gemini, SQLite, and Streamlit to create an intelligent e-commerce shopping assistant.** 🚀🛒
