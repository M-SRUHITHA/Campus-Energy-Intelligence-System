# 🌱 EcoVerse – Campus Energy Intelligence System

## 1. Project Overview

EcoVerse is a smart campus energy monitoring system designed to monitor electricity consumption and classroom occupancy across different areas of a college campus.

The system identifies unnecessary electricity usage when classrooms are empty but electrical appliances such as fans and lights remain switched on.

It provides a centralized dashboard to visualize energy consumption, monitor occupancy, and generate energy-wastage alerts.

## 2. Problem Statement

Educational institutions often experience unnecessary electricity consumption because fans and lights remain switched on even when classrooms are unoccupied.

This leads to:
- Increased electricity bills.
- Energy wastage.
- Unnecessary carbon emissions.
- Difficulty monitoring electricity usage across multiple classrooms.

## 3. Project Objectives

- Monitor classroom-wise electricity consumption.
- Display student occupancy in each classroom.
- Identify possible energy wastage.
- Generate alerts when empty classrooms consume electricity.
- Visualize energy consumption through charts and graphs.
- Support energy-efficient campus management.

## 4. Key Features

### 📊 Interactive Dashboard
Displays campus energy information in a centralized Streamlit dashboard.

### 🏫 Classroom-wise Monitoring
Displays occupancy, active fans, and active lights for individual classrooms.

### ⚡ Energy Consumption Analysis
Provides bar charts and line graphs to analyze electricity usage.

### 👨‍🎓 Occupancy Monitoring
Displays student occupancy information for different classrooms.

### 🚨 Energy Wastage Detection
Identifies situations where classroom occupancy is zero but electricity consumption is greater than zero.

### 🔔 Alert Notifications
Generates alerts showing the affected classroom, active appliances, and power consumption.

### 🌍 Energy and Environmental Awareness
Helps institutions understand energy wastage and encourages responsible electricity usage.

## 5. Technologies Used

- Python
- Streamlit
- Pandas
- Plotly
- CSV for sample classroom data
- Git and GitHub for version control

## 6. Project Structure

```text
Campus-Energy-Intelligence-System/
│
├── data/
│   └── classroom_data.csv
│
├── models/
│
├── utils/
│   ├── data_processing.py
│   ├── ai_detection.py
│   ├── alerts.py
│   └── visualizations.py
│
├── app.py
├── requirements.txt
└── README.md
```

## 7. How the System Works

1. Classroom readings are stored in a CSV file.
2. The system loads and cleans the classroom data.
3. Energy consumption is calculated using power readings and the 15-minute sampling interval.
4. Classroom occupancy is analyzed.
5. Energy-wastage detection checks whether an empty classroom is still consuming electricity.
6. Alerts are generated for detected wastage.
7. Streamlit displays the results through an interactive dashboard.

## 8. Energy Wastage Detection Logic

The current prototype uses rule-based detection.

**Condition:**

- Classroom occupancy = 0
- Power consumption > 0

When both conditions are satisfied, the system generates an energy-wastage alert.

## 9. Installation and Setup

### Prerequisites
- Python 3.10 or later
- Git

### Step 1: Clone the repository

```bash
git clone https://github.com/M-SRUHITHA/Campus-Energy-Intelligence-System.git
```

### Step 2: Navigate to the project folder

```bash
cd Campus-Energy-Intelligence-System
```

### Step 3: Create a virtual environment

```bash
python -m venv venv
```

### Step 4: Activate the virtual environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 5: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Run the application

```bash
python -m streamlit run app.py
```

The dashboard will open in your web browser.

## 10. Expected Outcomes

- Better visibility into classroom electricity usage.
- Identification of unnecessary electricity consumption.
- Improved awareness of energy-saving opportunities.
- Easier monitoring of classroom occupancy.
- Support for sustainable campus energy management.

## 11. Future Enhancements

- Computer vision-based automatic student occupancy detection.
- IoT-based real-time electricity monitoring.
- Automatic fan and light control.
- CO₂ emission estimation and environmental impact reporting.
- Mobile notifications for energy-wastage alerts.
- Machine-learning-based energy consumption prediction.

## 12. Team Information

**Team Name:** EcoVerse

**Project Title:** Campus Energy Intelligence System

**Project Domain:** Smart Campus / Sustainable Energy Management

---

**EcoVerse – Smart Monitoring for a Greener Campus! 🌱**