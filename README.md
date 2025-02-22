# CURA.AI: AI-Powered Medical Assistant

**CURA.AI** is an AI-powered medical assistant designed to provide healthcare-related insights, including preliminary diagnoses, treatment recommendations, and access to medical research from **PubMed**. It integrates advanced AI models and tools to assist both patients and healthcare professionals.

## Features

1. **Medical Diagnosis & Treatment Recommendations**  
   - Combines patient symptoms and medical history to provide **preliminary diagnoses** and tailored **treatment plans** using AI agents.

2. **PubMed Research Query**  
   - Fetches and summarizes relevant **medical research articles** based on user queries.

3. **User Authentication**  
   - Secure **login/signup system** powered by **Firebase**, ensuring user data privacy.

4. **Document Parsing**  
   - Supports parsing of **medical documents (PDF, DOCX, etc.)** using **LlamaParse** for enhanced medical history analysis.

5. **Chat History & Downloadable Reports**  
   - Saves chat sessions and generates **downloadable diagnosis and treatment plans** in DOCX format.

## Tech Stack

### **AI Models**
- **OpenAI's GPT-4**
- **HuggingFace's Mixtral-8x7B**
- **Ollama's Mistral**
- Utilized for **natural language processing and medical insights**.

### **Frameworks & Libraries**
- **Streamlit**: Frontend framework for interactive UI.
- **LangChain**: AI pipeline orchestration.
- **Haystack**: Document processing.
- **CrewAI**: Multi-agent task management.

### **Database & Storage**
- **SQLite**: Chat history storage.
- **Firebase**: User authentication.

### **APIs & Tools**
- **PubMed API**: Fetches medical research data.
- **SerperDev API**: Enables web search for additional resources.
- **LlamaParse**: Parses and processes medical documents.

## Getting Started

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/CURA.AI.git
cd CURA.AI
```

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```
### **3. Run the Application**
```bash
streamlit run app.py
```
