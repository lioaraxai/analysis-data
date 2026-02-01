"""
EDA Script: Retail Sales and Customer Behavior Analysis

Dataset: retail_data.csv (~1M rows, 100+ columns)

Goals:
- Support regression on `total_sales`
- Support classification on `churned`
- Extract features and insights that are directly useful for:
  - Customer value and churn modeling
  - Merchandising, promotions, and planogram / decision support
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
print("EDA: Retail Sales and Customer Behavior Analysis")
print("=" * 100)

# ======================================================================================
# LOAD DATA
# ======================================================================================

print("\nLoading dataset (this may take a moment)...")
df = pd.read_csv("retail_data.csv", low_memory=False)

print(f"\nShape: {df.shape[0]:,} rows x {df.shape[1]} columns")
print("\nFirst few columns:", list(df.columns[:25]), "...")


# ======================================================================================
# QUESTION 1: Structure, data quality, and missingness
# ======================================================================================

print("\n" + "=" * 80)
print("Q1: Overall structure, data quality, and missingness")
print("=" * 80)

print("\nData types (first ~40 columns):")
print(df.dtypes.head(40))

print("\nMissing values (top 30 by count):")
missing = df.isna().sum().sort_values(ascending=False)
print(missing.head(30))

numeric_cols = [
    c
    for c in [
        "total_sales",
        "total_transactions",
        "total_items_purchased",
        "total_discounts_received",
        "avg_purchase_value",
        "avg_transaction_value",
        "avg_items_per_transaction",
        "customer_lifetime_value",
        "loyalty_score",
        "churn_risk_score",
        "membership_years",
        "days_since_last_purchase",
        "avg_purchase_interval",
    ]
    if c in df.columns
]

if numeric_cols:
    print("\nSummary statistics for key numeric columns:")
    print(df[numeric_cols].describe(percentiles=[0.01, 0.05, 0.5, 0.95, 0.99]).T)

    # Basic distribution of total_sales
    if "total_sales" in df.columns:
        plt.figure()
        sns.histplot(
            df["total_sales"].clip(upper=df["total_sales"].quantile(0.99)),
            bins=50,
            kde=False,
            edgecolor="black",
        )
        plt.title("Distribution of Total Sales (clipped at 99th percentile)", fontsize=12)
        plt.xlabel("Total Sales")
        plt.ylabel("Count")
        save_fig("q1_total_sales_distribution.png")


# ======================================================================================
# QUESTION 2: Demographic profiles vs sales and churn
# ======================================================================================

print("\n" + "=" * 80)
print("Q2: Demographics vs total_sales and churn")
print("=" * 80)

target_reg = "total_sales" if "total_sales" in df.columns else None
target_cls = "churned" if "churned" in df.columns else None

demo_cols = [
    "age",
    "gender",
    "income_bracket",
    "marital_status",
    "number_of_children",
    "education_level",
]
demo_cols = [c for c in demo_cols if c in df.columns]

if target_reg and demo_cols:
    print("\nAverage total_sales by demographic groups:")
    for col in demo_cols:
        print(f"\n-- {col} --")
        print(
            df.groupby(col)[target_reg]
            .mean()
            .sort_values(ascending=False)
            .head(10)
        )

    # Example plot: income_bracket vs total_sales and churn
    if "income_bracket" in df.columns:
        plt.figure()
        sns.barplot(
            data=df,
            x="income_bracket",
            y=target_reg,
            estimator=np.mean,
            order=sorted(df["income_bracket"].dropna().unique()),
        )
        plt.title("Average Total Sales by Income Bracket", fontsize=12)
        plt.xlabel("Income Bracket")
        plt.ylabel("Average Total Sales")
        plt.xticks(rotation=30)
        save_fig("q2_avg_sales_by_income_bracket.png")

if target_cls and demo_cols:
    # Convert churned to binary if it's Yes/No
    churn_series = df[target_cls].astype(str).str.lower()
    churn_flag = churn_series.isin(["yes", "1", "true"])

    df["_churn_flag"] = churn_flag.astype(int)

    print("\nChurn rate by demographic groups:")
    for col in demo_cols:
        print(f"\n-- {col} --")
        print(
            df.groupby(col)["_churn_flag"]
            .mean()
            .sort_values(ascending=False)
            .head(10)
        )

    if "income_bracket" in df.columns:
        plt.figure()
        sns.barplot(
            data=df,
            x="income_bracket",
            y="_churn_flag",
            estimator=np.mean,
            order=sorted(df["income_bracket"].dropna().unique()),
        )
        plt.title("Churn Rate by Income Bracket", fontsize=12)
        plt.xlabel("Income Bracket")
        plt.ylabel("Churn Rate")
        plt.xticks(rotation=30)
        save_fig("q2_churn_rate_by_income_bracket.png")


# ======================================================================================
# QUESTION 3: Loyalty program, tenure vs sales and churn
# ======================================================================================

print("\n" + "=" * 80)
print("Q3: Loyalty & tenure vs sales and churn")
print("=" * 80)

if "loyalty_program" in df.columns and target_reg:
    print("\nTotal sales by loyalty_program:")
    print(df.groupby("loyalty_program")[target_reg].agg(["mean", "median", "count"]))

    plt.figure()
    sns.boxplot(data=df, x="loyalty_program", y=target_reg)
    plt.title("Total Sales by Loyalty Program Membership", fontsize=12)
    plt.xlabel("Loyalty Program")
    plt.ylabel("Total Sales")
    save_fig("q3_sales_by_loyalty_program.png")

if "membership_years" in df.columns and target_reg:
    # Bucket membership_years
    bins = [-np.inf, 1, 3, 5, 10, np.inf]
    labels = ["<1", "1-3", "3-5", "5-10", "10+"]
    df["_membership_bucket"] = pd.cut(df["membership_years"], bins=bins, labels=labels)

    print("\nAverage total_sales by membership tenure bucket:")
    print(
        df.groupby("_membership_bucket")[target_reg]
        .mean()
        .sort_index()
    )

    plt.figure()
    sns.barplot(
        data=df,
        x="_membership_bucket",
        y=target_reg,
        estimator=np.mean,
        order=labels,
    )
    plt.title("Average Total Sales by Membership Years", fontsize=12)
    plt.xlabel("Membership Years Bucket")
    plt.ylabel("Average Total Sales")
    save_fig("q3_avg_sales_by_membership_years.png")

if "_churn_flag" in df.columns and "membership_years" in df.columns:
    plt.figure()
    sns.barplot(
        data=df,
        x="_membership_bucket",
        y="_churn_flag",
        estimator=np.mean,
        order=labels,
    )
    plt.title("Churn Rate by Membership Years", fontsize=12)
    plt.xlabel("Membership Years Bucket")
    plt.ylabel("Churn Rate")
    save_fig("q3_churn_by_membership_years.png")


# ======================================================================================
# QUESTION 4: RFM-style patterns
# ======================================================================================

print("\n" + "=" * 80)
print("Q4: RFM patterns (Recency, Frequency, Monetary)")
print("=" * 80)

rfm_cols = [
    "days_since_last_purchase",
    "avg_purchase_interval",
    "total_transactions",
    target_reg,
]
rfm_cols = [c for c in rfm_cols if c in df.columns and c is not None]

if rfm_cols:
    print("\nCorrelation matrix for RFM-related variables:")
    print(df[rfm_cols].corr())

    if "days_since_last_purchase" in df.columns and target_cls:
        plt.figure()
        sns.boxplot(
            data=df,
            x="_churn_flag",
            y="days_since_last_purchase",
        )
        plt.title("Days Since Last Purchase vs Churn", fontsize=12)
        plt.xlabel("Churned (0=No, 1=Yes)")
        plt.ylabel("Days Since Last Purchase")
        save_fig("q4_recency_vs_churn.png")


# ======================================================================================
# QUESTION 5: Channel mix – online vs in-store behavior
# ======================================================================================

print("\n" + "=" * 80)
print("Q5: Channel mix (online vs in-store)")
print("=" * 80)

if "online_purchases" in df.columns and "in_store_purchases" in df.columns:
    df["total_purchase_count"] = (
        df["online_purchases"].fillna(0) + df["in_store_purchases"].fillna(0)
    )
    df["online_share"] = np.where(
        df["total_purchase_count"] > 0,
        df["online_purchases"] / df["total_purchase_count"],
        np.nan,
    )

    print("\nSummary of online_share:")
    print(df["online_share"].describe())

    plt.figure()
    sns.histplot(
        df["online_share"].dropna(), bins=20, edgecolor="black", kde=False
    )
    plt.title("Distribution of Online Purchase Share", fontsize=12)
    plt.xlabel("Online Share of Purchases")
    plt.ylabel("Number of Customers")
    save_fig("q5_online_share_distribution.png")

    if target_reg:
        plt.figure()
        sns.scatterplot(
            data=df.sample(min(20000, len(df)), random_state=42),
            x="online_share",
            y=target_reg,
            alpha=0.3,
            s=10,
        )
        plt.title("Total Sales vs Online Share (sampled)", fontsize=12)
        plt.xlabel("Online Share of Purchases")
        plt.ylabel("Total Sales")
        save_fig("q5_sales_vs_online_share.png")


# ======================================================================================
# QUESTION 6: Product categories and brands – revenue and returns
# ======================================================================================

print("\n" + "=" * 80)
print("Q6: Product categories, brands, and returns")
print("=" * 80)

if "product_category" in df.columns and target_reg:
    cat_agg = (
        df.groupby("product_category")[target_reg]
        .sum()
        .sort_values(ascending=False)
        .head(20)
    )
    print("\nTop 20 product categories by total_sales:")
    print(cat_agg)

    plt.figure()
    sns.barplot(
        x=cat_agg.values,
        y=cat_agg.index,
        orient="h",
        palette="Blues_r",
    )
    plt.title("Top 20 Product Categories by Total Sales", fontsize=12)
    plt.xlabel("Total Sales")
    plt.ylabel("Product Category")
    save_fig("q6_top_categories_by_sales.png")

if "product_brand" in df.columns and target_reg:
    brand_agg = (
        df.groupby("product_brand")[target_reg]
        .sum()
        .sort_values(ascending=False)
        .head(20)
    )
    print("\nTop 20 product brands by total_sales:")
    print(brand_agg)

    plt.figure()
    sns.barplot(
        x=brand_agg.values,
        y=brand_agg.index,
        orient="h",
        palette="Greens_r",
    )
    plt.title("Top 20 Brands by Total Sales", fontsize=12)
    plt.xlabel("Total Sales")
    plt.ylabel("Brand")
    save_fig("q6_top_brands_by_sales.png")

if "product_return_rate" in df.columns and "product_category" in df.columns:
    ret_agg = (
        df.groupby("product_category")["product_return_rate"]
        .mean()
        .sort_values(ascending=False)
        .head(20)
    )
    print("\nTop 20 categories by average return rate:")
    print(ret_agg)

    plt.figure()
    sns.barplot(
        x=ret_agg.values,
        y=ret_agg.index,
        orient="h",
        palette="Reds_r",
    )
    plt.title("Top 20 Categories by Return Rate", fontsize=12)
    plt.xlabel("Average Return Rate")
    plt.ylabel("Product Category")
    save_fig("q6_top_categories_by_return_rate.png")


# ======================================================================================
# QUESTION 7: Promotions – types and channels
# ======================================================================================

print("\n" + "=" * 80)
print("Q7: Promotions – type & channel effectiveness")
print("=" * 80)

if "promotion_type" in df.columns and target_reg:
    promo_agg = (
        df.groupby("promotion_type")[target_reg]
        .mean()
        .sort_values(ascending=False)
    )
    print("\nAverage total_sales by promotion_type:")
    print(promo_agg)

    plt.figure()
    sns.barplot(
        x=promo_agg.values,
        y=promo_agg.index,
        orient="h",
    )
    plt.title("Average Total Sales by Promotion Type", fontsize=12)
    plt.xlabel("Average Total Sales")
    plt.ylabel("Promotion Type")
    save_fig("q7_avg_sales_by_promotion_type.png")

if "promotion_channel" in df.columns and target_reg:
    chan_agg = (
        df.groupby("promotion_channel")[target_reg]
        .mean()
        .sort_values(ascending=False)
    )
    print("\nAverage total_sales by promotion_channel:")
    print(chan_agg)

    plt.figure()
    sns.barplot(
        x=chan_agg.values,
        y=chan_agg.index,
        orient="h",
    )
    plt.title("Average Total Sales by Promotion Channel", fontsize=12)
    plt.xlabel("Average Total Sales")
    plt.ylabel("Promotion Channel")
    save_fig("q7_avg_sales_by_promotion_channel.png")


# ======================================================================================
# QUESTION 8: Geography – distance and region
# ======================================================================================

print("\n" + "=" * 80)
print("Q8: Geography – distance & regional effects")
print("=" * 80)

if "distance_to_store" in df.columns and target_reg:
    # Bucket distance
    dist_bins = [-np.inf, 2, 5, 10, 20, np.inf]
    dist_labels = ["0–2km", "2–5km", "5–10km", "10–20km", "20km+"]
    df["_distance_bucket"] = pd.cut(
        df["distance_to_store"], bins=dist_bins, labels=dist_labels
    )

    print("\nAverage total_sales by distance bucket:")
    print(
        df.groupby("_distance_bucket")[target_reg]
        .mean()
        .sort_index()
    )

    plt.figure()
    sns.barplot(
        data=df,
        x="_distance_bucket",
        y=target_reg,
        estimator=np.mean,
        order=dist_labels,
    )
    plt.title("Average Total Sales by Distance to Store", fontsize=12)
    plt.xlabel("Distance Bucket")
    plt.ylabel("Average Total Sales")
    save_fig("q8_sales_by_distance_bucket.png")


# ======================================================================================
# QUESTION 9: Seasonality, holidays, and weekends
# ======================================================================================

print("\n" + "=" * 80)
print("Q9: Seasonality, holidays, and weekends")
print("=" * 80)

if "season" in df.columns and target_reg:
    plt.figure()
    sns.barplot(
        data=df,
        x="season",
        y=target_reg,
        estimator=np.mean,
        order=sorted(df["season"].dropna().unique()),
    )
    plt.title("Average Total Sales by Season", fontsize=12)
    plt.xlabel("Season")
    plt.ylabel("Average Total Sales")
    save_fig("q9_avg_sales_by_season.png")

if "holiday_season" in df.columns and target_reg:
    plt.figure()
    sns.barplot(
        data=df,
        x="holiday_season",
        y=target_reg,
        estimator=np.mean,
    )
    plt.title("Average Total Sales – Holiday vs Non-Holiday", fontsize=12)
    plt.xlabel("Holiday Season")
    plt.ylabel("Average Total Sales")
    save_fig("q9_avg_sales_holiday_vs_nonholiday.png")

if "weekend" in df.columns and target_reg:
    plt.figure()
    sns.barplot(
        data=df,
        x="weekend",
        y=target_reg,
        estimator=np.mean,
    )
    plt.title("Average Total Sales – Weekend vs Weekday", fontsize=12)
    plt.xlabel("Weekend")
    plt.ylabel("Average Total Sales")
    save_fig("q9_avg_sales_weekend_vs_weekday.png")


# ======================================================================================
# QUESTION 10: Engagement & interactions vs churn and value
# ======================================================================================

print("\n" + "=" * 80)
print("Q10: Engagement & interactions vs churn and value")
print("=" * 80)

eng_cols = [
    "customer_support_calls",
    "email_subscriptions",
    "app_usage",
    "website_visits",
    "social_media_engagement",
]
eng_cols = [c for c in eng_cols if c in df.columns]

if eng_cols:
    print("\nSummary of engagement columns:")
    print(df[eng_cols].describe(include="all").T)

if "customer_support_calls" in df.columns and target_cls:
    plt.figure()
    sns.boxplot(
        data=df,
        x="_churn_flag",
        y="customer_support_calls",
    )
    plt.title("Customer Support Calls vs Churn", fontsize=12)
    plt.xlabel("Churned (0=No, 1=Yes)")
    plt.ylabel("Customer Support Calls")
    save_fig("q10_support_calls_vs_churn.png")

if "app_usage" in df.columns and target_reg:
    plt.figure()
    sns.scatterplot(
        data=df.sample(min(20000, len(df)), random_state=42),
        x="app_usage",
        y=target_reg,
        alpha=0.3,
        s=10,
    )
    plt.title("App Usage vs Total Sales (sampled)", fontsize=12)
    plt.xlabel("App Usage Frequency")
    plt.ylabel("Total Sales")
    save_fig("q10_app_usage_vs_sales.png")


# ======================================================================================
# QUESTION 11: Derived scores – CLV, loyalty_score, churn_risk_score
# ======================================================================================

print("\n" + "=" * 80)
print("Q11: Derived scores consistency & predictive power")
print("=" * 80)

score_cols = [
    c
    for c in ["customer_lifetime_value", "loyalty_score", "churn_risk_score"]
    if c in df.columns
]

if score_cols:
    print("\nScore distributions (summary):")
    print(df[score_cols].describe().T)

    if target_reg:
        print("\nCorrelation of scores with total_sales:")
        print(df[score_cols + [target_reg]].corr()[target_reg].sort_values(ascending=False))

    if target_cls:
        print("\nAverage scores by churned flag:")
        print(df.groupby("_churn_flag")[score_cols].mean())

    for col in score_cols:
        plt.figure()
        sns.histplot(
            df[col].dropna(),
            bins=50,
            kde=False,
            edgecolor="black",
        )
        plt.title(f"Distribution of {col}", fontsize=12)
        plt.xlabel(col)
        plt.ylabel("Count")
        save_fig(f"q11_distribution_{col}.png")


print("\n" + "=" * 100)
print("EDA complete. Figures written to the 'figures/' directory.")
print("=" * 100)

