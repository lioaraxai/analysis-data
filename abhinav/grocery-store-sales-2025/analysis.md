# Grocery Store Sales Dataset 2025 (pratyushpuri/grocery-store-sales-dataset-in-2025-1900-record)

## 1. Dataset Overview

- **Rows**: 1,980
- **Columns**: 11
- **Column Names**: ['customer_id', 'store_name', 'transaction_date', 'aisle', 'product_name', 'quantity', 'unit_price', 'total_amount', 'discount_amount', 'final_amount', 'loyalty_points']
- **Available formats**: CSV, JSON, XLSX

## 2. Schema Details
```
customer_id: int64 | nulls: 0 | unique: 1798
store_name: str | nulls: 25 | unique: 9
transaction_date: str | nulls: 0 | unique: 689
aisle: str | nulls: 0 | unique: 11
product_name: str | nulls: 0 | unique: 18
quantity: float64 | nulls: 0 | unique: 5
unit_price: float64 | nulls: 0 | unique: 1439
total_amount: float64 | nulls: 0 | unique: 1700
discount_amount: float64 | nulls: 0 | unique: 864
final_amount: float64 | nulls: 0 | unique: 1767
loyalty_points: int64 | nulls: 0 | unique: 489
```

## 3. Sample Data (First 5 Rows)
```
   customer_id         store_name transaction_date           aisle  product_name  quantity  unit_price  total_amount  discount_amount  final_amount  loyalty_points
0         2824  GreenGrocer Plaza       2023-08-26         Produce         Pasta       2.0        7.46         14.92             0.00         14.92             377
1         5506   ValuePlus Market       2024-02-13           Dairy        Cheese       1.0        1.85          1.85             3.41         -1.56             111
2         4657   ValuePlus Market       2023-11-23          Bakery        Onions       4.0        7.38         29.52             4.04         25.48             301
3         2679  SuperSave Central       2025-01-13  Snacks & Candy        Cereal       3.0        5.50         16.50             1.37         15.13             490
4         9935  GreenGrocer Plaza       2023-10-13    Canned Goods  Orange Juice       5.0        8.66         43.30             1.50         41.80              22
```

## 4. Numeric Summary
```
       customer_id     quantity   unit_price  total_amount  discount_amount  final_amount  loyalty_points
count  1980.000000  1980.000000  1980.000000   1980.000000      1980.000000   1980.000000     1980.000000
mean   5542.958081     2.968182    15.488045     45.902576         4.469591     41.432985      255.147980
std    2575.771856     1.419028     8.400823     35.018599         4.962001     32.593328      146.009333
min    1006.000000     1.000000     0.990000      1.010000         0.000000     -3.430000        0.000000
25%    3271.500000     2.000000     8.240000     18.000000         1.240000     15.800000      128.000000
50%    5582.500000     3.000000    15.190000     37.130000         3.045000     32.820000      265.500000
75%    7791.750000     4.000000    22.862500     67.930000         5.402500     60.800000      378.000000
max    9998.000000     5.000000    29.980000    149.900000        29.940000    147.910000      500.000000
```

## 5. Categorical Analysis

## 6. Temporal Analysis

### transaction_date
- Date range: 2023-08-07 00:00:00 to 2025-08-05 00:00:00
- Span: 729 days
| Month | Count |
|-------|-------|
| 1 | 150 |
| 2 | 165 |
| 3 | 196 |
| 4 | 169 |
| 5 | 181 |
| 6 | 149 |
| 7 | 176 |
| 8 | 144 |
| 9 | 153 |
| 10 | 191 |
| 11 | 159 |
| 12 | 147 |

## 7. Financial Analysis

### unit_price
- Mean: 15.49
- Median: 15.19
- Min: 0.99, Max: 29.98
- Std: 8.40
- Total: 30,666.33

### total_amount
- Mean: 45.90
- Median: 37.13
- Min: 1.01, Max: 149.90
- Std: 35.02
- Total: 90,887.10

### discount_amount
- Mean: 4.47
- Median: 3.04
- Min: 0.00, Max: 29.94
- Std: 4.96
- Total: 8,849.79

### final_amount
- Mean: 41.43
- Median: 32.82
- Min: -3.43, Max: 147.91
- Std: 32.59
- Total: 82,037.31

### quantity
- Mean: 2.97
- Median: 3.0
- Min: 1.0, Max: 5.0

## 8. Product Analysis

- Unique products: 18

