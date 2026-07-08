import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ==========================
# CREATE OUTPUT DIRECTORIES
# ==========================

os.makedirs("reports", exist_ok=True)
os.makedirs("visualizations", exist_ok=True)
plt.style.use("ggplot")

# Configuration
# Change path accordingly to dataset folder of your own
DATA_FILE = "preprocessed_airline_dataset.csv"

# ------------
# Load Dataset
# ------------

def load_data():
    """Load the dataset."""

    try:
        df = pd.read_csv(DATA_FILE)

        print("✓ Dataset loaded successfully.")
        print(f"Total Records : {len(df)}")

        return df

    except FileNotFoundError:
        print("✗ Dataset not found.")
        return None


# ----------------
# Dataset Overview
# ----------------

def dataset_overview(df):

    print("\n" + "=" * 60)
    print("DATASET OVERVIEW")
    print("=" * 60)

    print(f"Rows              : {df.shape[0]}")
    print(f"Columns           : {df.shape[1]}")
    print(f"Duplicate Records : {df.duplicated().sum()}")

    print("\nColumn Names")
    print("-" * 60)

    for column in df.columns:
        print(column)

    print("\nData Types")
    print("-" * 60)
    print(df.dtypes)

    print("\nMissing Values")
    print("-" * 60)
    print(df.isnull().sum())
# -------------------
# Dataset Validation
# -------------------

def inspect_key_columns(df):

    print("\n" + "=" * 60)
    print("KEY COLUMN INSPECTION")
    print("=" * 60)

    print("\nUnique values - Recommended")
    print(df["recommended"].unique())

    print("\nUnique values - Trip Verified")
    print(df["trip_verified"].unique())

    print("\nSample 'date' values")
    print(df["date"].head(10))

    print("\nSample 'date_flown' values")
    print(df["date_flown"].head(10))
# ==================
# DATA PREPARATION
# ===================

def prepare_data(df):

    print("\n" + "=" * 65)
    print("DATA PREPARATION")
    print("=" * 65)

    # --------------------
    # Convert Date Columns
    # --------------------

    date_columns = ["date", "date_flown"]

    for col in date_columns:

        if col in df.columns:

            df[col] = pd.to_datetime(
                df[col],
                format="%d-%m-%Y",
                errors="coerce"
            )

    print(" Date columns converted to datetime.")
  # ------------------------
    # Convert Yes / No Columns
    # ------------------------

    df["recommended"] = (
        df["recommended"]
        .str.lower()
        .str.strip()
        .map({
            "yes": 1,
            "no": 0
        })
    )

    df["trip_verified"] = (
        df["trip_verified"]
        .str.lower()
        .str.strip()
        .map({
            "verified": 1,
            "not verified": 0
        })
    )

    print(" Recommendation columns converted.")
 # --------------------
    # Fill Missing Values
    # --------------------

    df["traveller_type"] = df["traveller_type"].fillna("Unknown")

    print(" Missing traveller type filled.")

    # -----------------------
    # Convert Numeric Columns
    # -----------------------

    numeric_columns = [

        "rating",

        "seat_comfort",

        "cabin_staff_service",

        "food_beverages",

        "ground_service",

        "value_for_money",

        "entertainment"

    ]

    for col in numeric_columns:

        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

    print(" Numeric columns verified.")

    # ----------------------
    # Create Useful Features
    # ----------------------

    df["review_year"] = df["date"].dt.year

    df["review_month"] = df["date"].dt.month_name()

    df["flight_year"] = df["date_flown"].dt.year

    df["flight_month"] = df["date_flown"].dt.month_name()

    print(" Date features extracted.")

    return df

# ====================
# PREPARATION SUMMARY
# ====================

def preparation_summary(df):

    print("\n" + "=" * 65)
    print("PREPARATION SUMMARY")
    print("=" * 65)

    print(f"Dataset Shape       : {df.shape}")

    print(f"Duplicate Records   : {df.duplicated().sum()}")

    print(f"Missing Values      : {df.isnull().sum().sum()}")

    print("\nMissing Values by Column")
    print("-" * 65)
      print(df.isnull().sum())

    print("\nUpdated Data Types")
    print("-" * 65)

    print(df.dtypes)

    print("\nDataset is ready for business analysis.")

# ===============================
# CUSTOMER SATISFACTION ANALYSIS
# ===============================

