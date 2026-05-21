import pandas as pd

from src.config import RAW_PATH, OUT_PATH

from src.io import load_csv

from src.cleaning import clean_data

from src.features import (
    build_features,
    extract_genres,
    categorize_duration
)

from src.utils import (
    assert_columns,
    dataset_info,
    value_counts_summary,
    movies_vs_shows_by_country,
    ratings_by_type
)

from src.viz import plot_graph


def main():

    # =========================
    # Load Dataset
    # =========================

    df = load_csv(RAW_PATH)

    print("\nDataset loaded successfully.")

    # =========================
    # Column Validation
    # =========================

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

    print("\nRequired columns validated.")

    # =========================
    # Data Quality Checks
    # =========================

    initial_shape = df.shape

    duplicates = df.duplicated().sum()

    missing_before = df.isnull().sum()

    print("\n========== DATA QUALITY REPORT ==========")

    print(f"\nInitial Shape: {initial_shape}")

    print(f"\nDuplicate Rows: {duplicates}")

    print("\nMissing Values BEFORE Cleaning:")
    print(missing_before)

    # =========================
    # Data Cleaning
    # =========================

    df = clean_data(df)

    missing_after = df.isnull().sum()

    print("\nMissing Values AFTER Cleaning:")
    print(missing_after)

    print("\nFinal Shape:")
    print(df.shape)

    # =========================
    # Feature Engineering
    # =========================

    df = build_features(df)

    df = extract_genres(df)

    df = categorize_duration(df)

    print("\nFeature engineering completed.")

    # =========================
    # Dataset Overview
    # =========================

    dataset_info(df)
    
    # Statistical Summary
    print("\n========== STATISTICAL SUMMARY ==========")
    print(df.describe())

    # Average movie duration
    print("\n========== AVERAGE DURATION BY TYPE ==========")

    print(
        df.groupby('type')['duration_int']
        .mean()
    )

    # =========================
    # Value Count Summaries
    # =========================

    value_counts_summary(df, "type")

    value_counts_summary(df, "listed_in")

    value_counts_summary(df, "main_genre")

    value_counts_summary(df, "country")

    # =========================
    # Pivot Tables
    # =========================

    country_pivot = movies_vs_shows_by_country(df)

    print("\n========== MOVIES VS TV SHOWS BY COUNTRY ==========")

    print(country_pivot)

    rating_pivot = ratings_by_type(df)

    print("\n========== RATINGS BY TYPE ==========")

    print(rating_pivot)

    # =========================
    # Visualizations
    # =========================

    plot_graph(df)

    # =========================
    # Export Clean Dataset
    # =========================

    OUT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(
        OUT_PATH,
        index=False
    )

    print(f"\nDataset saved successfully: {OUT_PATH}")


if __name__ == "__main__":
    main()
