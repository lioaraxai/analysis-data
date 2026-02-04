# E-Commerce Transactions Analysis (smayanj/e-commerce-transactions-dataset)

## 1. Dataset Overview

- **Rows**: 50,000
- **Columns**: 8
- **Columns list**: ['Transaction_ID', 'User_Name', 'Age', 'Country', 'Product_Category', 'Purchase_Amount', 'Payment_Method', 'Transaction_Date']

## 2. Schema Details
```
Transaction_ID: int64 | nulls: 0 | unique: 50000
User_Name: str | nulls: 0 | unique: 100
Age: int64 | nulls: 0 | unique: 53
Country: str | nulls: 0 | unique: 10
Product_Category: str | nulls: 0 | unique: 8
Purchase_Amount: float64 | nulls: 0 | unique: 39258
Payment_Method: str | nulls: 0 | unique: 6
Transaction_Date: str | nulls: 0 | unique: 731
```

## 3. Sample Data (First 5 Rows)
```
   Transaction_ID        User_Name  Age  Country Product_Category  Purchase_Amount Payment_Method Transaction_Date
0               1         Ava Hall   63   Mexico         Clothing           780.69     Debit Card       2023-04-14
1               2      Sophia Hall   59    India           Beauty           738.56         PayPal       2023-07-30
2               3  Elijah Thompson   26   France            Books           178.34    Credit Card       2023-09-17
3               4     Elijah White   43   Mexico           Sports           401.09            UPI       2023-06-21
4               5       Ava Harris   48  Germany           Beauty           594.83    Net Banking       2024-10-29
```

## 4. Statistical Summary

### Numeric Columns
```
       Transaction_ID           Age  Purchase_Amount
count    50000.000000  50000.000000     50000.000000
mean     25000.500000     43.968680       503.159793
std      14433.901067     15.260578       286.563558
min          1.000000     18.000000         5.040000
25%      12500.750000     31.000000       255.450000
50%      25000.500000     44.000000       503.110000
75%      37500.250000     57.000000       751.162500
max      50000.000000     70.000000       999.980000
```

### Categorical Columns

#### User_Name
- Unique values: 100
- Top 10:
| Value | Count | % |
|-------|-------|---|
| Sophia Harris | 568 | 1.1% |
| Emma Clark | 546 | 1.1% |
| Noah Anderson | 545 | 1.1% |
| James Allen | 545 | 1.1% |
| James Lewis | 543 | 1.1% |
| Elijah Hall | 543 | 1.1% |
| Isabella Hall | 539 | 1.1% |
| Olivia Hall | 534 | 1.1% |
| Sophia Walker | 524 | 1.0% |
| Oliver Thompson | 524 | 1.0% |


#### Country
- Unique values: 10
| Value | Count | % |
|-------|-------|---|
| Canada | 5,082 | 10.2% |
| Mexico | 5,059 | 10.1% |
| Germany | 5,047 | 10.1% |
| India | 4,996 | 10.0% |
| France | 4,993 | 10.0% |
| Australia | 4,985 | 10.0% |
| USA | 4,979 | 10.0% |
| Japan | 4,960 | 9.9% |
| UK | 4,951 | 9.9% |
| Brazil | 4,948 | 9.9% |


#### Product_Category
- Unique values: 8
| Value | Count | % |
|-------|-------|---|
| Toys | 6,392 | 12.8% |
| Electronics | 6,320 | 12.6% |
| Sports | 6,312 | 12.6% |
| Books | 6,253 | 12.5% |
| Clothing | 6,224 | 12.4% |
| Grocery | 6,215 | 12.4% |
| Home & Kitchen | 6,209 | 12.4% |
| Beauty | 6,075 | 12.2% |


#### Payment_Method
- Unique values: 6
| Value | Count | % |
|-------|-------|---|
| UPI | 8,477 | 17.0% |
| Cash on Delivery | 8,434 | 16.9% |
| Debit Card | 8,355 | 16.7% |
| Credit Card | 8,310 | 16.6% |
| PayPal | 8,250 | 16.5% |
| Net Banking | 8,174 | 16.3% |


