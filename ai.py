from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load Environment Variables
load_dotenv()


# Initialize Gemini Model
model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    temperature=1.0
)


# Test Gemini Connection
def test_model(model):
    response = model.invoke("Say Hello in one sentence.")
    return response.content


# Build Dataset Context
def prepare_context(
    shape,
    missing_values,
    duplicates,
    summary_statistics,
    numerical_columns,
    categorical_columns,
    unique_values,
    correlation_matrix,
):

    context = f"""
==============================
DATASET OVERVIEW
==============================

Rows: {shape[0]}
Columns: {shape[1]}

==============================
NUMERICAL COLUMNS
==============================

{numerical_columns}

==============================
CATEGORICAL COLUMNS
==============================

{categorical_columns}

==============================
MISSING VALUES
==============================

{missing_values}

==============================
DUPLICATE ROWS
==============================

{duplicates}

==============================
SUMMARY STATISTICS
==============================

{summary_statistics}

==============================
UNIQUE VALUES
==============================

{unique_values}

==============================
CORRELATION MATRIX
==============================

{correlation_matrix}
"""

    return context

def build_prompt(context, user_question):

    prompt = f"""
You are an expert Data Analyst.

Your task is to analyze datasets and answer user questions accurately based ONLY on the dataset information provided.

Instructions:
- Use only the dataset context below.
- Do not make up facts or statistics.
- If the answer cannot be determined from the provided context, clearly say so.
- Explain your reasoning in simple language.
- When appropriate, provide actionable insights or recommendations.
- Format your response using clear headings and bullet points where useful.

==============================
DATASET CONTEXT
==============================

{context}

==============================
USER QUESTION
==============================

{user_question}

==============================
ANSWER
==============================
"""

    return prompt

#def generate_response(model, prompt):
    response = model.invoke(prompt)

    if (
        isinstance(response.content, list)
        and len(response.content) > 0
        and isinstance(response.content[0], dict)
        and "text" in response.content[0]
    ):
        return response.content[0]["text"]

    return str(response.content)

def generate_response(model, prompt):
    response = model.invoke(prompt)

    if isinstance(response.content, list):
        return response.content[0]["text"]

    return response.content