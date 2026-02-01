# Exploratory Data Analysis: Store Transaction Data Imputation

## Problem Statement

Build an imputation/extrapolation model to fill missing data gaps in store-level POS data. Stores share data ranging from 2 to 28 days in a month, and certain transactions may not be scanned/recorded.

## Dataset Overview

### Files:
1. **Hackathon_Ideal_Data.csv**: Complete monthly aggregated data for 10 stores (P1-P10) for 3 months
2. **Hackathon_Working_Data.csv**: Transaction-level incomplete data for 10 stores (N1-N10) with day-level granularity
3. **Hackathon_Validation_Data.csv**: Store-category-month combinations requiring predictions
4. **Hackathon_Mapping_File.csv**: Column descriptions and data dictionary

## Key Questions Explored

### Question 1: What is the overall structure and completeness of the datasets?
**Detailed answer**:  
We first profiled both `Hackathon_Ideal_Data` (P-stores) and `Hackathon_Working_Data` (N-stores) to understand shapes, column types, value ranges for `QTY`, `VALUE`, `PRICE`, `BILL_AMT`, and the presence of missing values. We checked the number of unique stores, months, and (for working data) days, and verified that the mapping file correctly describes each field. Summary statistics highlighted the typical scale of sales per line item and per store–month, as well as any outliers or zeros.

**Why this is important for our project**:  
Before designing any imputation or forecasting logic, we must be sure what each dataset actually represents (ideal monthly aggregates vs. incomplete daily transactions), and that the fields we intend to use are clean and consistent. If we misunderstand data structure (for example, mixing bill-level and store-level granularity) the whole model will be biased or invalid.

**What we get from this analysis**:
- Clarity on **granularity**: ideal data is monthly store–brand aggregates, working data is transaction/day level.  
- Confirmation that key numeric fields are usable and mostly non-null.  
- A baseline understanding of data scale to choose appropriate models and evaluation metrics.

### Question 2: How many days of data are available per store per month?
**Detailed answer**:  
We grouped the working data by `STORECODE` and `MONTH` and counted distinct `DAY` values to compute `DAYS_COUNT` for each store–month. We then summarized and visualized this as a bar chart (days per store–month) and a histogram. This showed that some store–months have close to 28 days of data, while others have only a handful (down to ~2 days).

**Why this is important for our project**:  
The **core business problem** is that stores transmit only a subset of days. Knowing exactly how many days are observed per store–month tells us:
- where naive extrapolation is relatively safe (e.g., 20–28 days observed), and  
- where predictions will be highly uncertain (e.g., 2–5 days observed).  
This directly drives our **data-quality flags**, our confidence scores, and possibly different modeling strategies for high- vs low-coverage store–months.

**What we get from this analysis**:
- A per–store–month **coverage table** (`DAYS_COUNT`) that can be used as a model feature.  
- Identification of **high-risk cases** (very low coverage) where we may need stronger priors or category-level borrowing.  
- A visual explanation we can show stakeholders to justify why some predictions are less confident than others.

### Question 3: What is the sales volume and value distribution across stores and months?
**Detailed answer**:  
We aggregated working data by `STORECODE` and `MONTH` to compute `TOTAL_QTY`, `TOTAL_VALUE`, number of unique bills (`NUM_TRANSACTIONS`), and `NUM_DAYS`, and derived `AVG_TRANSACTION_VALUE` and `AVG_DAILY_VALUE`. Visualizations show how total and average sales differ by store and by month, and the distribution of `TOTAL_VALUE` across all store–months.

**Why this is important for our project**:  
Stores do not behave identically. Some are high‑volume, some low; some have more expensive baskets. Imputation models that ignore these differences will under‑ or over‑estimate sales for specific stores. Understanding these distributions helps us:
- decide whether to build **global models** or **store-segmented models**, and  
- set realistic **upper and lower bounds** on imputed values for each store.

**What we get from this analysis**:
- Quantitative evidence that **store effects** are strong and must be modeled.  
- A sense of which stores are **revenue-critical** and thus where accurate imputation matters most.  
- Reference distributions to check that imputed values remain within plausible ranges.

### Question 4: How do categories (GRP) contribute to total sales?
**Detailed answer**:  
We grouped transactions by `GRP` (category) to compute total and average `VALUE`, transaction counts, and total `QTY`. We ranked categories by `TOTAL_VALUE` and plotted the top 10–15 categories using bar and pie charts to understand their share of overall revenue.

**Why this is important for our project**:  
Imputation at the **store–category** level is exactly what the validation file requires. Some categories are extremely important for total revenue and for downstream applications like planogram optimization (e.g., biscuits, chocolate, packaged tea), while many long‑tail categories contribute little. For high‑value categories we may want more sophisticated models; for low‑impact ones, simpler rules may suffice.