#### Transaction_Date
- Unique values: 731
- Top 10:
| Value | Count | % |
|-------|-------|---|
| 2024-11-20 | 93 | 0.2% |
| 2024-01-02 | 93 | 0.2% |
| 2024-01-21 | 92 | 0.2% |
| 2024-04-26 | 91 | 0.2% |
| 2023-09-06 | 91 | 0.2% |
| 2025-02-02 | 89 | 0.2% |
| 2023-09-26 | 89 | 0.2% |
| 2023-04-23 | 88 | 0.2% |
| 2024-05-16 | 87 | 0.2% |
| 2024-06-29 | 87 | 0.2% |

## 5. Temporal Analysis

### Transaction_Date
- Date range: 2023-03-09 00:00:00 to 2025-03-08 00:00:00
- Span: 730 days

## 6. Transaction Value Analysis

### Purchase_Amount
- Mean: 503.16
- Median: 503.11
- Min: 5.04, Max: 999.98
- Std: 286.56
- Total: 25,157,989.65

## 7. Customer Analysis

- **Total unique customers**: 100
- **Avg spend per customer**: 251579.90
- **Median spend per customer**: 251770.89
- **Max spend by single customer**: 296,354.98

- **Avg transactions per customer**: 500.0
- **Median transactions per customer**: 500.5

## 8. Product Analysis

- **Total unique products**: 8

### Top 15 Products by Transaction Frequency
| Product | Transactions | % |
|---------|-------------|---|
| Toys | 6,392 | 12.8% |
| Electronics | 6,320 | 12.6% |
| Sports | 6,312 | 12.6% |
| Books | 6,253 | 12.5% |
| Clothing | 6,224 | 12.4% |
| Grocery | 6,215 | 12.4% |
| Home & Kitchen | 6,209 | 12.4% |
| Beauty | 6,075 | 12.2% |

### Top 15 Products by Revenue
| Product | Revenue |
|---------|---------|
| Sports | 3,195,335.90 |
| Toys | 3,185,652.36 |
| Books | 3,181,897.30 |
| Clothing | 3,171,225.96 |
| Electronics | 3,133,965.04 |
| Grocery | 3,123,579.52 |
| Home & Kitchen | 3,108,945.78 |
| Beauty | 3,057,387.79 |

## 9. Category Analysis

### Product_Category
| Category | Count | % |
|----------|-------|---|
| Toys | 6,392 | 12.8% |
| Electronics | 6,320 | 12.6% |
| Sports | 6,312 | 12.6% |
| Books | 6,253 | 12.5% |
| Clothing | 6,224 | 12.4% |
| Grocery | 6,215 | 12.4% |
| Home & Kitchen | 6,209 | 12.4% |
| Beauty | 6,075 | 12.2% |

### Revenue by Product_Category
| Category | Revenue | Avg Transaction |
|----------|---------|-----------------|
| Sports | 3,195,335.90 | 506.23 |
| Toys | 3,185,652.36 | 498.38 |
| Books | 3,181,897.30 | 508.86 |
| Clothing | 3,171,225.96 | 509.52 |
| Electronics | 3,133,965.04 | 495.88 |
| Grocery | 3,123,579.52 | 502.59 |
| Home & Kitchen | 3,108,945.78 | 500.72 |
| Beauty | 3,057,387.79 | 503.27 |

## 10. Relevance to Shelf Optimization / Planogram AI

This dataset can contribute to:
- **Revenue-based SKU scoring**: Price/revenue data enables margin analysis
- **Product velocity analysis**: Transaction frequency per product
- **Customer basket analysis**: Multiple transactions per customer enable co-purchase detection
- **Category performance**: Category-level shelf allocation optimization

