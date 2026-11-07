# SWYNEX – Data Preparation Using Python

## Internship Task 1
**Objective:** Prepare a raw dataset for data-science work by cleaning, validating, standardizing, and exporting it.

## Dataset
This project uses a sample student performance dataset with 26 raw rows and 10 columns. It contains deliberately introduced data-quality issues for practice, including:
- An exact duplicate record
- Missing values
- Inconsistent capitalization and extra spaces in categories
- Invalid values such as attendance above 100% and an out-of-range age

The dataset is synthetic and is intended for learning purposes only.

## Tools
- Python 3
- Pandas

## Project files
| File | Description |
|---|---|
| `raw_student_data.csv` | Original sample dataset containing data-quality issues |
| `prepare_data.py` | Python script that performs the cleaning steps |
| `cleaned_student_data.csv` | Cleaned output dataset |
| `data_quality_report.txt` | Summary of the cleaning results |

## How to run
1. Install Python 3.
2. Open a terminal in this project folder.
3. Install Pandas:
   ```bash
   pip install pandas
   ```
4. Run:
   ```bash
   python prepare_data.py
   ```

The script creates/overwrites `cleaned_student_data.csv` and `data_quality_report.txt`.

## Data preparation steps
1. Load the raw CSV file with Pandas.
2. Identify and remove exact duplicate rows.
3. Trim whitespace and standardize text categories.
4. Convert numeric columns to numeric data types.
5. Mark impossible/out-of-range values as missing.
6. Fill missing numeric values using the median.
7. Fill missing categorical values using the mode.
8. Set suitable data types and export the cleaned CSV.
9. Generate a data-quality report.

## Important note
Median and mode imputation are simple baseline techniques. For a real project, choose a missing-value strategy based on the meaning of each column and the downstream analysis. Do not use this synthetic dataset to make real decisions about students.
