# Netflix_content_EDA_project_MDS

## Project Overview

This project performs a complete Exploratory Data Analysis (EDA) on the Netflix Titles Dataset using Python.

The objective is to analyze Netflix’s catalog in order to understand:

- Content distribution
- Most common ratings
- Top producing countries
- Movies vs TV Shows
- Duration trends
- General business insights

The project follows a modular and scalable structure, separating:
- data loading,
- cleaning,
- feature engineering,
- utilities,
- visualizations,
- and execution logic.

---

# Project Structure

```bash
project/
│
├── data/
│   └── netflix_titles.csv
│
├── src/
│   ├── main.py
│   ├── cleaning.py
│   ├── config.py
│   ├── features.py
│   ├── data_io.py
│   ├── utils.py
│   └── viz.py
│
├── requirements.txt
└── README.md
```

---

# Technologies Used

## Python Libraries

- pandas
- numpy
- matplotlib
- seaborn

---

# Installation

## 1. Clone the repository

```bash
git clone <https://github.com/marinaxiuping/Netflix_content_EDA_project_MDS>
```

---

## 2. Create virtual environment

### Windows

```bash
python -m venv .venv
```

---

## 3. Activate virtual environment

### PowerShell

```bash
.venv\Scripts\activate
```

If PowerShell blocks execution:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate again.

---

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

# Dataset

The dataset used is the Netflix Titles Dataset containing information about:

- Movies
- TV Shows
- Directors
- Cast
- Countries
- Release years
- Ratings
- Duration
- Genres
- Date added to Netflix

---

# Data Cleaning

The cleaning process includes:

- Removing duplicates
- Handling missing values
- Converting `date_added` into datetime format
- Standardizing columns



---

# Feature Engineering

Additional features were created to improve analysis:

| Feature | Description |
|---|---|
| year_added | Year content was added |
| month_added | Month content was added |
| duration_int | Numeric duration extraction |


---

# Column Validation

The project validates required columns before running analysis.

```python
def assert_columns(df, required):
    missing = [c for c in required if c not in df.columns]

    if missing:
        raise ValueError(f'Missing columns: {missing}')
```

This prevents runtime errors caused by incorrect datasets.

---

# Exploratory Data Analysis (EDA)

## 1. Movies vs TV Shows

### Goal
Understand content distribution.

### Visualization
Countplot.

```python
sns.countplot(x='type', data=df)
```

### Insight
Netflix contains significantly more movies than TV Shows.

---

# 2. Release Year Distribution

### Goal
Analyze how modern the catalog is.

### Visualization
Histogram.

```python
sns.histplot(df['release_year'], bins=30)
```

### Insight
Most content belongs to recent decades.

---

# 3. Top Producing Countries

### Goal
Identify dominant countries.

### Visualization
Horizontal barplot.

```python
sns.barplot(
    x=top_countries.values,
    y=top_countries.index
)
```

### Insight
The United States dominates the catalog, followed by countries like India and the UK.

---

# 4. Rating Distribution

### Goal
Understand target audience.

### Visualization
Countplot.

```python
sns.countplot(
    y='rating',
    data=df
)
```

### Insight
TV-MA is among the most common ratings, indicating strong adult-oriented content.

---

# 7. Movie Duration Analysis

### Goal
Study movie duration patterns.

### Visualization
Histogram.

```python
sns.histplot(
    movies['duration_int'],
    bins=30
)
```

### Insight
Most movies last between 80 and 120 minutes.

---

# 7. Movies vs Series Through Time

### Goal
Compare growth between content types.

### Visualization
Countplot with hue.

```python
sns.countplot(
    x='year_added',
    hue='type',
    data=df
)
```

### Insight
TV Shows have increased significantly in recent years.

---

# Business Insights

The EDA reveals several strategic insights:

- Netflix heavily prioritizes movies.
- The catalog expanded aggressively after 2015.
- International content production is growing.
- Adult-oriented content dominates the platform.
- Recent content is strongly prioritized.

---

# Running the Project

Move into the source folder:

```bash
cd src
```

Run the main script:

```bash
python main.py
```

---

# Example Workflow

The pipeline executed by `main.py`:

1. Load dataset
2. Validate columns
3. Clean data
4. Create features
5. Generate summaries
6. Create visualizations
7. Extract insights

---

# Possible Future Improvements

- Dashboard with Streamlit
- Recommendation system
- NLP analysis on descriptions
- Genre clustering
- Predictive analytics
- Interactive visualizations

---

# Author

Created as a Data Science portfolio project focused on:
- Python
- Data Analysis
- EDA
- Visualization
- Clean project architecture
