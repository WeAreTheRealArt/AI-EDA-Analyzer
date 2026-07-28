# AI EDA Analyzer

An AI-powered Exploratory Data Analysis (EDA) application that helps users quickly inspect and understand CSV datasets through automated dataset profiling.

---

## Features

### Current Features

* Upload CSV datasets
* Dataset preview (first 5 rows)
* Dataset overview

  * Number of rows
  * Number of columns
  * Total missing values
  * Total duplicate rows
* Display column names
* Display data types of all columns

---

## Tech Stack

* Python
* Streamlit
* Pandas

---

## Project Structure

```text
AI_EDA_Analyzer/
│
├── app.py                 # Streamlit application
├── eda.py                 # EDA utility functions
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository

```bash
git clone <repository-url>
cd AI_EDA_Analyzer
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

**Windows**

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
streamlit run app.py
```

Open:

```
http://localhost:8501
```

---

## Current Workflow

1. Upload a CSV dataset.
2. Preview the uploaded dataset.
3. View dataset overview.
4. Inspect column names.
5. Check data types of each column.

---

## Upcoming Features

* Summary statistics
* Missing values analysis by column
* Duplicate row analysis
* Data visualizations
* AI-powered dataset insights using Google Gemini

---

## Author

**Krish Rathod**
