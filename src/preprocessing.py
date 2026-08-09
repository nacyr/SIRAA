import pandas as pd


class DataPreprocessor:
    """
    Cleans and standardizes the SIRA incident dataset.
    """

    def remove_duplicates(self, df):
        """Remove exact duplicate records."""

        df = df.drop_duplicates()

        return df

    def handle_missing_values(self, df):
        """Handle missing values in selected columns."""

        # report_text is required for the ML task
        df = df.dropna(subset=["report_text"])

        # Keep useful records even when these fields are missing
        df["location"] = df["location"].fillna("Unknown")
        df["reported_by"] = df["reported_by"].fillna("Unknown")

        return df

    def clean_report_text(self, df):
        """Clean and standardize incident report text."""

        # Remove leading and trailing spaces
        df["report_text"] = df["report_text"].str.strip()

        # Correct known spelling errors
        corrections = {
            "maintainance": "maintenance",
            "triggred": "triggered",
            "temprature": "temperature",
            "Presssure": "Pressure",
            "Pipline": "Pipeline"
        }

        for wrong, correct in corrections.items():
            df["report_text"] = df["report_text"].str.replace(
                wrong,
                correct,
                case=False,
                regex=False
            )

        # Standardize capitalization
        df["report_text"] = (
            df["report_text"]
            .str.lower()
            .str.capitalize()
        )

        return df

    def clean_location(self, df):
        """Standardize known location variations."""

        location_mapping = {
            "Pipeline7": "Pipeline 7",
            "PlatformA": "Platform A"
        }

        df["location"] = df["location"].replace(
            location_mapping
        )

        return df

    def clean_department(self, df):
        """Standardize department names."""

        department_mapping = {
            "PIPELINE OPERATIONS": "Pipeline Operations",
            "pipeline operations": "Pipeline Operations",
            "Pipeline Ops": "Pipeline Operations"
        }

        df["department"] = df["department"].replace(
            department_mapping
        )

        return df

    def clean_severity(self, df):
        """Standardize severity levels."""

        severity_mapping = {
            "HIGH": "High",
            "high": "High",
            "H": "High",

            "MEDIUM": "Medium",
            "medium": "Medium",
            "M": "Medium",

            "LOW": "Low",
            "low": "Low",
            "L": "Low"
        }

        df["severity"] = df["severity"].replace(
            severity_mapping
        )

        return df

    def clean_date(self, df):
        """Convert mixed date formats into YYYY-MM-DD."""

        df["report_date"] = pd.to_datetime(
            df["report_date"],
            format="mixed",
            dayfirst=True,
            errors="coerce"
        )

        df["report_date"] = df["report_date"].dt.strftime(
            "%Y-%m-%d"
        )

        return df

    def preprocess(self, df):
        """
        Run the complete preprocessing pipeline.
        """

        df = self.remove_duplicates(df)

        df = self.handle_missing_values(df)

        df = self.clean_report_text(df)

        df = self.clean_location(df)

        df = self.clean_department(df)

        df = self.clean_severity(df)

        df = self.clean_date(df)

        return df