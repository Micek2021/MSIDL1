import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def generate_conditional_histograms(file_path: str, output_dir: str) -> None:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} not found")

    df = pd.read_csv(file_path, low_memory=False)

    numeric_features = [
        "overall", "potential", "wage_eur", "value_eur",
        "age", "height_cm", "weight_kg"
    ]
    category = "preferred_foot"

    missing_cols = [col for col in numeric_features + [category] if col not in df.columns]
    if missing_cols:
        raise KeyError(f"Missing columns: {missing_cols}")

    os.makedirs(output_dir, exist_ok=True)

    for feature in numeric_features:
        plt.figure(figsize=(10, 6))

        sns.histplot(
            data=df.dropna(subset=[category]),
            x=feature,
            hue=category,
            bins=20,
            kde=False,
            alpha=0.7
        )

        plt.title(f"Conditional Distribution: {feature} by Preferred Foot")
        plt.xlabel(feature)
        plt.ylabel("Count")
        plt.savefig(os.path.join(output_dir, f"conditional_histogram_{feature}.png"))
        plt.close()


if __name__ == "__main__":
    generate_conditional_histograms("Data/players_22.csv", "Data/plots/")
    print("Conditional histograms generated successfully.")