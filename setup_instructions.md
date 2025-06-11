
---

## 📜 `setup_instructions.md`

```markdown
# 🌞 Local Setup Guide – Solar Industry AI Assistant

### 🧱 Prerequisites

- Python 3.8+
- pip (Python package manager)
- Internet connection (if using online models)

---

### 🔧 Installation

```bash
# Create a folder and move files into it
mkdir solar_ai_assistant && cd solar_ai_assistant

# Paste or clone project files

# Set up a virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate  # Windows

# Install all requirements
pip install -r requirements.txt

# Launch Streamlit app
streamlit run app.py
# If streamlit still isn’t recognized, try this:
python -m streamlit run app.py