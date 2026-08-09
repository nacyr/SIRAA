# Smart Incident Report Analyzer (SIRA)

## About the Application

The Smart Incident Report Analyzer (SIRA) is a data processing project designed to prepare oil and gas incident reports for machine learning.

The project focuses on investigating the quality of incident report data and applying automated preprocessing techniques to make the dataset more consistent, reliable, and suitable for future machine learning tasks.

The preprocessing pipeline is implemented using Python, Pandas, modules, classes, and reusable methods.

---

## Dataset

The original dataset contains 1,000 incident records and 10 columns.

The main columns include:

- incident_id
- report_text
- location
- reported_by
- department
- severity
- incident_type
- report_date
- shift
- status

The original dataset is stored in:

```text
data/incident_reports_1000.csv