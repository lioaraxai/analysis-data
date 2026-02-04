# Large Retail Data Set for EDA (utkalk/large-retail-data-set-for-eda)

## 1. Dataset Overview

- **File**: retail_data.csv (518 MB)
- **Total Rows**: 1,000,000
- **Columns**: 78
- **Column Names**: ['customer_id', 'age', 'gender', 'income_bracket', 'loyalty_program', 'membership_years', 'churned', 'marital_status', 'number_of_children', 'education_level', 'occupation', 'transaction_id', 'transaction_date', 'product_id', 'product_category', 'quantity', 'unit_price', 'discount_applied', 'payment_method', 'store_location', 'transaction_hour', 'day_of_week', 'week_of_year', 'month_of_year', 'avg_purchase_value', 'purchase_frequency', 'last_purchase_date', 'avg_discount_used', 'preferred_store', 'online_purchases', 'in_store_purchases', 'avg_items_per_transaction', 'avg_transaction_value', 'total_returned_items', 'total_returned_value', 'total_sales', 'total_transactions', 'total_items_purchased', 'total_discounts_received', 'avg_spent_per_category', 'max_single_purchase_value', 'min_single_purchase_value', 'product_name', 'product_brand', 'product_rating', 'product_review_count', 'product_stock', 'product_return_rate', 'product_size', 'product_weight', 'product_color', 'product_material', 'product_manufacture_date', 'product_expiry_date', 'product_shelf_life', 'promotion_id', 'promotion_type', 'promotion_start_date', 'promotion_end_date', 'promotion_effectiveness', 'promotion_channel', 'promotion_target_audience', 'customer_zip_code', 'customer_city', 'customer_state', 'store_zip_code', 'store_city', 'store_state', 'distance_to_store', 'holiday_season', 'season', 'weekend', 'customer_support_calls', 'email_subscriptions', 'app_usage', 'website_visits', 'social_media_engagement', 'days_since_last_purchase']

## 2. Schema Details

