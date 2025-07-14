# ⚡ Smart Complaint Prioritizer (AI-Powered)

A mini AI assistant that classifies electricity-related complaints by urgency, type, and geo-location. Helps utility providers like power distribution companies route issues faster and smarter.

---

## 🎯 Features

- 🔥 **Urgency Detection** – Detects critical issues like sparks, fire, wire faults.
- 🏷️ **Issue Tagging** – Tags complaints as Billing, Voltage, Outage, etc.
- 📍 **Location Detection** – Extracts city areas or pincodes from text.
- 📊 **Dashboard Visualization** – View classified complaints in real-time.
- 💡 Ideal for power companies, customer support teams, or smart cities.

---

## 🧠 Tech Stack

- Python
- Streamlit
- NLP (regex + keyword rules)
- CSV test data

---

## 🚀 How to Run

1. Clone this repo
2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Mac/Linux
```
3. Install dependencies:
```bash
   pip install -r requirements.txt
```
4. Run the app:
```bash
    streamlit run app.py
```
Then open http://localhost:8501 in your browser.

---

## 📁 Folder Structure
``` bash
Smart_Complaint_Prioritizer/
├── app.py
├── logic/
│   ├── complaint_classifier.py
│   └── geo_clustering.py
├── ui/
│   └── complaint_ui.py
├── utils/
│   └── location_utils.py
├── data/
│   ├── sample_complaints.csv
│   └── sample_complaints_2.csv
├── assets/
│   └── style.css
├── requirements.txt
└── README.md
```

---

## ✅ Sample Use Case
Complaint:
"There is a fire on transformer pole in Varachha, sparks coming out!"
→ Urgency: Critical
→ Type: Hardware Fault
→ Location: Varachha

You can also try bulk classification using the preloaded complaint samples in the data/ folder:
- sample_complaints.csv
- sample_complaints_2.csv
These files include a variety of real-world complaint examples categorized by urgency, type, and location.

---

## 🧠 Tech Stack
- streamlit
- pandas

---

## 🎓 Skills Demonstrated
- Regex-based NLP – Extract urgency keywords, issue types, and locations from free-text complaints
- Streamlit Dashboard Design – Interactive UI for real-time complaint classification
- Modular Python Architecture – Clean separation into logic/, ui/, utils/, and data/
- Geo-location Handling – Basic extraction and grouping by locality/pincode
- CSV Data Handling – Read, filter, and classify bulk complaint data from .csv
- Rapid Prototyping – Fast deployment-ready solution ideal for smart city or utility demo apps
- Simulated Dataset Design – Synthetic but realistic test complaint samples for development

---

## 🔐 Disclaimer
This is a simulated demo with synthetic data for learning purposes. No real user data is used.

---
