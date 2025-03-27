import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats


def generate_regression_plots(file_path: str, output_dir: str) -> None:
    df = pd.read_csv(file_path, low_memory=False)

    feature_pairs = [
        ('overall', 'value_eur'),
        ('age', 'wage_eur'),
        ('potential', 'overall'),
        ('height_cm', 'weight_kg'),
        ('pace', 'dribbling'),
        ('age', 'power_stamina')
    ]

    plt.figure(figsize=(18, 15))
    sns.set_style("whitegrid")

    for i, (x_feature, y_feature) in enumerate(feature_pairs, 1):
        plt.subplot(3, 2, i)

        subset = df[[x_feature, y_feature]].dropna()

        slope, intercept, r_value, p_value, std_err = stats.linregress(
            subset[x_feature], subset[y_feature]
        )

        ax = sns.regplot(
            data=subset,
            x=x_feature,
            y=y_feature,
            scatter_kws={'alpha': 0.3, 'color': '#2c7bb6'},
            line_kws={'color': '#d7191c', 'label': f'y = {slope:.2f}x + {intercept:.2f}\nR² = {r_value ** 2:.2f}'}
        )

        plt.title(f"{y_feature} vs {x_feature}", fontsize=14)
        plt.xlabel(x_feature, fontsize=12)
        plt.ylabel(y_feature, fontsize=12)
        plt.legend(fontsize=10)

    plt.tight_layout()
    plt.savefig(f"{output_dir}/regression_analysis.png", dpi=200)
    plt.close()


if __name__ == "__main__":
    generate_regression_plots("Data/players_22.csv", "Data/plots/")
    print("Regression analysis complete.")