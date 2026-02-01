"""
EDA Script: Grocery Store Chain Sales (2023–2025)

Dataset: grocery_chain_data.csv (~1,980 rows)

Goals:
- Understand store, aisle, and product performance
- Diagnose data quality issues (types, negatives, missing values)
- Extract features and insights for store comparison, promotion evaluation, and merchandising
"""

import os
import warnings

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")

sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)
plt.rcParams["font.size"] = 10


def ensure_fig_dir():
    os.makedirs("figures", exist_ok=True)


def save_fig(name: str):
    ensure_fig_dir()
    path = os.path.join("figures", name)
    plt.tight_layout()
    plt.savefig(path, dpi=300, bbox_inches="tight")
    print(f"Saved figure: {path}")
    plt.close()


print("=" * 100)
print("EDA: Grocery Store Chain Sales (2023–2025)")
print("=" * 100)

# ======================================================================================
# LOAD DATA
# ======================================================================================

print("\nLoading dataset...")
df = pd.read_csv("grocery_chain_data.csv", low_memory=False)

print(f"\nShape: {df.shape[0]} rows x {df.shape[1]} columns")
print("\nColumns:", list(df.columns))

# Standard column names we expect (defensive if names differ slightly)
col_customer = "customer_id"
col_store = "store_name"
col_date = "transaction_date"
col_aisle = "aisle"
col_product = "product_name"
col_qty = "quantity"
col_unit_price = "unit_price"
col_total = "total_amount"
col_discount = "discount_amount"
col_final = "final_amount"
col_points = "loyalty_points"

# ======================================================================================
# QUESTION 1: Structure, data quality, and missingness
# ======================================================================================

print("\n" + "=" * 80)
print("Q1: Structure, data quality, and missingness")
print("=" * 80)

print("\nData types:")
print(df.dtypes)

print("\nMissing values (all columns):")
print(df.isna().sum())

# Convert transaction_date to datetime
if col_date in df.columns:
    df[col_date] = pd.to_datetime(df[col_date], errors="coerce")
    print(
        f"\nTransaction date range: {df[col_date].min()} to {df[col_date].max()}"
    )

# Quantity is string – clean and convert
if col_qty in df.columns:
    print("\nCleaning 'quantity' column (string -> numeric)...")
    df[col_qty + "_raw"] = df[col_qty]
    df[col_qty] = (
        df[col_qty]
        .astype(str)
        .str.strip()
        .replace("", np.nan)
    )
    df[col_qty] = pd.to_numeric(df[col_qty], errors="coerce")

    print("Quantity summary after conversion:")
    print(df[col_qty].describe())

numeric_cols = [
    c
    for c in [
        col_unit_price,
        col_total,
        col_discount,
        col_final,
        col_points,
        col_qty,
    ]
    if c in df.columns
]

if numeric_cols:
    print("\nSummary statistics for key numeric columns:")
    print(df[numeric_cols].describe(percentiles=[0.01, 0.05, 0.5, 0.95, 0.99]).T)

    # Basic distribution of final_amount
    if col_final in df.columns:
        plt.figure()
        sns.histplot(
            df[col_final].clip(
                lower=df[col_final].quantile(0.01),
                upper=df[col_final].quantile(0.99),
            ),
            bins=40,
            kde=False,
            edgecolor="black",
        )
        plt.title(
            "Distribution of Final Transaction Amount (clipped 1st–99th pct)",
            fontsize=12,
        )
        plt.xlabel("Final Amount")
        plt.ylabel("Count")
        save_fig("q1_final_amount_distribution.png")

