# 🌍 SeismoGuard AI

### Intelligent Earthquake Prediction and Emergency Response System

An Artificial Intelligence and Machine Learning based disaster management platform designed to predict earthquake magnitude, assess risk levels, generate emergency response plans, allocate shelters using Constraint Satisfaction Problems (CSP), and visualize AI decision-making through State Space Search.

---

## 🚀 Project Overview

SeismoGuard AI is an intelligent disaster management system that combines Machine Learning and Artificial Intelligence techniques to support emergency response during earthquake events.

The system predicts earthquake magnitude using historical seismic data and automatically triggers an AI-driven decision engine that:

* Evaluates disaster severity
* Classifies risk levels
* Allocates emergency shelters
* Generates response strategies
* Visualizes state-space search
* Reaches the goal state of population safety

---

## 🎯 Project Objectives

* Predict earthquake magnitude using Machine Learning.
* Detect earthquake hotspot regions using clustering.
* Design an intelligent disaster-management agent.
* Implement Knowledge-Based Reasoning.
* Apply State Space Representation.
* Implement Search-Based Planning.
* Solve shelter allocation using CSP.
* Provide emergency response recommendations.
* Visualize AI decision-making interactively.

---

# 🧠 Artificial Intelligence Components

## 1. PEAS Formulation

### Performance Measure

* Accurate magnitude prediction
* Efficient emergency planning
* Population safety

### Environment

* Earthquake-prone regions
* Disaster management scenarios

### Actuators

* Public alerts
* Shelter allocation
* Emergency recommendations

### Sensors

* Earthquake dataset features
* Predicted magnitude
* Risk level
* Tsunami status

---

## 2. Knowledge Base

The system contains expert disaster-management rules.

### Risk Categories

* MODERATE_RISK
* HIGH_RISK
* EXTREME_RISK
* TSUNAMI_RISK

The Knowledge Base evaluates earthquake conditions and triggers the appropriate emergency strategy.

---

## 3. Inference Engine

The Inference Engine:

* Evaluates rules
* Selects risk category
* Chooses emergency strategy
* Triggers AI planning pipeline

---

## 4. State Space Representation

The emergency management process is represented as a graph of states.

### States

* Earthquake Detected
* Assess Magnitude
* Send Public Alert
* Open Emergency Shelters
* Allocate Best Shelter
* Monitor Region
* Evacuate Population
* Deploy Drones
* Damage Assessment
* Medical Response
* Tsunami Warning
* Coastal Evacuation
* Population Safe

---

## 5. Search Agent

The AI agent searches the state space and highlights the optimal emergency response path.

### Search Technique

* Breadth First Search (BFS)

---

## 6. Constraint Satisfaction Problem (CSP)

Shelter allocation is modeled as a CSP.

### Constraints

* Shelter Capacity
* Medical Support
* Road Accessibility
* Population Size

### Output

Best available shelter for evacuation.

---

# 🤖 Machine Learning Components

## Dataset

Earthquake Dataset

### Target Variable

```text
Magnitude
```

### Features

```text
cdi
mmi
tsunami
sig
nst
dmin
gap
depth
latitude
longitude
```

---

## Data Preprocessing

✔ Missing Value Handling

✔ Duplicate Removal

✔ Feature Selection

✔ Data Cleaning

✔ Feature Scaling

---

## Machine Learning Models

### Linear Regression

Baseline regression model.

### Decision Tree Regressor

Non-linear prediction model.

### Random Forest Regressor

Final deployed model.

---

## Model Evaluation Metrics

* MAE
* MSE
* RMSE
* R² Score

---

## Explainable AI

Feature importance analysis is performed using Random Forest.

This helps identify the most influential earthquake indicators.

---

## Clustering

### K-Means Clustering

Used for:

* Earthquake hotspot detection
* Regional seismic analysis

---

# 🖥️ Dashboard Features

## 🏠 Home Page

Project overview and system introduction.

---

## 📈 Magnitude Prediction

Predict earthquake magnitude using trained Random Forest model.

---

## ⚠️ Risk Assessment

