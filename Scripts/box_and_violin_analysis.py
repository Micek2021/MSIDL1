import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def generate_plots(file_path: str, output_dir: str) -> None:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} does not exist")

    df = pd.read_csv(file_path, low_memory=False)

    numeric_features = [
        "overall", "potential", "wage_eur", "value_eur",
        "age", "height_cm", "weight_kg"
    ]
    categorical_features = ["preferred_foot"]

    missing_features = [f for f in numeric_features + categorical_features if f not in df.columns]
    if missing_features:
        raise KeyError(f"Brakujące kolumny: {missing_features}")

    os.makedirs(output_dir, exist_ok=True)

    for feature in numeric_features:
        # Boxplot
        plt.figure(figsize=(10, 6))
        sns.boxplot(y=df[feature])
        plt.title(f"Boxplot: {feature}")
        plt.savefig(os.path.join(output_dir, f"boxplot_{feature}.png"), bbox_inches='tight')
        plt.close()

        # Violinplot
        plt.figure(figsize=(10, 6))
        sns.violinplot(y=df[feature])
        plt.title(f"Violinplot: {feature}")
        plt.savefig(os.path.join(output_dir, f"violinplot_{feature}.png"), bbox_inches='tight')
        plt.close()

    for feature in categorical_features:
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=df[feature], y=df["wage_eur"])
        plt.title(f"Rozkład wynagrodzeń względem: {feature}")
        plt.savefig(os.path.join(output_dir, f"boxplot_wage_by_{feature}.png"), bbox_inches='tight')
        plt.close()


if __name__ == "__main__":
    generate_plots("Data/players_22.csv", "Data/plots/")
    print("Analiza zakończona.")