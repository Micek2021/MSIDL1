import os

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_data(file_path: str) -> pd.DataFrame:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} does not exist")
    return pd.read_csv(file_path, low_memory=False)


def calculate_numeric_stats(df: pd.DataFrame) -> pd.DataFrame:
    numeric_stats = df.select_dtypes(include=["number"])
    stats = {
        "mean": numeric_stats.mean(),
        "median": numeric_stats.median(),
        "min": numeric_stats.min(),
        "max": numeric_stats.max(),
        "std": numeric_stats.std(),
        "5th percentile": numeric_stats.quantile(0.05),
        "95th percentile": numeric_stats.quantile(0.95),
        "missing values": numeric_stats.isnull().sum()
    }
    return pd.DataFrame(stats)


def calculate_categorical_stats(df: pd.DataFrame) -> pd.DataFrame:
    categorical_stats = df.select_dtypes(include=["object", "category"])
    stats = {
        "unique": categorical_stats.nunique(),
        "missing": categorical_stats.isnull().sum(),
        "class_proportion": categorical_stats.apply(lambda x: x.value_counts(normalize=True).to_dict())
    }
    return pd.DataFrame(stats)


if __name__ == '__main__':
    data = load_data('Data/players_22.csv')

    numeric_stats = calculate_numeric_stats(data)
    categorical_stats = calculate_categorical_stats(data)

    numeric_stats.to_csv('Data/numeric_stats.csv')
    categorical_stats.to_csv('Data/categorical_stats.csv')

    print("Statystyki zapisane do plików CSV.")
