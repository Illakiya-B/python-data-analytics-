# Airways Customer Experiance Analytics
Digging into airline passenger reviews using pandas, groupby, and pivot tables.
---
Tech Stack

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange)
![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-4C72B0)
---
## Project Overview
This project analyzes **1,324 British Airways passenger reviews** to answer important business questions such as:

- Which traveller type is the most satisfied?
- Which seat class receives the highest ratings?
- Which aircraft performs best?
- Which routes receive the most reviews?
- Which service factor has the greatest impact on customer satisfaction?
- How likely are passengers to recommend British Airways?

The project demonstrates practical use of **Pandas GroupBy, Pivot Tables, Correlation Analysis, Data Visualization, and Business Reporting**.

---
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
---

#  Sample Outputs

## Reports

```text
customer_report.txt

traveller_analysis.csv

seat_type_analysis.csv

top_routes.csv

aircraft_analysis.csv
```
---

## Visualizations

| Visualization | Description |
|--------------|-------------|
| Rating Distribution | Distribution of overall ratings |
| Traveller Rating | Average rating by traveller type |
| Seat Type Rating | Average rating by seat class |
| Recommendation Distribution | Recommended vs Not Recommended |
| Service Scores | Comparison of service metrics |
| Correlation Heatmap | Relationship among ratings |

## How to run


Clone the repository

```bash
git clone https://github.com/Illakiya-B/british-airways-customer-experience-analytics.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
python customer_experience_analysis.py
```

Outputs a few summary CSVs:
#  Screenshots

Screenshots of outputs and charts are available in the [docs/Screenshots/](./docs/Screenshots) folder.

# 👩‍💻 Author

**Illakiya B**
M.Sc. Data Analytics
Connect with me on **LinkedIn**

[LinkedIn Profile](https://www.linkedin.com/in/illakiya-boopathy-58680630a)

---