# Check consistency of total_amount ≈ quantity * unit_price
if all(c in df.columns for c in [col_qty, col_unit_price, col_total]):
    df["_recalc_total"] = df[col_qty] * df[col_unit_price]
    df["_total_diff"] = df[col_total] - df["_recalc_total"]

    print("\nConsistency check: total_amount vs quantity * unit_price:")
    print(df["_total_diff"].describe())

    plt.figure()
    sns.histplot(
        df["_total_diff"].clip(
            lower=df["_total_diff"].quantile(0.01),
            upper=df["_total_diff"].quantile(0.99),
        ),
        bins=40,
        kde=False,
        edgecolor="black",
    )
    plt.title("Difference: total_amount - quantity*unit_price", fontsize=12)
    plt.xlabel("Difference")
    plt.ylabel("Count")
    save_fig("q1_total_vs_qty_price_diff.png")


# ======================================================================================
# QUESTION 2: Sales trends over time
# ======================================================================================

print("\n" + "=" * 80)
print("Q2: Sales trends over time (monthly)")
print("=" * 80)

if col_date in df.columns and col_final in df.columns:
    df["year"] = df[col_date].dt.year
    df["month"] = df[col_date].dt.month
    df["year_month"] = df[col_date].dt.to_period("M").astype(str)

    month_agg = (
        df.groupby("year_month")[col_final]
        .sum()
        .reset_index()
        .sort_values("year_month")
    )
    print("\nMonthly total final_amount:")
    print(month_agg.head(24))

    plt.figure()
    sns.lineplot(
        data=month_agg,
        x="year_month",
        y=col_final,
        marker="o",
    )
    plt.xticks(rotation=45, ha="right")
    plt.title("Monthly Total Final Sales", fontsize=12)
    plt.xlabel("Year-Month")
    plt.ylabel("Total Final Amount")
    save_fig("q2_monthly_sales_trend.png")


# ======================================================================================
# QUESTION 3: Store performance (revenue, discount, loyalty)
# ======================================================================================

print("\n" + "=" * 80)
print("Q3: Store performance – revenue, discount, loyalty")
print("=" * 80)

if col_store in df.columns and col_final in df.columns:
    group_cols = [col_store]
    store_agg = df.groupby(group_cols).agg(
        total_final=(col_final, "sum"),
        avg_final=(col_final, "mean"),
        transactions=(col_final, "count"),
    )

    if col_discount in df.columns and col_total in df.columns:
        store_agg["avg_discount_rate"] = (
            df.groupby(col_store)[col_discount].mean()
            / df.groupby(col_store)[col_total].mean()
        )

    if col_points in df.columns:
        store_agg["avg_loyalty_points"] = df.groupby(col_store)[col_points].mean()

    store_agg = store_agg.sort_values("total_final", ascending=False)
    print("\nStore-level KPIs:")
    print(store_agg)

    plt.figure()
    sns.barplot(
        x=store_agg["total_final"],
        y=store_agg.index,
        orient="h",
        palette="Blues_r",
    )
    plt.title("Total Final Sales by Store", fontsize=12)
    plt.xlabel("Total Final Amount")
    plt.ylabel("Store Name")
    save_fig("q3_total_sales_by_store.png")


# ======================================================================================
# QUESTION 4: Aisle (category) contribution to revenue
# ======================================================================================

print("\n" + "=" * 80)
print("Q4: Aisle contribution to revenue and discount")
print("=" * 80)

if col_aisle in df.columns and col_final in df.columns:
    aisle_agg = (
        df.groupby(col_aisle)[col_final]
        .sum()
        .sort_values(ascending=False)
    )
    print("\nTotal final_amount by aisle:")
    print(aisle_agg)

    plt.figure()
    sns.barplot(
        x=aisle_agg.values,
        y=aisle_agg.index,
        orient="h",
        palette="Greens_r",
    )
    plt.title("Total Final Sales by Aisle", fontsize=12)
    plt.xlabel("Total Final Amount")
    plt.ylabel("Aisle")
    save_fig("q4_total_sales_by_aisle.png")

    if col_discount in df.columns and col_total in df.columns:
        aisle_disc = (
            df.groupby(col_aisle)[col_discount].mean()
            / df.groupby(col_aisle)[col_total].mean()
        )
        aisle_disc = aisle_disc.sort_values(ascending=False)
        print("\nAverage discount rate by aisle:")
        print(aisle_disc)

        plt.figure()
        sns.barplot(
            x=aisle_disc.values,
            y=aisle_disc.index,
            orient="h",
            palette="Reds_r",
        )
        plt.title("Average Discount Rate by Aisle", fontsize=12)
        plt.xlabel("Average Discount Rate")
        plt.ylabel("Aisle")
        save_fig("q4_discount_rate_by_aisle.png")


