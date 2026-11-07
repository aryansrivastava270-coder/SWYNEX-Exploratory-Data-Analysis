# SWYNEX – Exploratory Data Analysis

## Internship Task 2

### Objective

Perform Exploratory Data Analysis (EDA) on a student performance dataset using Python and Pandas to identify patterns, relationships, trends, and important insights from the data.

---

## Dataset

This project uses a student performance dataset containing information related to students' academic performance, attendance, study habits, and department.

The dataset contains **25 cleaned records and 10 columns** after data preparation.

The analysis focuses on variables such as:

- Department
- Study hours per week
- Attendance percentage
- Previous score
- Final score
- Other student performance-related attributes

---

## Tools & Technologies

- Python 3
- Pandas
- Matplotlib
- Google Colab
- GitHub

---

## EDA Performed

The following exploratory data analysis was performed:

1. Loaded the cleaned dataset using Pandas.
2. Checked the dataset shape and structure.
3. Calculated descriptive statistics.
4. Analyzed the average, highest, and lowest final scores.
5. Compared average final scores across departments.
6. Calculated correlations between numerical variables.
7. Identified relationships between study hours, attendance, previous scores, and final scores.
8. Created visualizations to make the findings easier to understand.

---

## Key Findings

### Overall Final Score

- **Average Final Score:** 80.08
- **Highest Final Score:** 96.0
- **Lowest Final Score:** 59.0

### Average Final Score by Department

| Department | Average Final Score |
|------------|---------------------:|
| CSE | 84.45 |
| ECE | 84.50 |
| ME | 66.17 |

The analysis shows that **CSE and ECE have similar average final scores**, while the average score for **ME is comparatively lower**.

### Correlation with Final Score

| Variable | Correlation |
|----------|------------:|
| Study Hours per Week | 0.969137 |
| Attendance Percentage | 0.948747 |
| Previous Score | 0.937067 |

The analysis indicates strong positive relationships between final score and:

- Study hours per week
- Attendance percentage
- Previous score

Among these variables, **study hours per week has the strongest correlation with final score** in this dataset.

---

## Visualizations

The project includes visualizations such as:

- Average Final Score by Department
- Correlation analysis
- Other exploratory charts based on the dataset

These visualizations help identify patterns and differences in student performance.

---

## Project Files

| File | Description |
|------|-------------|
| `SWYNEX_Exploratory_Data_Analysis.ipynb` | Main EDA notebook |
| `SWYNEX_Data_Preparation.ipynb` | Data preparation notebook |
| `cleaned_student_data.csv` | Cleaned dataset used for analysis |
| `raw_student_data.csv` | Original dataset |
| `prepare_data.py` | Python data preparation script |
| `data_quality_report.txt` | Data cleaning and quality report |
| `README.md` | Project documentation |

---

## How to Run

### 1. Install Python

Install Python 3 or use Google Colab.

### 2. Install Required Libraries

```bash
pip install pandas matplotlib
```

### 3. Open the Notebook

Open:

```text
SWYNEX_Exploratory_Data_Analysis.ipynb
```
