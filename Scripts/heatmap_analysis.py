import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os


def generate_full_heatmap(file_path: str, output_dir: str) -> None:
    df = pd.read_csv(file_path, low_memory=False)

    selected_features = [
        'overall', 'potential', 'wage_eur', 'age',
        'height_cm', 'weight_kg',
        'pace', 'shooting', 'passing', 'dribbling',
        'defending', 'physic', 'power_stamina'
    ]

    filtered_df = df[selected_features].dropna()
    corr_matrix = filtered_df.corr()

    plt.figure(figsize=(14, 12))

    sns.heatmap(
        data=corr_matrix,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        vmin=-1,
        vmax=1,
        linewidths=0.5,
        square=True,
        annot_kws={"size": 9},
        cbar_kws={"shrink": 0.8}
    )

    plt.title("Football Attributes Correlation Matrix", fontsize=14, pad=15)
    plt.xticks(
        rotation=45,
        ha='right',
        fontsize=10,
        fontweight='bold'
    )
    plt.yticks(
        rotation=0,
        fontsize=10,
        fontweight='bold'
    )

    plt.subplots_adjust(left=0.2, right=0.95, top=0.93, bottom=0.3)

    os.makedirs(output_dir, exist_ok=True)

    plt.savefig(
        f"{output_dir}/correlation_heatmap.png",
        dpi=120,
        bbox_inches='tight'
    )
    plt.close()


if __name__ == "__main__":
    generate_full_heatmap("Data/players_22.csv", "Data/plots/")
    print("Heatmap generated.")