def customer_satisfaction_analysis(df):

    print("\n" + "=" * 65)
    print("CUSTOMER SATISFACTION ANALYSIS")
    print("=" * 65)

    avg_rating = df["rating"].mean()
    median_rating = df["rating"].median()
    highest_rating = df["rating"].max()
    lowest_rating = df["rating"].min()

    recommendation_rate = df["recommended"].mean() * 100
    verified_rate = df["trip_verified"].mean() * 100

    print(f"Average Rating           : {avg_rating:.2f}/10")
    print(f"Median Rating            : {median_rating:.2f}")
    print(f"Highest Rating           : {highest_rating}")
    print(f"Lowest Rating            : {lowest_rating}")
    print(f"Recommendation Rate      : {recommendation_rate:.2f}%")
    print(f"Verified Reviews         : {verified_rate:.2f}%")

    return {
        "Average Rating": avg_rating,
        "Recommendation Rate": recommendation_rate,
        "Verified Reviews": verified_rate
    }


# ========================
# TRAVELLER TYPE ANALYSIS
# ========================

def traveller_analysis(df):

    print("\n" + "=" * 65)
    print("TRAVELLER TYPE ANALYSIS")
    print("=" * 65)

    summary = (
        df.groupby("traveller_type")
        .agg(
            Reviews=("rating", "count"),
            Avg_Rating=("rating", "mean"),
            Recommendation_Rate=("recommended", "mean"),
            Avg_Value_For_Money=("value_for_money", "mean")
        )
        .round(2)
    )

    summary["Recommendation_Rate"] *= 100

    print(summary)

    summary.to_csv(
        "reports/traveller_analysis.csv",
        index=True
    )

    return summary


# ==================
# SEAT TYPE ANALYSIS
# ==================

def seat_type_analysis(df):

    print("\n" + "=" * 65)
    print("SEAT TYPE ANALYSIS")
    print("=" * 65)

    seat_summary = (
        df.groupby("seat_type")
        .agg(
            Reviews=("rating", "count"),
            Avg_Rating=("rating", "mean"),
            Seat_Comfort=("seat_comfort", "mean"),
            Value_For_Money=("value_for_money", "mean"),
            Recommendation=("recommended", "mean")
        )
        .round(2)
    )

    seat_summary["Recommendation"] *= 100

    print(seat_summary)

    seat_summary.to_csv(
        "reports/seat_type_analysis.csv",
        index=True
    )

    return seat_summary


# ===============
# ROUTE ANALYSIS
# ===============

def route_analysis(df):

    print("\n" + "=" * 65)
    print("ROUTE ANALYSIS")
    print("=" * 65)

    top_routes = (
        df.groupby("route")
        .agg(
            Reviews=("rating", "count"),
            Avg_Rating=("rating", "mean")
        )
        .sort_values(
            by="Reviews",
            ascending=False
        )
        .head(10)
        .round(2)
    )

    print(top_routes)

    top_routes.to_csv(
        "reports/top_routes.csv",
        index=True
    )

    return top_routes


# ==================
# AIRCRAFT ANALYSIS
# ==================

def aircraft_analysis(df):

    print("\n" + "=" * 65)
    print("AIRCRAFT ANALYSIS")
    print("=" * 65)

    aircraft = (
        df.groupby("aircraft")
        .agg(
            Reviews=("rating", "count"),
            Avg_Rating=("rating", "mean"),
            Seat_Comfort=("seat_comfort", "mean"),
            Entertainment=("entertainment", "mean")
        )
        .sort_values(
            by="Reviews",
            ascending=False
        )
        .head(10)
        .round(2)
    )

    print(aircraft)

    aircraft.to_csv(
        "reports/aircraft_analysis.csv",
        index=True
    )

    return aircraft


# ========================
# SERVICE QUALITY ANALYSIS
# ========================

def service_quality_analysis(df):

    print("\n" + "=" * 65)
    print("SERVICE QUALITY ANALYSIS")
    print("=" * 65)

    service_columns = [

        "seat_comfort",

        "cabin_staff_service",

        "food_beverages",
      
        "ground_service",

        "value_for_money",

        "entertainment"

    ]

    summary = pd.DataFrame({

        "Average Score": df[service_columns].mean().round(2),

        "Minimum": df[service_columns].min(),

        "Maximum": df[service_columns].max()

    })

    print(summary)

    summary.to_csv(
        "reports/service_quality_summary.csv",
        index=True
    )

    return summary
  
# ====================
# MONTHLY REVIEW TREND
# ====================

def monthly_review_analysis(df):

    print("\n" + "=" * 65)
    print("MONTHLY REVIEW TREND")
    print("=" * 65)

    monthly = (
        df.groupby(
            ["review_year", "review_month"]
        )
        .size()
        .reset_index(name="Reviews")
    )

    print(monthly.head(15))

    monthly.to_csv(
        "reports/monthly_review_trend.csv",
        index=False)

    return monthly