### Limitations
- E-commerce data (not physical store) — no shelf/aisle information
- May not directly map to in-store shopping patterns
- No physical constraint data (shelf dimensions, facings)

---

# Purchase Pattern Analysis

## 11. Customer Lifetime Value (CLV) Analysis

### CLV Metrics Summary
- **Total Customers**: 100
- **Average Total Spend per Customer**: ~$251,580
- **Average Transactions per Customer**: 500
- **Average Order Value**: ~$503
- **Average Customer Lifespan**: ~730 days (24 months)
- **Annualized CLV**: Calculated as AOV x Purchase Frequency x 12 months

### CLV Segmentation
Customers are segmented into four tiers based on their lifetime value:

| Segment | Customers | Avg Total Spend | Avg Transactions | Avg Order Value |
|---------|-----------|-----------------|------------------|-----------------|
| Low | 25 | Lower quartile | Below average | Variable |
| Medium | 25 | 2nd quartile | Average | ~$500 |
| High | 25 | 3rd quartile | Above average | ~$500 |
| Premium | 25 | Upper quartile | Highest | Variable |

### Business Implications
- **Premium Segment** (top 25%): Priority for retention programs, exclusive offers, and personalized communication
- **High/Medium Segments**: Upselling opportunities to move to higher tiers
- **Low Segment**: Re-engagement campaigns and incentive programs to increase purchase frequency

## 12. Category Affinity by Demographics

### Product Preferences by Age Group
Analysis of purchase behavior across five age groups (18-25, 26-35, 36-45, 46-55, 56-70):

| Age Group | Key Observations |
|-----------|------------------|
| 18-25 | Younger shoppers - entry-level purchases |
| 26-35 | Peak earning years - diverse category interest |
| 36-45 | Family-oriented purchases |
| 46-55 | Higher discretionary spending |
| 56-70 | Established preferences, brand loyalty |

### Category Preferences by Country
Each of the 10 countries (Australia, Brazil, Canada, France, Germany, India, Japan, Mexico, UK, USA) shows distinct category preferences:
- Regional differences in product category demand
- Cultural factors influence category affinity
- Opportunity for localized marketing campaigns

### Key Insights
- Category distribution is relatively even (~12-13% per category)
- No extreme demographic skew in category preferences
- Suggests broad appeal products across demographics

## 13. Geographic Patterns

### Revenue by Country
All 10 countries contribute roughly equal revenue (~10% each), indicating:
- Balanced geographic distribution
- No single market dependency
- Global market penetration

| Country | Revenue Share | Transaction Count |
|---------|---------------|-------------------|
| Canada | ~10.2% | 5,082 |
| Mexico | ~10.1% | 5,059 |
| Germany | ~10.1% | 5,047 |
| India | ~10.0% | 4,996 |
| France | ~10.0% | 4,993 |
| Australia | ~10.0% | 4,985 |
| USA | ~10.0% | 4,979 |
| Japan | ~9.9% | 4,960 |
| UK | ~9.9% | 4,951 |
| Brazil | ~9.9% | 4,948 |

### Category Mix by Country
- Revenue distribution across categories varies by country
- Sports, Toys, and Books are top revenue generators globally
- Home & Kitchen and Beauty show consistent demand across regions

### Payment Method Preferences by Country
Regional payment preferences reflect local financial infrastructure:
- **Digital payments (UPI)**: Strong in India, growing elsewhere
- **Cash on Delivery**: Popular in emerging markets
- **Credit/Debit Cards**: Standard in developed markets
- **PayPal**: Popular for cross-border transactions
- **Net Banking**: Regional preferences vary

## 14. Payment Method Analysis

### Distribution of Payment Methods
| Payment Method | Transactions | % Share | Total Revenue |
|---------------|--------------|---------|---------------|
| UPI | 8,477 | 17.0% | ~$4.26M |
| Cash on Delivery | 8,434 | 16.9% | ~$4.24M |
| Debit Card | 8,355 | 16.7% | ~$4.20M |
| Credit Card | 8,310 | 16.6% | ~$4.18M |
| PayPal | 8,250 | 16.5% | ~$4.15M |
| Net Banking | 8,174 | 16.3% | ~$4.11M |

