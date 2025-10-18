# 📊 AI Data Analysis Agent (LLM + DuckDB + Pandas)

An intelligent data analysis agent that lets you **ask natural language questions about your data** — powered by **LLMs + DuckDB + Pandas**. Demoed in either **Jupyter Notebook** or **Streamlit UI**.

---

## 🚀 What This Agent Can Do

✅ Upload any CSV/XLSX file  
✅ Convert your question → SQL via LLM  
✅ Execute instantly on DuckDB + Pandas  
✅ Return clean, tabular answers  
✅ Fully local-compatible (mock LLM mode available)

---

## 🛠️ Run Options (Choose One)

### ✅ Option 1 — Jupyter Notebook (best for walkthrough/demo + hiring managers)

```
jupyter notebook
```

Then open the prebuilt notebook included in this repo

The notebook includes:
- Code + narrative explanation
- Preprocessing
- Full agent class
- Example query run


### ✅ Option 2 — Run as a Streamlit Web App (Interactive UI)

If you prefer a **live interactive experience** instead of running code manually, launch the Streamlit app:

```
pip install streamlit pandas duckdb openai python-dotenv
streamlit run streamlit_app.py
```

This opens a **clean web interface** in your browser where you can:

- Upload a **CSV or Excel** file  
- Ask a **natural language question** (e.g. *"show total revenue by country"*)  
- Instantly see:  
  ✅ The **generated SQL**  
  ✅ The **final answer as a table**  

> **No API key required for mock/demo mode** — it works offline too.


