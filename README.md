# FIFA 22 Player Data Analysis

## Project Setup

### Prerequisites:

- Python 3.9+
- pip package manager

### Installation:

1. Clone the repository:
   ```bash
   git clone [https://github.com/Micek2021/MSIDL1.git]
   cd [MSIDL1]
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

### Output:

The script will generate:

- **Numeric statistics**: `Data/numeric_stats.csv`
- **Categorical statistics**: `Data/categorical_stats.csv`

---

## Project Structure:

```
MSIDL1/
│── Data/
│   ├── numeric_stats.csv
│   ├── categorical_stats.csv
│   ├── players_22.csv
│
│── Scripts/
│   ├── data_analysis_main.py
│
│── venv/
│── requirements.txt
│── README.md
```

---

## Notes:

- Ensure that `players_22.csv` is correctly placed before running the script.
- If running on Windows, use `venv\Scripts\activate` instead of `source venv/bin/activate`.
- Modify the `[URL_DO_REPO]` placeholder to include the actual repository URL before sharing.