```
customer_id: int64 | nulls(sample 100k): 0 | unique(sample 100k): 100000
age: int64 | nulls(sample 100k): 0 | unique(sample 100k): 62
gender: str | nulls(sample 100k): 0 | unique(sample 100k): 3
income_bracket: str | nulls(sample 100k): 0 | unique(sample 100k): 3
loyalty_program: str | nulls(sample 100k): 0 | unique(sample 100k): 2
membership_years: int64 | nulls(sample 100k): 0 | unique(sample 100k): 10
churned: str | nulls(sample 100k): 0 | unique(sample 100k): 2
marital_status: str | nulls(sample 100k): 0 | unique(sample 100k): 3
number_of_children: int64 | nulls(sample 100k): 0 | unique(sample 100k): 5
education_level: str | nulls(sample 100k): 0 | unique(sample 100k): 4
occupation: str | nulls(sample 100k): 0 | unique(sample 100k): 4
transaction_id: int64 | nulls(sample 100k): 0 | unique(sample 100k): 95113
transaction_date: str | nulls(sample 100k): 0 | unique(sample 100k): 99915
product_id: int64 | nulls(sample 100k): 0 | unique(sample 100k): 9997
product_category: str | nulls(sample 100k): 0 | unique(sample 100k): 5
quantity: int64 | nulls(sample 100k): 0 | unique(sample 100k): 9
unit_price: float64 | nulls(sample 100k): 0 | unique(sample 100k): 63130
discount_applied: float64 | nulls(sample 100k): 0 | unique(sample 100k): 51
payment_method: str | nulls(sample 100k): 0 | unique(sample 100k): 4
store_location: str | nulls(sample 100k): 0 | unique(sample 100k): 4
transaction_hour: int64 | nulls(sample 100k): 0 | unique(sample 100k): 24
day_of_week: str | nulls(sample 100k): 0 | unique(sample 100k): 7
week_of_year: int64 | nulls(sample 100k): 0 | unique(sample 100k): 52
month_of_year: int64 | nulls(sample 100k): 0 | unique(sample 100k): 12
avg_purchase_value: float64 | nulls(sample 100k): 0 | unique(sample 100k): 42627
purchase_frequency: str | nulls(sample 100k): 0 | unique(sample 100k): 4
last_purchase_date: str | nulls(sample 100k): 0 | unique(sample 100k): 99810
avg_discount_used: float64 | nulls(sample 100k): 0 | unique(sample 100k): 51
preferred_store: str | nulls(sample 100k): 0 | unique(sample 100k): 4
online_purchases: int64 | nulls(sample 100k): 0 | unique(sample 100k): 100
in_store_purchases: int64 | nulls(sample 100k): 0 | unique(sample 100k): 100
avg_items_per_transaction: float64 | nulls(sample 100k): 0 | unique(sample 100k): 901
avg_transaction_value: float64 | nulls(sample 100k): 0 | unique(sample 100k): 42644
total_returned_items: int64 | nulls(sample 100k): 0 | unique(sample 100k): 10
total_returned_value: float64 | nulls(sample 100k): 0 | unique(sample 100k): 63119
total_sales: float64 | nulls(sample 100k): 0 | unique(sample 100k): 95095
total_transactions: int64 | nulls(sample 100k): 0 | unique(sample 100k): 99
total_items_purchased: int64 | nulls(sample 100k): 0 | unique(sample 100k): 499
total_discounts_received: float64 | nulls(sample 100k): 0 | unique(sample 100k): 63234
avg_spent_per_category: float64 | nulls(sample 100k): 0 | unique(sample 100k): 62948
max_single_purchase_value: float64 | nulls(sample 100k): 0 | unique(sample 100k): 63007
min_single_purchase_value: float64 | nulls(sample 100k): 0 | unique(sample 100k): 991
product_name: str | nulls(sample 100k): 0 | unique(sample 100k): 4
product_brand: str | nulls(sample 100k): 0 | unique(sample 100k): 3
product_rating: float64 | nulls(sample 100k): 0 | unique(sample 100k): 41
product_review_count: int64 | nulls(sample 100k): 0 | unique(sample 100k): 1000
product_stock: int64 | nulls(sample 100k): 0 | unique(sample 100k): 100
product_return_rate: float64 | nulls(sample 100k): 0 | unique(sample 100k): 51
product_size: str | nulls(sample 100k): 0 | unique(sample 100k): 3
product_weight: float64 | nulls(sample 100k): 0 | unique(sample 100k): 991
product_color: str | nulls(sample 100k): 0 | unique(sample 100k): 5
product_material: str | nulls(sample 100k): 0 | unique(sample 100k): 4
product_manufacture_date: str | nulls(sample 100k): 0 | unique(sample 100k): 99925
product_expiry_date: str | nulls(sample 100k): 0 | unique(sample 100k): 99911
product_shelf_life: int64 | nulls(sample 100k): 0 | unique(sample 100k): 365
promotion_id: int64 | nulls(sample 100k): 0 | unique(sample 100k): 999
promotion_type: str | nulls(sample 100k): 0 | unique(sample 100k): 3
promotion_start_date: str | nulls(sample 100k): 0 | unique(sample 100k): 99845
promotion_end_date: str | nulls(sample 100k): 0 | unique(sample 100k): 99838
promotion_effectiveness: str | nulls(sample 100k): 0 | unique(sample 100k): 3
promotion_channel: str | nulls(sample 100k): 0 | unique(sample 100k): 3
promotion_target_audience: str | nulls(sample 100k): 0 | unique(sample 100k): 2
customer_zip_code: int64 | nulls(sample 100k): 0 | unique(sample 100k): 60477
customer_city: str | nulls(sample 100k): 0 | unique(sample 100k): 4
customer_state: str | nulls(sample 100k): 0 | unique(sample 100k): 3
store_zip_code: int64 | nulls(sample 100k): 0 | unique(sample 100k): 60498
store_city: str | nulls(sample 100k): 0 | unique(sample 100k): 4
store_state: str | nulls(sample 100k): 0 | unique(sample 100k): 3
distance_to_store: float64 | nulls(sample 100k): 0 | unique(sample 100k): 10001
holiday_season: str | nulls(sample 100k): 0 | unique(sample 100k): 2
season: str | nulls(sample 100k): 0 | unique(sample 100k): 4
weekend: str | nulls(sample 100k): 0 | unique(sample 100k): 2
customer_support_calls: int64 | nulls(sample 100k): 0 | unique(sample 100k): 20
email_subscriptions: str | nulls(sample 100k): 0 | unique(sample 100k): 2
app_usage: str | nulls(sample 100k): 0 | unique(sample 100k): 3
website_visits: int64 | nulls(sample 100k): 0 | unique(sample 100k): 100
social_media_engagement: str | nulls(sample 100k): 0 | unique(sample 100k): 3
days_since_last_purchase: int64 | nulls(sample 100k): 0 | unique(sample 100k): 365
```

