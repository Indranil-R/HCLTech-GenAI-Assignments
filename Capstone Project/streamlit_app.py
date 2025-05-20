"""
Description
17. RAG-Based Research Paper Companion

Description:
Build a RAG pipeline-based AI agent that helps students or researchers understand and analyze research papers
(especially in AI/ML).

Key Features:

Accepts uploaded PDFs of research papers.
Extracts text and segments into logical sections: abstract, intro, methodology, etc.
Stores embeddings of each section in a vector store.
Users can ask questions like “What is the dataset used?”, “How does the proposed method improve over X?”, and get answers grounded in the paper.
Supports comparison with other papers by allowing multi-document RAG.
Use Case:
Speeds up research review, helps in writing literature surveys, and assists learners in grasping dense academic content.
"""
# from research_companion import get_assistant_response
import time
from research_companion import init_vector_store

# TBD Later
def sleep_for_10_seconds():
    time.sleep(10)

import streamlit as st


# Initialize vector store only once per session
@st.cache_resource
def get_vector_store():
    return init_vector_store()

# Set it in session state for easier access
if "vector_db" not in st.session_state:
    st.session_state.vector_db = get_vector_store()

# Sidebar for docs upload
st.sidebar.title("Welcome, Researcher!")
st.sidebar.divider()

st.sidebar.markdown("""
### How to Use the Research Companion

- Ask questions directly about research topics or concepts.
- To analyze a specific research paper, upload the PDF below.
- You can upload multiple papers for comparison or multi-document analysis.
""")


st.sidebar.divider()
st.sidebar.header("Upload PDFs")

uploaded_files = st.sidebar.file_uploader("📄 Upload Research Papers:", type=["pdf"], accept_multiple_files=True)


if uploaded_files:
    if st.sidebar.button("📎 Attach Papers for Analysis"):
        with st.sidebar:
            with st.spinner("Downloading data..."):
                st.write("Searching for data...")
                time.sleep(2)
                st.write("Found URL.")
                time.sleep(1)
                st.write("Downloading...")
                time.sleep(1)

            st.sidebar.success("Document loaded!")


# Main content
st.title("Research Companion")
st.caption("Research companion is a powerful AI based tool to help you quickly understand and analyze research papers. "
           "Provide you information based on some previous researches.")



if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = get_vector_store(query=prompt)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
