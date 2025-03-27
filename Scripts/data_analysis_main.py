import os

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_data(file_path: str) -> pd.DataFrame:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} does not exist")
    return pd.read_csv(file_path, low_memory=False)


def calculate_numeric_stats(df: pd.DataFrame) -> pd.DataFrame:
    numeric_stats = df.select_dtypes(include=["number"]).drop(columns=["sofifa_id"], errors="ignore")
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
        "class_proportion": categorical_stats.apply(
            lambda x: "; ".join([f"{k}: {v * 100:.2f}%" for k, v in x.value_counts(normalize=True).items()])
        )
    }
    stats_df = pd.DataFrame(stats)

    proportions_dir = os.path.join("Data", "categorical_proportions")
    os.makedirs(proportions_dir, exist_ok=True)

    for column in categorical_stats.columns:
        proportions = categorical_stats[column].value_counts(normalize=True).mul(100).round(2).reset_index()
        proportions.columns = ["class", "proportion (%)"]

        counts = categorical_stats[column].value_counts().reset_index()
        counts.columns = ["class", "count"]

        proportions = pd.merge(proportions, counts, on="class")

        proportions.to_csv(os.path.join(proportions_dir, f"{column}_proportions.csv"), index=False)

    return stats_df

if __name__ == '__main__':
    os.makedirs("Data", exist_ok=True)
    data = load_data('Data/players_22.csv')

    numeric_stats = calculate_numeric_stats(data)
    categorical_stats = calculate_categorical_stats(data)

    numeric_stats.to_csv('Data/numeric_stats.csv')
    categorical_stats.to_csv('Data/categorical_stats.csv')

    print("Done.")
