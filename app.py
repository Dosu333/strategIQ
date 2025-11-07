import streamlit as st
from agents.orchestrator import get_response


st.set_page_config(
    page_title="StrategIQ | Multi-Agent Chat",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 StrategIQ: Where Ideas meet Imagination")
st.caption("Powered by Google Gemini + Custom AI Agents")

# --- Initialize session state ---
if "messages" not in st.session_state:
    st.session_state.messages = []


# --- Chat display ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- User input ---
user_input = st.chat_input("Type your question or idea...")
if user_input:
    # Display user message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("🤔 Thinking..."):
        try:
            # Call Gemini orchestrator
            response = get_response(user_input)

            # Display response
            if response:
                st.chat_message("assistant").markdown(response)
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response
                })
            else:
                st.chat_message("assistant").markdown(
                    "_No response generated._")

        except Exception as e:
            st.error(f"⚠️ Error: {e}")