# ===========================
# EXECUTIVE BUSINESS INSIGHTS
# ===========================

def executive_insights(df):

    print("\n" + "="*65)
    print("EXECUTIVE BUSINESS INSIGHTS")
    print("="*65)

    # -------------------
    # Best Traveller Type
    # -------------------
    
    traveller = (
        df.groupby("traveller_type")["rating"]
        .mean()
        .sort_values(ascending=False)
    )

    best_traveller = traveller.idxmax()
    worst_traveller = traveller.idxmin()


    print(f"\nBest Traveller Type  : {best_traveller}")
    print(f"Average Rating       : {traveller.max():.2f}")

    print(f"\nLowest Rated Traveller : {worst_traveller}")
    print(f"Average Rating         : {traveller.min():.2f}")

    # --------------
    # Best Seat Type
    # --------------

    seat = (
        df.groupby("seat_type")["rating"]
        .mean()
        .sort_values(ascending=False)
    )

    print("\nHighest Rated Seat Type")
    print("-------------------------")

    print(f"{seat.idxmax()} ({seat.max():.2f})")

    # -------------
    # Best Aircraft
    # -------------

    aircraft = (
        df.groupby("aircraft")["rating"]
        .mean()
        .sort_values(ascending=False)
    )
    print("\nHighest Rated Aircraft")

    print(f"{aircraft.idxmax()} ({aircraft.max():.2f})")

    # -------------------
    # Most Reviewed Route
    # -------------------

    routes = df["route"].value_counts()

    print("\nMost Reviewed Route")

    print(routes.head(5))

    # -----------------------
    # Service Factor Rankings
    # -----------------------

    service_cols = [

        "seat_comfort",

        "cabin_staff_service",

        "food_beverages",

        "ground_service",

        "value_for_money",

        "entertainment"

    ]

    ranking = df[service_cols].mean().sort_values(ascending=False)

    print("\nService Ranking")

    print(ranking)

    return ranking

# ============
# PIVOT TABLES
# ============

def pivot_tables(df):

    print("\n" + "="*65)
    print("PIVOT TABLE ANALYSIS")
    print("="*65)

    # -------------------------------------------------

    pivot1 = pd.pivot_table(

        df,

        values="rating",

        index="seat_type",

        columns="traveller_type",

        aggfunc="mean"
    ).round(2)

    print("\nAverage Rating")

    print(pivot1)

    pivot1.to_csv("reports/pivot_rating.csv")

    # -------------------------------------------------

    pivot2 = pd.pivot_table(

        df,

        values="recommended",

        index="seat_type",

        columns="trip_verified",

        aggfunc="mean"

    ).round(2)

    print("\nRecommendation Rate")

    print(pivot2)

    pivot2.to_csv("reports/pivot_recommendation.csv")

    return pivot1, pivot2
# =====================
# CORRELATION ANALYSIS
# ======================

def correlation_analysis(df):

    print("\n" + "="*65)
    print("CORRELATION ANALYSIS")
    print("="*65)

    columns = [

        "rating",

        "seat_comfort",

        "cabin_staff_service",

        "food_beverages",

        "ground_service",

        "value_for_money",

        "entertainment"

    ]

    corr = df[columns].corr()

    print(corr)
    corr.to_csv("reports/correlation_matrix.csv")

    print("\nCorrelation with Overall Rating")

    print(corr["rating"].sort_values(ascending=False))

    return corr

# =====================
# TOP & BOTTOM INSIGHTS
# ======================

def top_bottom_analysis(df):

    print("\n" + "="*65)
    print("TOP & BOTTOM INSIGHTS")
    print("="*65)

    print("\nTop 5 Highest Rated Reviews")

    print(

        df[

            [

                "author",

                "route",

                "aircraft",

                "rating"

            ]

        ]

        .sort_values(

            by="rating",

            ascending=False

        )

        .head()

    )

    print("\nBottom 5 Lowest Rated Reviews")

    print(

        df[

            [

                "author",

                "route",

                "aircraft",
                "rating"

            ]

        ]

        .sort_values(

            by="rating"

        )

        .head()

    )

# =====================
# VISUALIZATION 1
# RATING DISTRIBUTION
# =====================

def plot_rating_distribution(df):

    plt.figure(figsize=(8,5))

    df["rating"].hist(bins=10)

    plt.title("Overall Rating Distribution")
    plt.xlabel("Rating")
    plt.ylabel("Number of Reviews")

    plt.tight_layout()
    plt.savefig("visualizations/rating_distribution.png")

    plt.close()

    print(" Saved : rating_distribution.png")

