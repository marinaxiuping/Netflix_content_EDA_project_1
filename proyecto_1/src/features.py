import pandas as pd  # type: ignore

def build_features(df):
    """Create new features for analysis."""

    # Extract year and month
    df["year_added"] = df["date_added"].dt.year
    df["month_added"] = df["date_added"].dt.month

    # Duration number
    df["duration_int"] = (
        df["duration"]
        .str.extract(r"(\d+)")
        .astype(float)
    )


    return df

def extract_genres(df):
    df['main_genre'] = df['listed_in'].str.split(',').str[0]

    return df

def categorize_duration(df):

    # Extraer número de duration
    df['duration_num'] = pd.to_numeric(
        df['duration'].astype(str).str.extract(r'(\d+)', expand=False),
        errors='coerce'
    )

    # Movies → minutos
    df.loc[df['type'] == 'Movie', 'duration_minutes'] = df['duration_num']

    # TV Shows → temporadas
    df.loc[df['type'] == 'TV Show', 'seasons'] = df['duration_num']

    # Duration ranges
    bins = [0, 60, 90, 120, 150, 300]
    labels = ['< 60 min', '60-90 min', '90-120 min', '120-150 min', '150+ min']

    df['duration_movies'] = pd.cut(
        df['duration_minutes'],
        bins=bins,
        labels=labels
    )

    df['duration_tv_shows'] = pd.cut(
        df['seasons'],
        bins=[0, 1, 3, 5, 10],
        labels=['< 1 season', '1-3 seasons', '4-5 seasons', '6+ seasons']   
    )


    return df

def genre_year(df):
    df['main_genre'] = df['listed_in'].str.split(',').str[0]

    genre_year = (
        df.groupby(['year_added', 'main_genre'])
        .size()
        .reset_index(name='count')
    )
    return genre_year
