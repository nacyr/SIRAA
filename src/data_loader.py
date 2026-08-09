import pandas as pd


class DataLoader:
    """
    Loads the SIRA incident dataset.
    """

    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        """Load the CSV dataset."""

        df = pd.read_csv(self.file_path)

        return df