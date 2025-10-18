import streamlit as st
import pandas as pd
import os
from your_agent_module import (
    LLMClient,
    DataAnalysisAgent,
    preprocess_and_save_local
)

st.set_page_config(page_title="AI Data Analysis Agent", page_icon="📊", layout="wide")
st.title("📊 AI Data Analysis Agent — Portfolio Demo")

# API Key Input (optional — will fall back to MOCK mode)
api_key = st.text_input("🔑 OpenAI API Key (optional, for real LLM responses)", type="password")

# File Upload
uploaded = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])
if uploaded:
    with open("uploaded_temp.csv", "wb") as f:
        f.write(uploaded.getbuffer())
    temp_path, cols, df = preprocess_and_save_local("uploaded_temp.csv")
    st.write("✅ Data Loaded:")
    st.dataframe(df)

    llm = LLMClient(api_key=api_key)  # falls back to mock if no key provided
    agent = DataAnalysisAgent(llm=llm, verbose=False)
    agent.register_table_from_csv(temp_path, table_name="uploaded_data")

    query = st.text_area("Ask a natural language question about your data:")

    if st.button("Run Query") and query.strip():
        with st.spinner("Analyzing..."):
            resp = agent.ask(query)
            if "result" in resp:
                st.success("✅ Query Success")
                st.code(resp["sql"], language="sql")
                st.dataframe(resp["result"])
            else:
                st.error(f"❌ Error: {resp.get('error', 'Unknown error')}")
