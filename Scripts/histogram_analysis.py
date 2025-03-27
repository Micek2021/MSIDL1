import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_histograms(file_path: str, output_dir: str) -> None:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} does not exist")

    df = pd.read_csv(file_path, low_memory=False)

    numeric_features = [
        "overall", "potential", "wage_eur", "value_eur",
        "age", "height_cm", "weight_kg"
    ]


    os.makedirs(output_dir, exist_ok=True)

    for feature in numeric_features:
        plt.figure(figsize=(8, 5))
        sns.histplot(df[feature], kde=True, bins=30, color='skyblue', edgecolor='black')
        plt.title(f"Histogram for {feature}")
        plt.xlabel(feature)
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.savefig(os.path.join(output_dir, f"histogram_{feature}.png"))
        plt.close()

if __name__ == "__main__":
    generate_histograms("Data/players_22.csv", "Data/plots/")

print("Done.")