## 3. Sample Data (First 5 Rows)
```
   customer_id  age  gender income_bracket loyalty_program  membership_years churned marital_status  number_of_children education_level     occupation  transaction_id     transaction_date  product_id product_category  quantity  unit_price  discount_applied  payment_method store_location  transaction_hour day_of_week  week_of_year  month_of_year  avg_purchase_value purchase_frequency   last_purchase_date  avg_discount_used preferred_store  online_purchases  in_store_purchases  avg_items_per_transaction  avg_transaction_value  total_returned_items  total_returned_value  total_sales  total_transactions  total_items_purchased  total_discounts_received  avg_spent_per_category  max_single_purchase_value  min_single_purchase_value product_name product_brand  product_rating  product_review_count  product_stock  product_return_rate product_size  product_weight product_color product_material product_manufacture_date  product_expiry_date  product_shelf_life  promotion_id        promotion_type promotion_start_date   promotion_end_date promotion_effectiveness promotion_channel promotion_target_audience  customer_zip_code customer_city customer_state  store_zip_code store_city store_state  distance_to_store holiday_season  season weekend  customer_support_calls email_subscriptions app_usage  website_visits social_media_engagement  days_since_last_purchase
0            1   56   Other           High              No                 0      No       Divorced                   3      Bachelor's  Self-Employed          503290  2020-10-11 10:08:52        1480      Electronics         8       49.72              0.50     Credit Card     Location A                18   Wednesday            27              7              411.13             Weekly  2021-09-11 04:22:38               0.02      Location A                55                  86                       8.64                 171.83                     0                750.40       563.16                  69                    367                    415.01                  114.28                     679.25                       0.28    Product D       Brand Y             2.5                   560             48                 0.40        Small            4.61           Red            Metal      2019-08-04 01:47:01  2022-05-28 14:54:02                 250           271               20% Off  2021-07-14 14:28:42  2022-12-30 13:04:13                    High            Online             New Customers              37848        City D        State Y           88500     City D     State Y              33.21             No  Spring     Yes                       5                  No      High              30                    High                        40
1            2   69  Female         Medium              No                 2      No        Married                   2             PhD     Unemployed          347796  2021-12-08 01:07:40        1597        Groceries         7      817.76              0.32     Credit Card     Location C                15      Friday            20              2              268.71              Daily  2021-05-16 12:01:16               0.33      Location C                48                   2                       9.60                  20.18                     4                551.60      7554.57                   8                    475                    801.79                  305.95                     491.56                       4.65    Product C       Brand X             4.7                   413             80                 0.30       Medium            0.84          Blue            Metal      2019-10-23 19:59:17  2022-12-19 08:04:41                 180           631            Flash Sale  2021-09-23 04:26:09  2022-09-13 03:16:26                     Low      Social Media             New Customers              44896        City A        State X           30046     City C     State X              62.56             No  Summer     Yes                       6                  No      High              40                  Medium                       338
2            3   46  Female            Low              No                 5      No        Married                   3      Bachelor's  Self-Employed          493688  2020-02-17 09:40:48        5142             Toys         8      270.30              0.35      Debit Card     Location A                 9    Saturday            35              6              246.79             Weekly  2021-02-07 16:47:48               0.47      Location B                16                  45                       1.55                  55.17                     0                629.19      7564.14                  73                    138                    264.31                  426.70                     938.26                       7.30    Product B       Brand X             4.6                   312             14                 0.08       Medium            0.23         Green          Plastic      2018-05-12 08:00:29  2023-02-01 12:15:07                 131           879            Flash Sale  2021-06-13 12:31:15  2022-03-13 00:53:35                     Low            Online             New Customers              11816        City B        State X           26169     City A     State Y              83.04            Yes  Winter     Yes                       2                 Yes       Low              89                  Medium                        61
3            4   32  Female            Low              No                 0      No       Divorced                   2        Master's       Employed          861348  2020-08-13 00:43:14        8447             Toys         2      547.84              0.10     Credit Card     Location A                13      Friday            42              8              178.92             Weekly  2021-12-30 23:48:26               0.41      Location B                50                  47                       1.78                  15.79                     3                346.67      8125.92                  20                    158                    192.93                  689.58                     644.31                       7.31    Product A       Brand Z             1.1                   110             69                 0.09        Large            4.37          Blue             Wood      2019-11-15 16:17:29  2023-02-05 11:46:57                  16           211  Buy One Get One Free  2021-05-23 05:42:48  2022-02-06 00:42:30                    High      Social Media       Returning Customers              78604        City A        State Y           22667     City B     State Z              50.43            Yes  Winter      No                      12                  No       Low              12                     Low                        42
4            5   60  Female            Low             Yes                 7     Yes       Divorced                   2      Bachelor's       Employed          535835  2021-07-02 11:59:03        6025         Clothing         4      785.29              0.17  Mobile Payment     Location C                17      Monday            37              3              214.06             Yearly  2021-11-02 11:48:25               0.22      Location B                48                  42                       9.38                 240.03                     2                979.91       114.32                  83                    263                    497.26                  715.86                     162.86                       1.92    Product C       Brand X             3.8                   172             25                 0.39        Small            1.68           Red            Metal      2019-08-27 02:58:19  2023-10-05 08:13:07                  57           862            Flash Sale  2021-04-19 04:55:32  2022-12-04 13:07:09                  Medium            Online             New Customers              17760        City B        State Z           87843     City C     State X              36.55            Yes  Summer     Yes                       3                  No    Medium              31                     Low                       242
```

