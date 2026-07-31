## 🤖 InsightPilot
AI-Powered Exploratory Data Analysis & Dataset Assistant

An AI-powered Exploratory Data Analysis (EDA) application built with **Streamlit**, **Python**, **LangChain**, and **Google Gemini**. Upload any CSV dataset, instantly explore its statistics through interactive visualizations, and ask natural language questions about your data using an integrated AI assistant.

---

## ✨ Features

### 📂 Dataset Upload
- Upload any CSV dataset.
- Instant preview of the uploaded data.

### 📊 Dataset Overview
- Number of rows and columns
- Missing value count
- Duplicate row count

### 📝 Data Exploration
- Column names
- Data types
- Numerical & categorical column identification
- Unique value count for every column

### 📈 Statistical Analysis
- Summary statistics
- Correlation matrix

### 📉 Interactive Visualizations
- Histogram
- Box Plot
- Count Plot
- Correlation Heatmap

### 🤖 AI Dataset Assistant
Ask questions about your uploaded dataset in natural language.

Examples:
- Which column has the highest correlation?
- Are there any missing values?
- Explain the salary distribution.
- Which numerical columns are available?
- Summarize this dataset.

The assistant understands the dataset context and generates intelligent responses powered by **Google Gemini**.

---

## 🛠️ Tech Stack

### Frontend
- Streamlit

### Backend
- Python

### Data Processing
- Pandas
- NumPy

### Data Visualization
- Matplotlib
- Seaborn

### Generative AI
- LangChain
- Google Gemini
- python-dotenv

---

## 📂 Project Structure

```text
AI_EDA_ANALYZER/

│── app.py                 # Streamlit application
│── ai.py                  # Gemini AI integration
│── eda.py                 # EDA utility functions
│── requirements.txt
│── README.md
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/your-username/AI_EDA_ANALYZER.git

cd AI_EDA_ANALYZER
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---



## 💡 Example Workflow

1. Upload a CSV dataset.
2. Explore dataset information.
3. Analyze statistics.
4. Visualize the data.
5. Ask questions using the AI assistant.

---

## 👨‍💻 Developer

**Krish Rathod**

GitHub:
https://github.com/WeAreTheRealArt

LinkedIn:
https://www.linkedin.com/in/krish-rathod-bb7809259/

---

## 📄 License

This project is licensed under the MIT License.