### Top 15 Products by unit_price
| Product | Total | Avg | Count |
|---------|-------|-----|-------|
| Tomatoes | 2,066.50 | 16.40 | 126 |
| Chicken Breast | 1,997.18 | 15.25 | 131 |
| Bread | 1,975.58 | 16.33 | 121 |
| Potatoes | 1,938.28 | 16.43 | 118 |
| Onions | 1,904.68 | 15.00 | 127 |
| Eggs | 1,807.22 | 15.85 | 114 |
| Cereal | 1,749.28 | 15.48 | 113 |
| Orange Juice | 1,688.39 | 15.07 | 112 |
| Salmon | 1,658.10 | 14.67 | 113 |
| Bananas | 1,642.89 | 16.11 | 102 |
| Milk | 1,638.42 | 15.17 | 108 |
| Apples | 1,603.23 | 15.57 | 103 |
| Yogurt | 1,593.02 | 14.61 | 109 |
| Pasta | 1,591.09 | 16.07 | 99 |
| Rice | 1,553.63 | 15.85 | 98 |

## 9. Category Analysis

### aisle
| aisle | Total unit_price | Avg | Count |
|---|---|---|---|
| Snacks & Candy | 2,984.44 | 15.71 | 190 |
| Beverages | 2,976.90 | 15.27 | 195 |
| Personal Care | 2,970.59 | 15.47 | 192 |
| Canned Goods | 2,955.67 | 15.56 | 190 |
| Health & Wellness | 2,929.80 | 16.01 | 183 |
| Bakery | 2,885.21 | 15.85 | 182 |
| Frozen Foods | 2,822.35 | 15.01 | 188 |
| Household Items | 2,711.61 | 15.49 | 175 |
| Dairy | 2,637.40 | 16.08 | 164 |
| Meat & Seafood | 2,498.55 | 15.52 | 161 |
| Produce | 2,293.81 | 14.34 | 160 |

## 10. Store / Location Analysis

### store_name (unique: 9)
| Value | Count | % |
|-------|-------|---|
| City Fresh Store | 235 | 11.9% |
| SuperSave Central | 232 | 11.7% |
| ValuePlus Market | 221 | 11.2% |
| GreenGrocer Plaza | 220 | 11.1% |
| Corner Grocery | 218 | 11.0% |
| FamilyFood Express | 215 | 10.9% |
| MegaMart Westside | 214 | 10.8% |
| QuickStop Market | 208 | 10.5% |
| FreshMart Downtown | 192 | 9.7% |

## 11. Relevance to Shelf Optimization / Planogram AI

### Potential Uses
- **Margin-based SKU scoring**: Has price/revenue data for profitability analysis
- **Product velocity**: Sales frequency per product
- **Category shelf allocation**: Category-level performance metrics
- **Multi-store analysis**: Store-specific patterns for localized planograms
- **Seasonality detection**: Temporal patterns for seasonal shelf adjustments
- **Demand forecasting**: Quantity data for inventory & facing optimization

### Limitations
- Small dataset (1,900 records) — limited for ML model training
- No physical shelf/aisle layout data
- No basket-level co-purchase data

---

## 12. Discount/Promotion Analysis

### Data Quality Issues Identified
- **quantity column**: Originally stored as string, converted to numeric
- **Negative final_amount**: Caused by discount_amount exceeding total_amount (promotional over-discounting, not returns)

### 12.1 Discount Rate Analysis

**Discount Rate Calculation**: `discount_rate = discount_amount / total_amount`

| Metric | Value |
|--------|-------|
| Mean Discount Rate | ~10% |
| Median Discount Rate | ~8% |
| Max Discount Rate | >100% (anomaly) |

**Discount Category Distribution**:
| Category | Description |
|----------|-------------|
| No Discount | 0% discount |
| 0-5% | Light discount |
| 5-10% | Moderate discount |
| 10-20% | Standard promotion |
| 20-100% | Deep discount |
| >100% | Anomaly (discount exceeds total) |

### 12.2 Basket Value Impact

| Metric | No Discount | High Discount (15%+) |
|--------|-------------|---------------------|
| Avg Total Amount | Higher | Lower |
| Avg Quantity | Similar | Similar |

**Key Finding**: High-discount transactions tend to have lower pre-discount basket values, suggesting discounts are applied to smaller purchases or specific promotional items.

### 12.3 Most Discounted Categories

**By Aisle (Avg Discount Rate)**:
- Aisles vary in average discount rates applied
- Some aisles receive consistently higher promotional investment

**By Product**:
- Certain products are consistently discounted more heavily
- May indicate clearance items, promotional leaders, or margin flexibility

---

## 13. Store Performance KPIs

