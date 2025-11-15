import streamlit as st
import requests
from typing import List

API_URL = "http://localhost:8000/summary/"

st.set_page_config(page_title="AI Text Summarizer", layout="centered")
st.title("AI-Powered Summary Assistant")
st.write("Paste the article text here.")

with st.form("summarize_form"):
    text_input = st.text_area("Input text", height=300)
    max_length = st.number_input("Maximum characters in summary", value=200, step=1)
    min_length = st.number_input("Minimum characters in summary", value=50, step=1)
    submit = st.form_submit_button("Summarize article")

if submit:
    if not text_input or text_input.strip() == "":
        st.warning("Please paste the article text to summarize")
    else:
        with st.spinner("Calling summarizer..."):
            try:
                resp = requests.post(API_URL, json={
                        "article": text_input,
                        "max_length": max_length,
                        "min_length": min_length
                    },
                timeout=60)
                resp.raise_for_status()
                data = resp.json()
                summary = data.get("summary", "")
                if not summary:
                    st.error("Response did not include a summary, please try again")
                else:
                    st.subheader("Summary")
                    st.write(summary)
                    st.download_button("Download summary (.txt)", summary, file_name="summary.txt")
                    st.success("Done")
            except Exception as e:
                st.error(f"Error calling backeng : {e}")