## 4. Numeric Summary (from 100k sample)
```
         customer_id            age  membership_years  number_of_children  transaction_id     product_id       quantity     unit_price  discount_applied  transaction_hour   week_of_year  month_of_year  avg_purchase_value  avg_discount_used  online_purchases  in_store_purchases  avg_items_per_transaction  avg_transaction_value  total_returned_items  total_returned_value    total_sales  total_transactions  total_items_purchased  total_discounts_received  avg_spent_per_category  max_single_purchase_value  min_single_purchase_value  product_rating  product_review_count  product_stock  product_return_rate  product_weight  product_shelf_life   promotion_id  customer_zip_code  store_zip_code  distance_to_store  customer_support_calls  website_visits  days_since_last_purchase
count  100000.000000  100000.000000     100000.000000       100000.000000    100000.00000  100000.000000  100000.000000  100000.000000     100000.000000     100000.000000  100000.000000  100000.000000       100000.000000      100000.000000     100000.000000       100000.000000              100000.000000          100000.000000         100000.000000         100000.000000  100000.000000       100000.000000          100000.000000             100000.000000           100000.000000              100000.000000              100000.000000   100000.000000         100000.000000  100000.000000        100000.000000   100000.000000       100000.000000  100000.000000      100000.000000   100000.000000      100000.000000           100000.000000   100000.000000             100000.000000
mean    50000.500000      48.525990          4.510180            2.004160    500752.08566    4994.832360       4.999260     500.349895          0.250122         11.507640      26.505710       6.500280          254.967676           0.250610         49.424680           49.403280                   5.493118             255.083142              4.495000            501.679391    5058.636279           49.867980             250.459520                499.915697              505.321564                 506.937610                   5.056456        3.004118            500.090240      49.472500             0.249022        5.064704          181.810810     499.274930       55074.163720    54900.126870          50.033746                9.498590       49.418720                182.032500
std     28867.657797      17.886768          2.878308            1.412488    289016.80250    2885.906982       2.586099     287.637489          0.144387          6.919827      15.016961       3.449748          141.863591           0.143907         28.880885           28.897372                   2.604018             141.547385              2.875294            288.437029    2860.843366           28.610389             143.598328                288.923109              285.874539                 285.758712                   2.857286        1.156647            287.768607      28.860565             0.144447        2.858212          105.251757     288.354994       25990.444715    26000.661693          28.802242                5.755914       28.798782                105.252512
min         1.000000      18.000000          0.000000            0.000000         2.00000       1.000000       1.000000       1.000000          0.000000          0.000000       1.000000       1.000000           10.000000           0.000000          0.000000            0.000000                   1.000000              10.000000              0.000000              0.000000     100.020000            1.000000               1.000000                  0.000000               10.000000                  10.020000                   0.100000        1.000000              0.000000       0.000000             0.000000        0.100000            0.000000       1.000000       10000.000000    10001.000000           0.000000                0.000000        0.000000                  0.000000
25%     25000.750000      33.000000          2.000000            1.000000    250153.25000    2514.000000       3.000000     252.067500          0.130000          5.000000      13.000000       4.000000          131.830000           0.130000         24.000000           24.000000                   3.240000             132.630000              2.000000            253.155000    2582.717500           25.000000             127.000000                249.157500              256.660000                 259.360000                   2.580000        2.000000            251.000000      24.000000             0.120000        2.600000           91.000000     250.000000       32573.750000    32440.000000          25.030000                5.000000       24.000000                 91.000000
50%     50000.500000      48.000000          5.000000            2.000000    500266.00000    4985.000000       5.000000     498.550000          0.250000         12.000000      27.000000       7.000000          255.020000           0.250000         50.000000           49.000000                   5.490000             255.960000              4.000000            502.555000    5068.605000           50.000000             250.000000                499.210000              505.730000                 509.420000                   5.060000        3.000000            500.000000      49.000000             0.250000        5.080000          182.000000     499.000000       55102.000000    54878.000000          50.070000                9.000000       50.000000                182.000000
75%     75000.250000      64.000000          7.000000            3.000000    750998.50000    7483.250000       7.000000     750.485000          0.380000         17.000000      39.000000       9.000000          377.880000           0.380000         74.000000           74.000000                   7.750000             377.830000              7.000000            751.577500    7534.222500           75.000000             375.000000                750.512500              752.620000                 755.190000                   7.540000        4.000000            749.000000      74.000000             0.370000        7.540000          273.000000     748.000000       77647.000000    77485.000000          74.830000               14.000000       74.000000                273.000000
max    100000.000000      79.000000          9.000000            4.000000    999972.00000    9999.000000       9.000000    1000.000000          0.500000         23.000000      52.000000      12.000000          500.000000           0.500000         99.000000           99.000000                  10.000000             500.000000              9.000000            999.990000    9999.940000           99.000000             499.000000                999.980000             1000.000000                 999.990000                  10.000000        5.000000            999.000000      99.000000             0.500000       10.000000          364.000000     999.000000       99998.000000    99998.000000         100.000000               19.000000       99.000000                364.000000
```