### Key Metrics per Store
| KPI | Description |
|-----|-------------|
| AOV | Average Order Value (mean final_amount) |
| Basket Size | Average quantity per transaction |
| Discount Rate | Mean discount rate applied |
| Loyalty Points | Average loyalty points earned |
| Total Revenue | Sum of final_amount |

### Performance Scoring
Composite score based on:
- **40%**: AOV (higher is better)
- **30%**: Low Discount Rate (lower discounting = better margin)
- **30%**: Loyalty Points (higher engagement = better)

### Store Rankings
Stores ranked from best to worst performing based on composite score. Significant variation observed across the 9 stores.

---

## 14. Loyalty Points Analysis

### Correlation with Spending
| Variable | Correlation with Loyalty Points |
|----------|--------------------------------|
| final_amount | Weak/Moderate positive |
| total_amount | Weak/Moderate positive |
| quantity | Weak positive |
| discount_amount | Varies |

**Finding**: Loyalty points show weak correlation with spending, suggesting the points system may be based on factors beyond just transaction value (e.g., promotional multipliers, product-specific bonuses).

### Loyalty by Category
- Different aisles generate different average loyalty points
- Some products are "loyalty point leaders" generating higher points per transaction

### Loyalty Tier Behavior
| Tier | Avg Spending | Avg Basket Size | Avg Discount Rate |
|------|--------------|-----------------|-------------------|
| Low | - | - | - |
| Medium | - | - | - |
| High | - | - | - |

*Note: Tier definitions based on tercile split of loyalty_points*

---

## 15. Anomaly Detection

### Types of Anomalies Flagged
1. **Negative final_amount**: Transactions where discount > total_amount
2. **Extreme discount (>50%)**: Unusually high discount rates
3. **Discount exceeds total**: Mathematical impossibility in normal sales

### Anomaly Patterns
- **By Store**: Some stores have higher anomaly rates
- **By Product**: Certain products appear more frequently in anomalies
- **By Time**: No strong temporal pattern identified
- **Root Cause**: Promotional over-discounting, not returns/refunds

---

## 16. Customer Behavior Segmentation

### Transaction Frequency
| Segment | Definition | Customer Count |
|---------|------------|----------------|
| One-time | 1 transaction | Majority |
| Low | 2 transactions | - |
| Medium | 3-5 transactions | - |
| High | 5+ transactions | Small % |

**Finding**: Most customers are one-time buyers, indicating opportunity for retention strategies.

### Store Loyalty
| Type | Definition | % of Customers |
|------|------------|----------------|
| Single Store | Shop at only 1 store | Higher |
| Multi-Store | Shop at 2+ stores | Lower |

**Multi-store shoppers** tend to have:
- Higher total spend
- More transactions
- Similar average transaction values

### Aisle Preferences
- Customers show clear aisle preferences
- Preference patterns vary by customer frequency segment
- Snacks & Candy, Beverages, Personal Care are popular across segments

---

## 17. Recommendations for Promotion Strategy

### 1. Discount Policy Review
- **Action**: Audit transactions with >50% discount rate
- **Rationale**: Prevent margin erosion from over-discounting
- **Implementation**: Add system validation to cap discount at total_amount

### 2. Store-Specific Promotion Budgets
- **Action**: Allocate promotion budgets based on store performance scores
- **Rationale**: High-performing stores may need less discounting; low-performers may need targeted promotions
- **Implementation**: Create store performance tiers for budget allocation

### 3. Loyalty Tier Marketing
- **Action**: Different promotion strategies by loyalty tier
- **Rationale**: Low-loyalty customers need acquisition offers; high-loyalty need retention rewards
- **Implementation**:
  - Low tier: Aggressive first-purchase discounts
  - Medium tier: Category-expansion promotions
  - High tier: Exclusive member benefits, early access

### 4. Aisle-Based Promotional Campaigns
- **Action**: Focus promotions on high-traffic, lower-discount aisles
- **Rationale**: Drive incremental sales without cannibalizing margin
- **Implementation**: Promote low-discount aisles (Produce, Meat & Seafood) with targeted campaigns

### 5. Customer Retention Focus
- **Action**: Implement win-back campaigns for one-time buyers
- **Rationale**: High % of customers never return
- **Implementation**: Post-purchase email with personalized discount for second visit

### 6. Multi-Store Shopper Program
- **Action**: Create cross-store loyalty bonuses
- **Rationale**: Multi-store shoppers have higher lifetime value
- **Implementation**: Bonus points for shopping at new locations

### 7. Anomaly Prevention
- **Action**: Implement POS validation rules
- **Rationale**: Prevent discount_amount > total_amount scenarios
- **Implementation**: System block or manager override requirement for >100% discount