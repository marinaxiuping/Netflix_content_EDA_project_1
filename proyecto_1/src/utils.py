import pandas as pd # type: ignore


def dataset_info(df: pd.DataFrame) -> None:    
    """Print dataset information."""    

    print("\nDataset Shape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nMissing Values:")
    print(df.isnull().sum())


def value_counts_summary(df: pd.DataFrame, column: str) -> None:
    """Show value counts for a column."""

    print(f"\nValue Counts for {column}:")
    print(df[column].value_counts().head(10))

def assert_columns(df: pd.DataFrame, required: list[str]) -> None:
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f'Missing columns: {missing}')
    
def movies_vs_shows_by_country(df):

    pivot = pd.pivot_table(
        df,
        index='country',
        columns='type',
        aggfunc='size',
        fill_value=0
    )

    return pivot.sort_values(
        by='Movie',
        ascending=False
    ).head(10)


def ratings_by_type(df):

    pivot = pd.pivot_table(
        df,
        index='rating',
        columns='type',
        aggfunc='size',
        fill_value=0
    )

    return pivot
