# AI Data Analyzer

The **AI Data Analyzer** is a powerful Streamlit app that allows users to upload CSV files and analyze them. The app performs data preprocessing steps like handling missing values, renaming columns, and detecting outliers, followed by the execution of user queries on the cleaned data. Visualizations are generated based on the analysis, making it easier for users to gain insights from their data.

## Features

- **CSV Upload**: Users can upload multiple CSV files.
- **Data Preprocessing**: Handles missing values, column renaming, removing incosistencies and other data cleaning tasks.
- **Data Summarization**: Summarizes the data and draws valuable insights. 
- **Data Analysis**: Users can input queries and the app will run analyses on the cleaned data.
- **Visualizations**: Automatically generates visualizations for numeric data (e.g., histograms).
- **Supports Multiple File Types**: The app supports CSV files with different delimiters and encodings.
  
## Requirements

To run this project, you'll need the following dependencies:

streamlit
langchain
langchain_openai
langchain-experimental
langchain-core
langchain-community
pandas
openai
tqdm
python-dotenv
faiss-cpu
tiktoken
tabulate
pytest
pytest-asyncio
pytest-cov
plotly

### Install Dependencies

1. Clone this repository:
    ```bash
    git clone https://github.com/fa-anony-mous/Ai-Data-Analyzer.git
    cd Ai-Data-Analyzer
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. If you don't have a `requirements.txt` file, you can create it by running:
    ```bash
    pip freeze > requirements.txt
    ```

## Usage

### Step 1: Run the Streamlit App

To start the app locally, use the following command:
```bash
streamlit run app.py