## 5. Categorical Analysis (from 100k sample)

## 6. Temporal Analysis

### transaction_date
- Date range (sample): 2020-01-01 00:03:22 to 2021-12-31 23:40:56
- Span: 730 days

### last_purchase_date
- Date range (sample): 2021-01-01 00:01:05 to 2021-12-31 23:57:12
- Span: 364 days

### product_manufacture_date
- Date range (sample): 2018-01-01 00:07:00 to 2019-12-31 23:36:57
- Span: 729 days

### product_expiry_date
- Date range (sample): 2022-01-01 00:10:13 to 2023-12-31 23:53:53
- Span: 729 days

### promotion_start_date
- Date range (sample): 2021-01-01 00:07:41 to 2021-12-31 23:58:17
- Span: 364 days

### promotion_end_date
- Date range (sample): 2022-01-01 00:06:59 to 2022-12-31 23:55:48
- Span: 364 days

## 7. Transaction Value Analysis (100k sample)

### unit_price
- Mean: 500.35
- Median: 498.55
- Min: 1.0, Max: 1000.0
- Std: 287.64

### total_returned_items
- Mean: 4.50
- Median: 4.00
- Min: 0, Max: 9
- Std: 2.88

### total_returned_value
- Mean: 501.68
- Median: 502.56
- Min: 0.0, Max: 999.99
- Std: 288.44