Generate earthquake risk scores based on important features.

---

## 🗺️ Earthquake Hotspot Map

Interactive Folium map displaying earthquake clusters.

---

## 🤖 AI Decision Center

Core AI module containing:

* Knowledge Base
* Inference Engine
* State Space Search
* CSP Shelter Allocation
* Goal State Planning

---

## 📢 Emergency Alert System

Automatically generates disaster alerts and can dispatch notifications through WhatsApp integration.

---

# 🏗️ System Architecture

```text
Earthquake Data
        │
        ▼
Machine Learning Model
(Random Forest)
        │
        ▼
Magnitude Prediction
        │
        ▼
Knowledge Base
        │
        ▼
Inference Engine
        │
        ▼
Risk Classification
        │
        ▼
State Space Search
        │
        ▼
CSP Shelter Allocation
        │
        ▼
Emergency Response Plan
        │
        ▼
Population Safe
```

---

# 🛠️ Technologies Used

## Frontend

* Streamlit

## Machine Learning

* Scikit-Learn
* Pandas
* NumPy

## Visualization

* Plotly
* Matplotlib
* Seaborn

## Mapping

* Folium
* Streamlit-Folium

## AI Graph Visualization

* Streamlit-Agraph

## Model Persistence

* Joblib

## Notifications

* PyWhatKit

---

# 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-repository/SeismoGuard-AI.git
cd SeismoGuard-AI
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Streamlit:

```bash
streamlit run app.py
```

---

# 📚 AI Concepts Implemented

✔ Intelligent Agent

✔ PEAS Formulation

✔ Knowledge Base

✔ Inference Engine

✔ State Space Representation

✔ Search Algorithms

✔ BFS Search

✔ Goal State Achievement

✔ Constraint Satisfaction Problem (CSP)

✔ Autonomous Decision Making

---

# 📚 Machine Learning Concepts Implemented

✔ Data Collection

✔ Data Cleaning

✔ Feature Engineering

✔ Feature Scaling

✔ Train/Test Split

✔ Model Training

✔ Model Evaluation

✔ Feature Importance

✔ Clustering

✔ Dashboard Deployment

---

# 🎓 Academic Relevance

This project demonstrates the integration of Artificial Intelligence and Machine Learning techniques for real-world disaster management and emergency response planning.

The system combines predictive analytics with intelligent decision-making to create a complete AI-driven emergency response framework.

---

## 👤 Student Details

**Name:** Muhammad Ali

**Registration Number:** 241383

**Degree:** BSAI

**Course:** AI and ML

---

## 📜 License

This project is developed for academic and educational purposes.


## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/SeismoGuard-AI.git
cd SeismoGuard-AI
```

### 2. Create a Virtual Environment (Recommended)

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Verify Project Structure

```text
SeismoGuard-AI/
│
├── app.py
├── pages/
├── knowledge_system/
├── models/
├── utils/
├── data/
├── requirements.txt
└── README.md
```

### 5. Run the Application

```bash
streamlit run app.py
```

### 6. Open in Browser

```text
http://localhost:8501
```

---


## 🧠 AI Workflow

```text
Earthquake Data
       │
       ▼
Random Forest Prediction
       │
       ▼
Knowledge Base
       │
       ▼
Inference Engine
       │
       ▼
Risk Classification
       │
       ▼
State Space Search
       │
       ▼
CSP Shelter Allocation
       │
       ▼
Emergency Response Plan
       │
       ▼
Population Safe
```

---

## 🎮 Dashboard Modules

### 🏠 Home

Project overview and introduction.

### 📈 Magnitude Prediction

Predict earthquake magnitude using Machine Learning.

### ⚠️ Risk Assessment

Generate risk scores using important seismic indicators.

### 🗺️ Hotspot Detection

Visualize earthquake clusters using K-Means and Folium.

### 🤖 AI Decision Center

Demonstrates:

* Knowledge Base
* Inference Engine
* State Space Representation
* BFS Search Agent
* CSP Shelter Allocation
* Goal State Achievement

### 📢 Emergency Alert System

Generates emergency notifications and response recommendations.