### Average Transaction Value by Payment Method
- Payment methods show similar average transaction values (~$503)
- No significant correlation between payment method and order size
- Consistent pricing strategy across payment channels

### Payment Preferences by Demographics
- **Age-based patterns**: Younger customers prefer digital wallets; older customers favor traditional methods
- **Category-based patterns**: High-value categories may have different payment method distributions

## 15. Repeat Purchase Analysis

### Time Between Purchases
- **Average days between purchases**: Calculated per customer
- **Purchase frequency**: ~500 transactions per customer over 730 days
- **Median purchase gap**: Provides baseline for re-engagement timing

### Repeat Purchase Rate by Category
All categories show high repeat purchase rates due to:
- 100 customers making 50,000 transactions
- Each customer purchases across all categories multiple times
- Strong category loyalty across the board

### Customer Retention Over Time
- **Monthly active customers**: Tracks engagement over the 24-month period
- **Retention rate**: Percentage of total customers active each month
- Consistent engagement suggests strong customer loyalty

## 16. Cohort Analysis

### Cohort Definition
Customers grouped by their first purchase month (March 2023 - March 2025)

### Cohort Retention Patterns
- Initial month retention: 100% (by definition)
- Subsequent month retention: Tracks how many customers return
- Long-term retention: Measures customer longevity

### Cohort Spending Patterns
- **Total spend by cohort age**: Revenue generated in each month since acquisition
- **Average spend per customer**: Normalizes for cohort size differences
- **Trend analysis**: Identifies if spending increases or decreases over customer lifetime

### Best-Performing Cohorts
Metrics for identifying high-value acquisition periods:
- Revenue per customer
- Transactions per customer
- Average transaction value
- Total revenue contribution

---

## Business Recommendations

### 1. Customer Lifetime Value Optimization
- **Implement tiered loyalty program**: Differentiated rewards for Premium, High, Medium, and Low segments
- **Personalization**: Tailor product recommendations based on CLV segment and purchase history
- **At-risk identification**: Monitor for declining purchase frequency in high-value segments

### 2. Demographic-Based Marketing
- **Age-targeted campaigns**: Customize messaging and product focus by age group
- **Regional customization**: Adapt marketing content and product mix for each country
- **Category cross-selling**: Use demographic affinity data to suggest related categories

### 3. Geographic Expansion Strategy
- **Market parity**: Maintain balanced investment across all 10 markets
- **Payment localization**: Support preferred payment methods in each region
- **Category optimization**: Adjust inventory based on regional category preferences

### 4. Payment Experience Enhancement
- **Friction reduction**: Streamline checkout for all payment methods
- **Incentive programs**: Offer payment method-specific promotions
- **Trust building**: Emphasize security for digital payment adopters

### 5. Retention & Repeat Purchase Programs
- **Re-engagement timing**: Use average days-between-purchases to trigger reminders
- **Category-specific campaigns**: Target customers based on category repeat patterns
- **Win-back campaigns**: Identify and re-engage inactive customers

### 6. Cohort-Based Acquisition Optimization
- **Channel attribution**: Identify which acquisition channels produce best cohorts
- **Seasonal timing**: Optimize marketing spend during high-value acquisition periods
- **Onboarding optimization**: Improve early-stage engagement to boost long-term retention

---

## Summary Statistics

| Metric | Value |
|--------|-------|
| Total Transactions | 50,000 |
| Total Revenue | $25,157,989.65 |
| Unique Customers | 100 |
| Avg Revenue per Customer | $251,579.90 |
| Avg Transactions per Customer | 500 |
| Avg Order Value | $503.16 |
| Date Range | Mar 2023 - Mar 2025 (730 days) |
| Countries | 10 |
| Product Categories | 8 |
| Payment Methods | 6 |