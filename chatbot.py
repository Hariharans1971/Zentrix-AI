from groq import Groq
import streamlit as st

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Zentrix AI ⚡", page_icon="🤖", layout="wide")

# ---------------- CUSTOM UI ----------------
st.markdown("""
<style>
body {
    background-color: #0f172a;
    color: white;
}

h1 {
    font-size: 2.8rem;
    font-weight: 800;
    background: linear-gradient(90deg, #00DBDE, #FC00FF);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.stChatMessage {
    padding: 12px;
    border-radius: 14px;
    margin-bottom: 10px;
}

.stChatMessage.user {
    background-color: #1e293b;
}

.stChatMessage.assistant {
    background-color: #020617;
    border: 1px solid #334155;
}

section[data-testid="stSidebar"] {
    background-color: #020617;
}

button {
    border-radius: 10px !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------- API ----------------
groq_client = Groq(api_key=st.secrets["groq"]["api_key"])

# ---------------- HEADER ----------------
st.markdown("<h1 style='text-align:center;'>⚡ Zentrix AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#94a3b8;'>Fast AI powered by Groq 🚀</p>", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.markdown("## 🚀 Zentrix Control Panel")

temperature = st.sidebar.slider("Creativity", 0.0, 1.0, 0.7)

st.sidebar.markdown("---")

# ⚠️ BETTER: use local image file (rename to profile.jpg)
st.sidebar.image(r'C:\Users\harih\OneDrive\Pictures\Saved Pictures\WhatsApp Image 2025-04-29 at 23.17.13_a412dc2d.jpg', use_column_width=True)


st.sidebar.markdown("### 👨‍💻 Hariharan")
st.sidebar.write("AI Engineer")

st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/hari-haran-b5aa50272/)")
st.sidebar.markdown("[GitHub](https://github.com/hariharansuresh1971-dotcom)")

st.sidebar.markdown("---")

if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.messages = []

# ---------------- MEMORY ----------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are Zentrix AI, a powerful, smart, and helpful assistant. Give clear, structured answers."
        }
    ]

# ---------------- DISPLAY ----------------
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["content"])
    elif msg["role"] == "assistant":
        st.chat_message("assistant").markdown(msg["content"])

# ---------------- RESPONSE ----------------
def get_response():
    try:
        response = groq_client.chat.completions.create(
            messages=st.session_state.messages,
            model="llama-3.3-70b-versatile",
            temperature=temperature,
            stream=True
        )

        full = ""
        placeholder = st.empty()

        for chunk in response:
            if chunk.choices[0].delta.content:
                full += chunk.choices[0].delta.content
                placeholder.markdown(full + "▌")

        return full

    except Exception as e:
        return f"⚠️ Error: {e}"

# ---------------- INPUT ----------------
user_input = st.chat_input("Ask Zentrix AI anything...")

if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        with st.spinner("Zentrix thinking..."):
            reply = get_response()

    st.session_state.messages.append({"role": "assistant", "content": reply})

# ---------------- FOOTER ----------------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>⚡ Built by Hariharan</p>", unsafe_allow_html=True)