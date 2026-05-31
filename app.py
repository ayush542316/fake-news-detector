import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyAykHb9netjUH0MCyenfa50tCCgWoqyvNU")

st.set_page_config(page_title="Fake News Detector", page_icon="🔍", layout="centered")
st.title("🔍 Fake News Detector")
st.markdown("Paste any news headline or article — AI will analyze it instantly.")

def analyze_news(text):
    model = genai.GenerativeModel("gemini-flash-latest")
    prompt = f"""You are a fake news detection expert. Analyze the following news text and provide:

1. VERDICT: One of these exactly — REAL, FAKE, or UNCERTAIN
2. CONFIDENCE: A score out of 100
3. REASONS: 3-4 bullet points explaining why
4. VERIFY: 2-3 suggestions on how to verify this news

Use these exact headings:
## Verdict
## Confidence Score
## Reasons
## How to Verify

News text to analyze:
{text}"""
    response = model.generate_content(prompt)
    return response.text

news_text = st.text_area(
    "Paste news headline or article here",
    height=200,
    placeholder="e.g. Scientists discover that drinking coffee makes you live forever..."
)

if st.button("🔍 Analyze News", type="primary"):
    if len(news_text.strip()) < 10:
        st.error("Please enter some news text to analyze.")
    else:
        with st.spinner("AI is analyzing the news..."):
            result = analyze_news(news_text)
        st.markdown("---")
        st.markdown(result)

st.markdown("---")
st.caption("Built with Streamlit + Gemini API | Fake News Detector")
