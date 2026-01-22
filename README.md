**Objective**

To explore and preprocess real-world datasets using Python, Pandas, and Matplotlib, inspecting data structure, handling missing values, visualizing patterns, and drawing insights.

**Scenario Summaries:**

**Scenario 1: E-commerce Sales Data**

**Dataset:** Kaggle – E-commerce Data

**Tasks Performed:**

1.Imported Pandas, Matplotlib, and Seaborn.

2.Loaded the dataset into a Pandas DataFrame.

3.Inspected data using head(), tail(), info(), and describe().

4.Checked for missing values.

5.Visualized product sales using bar and line charts.

**Observations & Inferences:**

1.Columns like CustomerID and InvoiceNo were complete; Description had missing values.

2.Missing descriptions did not heavily affect overall sales trend analysis.

3.Top-selling products and seasonal sales patterns were identified from the charts.

**Scenario 2: Hospital Patient Records**

**Dataset:** Kaggle – Pima Indians Diabetes Database

**Tasks Performed:**

1.Loaded dataset into Pandas.

2.Explored structure and checked for missing or zero-valued health metrics.

3.Visualized glucose levels and age distribution using histograms and boxplots.

**Observations & Inferences:**

1.Some entries had zero values for glucose or blood pressure, treated as missing.

2.Most patients had normal glucose levels; a small fraction were at risk.

3.Age distribution showed most patients were middle-aged, helping identify focus groups for monitoring.

**Scenario 3: Housing Dataset**

**Dataset:** Kaggle – Housing Price Prediction

**Tasks Performed:**

1.Loaded dataset and inspected all columns.

2.Detected and summarized missing values.

3.Visualized correlations between numerical features using scatter plots and heatmaps.

**Observations & Inferences:**

1.Features like GarageType and LotFrontage had missing entries, which were noted or imputed.

2.Scatter plots showed a strong correlation between house size and price.

3.Heatmaps helped identify highly correlated features useful for predictive modeling.

**Scenario 4: Customer Analysis Data**

**Dataset:** Kaggle – Customer Personality Analysis

**Tasks Performed:**

1.Imported dataset into Pandas.

2.Examined structure, null values, and column types.

3.Visualized age, income, and spending patterns using bar and box plots.

**Observations & Inferences:**

1.Minimal missing values, cleaned before analysis.

2.Most customers aged 30–50 with medium-to-high income.

3.Spending patterns revealed higher expenditure on specific categories.

4.Insights can guide targeted banking marketing and product recommendations.
