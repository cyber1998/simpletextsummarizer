# 📝 AI-Powered Note & Article Summarizer

A lightweight, fast, and privacy-friendly text summarization tool built with **FastAPI**, **Python**, and a **local HuggingFace BART-CNN model**.  
Paste long notes, articles, or documents and generate concise summaries in seconds.

This project is designed as a starter for building modern AI-assisted tools — fully local, reproducible, and easy to extend.

---

## 🚀 Features

- **Local inference** using `facebook/bart-large-cnn`
- **FastAPI backend** with a single clean `/summary` endpoint
- **Frontend** using Streamlit UI - simple, clean and quick
- **Handles long text** with automatic preprocessing
- **Simple, readable code structure**
- **No third-party API keys required**

---

## 📦 Tech Stack

### Backend
- Python 3.10+
- FastAPI
- HuggingFace Transformers
- PyTorch
- Uvicorn

### Frontend
- Streamlit

---

## 🧠 Model

This project uses the **BART Large CNN** summarization model:

- **Model:** `facebook/bart-large-cnn`
- **Type:** Abstractive summarizer
- **Strengths:** News articles, long-form text, clean grammar
- **Runs locally:** No API calls

Easy to swap in another model (T5, Pegasus, LED, LongT5, etc.) by editing the backend initializer.

## Run Locally

- Clone the Repository
- Install Dependencies using `pipenv install --python 3.13`
- Activate the virtual environment with `pipenv shell`
- Create a `.env` file in the root directory and set the `API_URL` variable:
  ```
  API_URL=http://localhost:8000/summary
  ```
- Start the FastAPI backend: `fastapi dev main.py --host=localhost --port=8000`
- In another terminal, start the Streamlit frontend: `streamlit run app.py`
- Open your browser to `http://localhost:8501` to access the app

---

