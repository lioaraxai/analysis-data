"""
Exploratory Data Analysis: Store Transaction Data Imputation

Problem Statement:
Build an imputation/extrapolation model to fill missing data gaps in store-level POS data.
Stores share data ranging from 2 to 28 days in a month, and certain transactions may not be scanned/recorded.

This script performs comprehensive EDA and answers key questions relevant to the imputation problem.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Set style for better visualizations
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 10

print("="*80)
print("EXPLORATORY DATA ANALYSIS: STORE TRANSACTION DATA IMPUTATION")
print("="*80)

# Load datasets
print("\nLoading datasets...")
ideal_data = pd.read_csv('Hackathon_Ideal_Data.csv')
working_data = pd.read_csv('Hackathon_Working_Data.csv')
validation_data = pd.read_csv('Hackathon_Validation_Data.csv')
mapping_file = pd.read_csv('Hackathon_Mapping_File.csv')

print(f"\nDataset Shapes:")
print(f"Ideal Data: {ideal_data.shape}")
print(f"Working Data: {working_data.shape}")
print(f"Validation Data: {validation_data.shape}")

# ============================================================================
# QUESTION 1: What is the overall structure and completeness of the datasets?
# ============================================================================
print("\n" + "="*80)
print("QUESTION 1: What is the overall structure and completeness of the datasets?")
print("="*80)

print("\n=== IDEAL DATA (Complete Reference Data) ===")
print(f"Shape: {ideal_data.shape}")
print(f"Columns: {list(ideal_data.columns)}")
print(f"Missing Values:\n{ideal_data.isnull().sum()}")
print(f"Unique Stores: {ideal_data['STORECODE'].nunique()} - {sorted(ideal_data['STORECODE'].unique())}")
print(f"Unique Months: {ideal_data['MONTH'].nunique()} - {sorted(ideal_data['MONTH'].unique())}")

print("\n=== WORKING DATA (Incomplete/Missing Data) ===")
print(f"Shape: {working_data.shape}")
print(f"Columns: {list(working_data.columns)}")
print(f"Missing Values:\n{working_data.isnull().sum()}")
print(f"Unique Stores: {working_data['STORECODE'].nunique()} - {sorted(working_data['STORECODE'].unique())}")
print(f"Unique Months: {working_data['MONTH'].nunique()} - {sorted(working_data['MONTH'].unique())}")
print(f"Unique Days: {working_data['DAY'].nunique()} - Range: {working_data['DAY'].min()} to {working_data['DAY'].max()}")

print("\n=== SUMMARY STATISTICS ===")
print("\nIdeal Data:")
print(ideal_data[['QTY', 'VALUE']].describe())
print("\nWorking Data:")
print(working_data[['QTY', 'VALUE', 'PRICE', 'BILL_AMT']].describe())

# ============================================================================
# QUESTION 2: How many days of data are available per store per month?
# ============================================================================
print("\n" + "="*80)
print("QUESTION 2: How many days of data are available per store per month?")
print("="*80)

days_per_store_month = working_data.groupby(['STORECODE', 'MONTH'])['DAY'].nunique().reset_index()
days_per_store_month.columns = ['STORECODE', 'MONTH', 'DAYS_COUNT']
days_per_store_month = days_per_store_month.sort_values(['STORECODE', 'MONTH'])

print("\nDays of data per store per month:")
print(days_per_store_month)

print(f"\n=== SUMMARY ===")
print(f"Minimum days: {days_per_store_month['DAYS_COUNT'].min()}")
print(f"Maximum days: {days_per_store_month['DAYS_COUNT'].max()}")
print(f"Average days: {days_per_store_month['DAYS_COUNT'].mean():.2f}")
print(f"Median days: {days_per_store_month['DAYS_COUNT'].median():.2f}")

# Visualization
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

pivot_days = days_per_store_month.pivot(index='STORECODE', columns='MONTH', values='DAYS_COUNT')
pivot_days.plot(kind='bar', ax=axes[0], width=0.8)
axes[0].set_title('Days of Data Available per Store per Month', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Store Code', fontsize=12)
axes[0].set_ylabel('Number of Days', fontsize=12)
axes[0].legend(title='Month', title_fontsize=10)
axes[0].grid(axis='y', alpha=0.3)
axes[0].axhline(y=28, color='r', linestyle='--', label='Full Month (28 days)', alpha=0.7)

axes[1].hist(days_per_store_month['DAYS_COUNT'], bins=range(1, 30), edgecolor='black', alpha=0.7)
axes[1].set_title('Distribution of Days per Store-Month', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Number of Days', fontsize=12)
axes[1].set_ylabel('Frequency', fontsize=12)
axes[1].axvline(x=28, color='r', linestyle='--', label='Full Month', alpha=0.7)
axes[1].legend()
axes[1].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('figures/q2_days_per_store_month.png', dpi=300, bbox_inches='tight')
print("\nFigure saved: q2_days_per_store_month.png")
plt.close()

# ============================================================================
# QUESTION 3: What is the sales volume and value distribution across stores?
# ============================================================================
print("\n" + "="*80)
print("QUESTION 3: What is the sales volume and value distribution across stores?")
print("="*80)

sales_by_store_month = working_data.groupby(['STORECODE', 'MONTH']).agg({
    'QTY': 'sum',
    'VALUE': 'sum',
    'BILL_ID': 'nunique',
    'DAY': 'nunique'
}).reset_index()
sales_by_store_month.columns = ['STORECODE', 'MONTH', 'TOTAL_QTY', 'TOTAL_VALUE', 'NUM_TRANSACTIONS', 'NUM_DAYS']
sales_by_store_month['AVG_TRANSACTION_VALUE'] = sales_by_store_month['TOTAL_VALUE'] / sales_by_store_month['NUM_TRANSACTIONS']
sales_by_store_month['AVG_DAILY_VALUE'] = sales_by_store_month['TOTAL_VALUE'] / sales_by_store_month['NUM_DAYS']

print("\nSales Summary by Store and Month:")
print(sales_by_store_month.sort_values(['STORECODE', 'MONTH']))

# Visualization
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

store_value = sales_by_store_month.groupby('STORECODE')['TOTAL_VALUE'].sum().sort_values(ascending=False)
store_value.plot(kind='bar', ax=axes[0, 0], color='steelblue')
axes[0, 0].set_title('Total Sales Value by Store', fontsize=12, fontweight='bold')
axes[0, 0].set_xlabel('Store Code', fontsize=10)
axes[0, 0].set_ylabel('Total Value', fontsize=10)
axes[0, 0].tick_params(axis='x', rotation=45)
axes[0, 0].grid(axis='y', alpha=0.3)

month_value = sales_by_store_month.groupby('MONTH')['TOTAL_VALUE'].sum()
month_value.plot(kind='bar', ax=axes[0, 1], color='coral')
axes[0, 1].set_title('Total Sales Value by Month', fontsize=12, fontweight='bold')
axes[0, 1].set_xlabel('Month', fontsize=10)
axes[0, 1].set_ylabel('Total Value', fontsize=10)
axes[0, 1].grid(axis='y', alpha=0.3)

store_daily = sales_by_store_month.groupby('STORECODE')['AVG_DAILY_VALUE'].mean().sort_values(ascending=False)
store_daily.plot(kind='bar', ax=axes[1, 0], color='green')
axes[1, 0].set_title('Average Daily Sales Value by Store', fontsize=12, fontweight='bold')
axes[1, 0].set_xlabel('Store Code', fontsize=10)
axes[1, 0].set_ylabel('Average Daily Value', fontsize=10)
axes[1, 0].tick_params(axis='x', rotation=45)
axes[1, 0].grid(axis='y', alpha=0.3)

axes[1, 1].hist(sales_by_store_month['TOTAL_VALUE'], bins=30, edgecolor='black', alpha=0.7, color='purple')
axes[1, 1].set_title('Distribution of Total Sales Value per Store-Month', fontsize=12, fontweight='bold')
axes[1, 1].set_xlabel('Total Value', fontsize=10)
axes[1, 1].set_ylabel('Frequency', fontsize=10)
axes[1, 1].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('figures/q3_sales_distribution.png', dpi=300, bbox_inches='tight')
print("\nFigure saved: q3_sales_distribution.png")
plt.close()

# ============================================================================
# QUESTION 4: How do categories contribute to total sales?
# ============================================================================
print("\n" + "="*80)
print("QUESTION 4: How do categories contribute to total sales?")
print("="*80)

category_sales = working_data.groupby('GRP').agg({
    'VALUE': ['sum', 'mean', 'count'],
    'QTY': 'sum'
}).reset_index()
category_sales.columns = ['GRP', 'TOTAL_VALUE', 'AVG_VALUE', 'TRANSACTION_COUNT', 'TOTAL_QTY']
category_sales = category_sales.sort_values('TOTAL_VALUE', ascending=False)

print(f"\nTotal Categories: {len(category_sales)}")
print(f"\nTop 20 Categories by Sales Value:")
print(category_sales.head(20))

# Visualization
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

top_categories = category_sales.head(15)
axes[0].barh(range(len(top_categories)), top_categories['TOTAL_VALUE'], color='steelblue')
axes[0].set_yticks(range(len(top_categories)))
axes[0].set_yticklabels(top_categories['GRP'], fontsize=9)
axes[0].set_xlabel('Total Sales Value', fontsize=11)
axes[0].set_title('Top 15 Categories by Sales Value', fontsize=12, fontweight='bold')
axes[0].grid(axis='x', alpha=0.3)

top_10 = category_sales.head(10)
others_value = category_sales.iloc[10:]['TOTAL_VALUE'].sum()
pie_data = list(top_10['TOTAL_VALUE']) + [others_value]
pie_labels = list(top_10['GRP']) + ['Others']

axes[1].pie(pie_data, labels=pie_labels, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 8})
axes[1].set_title('Sales Value Distribution - Top 10 Categories', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig('figures/q4_category_contribution.png', dpi=300, bbox_inches='tight')
print("\nFigure saved: q4_category_contribution.png")
plt.close()

# ============================================================================
# QUESTION 5: What is the relationship between number of days and total sales?
# ============================================================================
print("\n" + "="*80)
print("QUESTION 5: What is the relationship between number of days and total sales?")
print("="*80)

days_sales_relationship = sales_by_store_month[['STORECODE', 'MONTH', 'NUM_DAYS', 'TOTAL_VALUE', 'AVG_DAILY_VALUE']].copy()

correlation = days_sales_relationship['NUM_DAYS'].corr(days_sales_relationship['TOTAL_VALUE'])
print(f"\nCorrelation between Number of Days and Total Value: {correlation:.4f}")

# Visualization
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

axes[0].scatter(days_sales_relationship['NUM_DAYS'], days_sales_relationship['TOTAL_VALUE'], 
               alpha=0.6, s=100, color='steelblue')
axes[0].set_xlabel('Number of Days', fontsize=11)
axes[0].set_ylabel('Total Sales Value', fontsize=11)
axes[0].set_title(f'Days vs Total Value (Correlation: {correlation:.3f})', fontsize=12, fontweight='bold')
axes[0].grid(alpha=0.3)

z = np.polyfit(days_sales_relationship['NUM_DAYS'], days_sales_relationship['TOTAL_VALUE'], 1)
p = np.poly1d(z)
axes[0].plot(days_sales_relationship['NUM_DAYS'], p(days_sales_relationship['NUM_DAYS']), 
            "r--", alpha=0.8, label=f'Trend: y={z[0]:.2f}x+{z[1]:.2f}')
axes[0].legend()

axes[1].scatter(days_sales_relationship['NUM_DAYS'], days_sales_relationship['AVG_DAILY_VALUE'], 
               alpha=0.6, s=100, color='coral')
axes[1].set_xlabel('Number of Days', fontsize=11)
axes[1].set_ylabel('Average Daily Value', fontsize=11)
axes[1].set_title('Days vs Average Daily Value', fontsize=12, fontweight='bold')
axes[1].grid(alpha=0.3)

plt.tight_layout()
plt.savefig('figures/q5_days_sales_relationship.png', dpi=300, bbox_inches='tight')
print("\nFigure saved: q5_days_sales_relationship.png")
plt.close()

# ============================================================================
# QUESTION 6: How consistent is average daily sales across different days?
# ============================================================================
print("\n" + "="*80)
print("QUESTION 6: How consistent is average daily sales across different days?")
print("="*80)

daily_value_by_days = days_sales_relationship.groupby('NUM_DAYS')['AVG_DAILY_VALUE'].agg(['mean', 'std', 'count']).reset_index()
daily_value_by_days.columns = ['NUM_DAYS', 'MEAN_DAILY_VALUE', 'STD_DAILY_VALUE', 'COUNT']

print("\nAverage Daily Value Statistics by Number of Days:")
print(daily_value_by_days.sort_values('NUM_DAYS'))

# Visualization
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

days_list = sorted(days_sales_relationship['NUM_DAYS'].unique())
data_for_box = [days_sales_relationship[days_sales_relationship['NUM_DAYS'] == d]['AVG_DAILY_VALUE'].values 
                for d in days_list]
axes[0].boxplot(data_for_box, labels=days_list)
axes[0].set_xlabel('Number of Days', fontsize=11)
axes[0].set_ylabel('Average Daily Value', fontsize=11)
axes[0].set_title('Distribution of Average Daily Value by Number of Days', fontsize=12, fontweight='bold')
axes[0].grid(axis='y', alpha=0.3)

axes[1].errorbar(daily_value_by_days['NUM_DAYS'], daily_value_by_days['MEAN_DAILY_VALUE'], 
                yerr=daily_value_by_days['STD_DAILY_VALUE'], fmt='o-', capsize=5, capthick=2)
axes[1].set_xlabel('Number of Days', fontsize=11)
axes[1].set_ylabel('Mean Average Daily Value', fontsize=11)
axes[1].set_title('Mean Daily Value by Number of Days (with Std Dev)', fontsize=12, fontweight='bold')
axes[1].grid(alpha=0.3)

plt.tight_layout()
plt.savefig('figures/q6_daily_value_consistency.png', dpi=300, bbox_inches='tight')
print("\nFigure saved: q6_daily_value_consistency.png")
plt.close()

# ============================================================================
# QUESTION 7: Which stores have the most incomplete data?
# ============================================================================
print("\n" + "="*80)
print("QUESTION 7: Which stores have the most incomplete data?")
print("="*80)

incomplete_data = days_per_store_month[days_per_store_month['DAYS_COUNT'] < 28].copy()
incomplete_data = incomplete_data.sort_values('DAYS_COUNT')

print(f"\nStores with incomplete data (< 28 days): {len(incomplete_data)}")
print(f"\nMost Incomplete Store-Month Combinations:")
print(incomplete_data.head(20))

days_per_store_month['COMPLETENESS_PCT'] = (days_per_store_month['DAYS_COUNT'] / 28) * 100

print(f"\n=== COMPLETENESS SUMMARY ===")
print(f"Average Completeness: {days_per_store_month['COMPLETENESS_PCT'].mean():.2f}%")
print(f"Minimum Completeness: {days_per_store_month['COMPLETENESS_PCT'].min():.2f}%")
print(f"Maximum Completeness: {days_per_store_month['COMPLETENESS_PCT'].max():.2f}%")

# Visualization
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

completeness_pivot = days_per_store_month.pivot(index='STORECODE', columns='MONTH', values='COMPLETENESS_PCT')
sns.heatmap(completeness_pivot, annot=True, fmt='.1f', cmap='RdYlGn', ax=axes[0], cbar_kws={'label': 'Completeness %'})
axes[0].set_title('Data Completeness by Store and Month (%)', fontsize=12, fontweight='bold')
axes[0].set_xlabel('Month', fontsize=11)
axes[0].set_ylabel('Store Code', fontsize=11)

axes[1].hist(days_per_store_month['COMPLETENESS_PCT'], bins=20, edgecolor='black', alpha=0.7, color='purple')
axes[1].axvline(x=100, color='r', linestyle='--', label='100% Complete', alpha=0.7)
axes[1].set_xlabel('Completeness Percentage', fontsize=11)
axes[1].set_ylabel('Frequency', fontsize=11)
axes[1].set_title('Distribution of Data Completeness', fontsize=12, fontweight='bold')
axes[1].legend()
axes[1].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('figures/q7_data_completeness.png', dpi=300, bbox_inches='tight')
print("\nFigure saved: q7_data_completeness.png")
plt.close()

# ============================================================================
# QUESTION 8: How do brands and companies contribute to sales?
# ============================================================================
print("\n" + "="*80)
print("QUESTION 8: How do brands and companies contribute to sales?")
print("="*80)

company_sales = working_data.groupby('CMP').agg({
    'VALUE': 'sum',
    'BRD': 'nunique',
    'QTY': 'sum'
}).reset_index()
company_sales.columns = ['COMPANY', 'TOTAL_VALUE', 'NUM_BRANDS', 'TOTAL_QTY']
company_sales = company_sales.sort_values('TOTAL_VALUE', ascending=False)

print("\nTop 15 Companies by Sales Value:")
print(company_sales.head(15))

# Visualization
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

top_companies = company_sales.head(15)
axes[0].barh(range(len(top_companies)), top_companies['TOTAL_VALUE'], color='steelblue')
axes[0].set_yticks(range(len(top_companies)))
axes[0].set_yticklabels([c[:30] + '...' if len(c) > 30 else c for c in top_companies['COMPANY']], fontsize=9)
axes[0].set_xlabel('Total Sales Value', fontsize=11)
axes[0].set_title('Top 15 Companies by Sales Value', fontsize=12, fontweight='bold')
axes[0].grid(axis='x', alpha=0.3)

top_10_companies = company_sales.head(10)
others_value = company_sales.iloc[10:]['TOTAL_VALUE'].sum()
pie_data = list(top_10_companies['TOTAL_VALUE']) + [others_value]
pie_labels = [c[:20] + '...' if len(c) > 20 else c for c in top_10_companies['COMPANY']] + ['Others']

axes[1].pie(pie_data, labels=pie_labels, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 8})
axes[1].set_title('Market Share by Company (Top 10)', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig('figures/q8_company_contribution.png', dpi=300, bbox_inches='tight')
print("\nFigure saved: q8_company_contribution.png")
plt.close()

# ============================================================================
# QUESTION 9: What is the relationship between transaction count and sales?
# ============================================================================
print("\n" + "="*80)
print("QUESTION 9: What is the relationship between transaction count and sales?")
print("="*80)

transaction_stats = working_data.groupby(['STORECODE', 'MONTH']).agg({
    'BILL_ID': 'nunique',
    'VALUE': 'sum',
    'BILL_AMT': 'sum'
}).reset_index()
transaction_stats.columns = ['STORECODE', 'MONTH', 'NUM_TRANSACTIONS', 'TOTAL_VALUE', 'TOTAL_BILL_AMT']
transaction_stats['AVG_TRANSACTION_VALUE'] = transaction_stats['TOTAL_VALUE'] / transaction_stats['NUM_TRANSACTIONS']

corr_trans = transaction_stats['NUM_TRANSACTIONS'].corr(transaction_stats['TOTAL_VALUE'])
print(f"\nCorrelation between Number of Transactions and Total Value: {corr_trans:.4f}")

# Visualization
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

axes[0].scatter(transaction_stats['NUM_TRANSACTIONS'], transaction_stats['TOTAL_VALUE'], 
              alpha=0.6, s=100, color='steelblue')
axes[0].set_xlabel('Number of Transactions', fontsize=11)
axes[0].set_ylabel('Total Sales Value', fontsize=11)
axes[0].set_title(f'Transactions vs Total Value (Correlation: {corr_trans:.3f})', fontsize=12, fontweight='bold')
axes[0].grid(alpha=0.3)

z = np.polyfit(transaction_stats['NUM_TRANSACTIONS'], transaction_stats['TOTAL_VALUE'], 1)
p = np.poly1d(z)
axes[0].plot(transaction_stats['NUM_TRANSACTIONS'], p(transaction_stats['NUM_TRANSACTIONS']), 
            "r--", alpha=0.8, label=f'Trend: y={z[0]:.2f}x+{z[1]:.2f}')
axes[0].legend()

axes[1].hist(transaction_stats['AVG_TRANSACTION_VALUE'], bins=30, edgecolor='black', alpha=0.7, color='coral')
axes[1].set_xlabel('Average Transaction Value', fontsize=11)
axes[1].set_ylabel('Frequency', fontsize=11)
axes[1].set_title('Distribution of Average Transaction Value', fontsize=12, fontweight='bold')
axes[1].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('figures/q9_transaction_relationship.png', dpi=300, bbox_inches='tight')
print("\nFigure saved: q9_transaction_relationship.png")
plt.close()

# ============================================================================
# QUESTION 10: How do sales vary by day of month?
# ============================================================================
print("\n" + "="*80)
print("QUESTION 10: How do sales vary by day of month?")
print("="*80)

day_sales = working_data.groupby('DAY').agg({
    'VALUE': ['sum', 'mean', 'count'],
    'QTY': 'sum'
}).reset_index()
day_sales.columns = ['DAY', 'TOTAL_VALUE', 'AVG_VALUE', 'TRANSACTION_COUNT', 'TOTAL_QTY']
day_sales['DAY_OF_WEEK'] = (day_sales['DAY'] - 1) % 7
day_sales['DAY_NAME'] = day_sales['DAY_OF_WEEK'].map({0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'})

print("\nSales by Day of Month:")
print(day_sales.sort_values('DAY'))

# Visualization
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

axes[0, 0].plot(day_sales['DAY'], day_sales['TOTAL_VALUE'], marker='o', linewidth=2, markersize=6, color='steelblue')
axes[0, 0].set_xlabel('Day of Month', fontsize=11)
axes[0, 0].set_ylabel('Total Sales Value', fontsize=11)
axes[0, 0].set_title('Total Sales Value by Day of Month', fontsize=12, fontweight='bold')
axes[0, 0].grid(alpha=0.3)

axes[0, 1].plot(day_sales['DAY'], day_sales['AVG_VALUE'], marker='s', linewidth=2, markersize=6, color='coral')
axes[0, 1].set_xlabel('Day of Month', fontsize=11)
axes[0, 1].set_ylabel('Average Transaction Value', fontsize=11)
axes[0, 1].set_title('Average Transaction Value by Day of Month', fontsize=12, fontweight='bold')
axes[0, 1].grid(alpha=0.3)

dow_sales = day_sales.groupby('DAY_NAME')['TOTAL_VALUE'].sum().reindex(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
dow_sales.plot(kind='bar', ax=axes[1, 0], color='green')
axes[1, 0].set_xlabel('Day of Week', fontsize=11)
axes[1, 0].set_ylabel('Total Sales Value', fontsize=11)
axes[1, 0].set_title('Total Sales Value by Day of Week', fontsize=12, fontweight='bold')
axes[1, 0].tick_params(axis='x', rotation=0)
axes[1, 0].grid(axis='y', alpha=0.3)

axes[1, 1].bar(day_sales['DAY'], day_sales['TRANSACTION_COUNT'], color='purple', alpha=0.7)
axes[1, 1].set_xlabel('Day of Month', fontsize=11)
axes[1, 1].set_ylabel('Transaction Count', fontsize=11)
axes[1, 1].set_title('Transaction Count by Day of Month', fontsize=12, fontweight='bold')
axes[1, 1].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('figures/q10_temporal_patterns.png', dpi=300, bbox_inches='tight')
print("\nFigure saved: q10_temporal_patterns.png")
plt.close()

# ============================================================================
# QUESTION 11: What categories need to be predicted?
# ============================================================================
print("\n" + "="*80)
print("QUESTION 11: What categories need to be predicted?")
print("="*80)

print(f"\nTotal predictions needed: {len(validation_data)}")
print(f"Unique Stores: {validation_data['STORECODE'].nunique()} - {sorted(validation_data['STORECODE'].unique())}")
print(f"Unique Months: {validation_data['MONTH'].nunique()} - {sorted(validation_data['MONTH'].unique())}")
print(f"Unique Categories: {validation_data['GRP'].nunique()}")

predictions_per_store = validation_data.groupby('STORECODE').size().reset_index(name='COUNT')
predictions_per_store = predictions_per_store.sort_values('COUNT', ascending=False)

print(f"\nPredictions per Store:")
print(predictions_per_store)

predictions_per_category = validation_data.groupby('GRP').size().reset_index(name='COUNT')
predictions_per_category = predictions_per_category.sort_values('COUNT', ascending=False)

print(f"\nTop 20 Categories by Prediction Count:")
print(predictions_per_category.head(20))

# Visualization
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

predictions_per_store.plot(x='STORECODE', y='COUNT', kind='bar', ax=axes[0], color='steelblue')
axes[0].set_xlabel('Store Code', fontsize=11)
axes[0].set_ylabel('Number of Predictions', fontsize=11)
axes[0].set_title('Number of Predictions Required per Store', fontsize=12, fontweight='bold')
axes[0].tick_params(axis='x', rotation=45)
axes[0].grid(axis='y', alpha=0.3)

top_cat_pred = predictions_per_category.head(15)
axes[1].barh(range(len(top_cat_pred)), top_cat_pred['COUNT'], color='coral')
axes[1].set_yticks(range(len(top_cat_pred)))
axes[1].set_yticklabels([c[:40] + '...' if len(c) > 40 else c for c in top_cat_pred['GRP']], fontsize=9)
axes[1].set_xlabel('Number of Predictions', fontsize=11)
axes[1].set_title('Top 15 Categories by Prediction Count', fontsize=12, fontweight='bold')
axes[1].grid(axis='x', alpha=0.3)

plt.tight_layout()
plt.savefig('figures/q11_validation_requirements.png', dpi=300, bbox_inches='tight')
print("\nFigure saved: q11_validation_requirements.png")
plt.close()

# ============================================================================
# SUMMARY AND KEY INSIGHTS
# ============================================================================
print("\n" + "="*80)
print("KEY INSIGHTS AND RECOMMENDATIONS FOR IMPUTATION MODEL")
print("="*80)

print("""
### Summary of Findings:

1. **Data Completeness**: Stores have varying levels of data completeness (2-28 days per month)

2. **Days-Value Relationship**: Strong correlation between number of days and total sales value suggests extrapolation is feasible

3. **Average Daily Value**: Can be used as a baseline for imputation if consistent across stores

4. **Category Patterns**: Different categories show different sales patterns - category-level imputation may be needed

5. **Store Characteristics**: Stores have different product mixes and sales volumes - store-specific models may help

6. **Temporal Patterns**: Day-of-week and day-of-month patterns exist - can be used for temporal imputation

7. **Transaction Patterns**: Number of transactions correlates with sales value - can be a feature

### Recommended Imputation Strategies:

1. **Extrapolation Method**: Use average daily value × remaining days for missing days

2. **Category-Level Imputation**: Impute at category level, then aggregate

3. **Store-Specific Models**: Build models that account for store characteristics

4. **Temporal Features**: Include day-of-week, day-of-month as features

5. **Hybrid Approach**: Combine multiple methods (extrapolation, regression, time series)
""")

print("\nEDA Complete! All figures saved in 'figures' directory.")
print("="*80)
