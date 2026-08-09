import pandas as pd


FILE_PATH = "data/incident_reports_1000.csv"

df = pd.read_csv(FILE_PATH)


print("=" * 60)
print("SIRA DETAILED DATA QUALITY INVESTIGATION")
print("=" * 60)


# 1. Records with missing report_text
print("\n1. RECORDS WITH MISSING REPORT TEXT")
print("-" * 60)

missing_report = df[df["report_text"].isna()]

print(f"Number of records: {len(missing_report)}")
print(missing_report.to_string(index=False))


# 2. Records with missing location
print("\n2. RECORDS WITH MISSING LOCATION")
print("-" * 60)

missing_location = df[df["location"].isna()]

print(f"Number of records: {len(missing_location)}")
print(missing_location.to_string(index=False))


# 3. Records with missing reported_by
print("\n3. RECORDS WITH MISSING REPORTER")
print("-" * 60)

missing_reporter = df[df["reported_by"].isna()]

print(f"Number of records: {len(missing_reporter)}")
print(missing_reporter.to_string(index=False))


# 4. Duplicate incident IDs
print("\n4. DUPLICATE INCIDENT IDs")
print("-" * 60)

duplicate_ids = df[df["incident_id"].duplicated(keep=False)]

print(f"Number of records involved: {len(duplicate_ids)}")
print(duplicate_ids.sort_values("incident_id").to_string(index=False))


# 5. Exact duplicate rows
print("\n5. EXACT DUPLICATE ROWS")
print("-" * 60)

duplicate_rows = df[df.duplicated(keep=False)]

print(f"Number of records involved: {len(duplicate_rows)}")
print(duplicate_rows.sort_values("incident_id").to_string(index=False))


print("\n" + "=" * 60)
print("DETAILED INVESTIGATION COMPLETE")
print("=" * 60)