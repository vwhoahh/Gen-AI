import streamlit as st
from openai import OpenAI
from fpdf import FPDF
import os
from dotenv import load_dotenv

# -------------------------
# Load API key from .env
# -------------------------
load_dotenv()
if not (api_key := os.getenv("OPENAI_API_KEY")):
    st.error("OpenAI API key not found. Please set OPENAI_API_KEY in your .env file.")
    st.stop()

client = OpenAI(api_key=api_key)

# -------------------------
# Streamlit UI
# -------------------------
st.set_page_config(page_title="AI Email Assistant", page_icon="📧", layout="centered")
st.markdown(
    """
    <style>
        body {
            background: linear-gradient(120deg, #e3f0ff 0%, #f8fafc 100%);
        }
        .main-card {
            background: #fff;
            border-radius: 18px;
            box-shadow: 0 4px 24px rgba(99,102,241,0.07);
            padding: 32px 28px;
            margin-top: 24px;
        }
        .email-card {
            background: #f1f5ff;
            border-radius: 14px;
            box-shadow: 0 2px 8px rgba(99,102,241,0.08);
            padding: 24px 18px;
            margin-top: 18px;
            border: 1px solid #c7d2fe;
        }
        .stTextInput>div>div>input, .stTextArea textarea {
            font-size: 16px;
            background: transparent;
            border-radius: 8px;
            border: 1px solid #c7d2fe;
        }
        .stButton>button {
            font-size: 16px;
            border-radius: 8px;
            background: #2563eb;
            color: #fff;
            padding: 8px 18px;
            margin-top: 8px;
            border: none;
            box-shadow: 0 2px 8px rgba(99,102,241,0.08);
        }
        .stDownloadButton>button {
            background: #6366f1;
            color: #fff;
            border-radius: 8px;
            font-size: 15px;
            padding: 8px 18px;
            border: none;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="main-card">
    <h1 style='font-size:2.5rem; margin-bottom:0; color:#2563eb; font-weight:900;'>📧 AI Email Assistant</h1>
    <p style='font-size:1.25rem; color:#2563eb; margin-top:6px; font-weight:600;'>Generate professional emails instantly using AI.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# -------------------------
# User Inputs
# -------------------------
recipient = st.text_input("Recipient Name / Role")
purpose = st.text_area("Purpose / Context of Email", "Requesting a meeting regarding project updates")
tone = st.selectbox("Select Tone", ["Formal", "Casual", "Persuasive", "Friendly", "Urgent"])
extra_instructions = st.text_area("Additional Instructions (optional)")

generate_btn = st.button("Generate Email")

# -------------------------
# Email Generation
# -------------------------
if generate_btn:
    with st.spinner("🧠 AI is drafting your email..."):
        prompt = f"""
        You are a professional assistant. Draft a {tone.lower()} email.
        Recipient: {recipient}
        Purpose: {purpose}
        {extra_instructions if extra_instructions else ""}
        Make it concise, clear, and professional.
        """
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=300
            )
            email_text = response.choices[0].message.content

            st.markdown("<div class='email-card'>", unsafe_allow_html=True)
            st.subheader("✉️ Generated Email")
            st.text_area("Email", value=email_text, height=250)
            st.markdown("</div>", unsafe_allow_html=True)

            # -------------------------
            # PDF Download
            # -------------------------
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", "B", 16)
            pdf.cell(0, 10, "AI Generated Email", ln=True, align="C")
            pdf.ln(10)
            pdf.set_font("Arial", "", 12)
            pdf.multi_cell(0, 8, email_text)
            pdf_file = "ai_email.pdf"
            pdf.output(pdf_file)

            with open(pdf_file, "rb") as f:
                st.download_button(
                    label="📥 Download Email as PDF",
                    data=f,
                    file_name="ai_email.pdf",
                    mime="application/pdf"
                )

        except Exception as e:
            st.error(f"Error generating email: {e}")
