import streamlit as st
from rag_pipeline import chatbot

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="ML Chatbot",
    page_icon="🤖",
    layout="centered"
)

# ------------------ CLEAN UI STYLE ------------------
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background-color: #0e1117;
}
</style>
""", unsafe_allow_html=True)

# ------------------ TITLE ------------------
st.title("🤖 Machine Learning Chatbot")
st.markdown("Ask your Machine Learning questions in any language!")

# ------------------ LANGUAGE DROPDOWN (FIXED) ------------------
lang_option = st.selectbox(
    "🌐 Select Language",
    ["English", "Hindi", "Marathi"]
)

# Language mapping
lang_map = {
    "English": "en",
    "Hindi": "hi",
    "Marathi": "mr"
}

language = lang_map[lang_option]

# ------------------ SESSION STATE ------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ------------------ DISPLAY CHAT HISTORY ------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ------------------ USER INPUT ------------------
user_input = st.chat_input("💬 Ask something about Machine Learning...")

if user_input:
    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("🤔 Thinking..."):
            response = chatbot(user_input, language)

        # Safety check
        if not response or response.strip() == "":
            response = "⚠️ No response generated. Please try again."

        st.markdown(response)

    # Save bot response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

# ------------------ CLEAR CHAT BUTTON ------------------
if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()