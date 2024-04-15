# streamlit 1.24.0 and up
import streamlit as st 


st.title("Streamlit Chatbot App")
# Create a Storage for Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat history
# st.write(st.session_state.messages)
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])



prompt = st.chat_input("Ask Something")
if prompt:

    # Add the user prompt to the chat history
    st.session_state.messages.append({"role":"user","content": prompt})
    # Display the message
    with st.chat_message("user"):
        st.write(prompt)
    
    st.session_state.messages.append({"role":"assistant","content": prompt})
    with st.chat_message("assistant"):
        st.write(prompt)

    # custom
    with st.chat_message("bot",avatar="😃"):
        st.write(prompt)