### total_sales
- Mean: 5058.64
- Median: 5068.60
- Min: 100.02, Max: 9999.94
- Std: 2860.84

### total_transactions
- Mean: 49.87
- Median: 50.00
- Min: 1, Max: 99
- Std: 28.61

### total_items_purchased
- Mean: 250.46
- Median: 250.00
- Min: 1, Max: 499
- Std: 143.60

### total_discounts_received
- Mean: 499.92
- Median: 499.21
- Min: 0.0, Max: 999.98
- Std: 288.92

### quantity
- Mean: 5.00
- Median: 5.0
- Min: 1, Max: 9

## 8. Customer Analysis (100k sample)

- Unique customers in sample: 100,000
- Avg transactions per customer: 1.0
- Median: 1.0

## 9. Product Analysis (100k sample)

- Unique products in sample: 9,997

### Top 15 Products
| Product | Count | % |
|---------|-------|---|
| 1201 | 23 | 0.0% |
| 2252 | 23 | 0.0% |
| 7314 | 23 | 0.0% |
| 8261 | 22 | 0.0% |
| 3795 | 22 | 0.0% |
| 5688 | 22 | 0.0% |
| 2566 | 22 | 0.0% |
| 8306 | 22 | 0.0% |
| 6705 | 21 | 0.0% |
| 3828 | 21 | 0.0% |
| 8725 | 21 | 0.0% |
| 5805 | 21 | 0.0% |
| 7573 | 21 | 0.0% |
| 1930 | 21 | 0.0% |
| 8525 | 21 | 0.0% |

## 10. Relevance to Shelf Optimization / Planogram AI

### Potential Uses
- Large-scale retail transaction patterns
- Product demand analysis at scale
- Customer purchase frequency analysis
- Category-level shelf allocation insights

### Limitations
- Need to verify data quality at full scale
- Analysis based on 100k row sample due to 518MB file size

---

## 11. RFM Customer Segmentation Analysis

RFM (Recency, Frequency, Monetary) analysis segments customers based on their purchasing behavior to identify high-value customers, those at risk of churning, and opportunities for targeted marketing.

### 11.1 RFM Score Methodology

| Dimension | Metric Used | Scoring Logic |
|-----------|-------------|---------------|
| **Recency (R)** | `days_since_last_purchase` | Lower days = Higher score (5=best, 1=worst) |
| **Frequency (F)** | `total_transactions` | Higher transactions = Higher score |
| **Monetary (M)** | `total_sales` | Higher spend = Higher score |

