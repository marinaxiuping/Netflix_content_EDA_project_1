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