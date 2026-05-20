import pandas as pd # type: ignore

def clean_data(df):
    """Clean Netflix dataset."""

    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df["director"] = df["director"].fillna("Unknown")
    df["cast"] = df["cast"].fillna("Unknown")
    df["country"] = df["country"].fillna("Unknown")
    df["rating"] = df["rating"].fillna("Not Rated")

    # Convert date_added to datetime
    df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

    return df