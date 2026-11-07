"""
SWYNEX Internship Task 1: Dataset Preparation
Run: python prepare_data.py
Install dependency: pip install pandas
"""
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
RAW_FILE = BASE_DIR / "raw_student_data.csv"
CLEAN_FILE = BASE_DIR / "cleaned_student_data.csv"
REPORT_FILE = BASE_DIR / "data_quality_report.txt"

def main():
    # 1. Load raw data
    df = pd.read_csv(RAW_FILE)
    original_rows = len(df)

    # 2. Remove exact duplicate rows
    duplicate_rows = int(df.duplicated().sum())
    df = df.drop_duplicates().copy()

    # 3. Standardize text fields
    for col in ["name", "gender", "department", "city"]:
        df[col] = df[col].astype("string").str.strip()

    df["gender"] = df["gender"].str.title()
    df["department"] = df["department"].str.upper()
    df["city"] = df["city"].str.title()

    # 4. Convert numeric columns and mark impossible values as missing
    numeric_cols = [
        "age", "attendance_pct", "study_hours_per_week",
        "previous_score", "final_score"
    ]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df.loc[~df["age"].between(16, 30), "age"] = pd.NA
    df.loc[~df["attendance_pct"].between(0, 100), "attendance_pct"] = pd.NA
    df.loc[~df["study_hours_per_week"].between(0, 100), "study_hours_per_week"] = pd.NA
    for col in ["previous_score", "final_score"]:
        df.loc[~df[col].between(0, 100), col] = pd.NA

    # 5. Fill missing numeric values with column medians
    missing_before = int(df.isna().sum().sum())
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].median())

    # 6. Fill missing categorical values with the most frequent value
    categorical_cols = ["name", "gender", "department", "city"]
    for col in categorical_cols:
        if df[col].isna().any():
            mode = df[col].mode(dropna=True)
            fill_value = mode.iloc[0] if not mode.empty else "Unknown"
            df[col] = df[col].fillna(fill_value)

    # 7. Set appropriate data types
    df["age"] = df["age"].round().astype("int64")
    df["attendance_pct"] = df["attendance_pct"].round(2)
    df["study_hours_per_week"] = df["study_hours_per_week"].round(2)
    df["previous_score"] = df["previous_score"].round(2)
    df["final_score"] = df["final_score"].round(2)

    # 8. Save cleaned data
    df.to_csv(CLEAN_FILE, index=False)

    # 9. Create a simple quality report
    report = [
        "SWYNEX - DATA PREPARATION REPORT",
        "================================",
        f"Rows in raw dataset: {original_rows}",
        f"Exact duplicate rows removed: {duplicate_rows}",
        f"Rows in cleaned dataset: {len(df)}",
        f"Missing/invalid values handled: {missing_before}",
        f"Remaining missing values: {int(df.isna().sum().sum())}",
        "",
        "Cleaned dataset shape:",
        f"Rows: {df.shape[0]}, Columns: {df.shape[1]}",
        "",
        "Column data types:",
        df.dtypes.to_string(),
        "",
        "Preview:",
        df.head(5).to_string(index=False),
    ]
    REPORT_FILE.write_text("\n".join(report), encoding="utf-8")
    print("\n".join(report[:8]))
    print(f"\nSaved: {CLEAN_FILE.name}")
    print(f"Saved: {REPORT_FILE.name}")

if __name__ == "__main__":
    main()
