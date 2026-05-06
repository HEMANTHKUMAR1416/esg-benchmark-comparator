import os
import time
from datetime import datetime
from dotenv import load_dotenv

import chromadb
from sentence_transformers import SentenceTransformer

from groq import Groq

# Load env variables
load_dotenv()

# 🔑 Groq client
client_groq = Groq(api_key=os.getenv("GROQ_API_KEY"))

# 🧠 Load embedding model (once)
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# 📚 ChromaDB setup
chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection(name="esg_knowledge")


def generate_ai_response(company_data: dict):
    """
    Main function used by all routes
    """

    start_time = time.time()

    try:
        # 🧾 Extract input
        company_name = company_data.get("company_name", "")
        env = company_data.get("envScore", "")
        social = company_data.get("socialScore", "")
        gov = company_data.get("govScore", "")
        notes = company_data.get("notes", "")

        # 📄 Build company text
        company_text = f"""
        Company: {company_name}
        Environmental Score: {env}
        Social Score: {social}
        Governance Score: {gov}
        Notes: {notes}
        """

        # 🔍 STEP 1 — Convert to embedding
        query_embedding = embedding_model.encode(company_text).tolist()

        # 🔍 STEP 2 — Search ChromaDB
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=2
        )

        # 🧠 STEP 3 — Get context
        context_docs = results.get("documents", [[]])[0]
        context = " ".join(context_docs) if context_docs else ""

        # 🧠 STEP 4 — Build prompt (RAG)
        prompt = f"""
        You are an ESG analyst.

        Use this knowledge:
        {context}

        Analyze the following company:

        {company_text}

        Provide:
        - Summary
        - Key insights
        - Recommendations
        """

        # 🤖 STEP 5 — Call Groq
        response = client_groq.chat.completions.create(
            model="llama-3.1-8b-instant",  # ✅ updated working model
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        ai_output = response.choices[0].message.content

        end_time = time.time()

        return {
            "generated_at": datetime.utcnow().isoformat(),
            "result": ai_output,
            "is_fallback": False,
            "response_time": round(end_time - start_time, 2)
        }

    except Exception as e:
        print("🔥 GROQ ERROR:", str(e))

        end_time = time.time()

        # 🛟 Fallback response
        fallback_text = "AI service temporarily unavailable. Showing fallback response."

        return {
            "generated_at": datetime.utcnow().isoformat(),
            "result": fallback_text,
            "is_fallback": True,
            "response_time": round(end_time - start_time, 2)
        }