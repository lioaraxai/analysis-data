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