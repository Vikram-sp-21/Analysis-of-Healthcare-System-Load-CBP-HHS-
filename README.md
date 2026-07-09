# 🏥 Analysis of Healthcare System Load (CBP & HHS)

An interactive healthcare analytics project that monitors healthcare system capacity using operational data from the **U.S. Customs and Border Protection (CBP)** and the **U.S. Department of Health and Human Services (HHS)**.

The project applies **Exploratory Data Analysis (EDA), Time-Series Analysis, Feature Engineering, and Interactive Dashboarding** to identify healthcare demand trends, capacity stress, and operational bottlenecks.

---

# 📌 Project Overview

Healthcare systems require continuous monitoring to ensure that patient demand is balanced with available healthcare resources.

This project develops a centralized analytical framework to monitor:

- Total Healthcare System Load
- Patient Inflow and Outflow
- Capacity Stress and Relief Periods
- Backlog Growth
- Operational Sustainability

An interactive **Streamlit Dashboard** provides policymakers and healthcare administrators with real-time insights for informed decision-making.

---

# 🎯 Objectives

## Primary Objectives

- Quantify daily and cumulative healthcare system load.
- Compare CBP custody and HHS care populations.
- Analyze patient intake, transfers, and discharges.
- Identify periods of capacity strain and relief.

## Secondary Objectives

- Support healthcare staffing and resource planning.
- Improve situational awareness.
- Enable data-driven humanitarian response evaluation.
- Develop an interactive dashboard for operational monitoring.

---

# 📂 Dataset

**Dataset Duration:** 2023 – 2025

### Key Features

- Date
- Children in CBP Custody
- Children in HHS Care
- Children Transferred Out of CBP Custody
- Children Discharged from HHS Care

---

# ⚙️ Methodology

## 1. Data Ingestion

- Load healthcare operational data
- Convert Date to datetime format
- Sort data chronologically
- Create complete daily index

---

## 2. Data Quality Validation

- Missing date detection
- Duplicate record detection
- Logical constraint validation
- Reporting anomaly detection

---

## 3. Feature Engineering

Derived healthcare metrics include:

- Total System Load
- Net Daily Intake
- Care Load Growth Rate
- Backlog Indicator
- 7-Day Rolling Average
- 14-Day Rolling Average
- Capacity Variability
- Prolonged Strain Indicator

---

## 4. Exploratory Data Analysis

Performed analyses include:

- Daily Trend Analysis
- Weekly Trend Analysis
- Monthly Trend Analysis
- Rolling Average Analysis
- Variability Analysis
- Capacity Stress Identification
- Backlog Trend Analysis

---

## 5. Dashboard Development

Developed an interactive Streamlit dashboard featuring:

- KPI Summary Cards
- System Load Overview
- CBP vs HHS Comparison
- Net Intake Trend
- Rolling Average Analysis
- Capacity Stress Monitoring
- Interactive Filtering
- Downloadable Reports

---

# 📊 Dashboard Features

✅ KPI Summary Cards

✅ System Load Overview

✅ CBP vs HHS Comparison

✅ Net Daily Intake Analysis

✅ Backlog Trend Analysis

✅ Rolling Average Visualization

✅ Pressure & Stress Detection

✅ Date Range Filter

✅ Daily / Weekly / Monthly Analysis

✅ Interactive Plotly Charts

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Plotly
- Streamlit
- Matplotlib

---

# 📁 Project Structure

```
Analysis-of-Healthcare-System-Load/
│
├── app.py
├── Healthcare_Pressure_Analysis.csv
├── requirements.txt
├── README.md
└── screenshots/
```

---

# 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/your-username/Analysis-of-Healthcare-System-Load.git
```

### Navigate to Project Folder

```bash
cd Analysis-of-Healthcare-System-Load
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Dashboard

```bash
streamlit run app.py
```

---

# 📈 Key Performance Indicators (KPIs)

- Total System Load
- Net Daily Intake
- Care Load Growth Rate
- Backlog Indicator
- 7-Day Rolling Average
- 14-Day Rolling Average
- Capacity Variability
- Prolonged Strain Windows

---

# 📊 Key Insights

- Identified daily, weekly, and monthly healthcare demand trends.
- Measured operational balance between CBP and HHS.
- Detected sustained high-load periods using rolling averages.
- Monitored backlog growth through Net Daily Intake.
- Highlighted prolonged capacity strain requiring operational attention.
- Enabled data-driven monitoring through an interactive dashboard.

---

# 💡 Recommendations

- Deploy centralized healthcare monitoring dashboards.
- Implement predictive analytics for healthcare demand forecasting.
- Introduce automated alerts for sustained capacity stress.
- Optimize staffing based on historical workload trends.
- Improve coordination between CBP and HHS through shared operational insights.

---

# 🔮 Future Enhancements

- Machine Learning-based Demand Forecasting
- Real-time API Integration
- Geographic Healthcare Mapping
- Automated Anomaly Detection
- Predictive Capacity Planning
- Interactive Report Generation

---

# 📸 Dashboard Preview

Add screenshots of your dashboard inside the **screenshots/** folder.

Example:

```markdown
![Dashboard](screenshots/dashboard.png)
```

---

# 📜 License

This project is intended for educational, research, and demonstration purposes.

---

# 👨‍💻 Author

**Vicky Chaudhary**

B.Tech – Artificial Intelligence & Machine Learning

Interested in:

- Data Analytics
- Machine Learning
- Artificial Intelligence
- Data Visualization
- Dashboard Development

---

# ⭐ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub.

Feedback and suggestions are always welcome.****
