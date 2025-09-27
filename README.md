# COVID-19 Data Analysis Project

This project explores COVID-19 research papers using the **CORD-19 dataset**. It demonstrates **data loading, cleaning, analysis, visualization**, and a **simple interactive web app** using Streamlit.

## Features

1. **Data Loading & Exploration**
   - Load a subset of the dataset (first 5000 rows) for faster processing.
   - Examine the structure, data types, and missing values.
   - Generate basic statistics for numerical columns.

2. **Data Cleaning & Preparation**
   - Drop columns with all missing values.
   - Convert publication dates to datetime format.
   - Extract the publication year.
   - Compute word count for abstracts.

3. **Data Analysis & Visualization**
   - Count papers by publication year.
   - Identify top journals publishing COVID-19 research.
   - Generate a word cloud of paper titles.
   - Show distribution of papers by source.

4. **Interactive Streamlit App**
   - Display sample data in a table.
   - Filter publications by year using a slider.
   - Visualize charts and word cloud interactively.

## How to Run

### Requirements
- Python 3.7+
- pandas
- matplotlib
- seaborn
- wordcloud
- streamlit

Install dependencies using:

```bash
pip install pandas matplotlib seaborn wordcloud streamlit
