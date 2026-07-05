# Gold Price Analysis Engine

A command-line tool for statistical analysis of historical gold futures prices  summary
statistics, outlier detection, trend analysis, daily price changes, period comparison,
and report export.

## Features

- **Statistical Summary** - mean, median, min, max, range, std dev, variance, percentiles
- **Outlier Detection** - IQR-based outlier flagging
- **Trend Analysis** - compares first half vs. second half average price
- **Daily Price Change** - average, largest increase, largest decrease
- **Period Comparison** - mean difference between two halves of the dataset
- **Export Report** - writes a summary report to `gold_report.txt`

## Requirements

- Python 3.8+
- pandas
- numpy

Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Place your dataset CSV in the project folder, named `Gold Futures Historical Data.csv`
   (or update `FILE_NAME` in `gold_analysis.py` to match your file).
2. Run the script:
   ```bash
   python gold_analysis.py
   ```
3. Choose an option from the menu (1–7).

## Data Source

The dataset used for this analysis (`Gold Futures Historical Data.csv`) was obtained from
[Investing.com](https://www.investing.com/), specifically their historical gold futures
price data page. All rights to the original data belong to Investing.com and its data
providers.

This project uses the data strictly for personal/academic (internship) analysis purposes.
The raw dataset file is **not redistributed** in this repository — see the note below.

> **Note:** Investing.com's terms of use restrict redistribution of their historical data.
> If you want to reproduce this analysis, please download the dataset yourself from
> Investing.com rather than relying on a copy in this repo. The `.gitignore` below keeps
> the CSV out of version control for this reason.

## Project Structure

```
.
├── gold_analysis.py     # Main analysis script
├── requirements.txt      # Python dependencies
├── readme.md             # Project documentation
├── docs
    ├── Screenshots
    └──testcase.md            # Test Run documentation             
└── gold_report.txt       # Generated on running "Export Report" (not tracked)
```

## Disclaimer

This project is for educational/internship purposes only and does not constitute
financial advice. Prices and analysis outputs should not be used for actual trading
or investment decisions.
