# import streamlit as st
# from rag_with_palm import RAGPaLMQuery
#
# # Instantiate the class
# rag_palm_query_instance = RAGPaLMQuery()
#
#
#
# st.title(f"**READIFY Assistant** :panda_face:")  # Add emojis and colors to the title
# # Initialize chat history
#
#
# if "messages" not in st.session_state:
#     st.session_state.messages = []
#
# # Display chat messages from history on app rerun
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])
#
# # React to user input
# if prompt := st.chat_input("Need info? Drop your question here!"):
#     # Display user message in chat message container
#     st.chat_message("user").markdown(prompt)
#     # Add user message to chat history
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     response = rag_palm_query_instance.query_response(prompt)
#     # Display assistant response in chat message container
#     with st.chat_message("assistant"):
#         st.markdown(response)
#     # Add assistant response to chat history
#     st.session_state.messages.append({"role": "assistant", "content": response})


import streamlit as st
from rag_with_palm import RAGPaLMQuery
st.set_page_config(page_title="Online retail fashion", page_icon="", layout="wide", initial_sidebar_state="expanded")

#st.session_state.messages = []


# Instantiate the class
rag_palm_query_instance = RAGPaLMQuery()

# Check if 'key' already exists in session_state
# If not, then initialize it
if 'key' not in st.session_state:
    st.session_state.key = 'value'

# # Session State also supports the attribute-based syntax
# if 'key' not in st.session_state:
#     st.session_state.key = 'value'

st.title(f"Dear Customer Welcome to our fashion store")  # Add emojis and colors to the title


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
prompt = st.chat_input("Ask me any questions?")
if prompt:
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    response = rag_palm_query_instance.query_response(prompt)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
