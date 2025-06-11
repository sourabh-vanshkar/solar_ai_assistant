# 🌞 Solar Industry AI Assistant

An AI-powered rooftop analysis tool to assess solar potential using satellite images.

## 🚀 Features

- Upload rooftop image
- AI-based analysis of usable rooftop area
- Estimate daily/yearly solar output
- Calculate installation cost, ROI, and payback
- Generate a downloadable report

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **AI Support**: Simulated logic (can be extended with Vision AI)
- **Report**: LLM-style summary (mocked)

---

## 🧩 Project Structure

solar_ai_assistant/
│
├── app.py # Streamlit app
├── analysis.py # Rooftop image area estimation
├── cost_estimator.py # Output, cost, ROI estimation
├── llm_report.py # Report generator
├── requirements.txt # Python dependencies
├── README.md # This file
└── setup_instructions.md # Step-by-step local setup



## 🔬 Future Improvements

- Integrate real Vision AI model (Hugging Face or SAM)
- Use OpenRouter or OpenAI LLM for report generation
- Add geo-location based sunlight data
- Include subsidy calculator and region-specific policies

## 📷 Example Use Case
    Upload a rooftop satellite image from Google Earth, and instantly receive:

- Usable solar panel area
- Cost & savings estimate
- Professional-style report

---

## 🖼️ Upload Example
    Use a rooftop image (satellite view). The app will:
    
- Analyze usable area
- Suggest energy output
- Estimate ROI
- Generate report

## 🛠️ Troubleshooting

- Make sure your image is in .jpg, .jpeg, or .png format.
- Run pip install --upgrade streamlit if you encounter compatibility errors.



---

## 🔧 Local Setup Instructions

```bash
# Clone the repo or unzip the folder
cd solar_ai_assistant

# Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py

# If streamlit still isn’t recognized, try this:
python -m streamlit run app.py

---