# ======================================================================================
# QUESTION 5: Product performance – revenue and volume
# ======================================================================================

print("\n" + "=" * 80)
print("Q5: Product performance – revenue and volume")
print("=" * 80)

if col_product in df.columns and col_final in df.columns:
    prod_agg = df.groupby(col_product).agg(
        total_final=(col_final, "sum"),
        total_qty=(col_qty, "sum"),
        transactions=(col_final, "count"),
    )
    prod_agg = prod_agg.sort_values("total_final", ascending=False)
    print("\nTop 15 products by total_final:")
    print(prod_agg.head(15))

    top_prod = prod_agg.head(15)

    plt.figure()
    sns.barplot(
        x=top_prod["total_final"],
        y=top_prod.index,
        orient="h",
        palette="Blues_r",
    )
    plt.title("Top 15 Products by Total Final Sales", fontsize=12)
    plt.xlabel("Total Final Amount")
    plt.ylabel("Product Name")
    save_fig("q5_top_products_by_sales.png")


# ======================================================================================
# QUESTION 6: Discount behavior and its impact
# ======================================================================================

print("\n" + "=" * 80)
print("Q6: Discounts – penetration and impact")
print("=" * 80)

if col_discount in df.columns and col_total in df.columns:
    df["_discount_rate"] = np.where(
        df[col_total].fillna(0) > 0,
        df[col_discount] / df[col_total],
        np.nan,
    )

    print("\nDiscount rate summary:")
    print(df["_discount_rate"].describe())

    plt.figure()
    sns.histplot(
        df["_discount_rate"].clip(
            lower=df["_discount_rate"].quantile(0.01),
            upper=df["_discount_rate"].quantile(0.99),
        ).dropna(),
        bins=40,
        edgecolor="black",
    )
    plt.title("Distribution of Discount Rate (clipped 1st–99th pct)", fontsize=12)
    plt.xlabel("Discount Rate")
    plt.ylabel("Count")
    save_fig("q6_discount_rate_distribution.png")

    if col_final in df.columns:
        plt.figure()
        sns.scatterplot(
            data=df,
            x="_discount_rate",
            y=col_final,
            alpha=0.4,
            s=30,
        )
        plt.title("Final Amount vs Discount Rate", fontsize=12)
        plt.xlabel("Discount Rate")
        plt.ylabel("Final Amount")
        save_fig("q6_final_amount_vs_discount_rate.png")


# ======================================================================================
# QUESTION 7: Anomalies – negative final_amount and odd quantities
# ======================================================================================

print("\n" + "=" * 80)
print("Q7: Anomalous transactions (negatives, out-of-range quantities)")
print("=" * 80)

if col_final in df.columns:
    negative_final = df[df[col_final] < 0]
    print(f"\nNumber of transactions with negative final_amount: {len(negative_final)}")
    if len(negative_final) > 0:
        print(negative_final.head())

if col_qty in df.columns:
    out_of_range_qty = df[(df[col_qty] < 1) | (df[col_qty] > 5)]
    print(
        f"\nNumber of transactions with quantity outside [1,5]: {len(out_of_range_qty)}"
    )
    if len(out_of_range_qty) > 0:
        print(out_of_range_qty.head())


# ======================================================================================
# QUESTION 8: Customer behavior across stores and aisles
# ======================================================================================

print("\n" + "=" * 80)
print("Q8: Customer behavior – store and aisle diversity")
print("=" * 80)