**What we get from this analysis**:
- A prioritized list of **high-impact categories** where accurate imputation has the biggest business value.  
- Evidence that categories have different sales magnitudes, which supports category‑specific modeling or feature engineering.  
- A way to sanity‑check category‑level imputations (e.g., category share of store revenue should stay within a reasonable band).

### Question 5: What is the relationship between number of days and total sales value?
**Detailed answer**:  
Using the store–month aggregates, we correlated `NUM_DAYS` with `TOTAL_VALUE` and plotted a scatter with a fitted trend line. The correlation is strongly positive: store–months with more observed days almost always have higher reported sales, roughly proportional to days observed.

**Why this is important for our project**:  
This is the **core statistical justification** for extrapolation. If total sales scaled poorly with days (e.g., no or very weak correlation), then using `(observed value / observed days) × full days` would be unsafe. The strong linear pattern tells us that, at least on average, sales per day are relatively stable within a store–month and extrapolation is a reasonable first‑order approach.

**What we get from this analysis**:
- Empirical support for a **baseline imputation formula**: `Predicted_Total_Value ≈ (Observed_Total_Value / NUM_DAYS) × 28`.  
- A feature (`NUM_DAYS`) that explains a large portion of variance in `TOTAL_VALUE`.  
- A visual argument to share with business stakeholders on why extrapolation is mathematically grounded.

### Question 6: How consistent is average daily sales across different numbers of days?
**Detailed answer**:  
We examined `AVG_DAILY_VALUE` as a function of `NUM_DAYS`, computing mean and standard deviation per `NUM_DAYS` bucket, and visualized this with boxplots and error bars. While there is noise, average daily sales remain within a relatively stable band for many day-counts, with some increase in variance at low `NUM_DAYS`.

**Why this is important for our project**:  
Extrapolation assumes that the **observed days are representative** of the unobserved days. If average daily sales systematically changed with `NUM_DAYS` (e.g., stores only uploading high‑sales days), the extrapolated monthly sales would be biased. Seeing reasonable stability suggests that using daily averages is acceptable, but the higher variance at low coverage warns us to treat those predictions with lower confidence.

**What we get from this analysis**:
- Validation that **average daily sales** is a usable signal for imputation.  
- A quantitative understanding of **uncertainty vs. coverage** (fewer days → more variance), which we can translate into confidence scores.  
- Motivation to complement simple extrapolation with additional features (category mix, store type, etc.) especially when `NUM_DAYS` is small.

### Question 7: Which stores and months have the most incomplete data?
**Detailed answer**:  
From `DAYS_COUNT` we computed a completeness percentage (`COMPLETENESS_PCT = DAYS_COUNT / 28 × 100`) per store–month and visualized it with a heatmap and histogram. This clearly highlights which store–month combinations are close to fully observed and which are extremely sparse (e.g., <10% completeness).

**Why this is important for our project**:  
Different completeness levels should drive **different modeling choices and risk communication**. For nearly full months, simple extrapolation is fine and risk is low. For heavily missing months, we may want to borrow strength from ideal data, similar stores, or category benchmarks, and explicitly flag those predictions as low‑confidence in any dashboard or downstream system.

**What we get from this analysis**:
- A ready‑to‑use **coverage feature** (`COMPLETENESS_PCT`) for the model.  
- A list of **critical gaps** where we might prioritize additional business rules or manual review.  
- A transparent story for stakeholders about where the data is weakest and how the model handles it.

### Question 8: How do brands and companies contribute to sales?
**Detailed answer**:  
We grouped transactions by `CMP` (company), `MBRD` (mother brand), and `BRD` (brand) to calculate total sales value, quantity, and transaction counts. Sorting by `TOTAL_VALUE` and plotting the top companies/brands reveals a highly concentrated market: a small number of FMCG players contribute a large share of category sales.

**Why this is important for our project**:  
For both **imputation** and any future **planogram optimization** work, understanding which brands drive revenue is crucial. When data is missing, it is more important to get big brands right than long‑tail SKUs. Company/brand identifiers also act as powerful categorical features for any ML model, capturing pricing power, promotion intensity, and brand loyalty patterns.

**What we get from this analysis**:
- A ranking of **key companies and brands** to prioritize in modeling and validation.  
- Justification for including brand/company as features and possibly applying **brand‑level shrinkage** when data is sparse.  
- A better link between this imputation work and later **SKU performance scoring** or **planogram optimization** modules.

### Question 9: What is the relationship between transaction count and sales value?
**Detailed answer**:  
We aggregated by store–month to compute `NUM_TRANSACTIONS` (unique `BILL_ID`) and `TOTAL_VALUE`, then measured their correlation and visualized a scatter with a trend line. As expected, months with more transactions typically have higher sales, with a strong positive correlation. We also examined the distribution of `AVG_TRANSACTION_VALUE`.

