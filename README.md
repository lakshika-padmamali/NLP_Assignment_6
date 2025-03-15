# NLP_Assignment_6

# 💬 AI Chatbot - Professional & Interactive

### **A Retrieval-Augmented Generation (RAG) Web Application for Personal Information Querying**

## 📚 Overview

This project implements a **Retrieval-Augmented Generation (RAG) AI Chatbot** that answers questions based on personal information sources. The chatbot extracts data from **documents, GitHub repositories, and structured data** and generates responses using **GPT-4 (for debugging) and Groq LLaMA3-70B (for final results & analysis).**

---

## 🎯 **Project Objectives**

- **Retrieve and process personal data** (LinkedIn, CV, GitHub, Facebook profile) 💒
- **Implement RAG-based retrieval** using FAISS for efficient search 🔍
- **Generate professional and structured chatbot responses** 🤖
- **Develop a user-friendly web interface with a professional UI** 🎨
- **Support multiple models (GPT-4 for testing, Groq LLaMA3-70B for final analysis)**

---

## 🏢 **Git Content**

```
📂 AI-Chatbot
📂 nlp_A6.ipynb               # Notebook
🏃 chatbot_results.json   # Pre-generated answers for the chatbot
📄 README.md              # Project Documentation
📒 requirements.txt       # Required Python packages              
🎨 chatbot_ui.py          # Streamlit-based frontend UI
```

---

## 🛀 **Setup & Installation**

### **🔧 1️⃣ Prerequisites**

- Python **3.10+**
- Install dependencies:

```bash
pip install -r requirements.txt
```

### **🚀 2️⃣ Running the Application**

#### **Start the Frontend (Streamlit)**

```bash
streamlit run chatbot_ui.py
```

Web UI will be available at: **[http://localhost:8501](http://localhost:8501)**

---

## 📊 **Retrieval & Response Process**

1️⃣ **Data Processing** 📂

- Loads **personal documents** (CV, LinkedIn, GitHub README, etc.).
- Splits text into **semantic chunks** using `RecursiveCharacterTextSplitter`.
- Converts text into **embeddings using OpenAI Embeddings**.
- Stores embeddings **efficiently in FAISS vector database**.

2️⃣ **Retrieval-Augmented Generation (RAG) Process** 🔎

- User enters a query in the chatbot UI.
- FAISS retrieves **relevant context from stored embeddings**.
- Context is **fed into GPT-4 or Groq LLaMA3-70B** for response generation.
- Chatbot displays **a professional, coherent answer with references**.

---

## 📅 **Example Questions Handled**

This chatbot can answer **10 key questions** related to personal and professional background:

✅ **Education & Experience**

- **What is your highest level of education?**
- **What major or field of study did you pursue during your education?**
- **How many years of work experience do you have?**
- **What type of work or industry have you been involved in?**

✅ **Professional & Research Interests**

- **Can you describe your current role or job responsibilities?**
- **What are your core beliefs regarding the role of technology in shaping society?**
- **How do you think cultural values should influence technological advancements?**

✅ **Master’s Studies & Challenges**

- **As a master’s student, what is the most challenging aspect of your studies so far?**
- **What specific research interests or academic goals do you hope to achieve during your time as a master’s student?**

---

## 🎨 **Web Application UI Features**

- **Modern & Professional Look** 🖥️
- **Responsive & user-friendly chat interface**
- **A video demonstrating the chatbot's output responses is included in the link: https://drive.google.com/drive/folders/1ssm8v9ykEBOUV3rvsFhudOFrkyYJ-Xum?usp=sharing
  

- 
![image](https://github.com/user-attachments/assets/27a4ae70-ce4b-403e-9680-b197dbcab124)

---

## 📊 **Performance Analysis & Model Comparison**

| Model                       | Accuracy | Response Quality    | Speed    | Context Retention |
| --------------------------- | -------- | ------------------- | -------- | ----------------- |
| **GPT-4** (Testing)         | Moderate | Less context-aware  | Slower   | Weak              |
| **Groq LLaMA3-70B** (Final) | High     | More accurate       | Fast     | Strong            |

**🛠️ Key Observations:**

- **GPT-4** does **not always provide accurate answers** for some questions and compaired to **Groq LLaMA3-70B** the responses are not context relavant.
- **Groq LLaMA3-70B** provides **faster, more accurate answers** while maintaining better context relations and provide more accurate answers according to the provided personal details.
- Results from both models can be seen in the `chatbot_results.json` file.

---


This project **successfully implements a powerful AI chatbot** that is **RAG-based, multi-model, and provides structured answers**. With a **modern UI , it is optimized for professional applications.

🚀 **Try it out and experience AI-powered personal insights!**

