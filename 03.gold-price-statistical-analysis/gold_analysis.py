import numpy as np
import pandas as pd

# Load Dataset

FILE_NAME = "Gold Futures Historical Data.csv"
try:
    df = pd.read_csv(FILE_NAME)
except FileNotFoundError:
    print("Dataset not found!")
    exit()

# Remove commas and convert Price column to float
prices = df["Price"].str.replace(",", "", regex=False).astype(float).to_numpy()


# Statistical Summary

def statistical_summary(data):
    print("\n" + "=" * 55)
    print("        GOLD PRICE STATISTICAL SUMMARY")
    print("=" * 55)
    print(f"Total Observations : {len(data)}")
    print(f"Average Price      : {np.mean(data):.2f}")
    print(f"Median Price       : {np.median(data):.2f}")
    print(f"Minimum Price      : {np.min(data):.2f}")
    print(f"Maximum Price      : {np.max(data):.2f}")
    print(f"Range              : {np.ptp(data):.2f}")
    print(f"Standard Deviation : {np.std(data):.2f}")
    print(f"Variance           : {np.var(data):.2f}")
    print("\nPercentiles")
    print("-" * 55)
    print(f"10th Percentile    : {np.percentile(data, 10):.2f}")
    print(f"25th Percentile(Q1): {np.percentile(data, 25):.2f}")
    print(f"50th Percentile    : {np.percentile(data, 50):.2f}")
    print(f"75th Percentile(Q3): {np.percentile(data, 75):.2f}")
    print(f"90th Percentile    : {np.percentile(data, 90):.2f}")


# Outlier Detection

def detect_outliers(data):
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    outliers = data[(data < lower) | (data > upper)]
    print("\n" + "=" * 55)
    print("OUTLIER DETECTION")
    print("=" * 55)
    print(f"Q1          : {q1:.2f}")
    print(f"Q3          : {q3:.2f}")
    print(f"IQR         : {iqr:.2f}")
    print(f"Lower Limit : {lower:.2f}")
    print(f"Upper Limit : {upper:.2f}")
    if len(outliers) == 0:
        print("\nNo Outliers Found")
    else:
        print("\nOutliers")
        print(outliers)


# Trend Analysis

def trend_analysis(data):
    first_half = data[:len(data) // 2]
    second_half = data[len(data) // 2:]
    avg1 = np.mean(first_half)
    avg2 = np.mean(second_half)
    print("\n" + "=" * 55)
    print("TREND ANALYSIS")
    print("=" * 55)
    print(f"Average (First Half)  : {avg1:.2f}")
    print(f"Average (Second Half) : {avg2:.2f}")
    if avg2 > avg1:
        print("\nTrend : Increasing ^")
    elif avg2 < avg1:
        print("\nTrend : Decreasing v")
    else:
        print("\nTrend : Stable -")


# Price Change Analysis

def daily_changes(data):
    changes = np.diff(data)
    print("\n" + "=" * 55)
    print("PRICE CHANGE ANALYSIS")
    print("=" * 55)
    print(f"Average Daily Change : {np.mean(changes):.2f}")
    print(f"Largest Increase     : {np.max(changes):.2f}")
    print(f"Largest Decrease     : {np.min(changes):.2f}")


# Compare Two Periods

def compare_periods(data):
    mid = len(data) // 2
    first = data[:mid]
    second = data[mid:]
    print("\n" + "=" * 55)
    print("PERIOD COMPARISON")
    print("=" * 55)
    print(f"First Half Mean : {np.mean(first):.2f}")
    print(f"Second Half Mean: {np.mean(second):.2f}")
    print(f"\nDifference : {np.mean(second) - np.mean(first):.2f}")


# Export Report

def export_report(data):
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    report = f"""
=============================
 GOLD PRICE REPORT
=============================
Observations : {len(data)}
Mean         : {np.mean(data):.2f}
Median       : {np.median(data):.2f}
Minimum      : {np.min(data):.2f}
Maximum      : {np.max(data):.2f}
Std Dev      : {np.std(data):.2f}
Variance     : {np.var(data):.2f}
Q1           : {q1:.2f}
Q3           : {q3:.2f}
IQR          : {q3 - q1:.2f}
"""
    with open("gold_report.txt", "w") as f:
        f.write(report)
    print("\nReport exported successfully.")


# Menu

def main():
    while True:
        print("\n")
        print("=" * 45)
        print(" GOLD PRICE ANALYSIS ENGINE ")
        print("=" * 45)
        print("1. Statistical Summary")
        print("2. Outlier Detection")
        print("3. Trend Analysis")
        print("4. Daily Price Change")
        print("5. Compare Two Periods")
        print("6. Export Report")
        print("7. Exit")
        choice = input("\nEnter Choice : ")
        if choice == "1":
            statistical_summary(prices)
        elif choice == "2":
            detect_outliers(prices)
        elif choice == "3":
            trend_analysis(prices)
        elif choice == "4":
            daily_changes(prices)
        elif choice == "5":
            compare_periods(prices)
        elif choice == "6":
            export_report(prices)
        elif choice == "7":
            print("\nThank You!")
            break
        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    main()