**Why this is important for our project**:  
Even if some item‑level details are missing, **transaction volume** is a strong proxy for store activity. In imputation, we can use `NUM_TRANSACTIONS` together with `NUM_DAYS` to refine predictions—e.g., two store–months with the same number of days but different transaction counts should not have the same total value. For future analytics (like identifying lost sales due to poor shelf placement), transaction metrics are also key.

**What we get from this analysis**:
- Confirmation that `NUM_TRANSACTIONS` is a **high-signal feature** for predicting sales.  
- Insight into **basket size / ticket value** via `AVG_TRANSACTION_VALUE`, which can help detect anomalies in imputed data.  
- Another handle to distinguish low‑traffic vs high‑traffic stores when extrapolating from partial data.

### Question 10: How do sales vary by day of month? Are there weekly patterns?
**Detailed answer**:  
We aggregated by `DAY` to compute total and average `VALUE` and transaction counts, then derived an approximate `DAY_NAME` (Mon–Sun). Line charts show how sales evolve over the days of the month, while bar charts by day of week highlight systematic patterns (e.g., higher sales on weekends or pay‑day spikes).

**Why this is important for our project**:  
If specific days (e.g., weekends) are structurally higher or lower, and those days happen to be missing in the working data, naive extrapolation from the remaining days will be biased. Incorporating **day-of-week effects** into the model lets us adjust imputed daily values depending on which days are observed. For a future merchandiser dashboard or planogram simulator, temporal patterns also matter for understanding promotions and seasonality.

**What we get from this analysis**:
- Evidence that **temporal features** (day-of-week, day-of-month) should be included in the model.  
- An understanding of how missing particular days (e.g., always missing Sundays) could skew results.  
- A foundation for more advanced time‑series or seasonality-aware models if we decide to build them.

### Question 11: What categories need to be predicted in the validation dataset?
**Detailed answer**:  
We inspected `Hackathon_Validation_Data` to count how many rows (store–month–category combinations) require `TOTALVALUE` predictions, and how these are distributed across stores and categories. The result is that every N-store and each month appears across many categories, leading to a large number of required outputs, with some categories requested more frequently than others.

**Why this is important for our project**:  
This defines the **target space** for our model. Knowing which combinations appear in the validation set ensures we engineer features that can be computed for all of them, and that we focus extra effort on categories that appear most often or drive more revenue. It also tells us the expected **scale of deployment** (thousands of predictions per refresh).

**What we get from this analysis**:
- A clear list of **prediction targets** (store, month, category triples).  
- A sense of workload and performance needs for any production scoring pipeline.  
- Guidance on which categories/stores to inspect first when validating model quality.

## Key Insights

1. **Data Completeness**: Stores have varying levels of data completeness (2-28 days per month)
2. **Days-Value Relationship**: Strong correlation suggests extrapolation is feasible
3. **Average Daily Value**: Can be used as a baseline for imputation
4. **Category Patterns**: Different categories show different sales patterns
5. **Store Characteristics**: Stores have different product mixes and sales volumes
6. **Temporal Patterns**: Day-of-week and day-of-month patterns exist
7. **Transaction Patterns**: Number of transactions correlates with sales value

## Recommended Imputation Strategies

1. **Extrapolation Method**: Use average daily value × remaining days for missing days
2. **Category-Level Imputation**: Impute at category level, then aggregate
3. **Store-Specific Models**: Build models that account for store characteristics
4. **Temporal Features**: Include day-of-week, day-of-month as features
5. **Hybrid Approach**: Combine multiple methods (extrapolation, regression, time series)

## Running the EDA

```bash
cd Store_Transaction_data
python eda_store_transaction.py
```

The script will:
- Load all datasets
- Perform comprehensive analysis
- Generate visualizations (saved in `figures/` directory)
- Print key findings and statistics

## Output Files

All visualizations are saved in the `figures/` directory:
- `q2_days_per_store_month.png`: Days of data availability
- `q3_sales_distribution.png`: Sales distribution across stores
- `q4_category_contribution.png`: Category contribution to sales
- `q5_days_sales_relationship.png`: Relationship between days and sales
- `q6_daily_value_consistency.png`: Consistency of daily values
- `q7_data_completeness.png`: Data completeness heatmap
- `q8_company_contribution.png`: Company market share
- `q9_transaction_relationship.png`: Transaction-sales relationship
- `q10_temporal_patterns.png`: Temporal sales patterns
- `q11_validation_requirements.png`: Validation data requirements

## Next Steps

1. Build baseline imputation models using average daily value
2. Develop category-level imputation models
3. Create store-specific models accounting for characteristics
4. Implement hybrid approach combining multiple methods
5. Validate models on validation dataset
6. Fine-tune based on performance metrics