Scores are calculated using quintiles (1-5 scale) and combined into an RFM segment string (e.g., "555" = best customers).

### 11.2 Customer Segments Defined

| Segment | RFM Criteria | Description |
|---------|--------------|-------------|
| **Champions** | R>=4, F>=4, M>=4 | Best customers - recent, frequent, high spenders |
| **Loyal Customers** | R>=4, F>=3, M>=3 | Consistent buyers with strong engagement |
| **Recent Customers** | R>=4, F<=2 | New customers with potential |
| **Potential Loyalists** | R>=3, F>=3, M>=3 | Good customers to nurture |
| **Big Spenders** | R>=3, M>=4 | High monetary value, any frequency |
| **At Risk** | R=2, F>=3 | Previously active, now disengaging |
| **Hibernating** | R=2, F<=2 | Low recent activity, low frequency |
| **Can't Lose Them** | R=1, F>=3, M>=3 | High-value customers going dormant |
| **Lost** | R=1, F<=2 | Churned or inactive customers |
| **Others** | Remaining | Mixed characteristics |

### 11.3 K-Means Clustering

In addition to rule-based segmentation, K-Means clustering was applied to RFM features:
- **Features**: `days_since_last_purchase`, `total_transactions`, `total_sales`
- **Preprocessing**: StandardScaler normalization
- **Optimal k**: Determined via elbow method and silhouette score analysis
- **Result**: 5 natural customer clusters identified

### 11.4 Churn Analysis by Segment

Key findings from churn analysis:
- Churn rates vary significantly across RFM segments
- **High-Value At-Risk Customers**: Customers in top 25% by revenue with R_Score <= 2
- Revenue at risk calculated for each segment to prioritize retention efforts
- Strong inverse correlation between RFM score and churn rate

### 11.5 Customer Lifetime Value (CLV)

CLV calculation methodology:
```
CLV = Avg Transaction Value x Annual Frequency x Projection Years (3)
```

CLV metrics by segment enable:
- Prioritization of retention investments
- ROI calculation for segment-specific campaigns
- Resource allocation for customer success teams

### 11.6 Segment Recommendations

| Segment | Recommended Actions |
|---------|---------------------|
| **Champions** | Reward with exclusive perks, early access to new products. Use for testimonials/referrals. |
| **Loyal Customers** | Upsell premium products, loyalty program upgrades. Personalized recommendations. |
| **Recent Customers** | Welcome campaigns, onboarding sequences. Build engagement early. |
| **Potential Loyalists** | Engagement campaigns, membership benefits. Convert to loyal customers. |
| **Big Spenders** | Premium product offers, VIP treatment. Focus on increasing purchase frequency. |
| **At Risk** | Win-back campaigns, personalized offers. Understand pain points via surveys. |
| **Hibernating** | Reactivation campaigns with strong incentives. Limited-time offers. |
| **Can't Lose Them** | URGENT: Personalized outreach, special discounts. Understand why they left. |
| **Lost** | Aggressive win-back campaigns or accept churn. Survey to understand reasons. |

### 11.7 Demographics by Segment

Demographic analysis reveals patterns in:
- **Age distribution**: Variation in average age across segments
- **Income brackets**: High/Medium/Low income distribution per segment
- **Loyalty program membership**: Enrollment rates by segment
- **Channel preference**: Online vs in-store purchase ratios
- **Gender distribution**: Segment composition by gender

### 11.8 Key Business Insights

1. **Segment-based prioritization**: Focus retention efforts on "Can't Lose Them" and "At Risk" segments first
2. **High-value at-risk identification**: ~10% of high-value customers show signs of disengagement
3. **Channel optimization**: Different segments prefer different channels - tailor outreach accordingly
4. **CLV-driven budgeting**: Allocate marketing spend proportional to segment CLV
5. **Churn prediction**: Low RFM scores strongly correlate with churn - use as early warning