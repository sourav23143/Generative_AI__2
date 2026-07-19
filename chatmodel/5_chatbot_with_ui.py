import streamlit as st
from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

st.set_page_config(page_title="Mood AI Chatbot", page_icon="🎭", layout="centered")

model = ChatMistralAI(model="mistral-small-2603", temperature=0.9)

MODES = {
    "Angry 😠": "You are an angry AI Agent. You respond aggressively and impatiently",
    "Sad 😢": "You are a sad AI Agent. You respond with empathy and understanding",
    "Funny 😂": "You are a funny AI Agent. You respond with humor and wit",
}

# initialize state
if "mode_selected" not in st.session_state:
    st.session_state.mode_selected = False
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🎭 Mood AI Chatbot")

# ---- Mode selection screen ----
if not st.session_state.mode_selected:
    st.subheader("Choose your AI mode:")
    choice = st.radio("Pick a personality:", list(MODES.keys()))

    if st.button("Start Chat", use_container_width=True):
        st.session_state.messages = [SystemMessage(content=MODES[choice])]
        st.session_state.mode_selected = True
        st.session_state.mode_label = choice
        st.rerun()

# ---- Chat screen ----
else:
    st.caption(f"Current mode: **{st.session_state.mode_label}**")

    for msg in st.session_state.messages:
        if isinstance(msg, HumanMessage):
            with st.chat_message("user"):
                st.write(msg.content)
        elif isinstance(msg, AIMessage):
            with st.chat_message("assistant"):
                st.write(msg.content)

    prompt = st.chat_input("You:")

    if prompt:
        st.session_state.messages.append(HumanMessage(content=prompt))
        with st.chat_message("user"):
            st.write(prompt)

        response = model.invoke(st.session_state.messages)
        st.session_state.messages.append(AIMessage(content=response.content))

        with st.chat_message("assistant"):
            st.write(response.content)

    if st.button("🔄 Restart / Change Mode"):
        st.session_state.mode_selected = False
        st.session_state.messages = []
        st.rerun()