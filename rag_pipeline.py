# ------------------ IMPORTS ------------------
from scraper import load_documents

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from groq import Groq
from deep_translator import GoogleTranslator

# ------------------ LOAD DATA ------------------
print("📥 Loading documents...")
docs = load_documents()

# ------------------ CHUNKING ------------------
print("✂️ Splitting documents...")
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = splitter.split_documents(docs)

print(f"📄 Total chunks created: {len(chunks)}")

# ------------------ EMBEDDINGS ------------------
print("🧠 Creating embeddings...")
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ------------------ VECTOR DATABASE ------------------
print("📦 Building FAISS index...")
db = FAISS.from_documents(chunks, embeddings)

print("✅ Vector DB ready!")

# ------------------ LLM SETUP ------------------
client = Groq(api_key="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")  # 🔑 PUT YOUR KEY HERE


def generate_answer(query, context):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",   # ✅ correct model
            messages=[
                {
                    "role": "system",
                    "content": "You are a Machine Learning expert. Answer clearly using the provided context."
                },
                {
                    "role": "user",
                    "content": f"Context:\n{context}\n\nQuestion:\n{query}"
                }
            ]
        )

        answer = response.choices[0].message.content

        if answer is None or answer.strip() == "":
            return "⚠️ No response generated from model"

        return answer

    except Exception as e:
        print("LLM ERROR:", e)
        return f"⚠️ LLM Error: {str(e)}"


# ------------------ TRANSLATION ------------------
def translate(text, target):
    try:
        if not text or text.strip() == "":
            return text

        # Normalize language codes
        lang_map = {
            "en": "en",
            "hi": "hi",
            "mr": "mr"
        }

        target_lang = lang_map.get(target, "en")

        # If already English and target is English
        if target_lang == "en":
            return text

        translated = GoogleTranslator(
            source='auto',
            target=target_lang
        ).translate(text)

        return translated if translated else text

    except Exception as e:
        print("Translation error:", e)
        return text


# ------------------ MAIN CHAT FUNCTION ------------------
def chatbot(query, lang="en"):
    try:
        print("\n--- DEBUG ---")
        print("Original Query:", query)
        print("Selected Language:", lang)

        # Step 1: Translate query to English (for LLM)
        if lang != "en":
            query_en = translate(query, "en")
        else:
            query_en = query

        print("Query used for LLM:", query_en)

        # Step 2: Retrieve context
        docs = db.similarity_search(query_en, k=3)
        context = " ".join([doc.page_content for doc in docs])

        if len(context.strip()) == 0:
            context = "General machine learning knowledge."

        print("Context length:", len(context))

        # Step 3: Generate answer (English)
        answer_en = generate_answer(query_en, context)
        print("LLM Answer (EN):", answer_en)

        # Step 4: ALWAYS translate to selected language
        final_answer = translate(answer_en, lang)

        print("Final Answer:", final_answer)
        print("--- END DEBUG ---\n")

        return final_answer

    except Exception as e:
        return f"⚠️ Error: {str(e)}"


# ------------------ TEST RUN ------------------
if __name__ == "__main__":
    print("\n🤖 Testing chatbot...\n")
    
    test_query = "What is machine learning?"
    response = chatbot(test_query, "en")
    
    print("Q:", test_query)
    print("A:", response)