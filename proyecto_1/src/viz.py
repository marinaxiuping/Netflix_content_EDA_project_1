import pandas as pd  # type: ignore
import numpy as np  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
import seaborn as sns  # type: ignore


def plot_graph(df: pd.DataFrame) -> None:
    """Create visualizations for Netflix EDA."""

    sns.set_style("whitegrid")

    # ---------------------------
    # Movies vs Series
    # ---------------------------
    plt.figure(figsize=(6, 4))
    sns.countplot(x='type', data=df, palette='Set2')
    plt.title("Movies vs Series", fontsize=14)
    plt.xlabel("Type")
    plt.ylabel("Count")
    plt.show()

    # ---------------------------
    # Top countries
    # ---------------------------
    plt.figure(figsize=(10, 6))
    top_countries = df['country'].value_counts().head(10)
    sns.barplot(x=top_countries.values, y=top_countries.index, palette='viridis')
    plt.title("Top 10 Countries with Most Netflix Titles", fontsize=14)
    plt.xlabel("Count")
    plt.ylabel("Country")
    plt.show()

    # ---------------------------
    # Release year distribution
    # ---------------------------
    plt.figure(figsize=(10, 5))
    sns.histplot(df['release_year'].dropna(), bins=30, color='purple', kde=True)
    plt.title("Release Year Distribution", fontsize=14)
    plt.xlabel("Release Year")
    plt.ylabel("Frequency")
    plt.show()

    # ---------------------------
    # Top genres (no modifica df original)
    # ---------------------------
    main_genre = df['listed_in'].dropna().str.split(',').str[0].str.strip()
    top_genres = main_genre.value_counts().head(10)

    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_genres.values, y=top_genres.index, palette='magma')
    plt.title("Top 10 Genres in Netflix", fontsize=14)
    plt.xlabel("Count")
    plt.ylabel("Genre")
    plt.show()

    # ---------------------------
    # Movies vs Series over time
    # ---------------------------
    if 'year_added' not in df.columns and 'date_added' in df.columns:
        df = df.copy()
        df['year_added'] = pd.to_datetime(df['date_added'], errors='coerce').dt.year

    if 'year_added' in df.columns:
        plt.figure(figsize=(10, 6))
        sns.countplot(x='year_added', hue='type', data=df, palette='Set1')
        plt.xticks(rotation=45)
        plt.title("Movies vs Series Added Over Time", fontsize=14)
        plt.xlabel("Year Added")
        plt.ylabel("Count")
        plt.show()

    # ---------------------------
    # Top ratings
    # ---------------------------
    top_10_ratings = df['rating'].value_counts().nlargest(10).index

    plt.figure(figsize=(16, 6))
    sns.countplot(
        x='rating',
        data=df,
        palette='Set3',
        order=top_10_ratings
    )
    plt.title("Top 10 Rating Distribution", fontsize=14)
    plt.xlabel("Rating")
    plt.ylabel("Count")
    plt.show()

    # ---------------------------
    # Movie duration ranges
    # ---------------------------
    if 'duration_movies' in df.columns:
        plt.figure(figsize=(10, 6))
        sns.countplot(
            data=df,
            x='duration_movies',
            order=[
                '< 60 min',
                '60-90 min',
                '90-120 min',
                '120-150 min',
                '150+ min'
            ]
        )
        plt.title('Movie Duration Ranges')
        plt.xlabel('Duration Range')
        plt.ylabel('Number of Movies')
        plt.show()

    # ---------------------------
    # TV show duration ranges
    # ---------------------------
    if 'duration_tv_shows' in df.columns:
        plt.figure(figsize=(10, 6))
        sns.countplot(
            data=df,
            x='duration_tv_shows',
            order=[
                '< 1 season',
                '1-3 seasons',
                '4-5 seasons',
                '6+ seasons'
            ]
        )
        plt.title('TV Show Duration Ranges')
        plt.xlabel('Duration Range')
        plt.ylabel('Number of TV Shows')
        plt.show()
