# FIFA 22 Player Data Analysis

## Project Setup

### Prerequisites:

- Python 3.9+
- pip package manager

### Installation:

1. Clone the repository:
   ```bash
   git clone https://github.com/Micek2021/MSIDL1.git
   cd MSIDL1
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Dataset preparation:
    - Download the dataset from: [FIFA 22 Complete Player Dataset](https://www.kaggle.com/datasets/stefanoleone992/fifa-22-complete-player-dataset)
    - Place the file `players_22.csv` in the `Data/` directory (create the directory if it does not exist):
      ```bash
      mkdir -p Data
      mv players_22.csv Data/
      ```

### Running the analysis:

To execute the main script, run:
```bash
python Scripts/data_analysis_main.py
```

To generate boxplots and violinplots, run:
```bash
python Scripts/box_and_violin_analysis.py
```

To generate conditional histograms, run:
```bash
python Scripts/conditional_histogram_analysis.py
```

To generate error bars, run:
```bash
python Scripts/error_bars_analysis.py
```

To generate a heatmap of correlations, run:
```bash
python Scripts/heatmap_analysis.py
```

To generate linear regression analysis, run:
```bash
python Scripts/regression_analysis.py
```

To generate histograms, run:
```bash
python Scripts/histogram_analysis.py
```

### Output:

The script will generate:

- **Numeric statistics**: `Data/numeric_stats.csv`  
  *Mean, median, min/max, percentiles, missing values for numerical features*.

- **Categorical statistics**: `Data/categorical_stats.csv`  
  *Number of unique classes, missing values, and class proportions in text format*.

- **Detailed categorical proportions**:  
  *CSV files for each categorical feature stored in `Data/categorical_proportions/`, containing:*
  - Percentage share of classes (e.g., `nationality_name_proportions.csv`),
  - Absolute class frequencies.

- **Boxplots & Violinplots**: PNG files stored in `Data/plots/`, representing selected numerical features.

- **Conditional histograms**: PNG files visualizing distributions by categorical attributes.

- **Error bars**: PNG files showing confidence intervals for numeric features by position.

- **Correlation heatmap**: PNG file showing relationships between selected numerical attributes.

- **Linear regression plots**: PNG file (`regression_analysis.png`) showing regression lines for selected feature pairs.

- **Histograms**: PNG files for selected numerical attributes stored in `Data/plots/`.

---

## Project Structure:

```
MSIDL1/
│── Data/
│   ├── numeric_stats.csv
│   ├── categorical_stats.csv
│   ├── players_22.csv
│   ├── plots/
│   │   ├── boxplot_overall.png
│   │   ├── violinplot_overall.png
│   │   ├── conditional_histogram_overall.png
│   │   ├── error_bars_overall.png
│   │   ├── correlation_heatmap.png
│   │   ├── regression_analysis.png
│   │   ├── histogram_overall.png
│   │   └── ...
│   └── categorical_proportions/
│       ├── nationality_proportions.csv
│       ├── position_proportions.csv
│       └── ... (files for other features)
│
│── Scripts/
│   ├── data_analysis_main.py
│   ├── box_and_violin_analysis.py
│   ├── conditional_histogram_analysis.py
│   ├── error_bars_analysis.py
│   ├── heatmap_analysis.py
│   ├── regression_analysis.py
│   ├── histogram_analysis.py
│── requirements.txt
│── venv/
│── README.md
```

---

## Notes:

- Ensure that `players_22.csv` is correctly placed before running the script.
- If running on Windows, use `venv\Scripts\activate` instead of `source venv/bin/activate`.
- Generated output files are stored in the `Data/` directory.

