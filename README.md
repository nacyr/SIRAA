# Smart Incident Report Analyzer (SIRA)

## About the Project

The Smart Incident Report Analyzer (SIRA) is a data preprocessing project developed to prepare Oil and Gas incident reports for future machine learning tasks.

The main purpose of this assignment was to investigate the quality of the incident dataset, identify problems that could affect data analysis or machine learning, and build an automated preprocessing pipeline to clean the data.

Instead of manually editing the CSV file, I used Python and Pandas to perform the investigation and cleaning. The preprocessing process is implemented using classes, functions, and Python modules so that it can be executed repeatedly whenever the dataset needs to be cleaned.

---

## Dataset

The original dataset contains **1,000 incident records** and **10 columns**.

The columns are:

- `incident_id`
- `report_text`
- `location`
- `reported_by`
- `department`
- `severity`
- `incident_type`
- `report_date`
- `shift`
- `status`

The original dataset is stored in:

```text
data/incident_reports_1000.csv



The cleaned dataset is generated as:

data/incident_reports_clean.csv
Data Quality Issues Found

I investigated the dataset before applying any cleaning operations. The following data quality issues were identified.

1. Duplicate Records

The dataset contained 40 duplicate rows.

Duplicate records can cause the same incident to be counted more than once and may affect statistical analysis and future machine learning models.

The preprocessing pipeline removes exact duplicate records automatically.

2. Missing Values

Missing values were found in three columns:

Column	Missing Values
report_text	38
location	21
reported_by	26

The missing values were handled based on the importance of each field.

Records with missing report_text were removed because the incident description is an important part of the dataset and there was no reliable information available to reconstruct it.

Missing values in location and reported_by were replaced with Unknown. This allows the remaining information in those records to be retained without making up information.

3. Inconsistent Report Text

The report_text column contained inconsistent capitalization, unnecessary spaces, and some spelling errors.

Examples included different versions of the same report such as:

SMOKE OBSERVED FROM ELECTRICAL CONTROL PANEL.
smoke observed from electrical control panel.

Some spelling errors such as maintainance and triggred were also found.

The preprocessing pipeline removes unnecessary spaces, corrects known spelling errors, and standardizes the capitalization of the report text.

4. Inconsistent Location Names

Some locations were represented using different formats.

For example:

Pipeline7
Pipeline 7

and:

PlatformA
Platform A

These values were standardized so that the same location is represented consistently.

5. Inconsistent Department Names

Different forms of the same department were found, including:

Pipeline Operations
PIPELINE OPERATIONS
pipeline operations
Pipeline Ops

These values were standardized to:

Pipeline Operations

This prevents the same department from being treated as several different categories during future analysis or machine learning.

6. Inconsistent Severity Values

The severity column contained several representations of the same severity level.

For example:

High
high
HIGH
H

The same problem occurred with Medium and Low.

These values were standardized into three consistent categories:

High
Medium
Low
7. Inconsistent Date Formats

The report_date column contained dates written in different formats.

Examples included:

2025-09-30
12/06/2025
Aug 15 2025
May 31 2025
Dec 30 2025

The dates were converted into a consistent format:

YYYY-MM-DD

This makes the date column easier to use for analysis and future feature engineering.

How I Identified the Issues

I used Python and Pandas to inspect the dataset before cleaning it.

The investigation included checking:

Dataset shape
Column names
Data types
Missing values
Duplicate records
Duplicate incident IDs
Unique values in categorical columns
Location variations
Department variations
Severity variations
Date formats
Incident report text samples

The initial investigation showed:

Rows: 1000
Columns: 10
Duplicate rows: 40
Missing report_text: 38
Missing location: 21
Missing reported_by: 26

I also inspected the unique values in columns such as location, department, and severity to identify values that represented the same category in different forms.

Preprocessing Approach

The cleaning process was implemented in:

src/preprocessing.py

The main class is:

DataPreprocessor

The class contains separate methods for different preprocessing tasks:

remove_duplicates()
handle_missing_values()
clean_report_text()
clean_location()
clean_department()
clean_severity()
clean_date()
preprocess()

The preprocess() method runs the cleaning steps as one complete pipeline.

The general process is:

Load the original dataset.
Remove duplicate records.
Handle missing values.
Clean and standardize incident report text.
Standardize location names.
Standardize department names.
Standardize severity values.
Convert dates to a consistent format.
Validate the cleaned dataset.
Save the cleaned dataset.
Why These Methods Were Used

The preprocessing decisions were based on the problems discovered during the investigation.

Duplicate records were removed because keeping them could result in the same incident being counted multiple times.

Records with missing report_text were removed because there was no reliable information available to reconstruct the incident description.

Missing locations and reporter names were replaced with Unknown rather than removing the entire records because the other information in those records may still be useful.

Text was standardized to reduce unnecessary differences caused by spaces, capitalization, and known spelling errors.

Categorical values such as department and severity were standardized so that different representations of the same category would not be treated as separate categories.

Dates were standardized because having multiple date formats can cause problems during analysis and feature engineering.

Preprocessing Results

The preprocessing pipeline produced the following result:

Original rows:          1000
Clean rows:              924
Rows removed:             76

The final validation showed:

Missing values:          0
Duplicate rows:          0
Duplicate incident IDs:  0

The cleaned dataset was successfully saved to:

data/incident_reports_clean.csv

The original CSV file was not manually edited. The cleaned dataset was generated automatically by the preprocessing program.

Project Structure
SIRAA/
│
├── data/
│   ├── incident_reports_1000.csv
│   └── incident_reports_clean.csv
│
├── notebooks/
│
├── src/
│   ├── __init__.py
│   ├── incident.py
│   ├── data_loader.py
│   ├── preprocessing.py
│   └── utils.py
│
├── clean_data.py
├── inspect_data.py
├── README.md
└── .gitignore
How to Run the Project

Create and activate a virtual environment:

python -m venv .venv

Activate it on Windows PowerShell:

.venv\Scripts\Activate.ps1

Install Pandas:

pip install pandas

Run the preprocessing pipeline:

python clean_data.py

The program will automatically load the original dataset, perform the preprocessing steps, validate the results, and generate:

data/incident_reports_clean.csv

The pipeline can be executed multiple times without manually modifying the CSV file.

Technologies Used
Python
Pandas
Object-Oriented Programming
Python Modules
Data Analysis
Data Preprocessing
Git
GitHub
Visual Studio Code
Conclusion

This assignment demonstrated the importance of investigating data before using it for machine learning.

The original SIRA dataset contained duplicate records, missing values, inconsistent text, inconsistent categorical values, and mixed date formats. These issues were identified through systematic inspection using Python and Pandas.

A reusable preprocessing pipeline was then developed to clean the data automatically. The final dataset contains 924 records with no missing values, no duplicate rows, and no duplicate incident IDs.

The cleaned dataset is now ready for the next stage of the SIRA project, where it can be used for further analysis, feature engineering, and machine learning.