# 📧 AI Email Assistant

**AI Email Assistant** is a web application that leverages **OpenAI GPT-4o-mini** to generate professional emails instantly. With just a few inputs like recipient, purpose, and tone, the AI drafts clear, concise, and polished emails. Users can also download the generated email as a PDF.

---

## 🚀 Features

* Generate professional emails in different tones: **Formal, Casual, Persuasive, Friendly, Urgent**
* Customize emails with **additional instructions**
* **Download emails as PDF** for offline use or record-keeping
* Clean, modern **Streamlit UI** with cards and gradient design
* Automatic OpenAI API key integration from `.env` (no manual input required)

---

## 🛠 Tech Stack

* **Frontend & UI:** Streamlit
* **AI Backend:** OpenAI GPT-4o-mini
* **PDF Generation:** FPDF
* **Environment Variables:** python-dotenv

---

## ⚡ Getting Started

### Prerequisites

* Python 3.10+
* OpenAI API key

### Installation

1. Clone the repository:

```bash
git clone https://github.com/vwhoahh/Gen-AI.git
cd Gen-AI
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_openai_api_key_here
```

---

### Running the App

```bash
streamlit run app.py
```

Open your browser at [http://localhost:8501](http://localhost:8501).

---

## 👩‍💻 Usage

1. Enter **Recipient Name/Role**
2. Enter **Purpose / Context of Email**
3. Select a **Tone**
4. Add **Additional Instructions** (optional)
5. Click **Generate Email**
6. View the generated email and **download as PDF**

---

## 💡 Future Enhancements

* Generate multiple email variations at once
* Direct integration with Gmail or other email clients
* Smart suggestions for email subject lines
* Enhanced UI with themes and better visual cues

---

## 📜 License

MIT License – see the [LICENSE](LICENSE) file for details.

---