if col_customer in df.columns:
    cust_agg = df.groupby(col_customer).agg(
        transactions=(col_final, "count"),
        total_final=(col_final, "sum"),
        total_qty=(col_qty, "sum"),
        num_stores=(col_store, "nunique") if col_store in df.columns else ("store", "nunique"),
        num_aisles=(col_aisle, "nunique") if col_aisle in df.columns else ("aisle", "nunique"),
    )
    print("\nCustomer-level summary (head):")
    print(cust_agg.head())

    if "num_stores" in cust_agg.columns:
        plt.figure()
        sns.histplot(
            cust_agg["num_stores"],
            bins=range(1, cust_agg["num_stores"].max() + 2),
            edgecolor="black",
        )
        plt.title("Distribution of Distinct Stores Visited per Customer", fontsize=12)
        plt.xlabel("Number of Stores")
        plt.ylabel("Number of Customers")
        save_fig("q8_num_stores_per_customer.png")


# ======================================================================================
# QUESTION 9: Temporal patterns – day of week, month, season
# ======================================================================================

print("\n" + "=" * 80)
print("Q9: Temporal patterns – day of week and month")
print("=" * 80)

if col_date in df.columns and col_final in df.columns:
    df["day_of_week"] = df[col_date].dt.day_name()
    df["month_name"] = df[col_date].dt.month_name()

    dow_agg = (
        df.groupby("day_of_week")[col_final]
        .sum()
        .reindex(
            [
                "Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
                "Saturday",
                "Sunday",
            ]
        )
    )

    print("\nTotal final_amount by day of week:")
    print(dow_agg)

    plt.figure()
    sns.barplot(
        x=dow_agg.index,
        y=dow_agg.values,
        palette="Blues",
    )
    plt.title("Total Final Sales by Day of Week", fontsize=12)
    plt.xlabel("Day of Week")
    plt.ylabel("Total Final Amount")
    plt.xticks(rotation=30)
    save_fig("q9_sales_by_day_of_week.png")

    month_agg2 = (
        df.groupby("month_name")[col_final]
        .sum()
        .reindex(
            [
                "January",
                "February",
                "March",
                "April",
                "May",
                "June",
                "July",
                "August",
                "September",
                "October",
                "November",
                "December",
            ]
        )
    )

    print("\nTotal final_amount by month:")
    print(month_agg2.dropna())

    plt.figure()
    sns.barplot(
        x=month_agg2.index,
        y=month_agg2.values,
        palette="Greens",
    )
    plt.title("Total Final Sales by Month", fontsize=12)
    plt.xlabel("Month")
    plt.ylabel("Total Final Amount")
    plt.xticks(rotation=45)
    save_fig("q9_sales_by_month.png")


# ======================================================================================
# QUESTION 10: Loyalty points behavior
# ======================================================================================

print("\n" + "=" * 80)
print("Q10: Loyalty points – distribution and link to spend")
print("=" * 80)

if col_points in df.columns:
    print("\nLoyalty points summary:")
    print(df[col_points].describe())

    plt.figure()
    sns.histplot(
        df[col_points],
        bins=30,
        edgecolor="black",
    )
    plt.title("Distribution of Loyalty Points per Transaction", fontsize=12)
    plt.xlabel("Loyalty Points")
    plt.ylabel("Count")
    save_fig("q10_loyalty_points_distribution.png")

    if col_final in df.columns:
        plt.figure()
        sns.scatterplot(
            data=df,
            x=col_points,
            y=col_final,
            alpha=0.5,
            s=30,
        )
        plt.title("Final Amount vs Loyalty Points", fontsize=12)
        plt.xlabel("Loyalty Points")
        plt.ylabel("Final Amount")
        save_fig("q10_final_amount_vs_loyalty_points.png")


print("\n" + "=" * 100)
print("EDA complete. Figures written to the 'figures/' directory.")
print("=" * 100)

