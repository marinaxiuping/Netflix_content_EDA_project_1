from src.config import RAW_PATH, OUT_PATH
from src.io import load_csv
from src.cleaning import clean_data
from src.features import build_features, extract_genres, categorize_duration
from src.utils import assert_columns, dataset_info, value_counts_summary
from src.viz import plot_graph


def main():
    df = load_csv(RAW_PATH)
    # Validate required columns
    required_cols = [
        'title',
        'type',
        'country',
        'release_year',
        'rating',
        'duration',
        'date_added'
    ]

    assert_columns(df, required_cols)
    df = clean_data(df)
    df = build_features(df)
    df = extract_genres(df)
    df = categorize_duration(df)
    dataset_info(df)

    value_counts_summary(df, "type")
    value_counts_summary(df, "listed_in")
    value_counts_summary(df, "main_genre")
    value_counts_summary(df, "country")
    

    plot_graph(df)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_PATH, index=False)
    print(f"Saved: {OUT_PATH}")


if __name__ == "__main__":
    main()