# =================
# VISUALIZATION 2
# =================

def plot_traveller_rating(df):

    data = df.groupby("traveller_type")["rating"].mean().sort_values()

    plt.figure(figsize=(8,5))

    data.plot(kind="barh")

    plt.title("Average Rating by Traveller Type")

    plt.xlabel("Average Rating")

    plt.tight_layout()

    plt.savefig("visualizations/traveller_rating.png")

    plt.close()

    print(" Saved : traveller_rating.png")
# ================
# VISUALIZATION 3
# ================

def plot_seat_rating(df):

    data = df.groupby("seat_type")["rating"].mean()

    plt.figure(figsize=(8,5))

    data.plot(kind="bar")

    plt.title("Average Rating by Seat Type")

    plt.ylabel("Rating")

    plt.tight_layout()

    plt.savefig("visualizations/seat_rating.png")

    plt.close()

    print(" Saved : seat_rating.png")
# ================
# VISUALIZATION 4
# ================

def plot_recommendation(df):

    plt.figure(figsize=(6,6))

    df["recommended"].value_counts().plot(
        kind="pie",
        autopct="%1.1f%%"
    )

    plt.ylabel("")

    plt.title("Recommendation Distribution")

    plt.tight_layout()

    plt.savefig("visualizations/recommendation_distribution.png")

    plt.close()

    print(" Saved : recommendation_distribution.png")
# ================
# VISUALIZATION 5
# ==================

def plot_service_scores(df):

    service = [

        "seat_comfort",

        "cabin_staff_service",

        "food_beverages",

        "ground_service",

        "value_for_money",

        "entertainment"

    ]

    scores = df[service].mean()

    plt.figure(figsize=(10,5))

    scores.plot(kind="bar")

    plt.title("Average Service Scores")

    plt.ylabel("Average Score")

    plt.tight_layout()

    plt.savefig("visualizations/service_scores.png")

    plt.close()

    print(" Saved : service_scores.png")

# ================
# VISUALIZATION 6
# =================

def plot_correlation(df):

    columns = [

        "rating",

        "seat_comfort",

        "cabin_staff_service",

        "food_beverages",

        "ground_service",

        "value_for_money",

        "entertainment"

    ]

    plt.figure(figsize=(8,6))

    sns.heatmap(

        df[columns].corr(),

        annot=True,

        cmap="Blues"

    )

    plt.title("Correlation Heatmap")

    plt.tight_layout()

    plt.savefig("visualizations/correlation_heatmap.png")

    plt.close()

    print(" Saved : correlation_heatmap.png")
# ================
# GENERATE REPORT
# =================

def generate_report(df):

    avg_rating = df["rating"].mean()

    recommendation = df["recommended"].mean()*100

    verified = df["trip_verified"].mean()*100

    top_traveller = (
        df.groupby("traveller_type")["rating"]
        .mean()
        .idxmax()
    )

    best_seat = (
        df.groupby("seat_type")["rating"]
        .mean()
        .idxmax()
    )

    top_route = df["route"].value_counts().idxmax()

    report = f"""
========================================================

BRITISH AIRWAYS CUSTOMER EXPERIENCE REPORT

========================================================

Total Reviews :
{len(df)}

Average Rating :
{avg_rating:.2f}

Recommendation Rate :
{recommendation:.2f}%

Verified Reviews :
{verified:.2f}%

Highest Rated Traveller :
{top_traveller}

Highest Rated Seat :
{best_seat}

Most Reviewed Route :
{top_route}

========================================================

End of Report

========================================================

"""

    with open("reports/customer_report.txt","w") as f:

        f.write(report)

    print("✓ Saved : customer_report.txt")
# ------
# Main
# ------

def main():

    df = load_data()

    if df is None:
        return

    dataset_overview(df)

    inspect_key_columns(df)

    df = prepare_data(df)

    preparation_summary(df)

    customer_satisfaction_analysis(df)

    traveller_analysis(df)

    seat_type_analysis(df)

    route_analysis(df)

    aircraft_analysis(df)

    service_quality_analysis(df)

    monthly_review_analysis(df)

    executive_insights(df)
    
    pivot_tables(df)
    
    correlation_analysis(df)
    
    top_bottom_analysis(df)

    plot_rating_distribution(df)

    plot_traveller_rating(df)

    plot_seat_rating(df)

    plot_recommendation(df)

    plot_service_scores(df)
    
    plot_correlation(df)

    generate_report(df)

if __name__ == "__main__":
    main()
