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

## Screenshots

![Screenshot 2024-07-20 073528](https://github.com/user-attachments/assets/862c890f-ba30-4905-901f-31d56f24e00a)
![Screenshot 2024-07-20 100217](https://github.com/user-attachments/assets/a8bf7e5b-9f46-495f-9b19-250bc28b760a)
![Screenshot 2024-07-20 100352](https://github.com/user-attachments/assets/91e88911-150b-4edb-962e-6c510059a760)
![Screenshot 2024-07-20 100402](https://github.com/user-attachments/assets/71ffa0ae-0a11-425c-89db-dc5f4b83265b)

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
