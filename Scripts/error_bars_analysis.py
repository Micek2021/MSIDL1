import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_error_bars(file_path: str, output_dir: str) -> None:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} does not exist")

    df = pd.read_csv(file_path, low_memory=False)

    numeric_features = [
        "overall", "potential", "wage_eur", "value_eur",
        "age", "height_cm", "weight_kg"
    ]
    category = "player_positions"

    df[category] = df[category].str.split(",").str[0]

    os.makedirs(output_dir, exist_ok=True)

    for feature in numeric_features:
        plt.figure(figsize=(12, 6))
        sns.pointplot(data=df, x=category, y=feature, errorbar=("ci", 95), capsize=0.2)
        plt.xticks(rotation=90)
        plt.title(f"Error Bars for {feature} by {category}")
        plt.xlabel("Player Position")
        plt.ylabel(feature)
        plt.grid()
        plt.savefig(os.path.join(output_dir, f"error_bars_{feature}.png"))
        plt.close()

if __name__ == "__main__":
    generate_error_bars("Data/players_22.csv", "Data/plots/")
    print("Done.")
