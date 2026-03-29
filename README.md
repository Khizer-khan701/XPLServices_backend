# XPLServices AI Agent 🤖

A robust, multi-model AI backend designed for **Sunmarke School**. This system leverages **RAG (Retrieval-Augmented Generation)** to provide accurate answers based on school-specific documentation, comparing responses from multiple state-of-the-art LLMs.

---

## 🌟 Key Features

- **Multi-Model Intelligence**: Simultaneously queries **GPT-4 (OpenAI)**, **Gemini 2.0 Flash (Google)**, and **Kimi (via OpenRouter)** for a comprehensive comparison.
- **RAG Architecture**: Uses **PGVector** and **PostgreSQL** to retrieve relevant context from school documents before generating answers.
- **Async Processing**: High-performance asynchronous execution using **FastAPI** to minimize response latency.
- **Modern Tech Stack**: Built with **LangChain**, **Pydantic**, and **Uvicorn**.
- **Deployment Ready**: Fully configured for seamless deployment on **Railway**.

---

## 🛠️ Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Orchestration**: [LangChain](https://www.langchain.com/)
- **Database**: PostgreSQL with [pgvector](https://github.com/pgvector/pgvector)
- **AI Models**:
  - OpenAI GPT-4
  - Google Gemini 2.0 Flash
  - Moonshot AI (Kimi K2.5) via OpenRouter
- **Embeddings**: OpenAI `text-embedding-ada-002`

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.10+
- PostgreSQL with Vector Extension
- API Keys for OpenAI, Google AI, OpenRouter, and ElevenLabs

### 2. Installation
```bash
# Clone the repository
git clone https://github.com/Khizer-khan701/XPLServices_backend
cd xpl-ai-agent-backend

# Create and activate virtual environment (Windows)
python -m venv env
.\env\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration
Create a `.env` file in the root directory:
```env
OPENAI_API_KEY=your_openai_key
GEMINI_API_KEY=your_gemini_key
OPENROUTER_API_KEY=your_openrouter_key
ELEVENLABS_API_KEY=your_elevenlabs_key
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
```

### 4. Running the App locally
```bash
uvicorn app.main:app --reload
```
The API will be available at `http://127.0.0.1:8000`.

---

## 🔌 API Documentation

### POST `/api/query/ask`
Queries the AI agent and returns context-aware answers from all three LLMs.

**Request Body:**
```json
{
  "question": "What are the school timings for Sunmarke School?"
}
```

**Response:**
```json
{
  "question": "What are the school timings for Sunmarke School?",
  "context": "...relevant document snippets found in the vector store...",
  "answers": {
    "gpt4o": "Response from GPT-4...",
    "kimi": "Response from Kimi...",
    "gemini": "Response from Gemini..."
  }
}
```

---

## 🚢 Deployment
This project is pre-configured for **Railway**. Refer to [DEPLOYMENT.md](./DEPLOYMENT.md) for detailed instructions.

---

## 📂 Project Structure
- `app/api`: API route definitions.
- `app/core`: Configuration and environment settings.
- `app/services`: Core logic for LLMs, RAG, STT, and TTS.
- `app/main.py`: Entry point of the application.
- `requirements.txt`: Project dependencies.
