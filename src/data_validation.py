import pandas as pd


class DataValidator:

    def __init__(self, df):
        self.df = df

    def dataset_shape(self):
        print("\nDataset Shape")
        print("-" * 40)
        print(self.df.shape)

    def columns(self):
        print("\nColumns")
        print("-" * 40)
        print(self.df.columns.tolist())

    def data_types(self):
        print("\nData Types")
        print("-" * 40)
        print(self.df.dtypes)

    def missing_values(self):
        print("\nMissing Values")
        print("-" * 40)
        print(self.df.isnull().sum())

    def duplicate_rows(self):
        print("\nDuplicate Rows")
        print("-" * 40)
        print(self.df.duplicated().sum())

    def statistics(self):
        print("\nStatistical Summary")
        print("-" * 40)
        print(self.df.describe(include="all"))