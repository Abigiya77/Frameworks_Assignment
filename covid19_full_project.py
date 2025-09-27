# ===== COVID-19 Full Project =====
# Tools: pandas, matplotlib, seaborn, wordcloud, streamlit
# Author: Abi

# ----------------------
# Part 1: Data Loading & Basic Exploration
# ----------------------
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import streamlit as st

# Load only first 5000 rows from the metadata.csv
data_path = r"C:\Users\Hp\Downloads\archive\metadata.csv"
df = pd.read_csv(data_path, nrows=5000)

# Basic exploration
print("===== First 5 Rows =====")
print(df.head())
print("\nShape of dataset:", df.shape)
print("\nData Types:\n", df.dtypes)
print("\nMissing Values in key columns:\n", df[['title','journal','publish_time']].isnull().sum())
print("\nBasic Stats for numerical columns:\n", df.describe())

# ----------------------
# Part 2: Data Cleaning & Preparation
# ----------------------
# Drop columns with all missing values
df = df.dropna(axis=1, how='all')

# Convert publish_time to datetime and extract year
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year

# Create abstract word count
df['abstract_word_count'] = df['abstract'].fillna("").apply(lambda x: len(x.split()))

# Save cleaned dataset
clean_file = r"C:\Users\Hp\Downloads\archive\metadata_small_clean.csv"
df.to_csv(clean_file, index=False)
print("\nCleaned data saved successfully!")
print("\n===== Cleaned Data Sample =====")
print(df[['publish_time','year','abstract_word_count']].head())

# ----------------------
# Part 3: Data Analysis & Visualization
# ----------------------
# Publications by Year
plt.figure(figsize=(8,5))
year_counts = df['year'].value_counts().sort_index()
plt.bar(year_counts.index, year_counts.values, color='skyblue')
plt.xlabel("Year")
plt.ylabel("Number of Papers")
plt.title("Publications by Year")
plt.show()

# Top 10 Journals
plt.figure(figsize=(10,5))
top_journals = df['journal'].value_counts().head(10)
top_journals.plot(kind='bar', color='lightgreen')
plt.xlabel("Journal")
plt.ylabel("Number of Papers")
plt.title("Top 10 Journals Publishing COVID-19 Research")
plt.show()

# Word Cloud of Titles
titles_text = " ".join(df['title'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(titles_text)
plt.figure(figsize=(12,6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Word Cloud of Paper Titles")
plt.show()

# Source distribution
plt.figure(figsize=(8,5))
source_counts = df['source_x'].value_counts()
source_counts.plot(kind='bar', color='salmon')
plt.xlabel("Source")
plt.ylabel("Number of Papers")
plt.title("Distribution of Papers by Source")
plt.show()

print("\nAll tasks completed successfully!")

# ----------------------
# Part 4: Streamlit Application
# ----------------------
st.title("COVID-19 Research Data Explorer 🦠")
st.write("Explore COVID-19 research papers from the CORD-19 metadata dataset.")

# Sidebar filters
st.sidebar.header("Filters")
min_year = int(df['year'].min())
max_year = int(df['year'].max())
year_range = st.sidebar.slider("Select Year Range", min_year, max_year, (min_year, max_year))

# Filter data by year
filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# Display sample data
st.subheader("Sample Data")
st.dataframe(filtered_df[['title','journal','year','abstract_word_count']].head(10))

# Publications by year
st.subheader("Publications by Year")
fig1, ax1 = plt.subplots()
year_counts_filtered = filtered_df['year'].value_counts().sort_index()
ax1.bar(year_counts_filtered.index, year_counts_filtered.values, color='skyblue')
ax1.set_xlabel("Year")
ax1.set_ylabel("Number of Papers")
st.pyplot(fig1)

# Top 10 Journals
st.subheader("Top 10 Journals")
top_journals_filtered = filtered_df['journal'].value_counts().head(10)
fig2, ax2 = plt.subplots()
top_journals_filtered.plot(kind='bar', ax=ax2, color='lightgreen')
ax2.set_xlabel("Journal")
ax2.set_ylabel("Number of Papers")
st.pyplot(fig2)

# Word Cloud of Titles
st.subheader("Word Cloud of Paper Titles")
titles_text_filtered = " ".join(filtered_df['title'].dropna())
wordcloud_filtered = WordCloud(width=800, height=400, background_color='white').generate(titles_text_filtered)
fig3, ax3 = plt.subplots(figsize=(10,5))
ax3.imshow(wordcloud_filtered, interpolation='bilinear')
ax3.axis('off')
st.pyplot(fig3)
