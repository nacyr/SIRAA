from src.data_loader import DataLoader
from src.preprocessing import DataPreprocessor


INPUT_FILE = "data/incident_reports_1000.csv"
OUTPUT_FILE = "data/incident_reports_clean.csv"


def main():

    print("=" * 60)
    print("SMART INCIDENT REPORT ANALYZER")
    print("DATA PREPROCESSING PIPELINE")
    print("=" * 60)

    # Load dataset
    print("\nLoading dataset...")

    loader = DataLoader(INPUT_FILE)
    df = loader.load_data()

    original_rows = len(df)

    print(f"Original rows: {original_rows}")

    # Preprocess dataset
    print("\nCleaning dataset...")

    preprocessor = DataPreprocessor()
    clean_df = preprocessor.preprocess(df)

    clean_rows = len(clean_df)
    rows_removed = original_rows - clean_rows

    # Validation
    missing_values = clean_df.isna().sum().sum()
    duplicate_rows = clean_df.duplicated().sum()
    duplicate_ids = clean_df["incident_id"].duplicated().sum()

    # Save cleaned dataset
    clean_df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    # Display results
    print("\n" + "=" * 60)
    print("PREPROCESSING RESULTS")
    print("=" * 60)

    print(f"Original rows:          {original_rows}")
    print(f"Clean rows:             {clean_rows}")
    print(f"Rows removed:           {rows_removed}")

    print(f"\nMissing values:         {missing_values}")
    print(f"Duplicate rows:         {duplicate_rows}")
    print(f"Duplicate incident IDs: {duplicate_ids}")

    print("\n" + "=" * 60)
    print("DATASET VALIDATION")
    print("=" * 60)

    if missing_values == 0:
        print("[OK] No missing values")
    else:
        print("[WARNING] Missing values found")

    if duplicate_rows == 0:
        print("[OK] No duplicate rows")
    else:
        print("[WARNING] Duplicate rows found")

    if duplicate_ids == 0:
        print("[OK] No duplicate incident IDs")
    else:
        print("[WARNING] Duplicate incident IDs found")

    print("\n" + "=" * 60)
    print("OUTPUT")
    print("=" * 60)

    print("Clean dataset saved to:")
    print(OUTPUT_FILE)

    print("\nPreprocessing completed successfully.")


if __name__ == "__main__":
    main()