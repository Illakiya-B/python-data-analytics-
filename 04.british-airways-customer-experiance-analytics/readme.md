# Airways Customer Experiance Analytics

Week 4 internship project — digging into airline passenger reviews using pandas, groupby, and pivot tables.

## Data

Dataset: `processed_airline.csv`
Source: [Kaggle](https://www.kaggle.com/) (airline reviews dataset)

It's a cleaned mix of review text (headline, author, content, date) and passenger ratings (seat comfort, food, service, value for money, etc). Rows missing route/aircraft info were dropped, and numeric fields were standardized during preprocessing.

**Columns:** header, author, date, place, content, aircraft, traveller_type, seat_type, route, date_flown, recommended, trip_verified, rating, seat_comfort, cabin_staff_service, food_beverages, ground_service, value_for_money, entertainment

## What I did

- Explored the data (shape, missing values, dtypes)
- Cleaned up dates and rating columns
- Used **groupby** to compare ratings across seat types, traveller types, and routes
- Used **pivot_table** to cross-tab ratings by seat type vs traveller type, and recommendation rate by seat type vs verified trips
- Checked which service factors (comfort, staff, food, etc) correlate most with overall rating

## How to run

``` bash
pip install pandas numpy matplotlib seaborn
python airline_analysis.py
```

Outputs a few summary CSVs:
- summary_by_seat_type.csv
- pivot_rating_seat_vs_traveller.csv
- recommendation_rate_by_traveller.csv

## Findings

_(fill in once run on real data — e.g. which seat type is happiest, which service factor matters most, busiest routes)_

