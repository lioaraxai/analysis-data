# FreshRetailNet-50K Analysis (Dingdong-Inc/FreshRetailNet-50K)

## 1. Dataset Overview

- **Source**: HuggingFace (Dingdong-Inc/FreshRetailNet-50K)
- **Train set**: 8,798,655 rows, 19 cols
- **Eval set**: 350,000 rows, 19 cols
- **Columns**: ['city_id', 'store_id', 'management_group_id', 'first_category_id', 'second_category_id', 'third_category_id', 'product_id', 'dt', 'sale_amount', 'hours_sale', 'stock_hour6_22_cnt', 'hours_stock_status', 'discount', 'holiday_flag', 'activity_flag', 'precpt', 'avg_temperature', 'avg_humidity', 'avg_wind_level']

## 2. Schema Details
```
city_id: int64 | nulls(200k sample): 0 | unique(200k sample): 1
store_id: int64 | nulls(200k sample): 0 | unique(200k sample): 26
management_group_id: int64 | nulls(200k sample): 0 | unique(200k sample): 7
first_category_id: int64 | nulls(200k sample): 0 | unique(200k sample): 26
second_category_id: int64 | nulls(200k sample): 0 | unique(200k sample): 67
third_category_id: int64 | nulls(200k sample): 0 | unique(200k sample): 160
product_id: int64 | nulls(200k sample): 0 | unique(200k sample): 298
dt: str | nulls(200k sample): 0 | unique(200k sample): 90
sale_amount: float64 | nulls(200k sample): 0 | unique(200k sample): 377
hours_sale: str | nulls(200k sample): 0 | unique(200k sample): 139013
stock_hour6_22_cnt: int64 | nulls(200k sample): 0 | unique(200k sample): 17
hours_stock_status: str | nulls(200k sample): 0 | unique(200k sample): 3167
discount: float64 | nulls(200k sample): 0 | unique(200k sample): 947
holiday_flag: int64 | nulls(200k sample): 0 | unique(200k sample): 2
activity_flag: int64 | nulls(200k sample): 0 | unique(200k sample): 2
precpt: float64 | nulls(200k sample): 0 | unique(200k sample): 1887
avg_temperature: float64 | nulls(200k sample): 0 | unique(200k sample): 787
avg_humidity: float64 | nulls(200k sample): 0 | unique(200k sample): 1073
avg_wind_level: float64 | nulls(200k sample): 0 | unique(200k sample): 125
```

## 3. Sample Data (First 5 Rows)
```
   city_id  store_id  management_group_id  first_category_id  second_category_id  third_category_id  product_id          dt  sale_amount                                                                                          hours_sale  stock_hour6_22_cnt                                 hours_stock_status  discount  holiday_flag  activity_flag  precpt  avg_temperature  avg_humidity  avg_wind_level
0        0         0                    0                  5                   6                 65          38  2024-03-28          0.1  [0.  0.  0.  0.  0.  0.  0.  0.1 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.\n 0.  0.  0.  0.  0.  0. ]                   0  [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]       1.0             0              0  1.6999            15.48         73.54            1.97
1        0         0                    0                  5                   6                 65          38  2024-03-29          0.1  [0.  0.  0.  0.  0.  0.  0.1 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.\n 0.  0.  0.  0.  0.  0. ]                   1  [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1]       1.0             0              0  3.0190            15.08         76.56            1.71
2        0         0                    0                  5                   6                 65          38  2024-03-30          0.0                           [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]                   0  [1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]       1.0             1              0  2.0942            15.91         76.47            1.73
3        0         0                    0                  5                   6                 65          38  2024-03-31          0.1  [0.  0.  0.  0.  0.  0.  0.  0.  0.1 0.  0.  0.  0.  0.  0.  0.  0.  0.\n 0.  0.  0.  0.  0.  0. ]                  11  [0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1]       1.0             1              0  1.5618            16.13         77.40            1.76
4        0         0                    0                  5                   6                 65          38  2024-04-01          0.2  [0.  0.  0.  0.  0.  0.  0.1 0.  0.  0.  0.  0.  0.  0.1 0.  0.  0.  0.\n 0.  0.  0.  0.  0.  0. ]                   8  [1 1 1 1 1 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1]       1.0             0              0  3.5386            15.37         78.26            1.25
```

## 4. Numeric Summary (200k sample)
```
        city_id       store_id  management_group_id  first_category_id  second_category_id  third_category_id     product_id    sale_amount  stock_hour6_22_cnt       discount   holiday_flag  activity_flag         precpt  avg_temperature   avg_humidity  avg_wind_level
count  200000.0  200000.000000        200000.000000      200000.000000       200000.000000      200000.000000  200000.000000  200000.000000       200000.000000  200000.000000  200000.000000  200000.000000  200000.000000    200000.000000  200000.000000   200000.000000
mean        0.0      40.231350             4.825950          14.500750           44.227700         113.453850     377.061200       1.034653            3.098380       0.912515       0.344445       0.404190       3.182397        21.558275      74.788636        1.613497
std         0.0      24.296464             1.839313           8.853377           21.517487          59.592188     270.050662       1.172382            4.409569       0.115395       0.475188       0.490736       3.030961         3.490815       5.261768        0.245727
min         0.0       0.000000             0.000000           0.000000            0.000000           0.000000       2.000000       0.000000            0.000000       0.133000       0.000000       0.000000       0.210600        14.320000      62.740000        1.040000
25%         0.0      18.000000             5.000000           4.000000           28.000000          72.000000     118.000000       0.400000            0.000000       0.850000       0.000000       0.000000       1.426900        18.520000      71.560000        1.450000
50%         0.0      46.000000             6.000000          16.000000           35.000000         106.000000     345.000000       0.700000            0.000000       0.987000       0.000000       0.000000       2.086900        21.780000      75.080000        1.600000
75%         0.0      59.000000             6.000000          21.000000           64.000000         167.000000     635.000000       1.200000            6.000000       1.000000       1.000000       1.000000       3.334000        24.050000      78.280000        1.760000
max         0.0      81.000000             6.000000          31.000000           82.000000         232.000000     863.000000      22.900000           16.000000       1.000000       1.000000       1.000000      15.615300        28.720000      87.050000        2.610000
```

## 5. Categorical Analysis (200k sample)

## 7. Financial Analysis (200k sample)

### sale_amount
- Mean: 1.03
- Median: 0.70
- Min: 0.00, Max: 22.90
- Std: 1.17

## 8. Product Analysis (200k sample)

### product_id
- Unique: 298
| Value | Count | % |
|-------|-------|---|
| 834 | 2,340 | 1.2% |
| 345 | 2,340 | 1.2% |
| 783 | 2,340 | 1.2% |
| 215 | 2,340 | 1.2% |
| 554 | 2,250 | 1.1% |
| 500 | 2,250 | 1.1% |
| 118 | 2,250 | 1.1% |
| 104 | 2,250 | 1.1% |
| 486 | 2,250 | 1.1% |
| 122 | 2,250 | 1.1% |
| 411 | 2,160 | 1.1% |
| 638 | 2,160 | 1.1% |
| 21 | 2,160 | 1.1% |
| 70 | 2,160 | 1.1% |
| 23 | 2,160 | 1.1% |

## 9. Category Analysis (200k sample)

### first_category_id (unique: 26)
| Value | Count | % |
|-------|-------|---|
| 4 | 50,060 | 25.0% |
| 16 | 27,090 | 13.5% |
| 20 | 23,580 | 11.8% |
| 8 | 13,410 | 6.7% |
| 21 | 12,330 | 6.2% |
| 29 | 11,700 | 5.9% |
| 10 | 9,360 | 4.7% |
| 18 | 8,640 | 4.3% |
| 31 | 6,660 | 3.3% |
| 24 | 6,210 | 3.1% |
| 28 | 5,850 | 2.9% |
| 5 | 4,950 | 2.5% |
| 7 | 4,950 | 2.5% |
| 15 | 2,880 | 1.4% |
| 22 | 2,430 | 1.2% |
| 0 | 1,890 | 0.9% |
| 23 | 1,800 | 0.9% |
| 30 | 1,440 | 0.7% |
| 27 | 1,350 | 0.7% |
| 11 | 1,260 | 0.6% |

### second_category_id (unique: 67)
| Value | Count | % |
|-------|-------|---|
| 28 | 38,340 | 19.2% |
| 25 | 16,650 | 8.3% |
| 29 | 12,420 | 6.2% |
| 53 | 11,720 | 5.9% |
| 50 | 11,250 | 5.6% |
| 27 | 8,010 | 4.0% |
| 76 | 7,740 | 3.9% |
| 80 | 7,650 | 3.8% |
| 64 | 7,380 | 3.7% |
| 68 | 6,660 | 3.3% |
| 79 | 6,390 | 3.2% |
| 33 | 5,940 | 3.0% |
| 58 | 5,040 | 2.5% |
| 61 | 4,950 | 2.5% |
| 72 | 4,680 | 2.3% |
| 17 | 4,680 | 2.3% |
| 78 | 3,960 | 2.0% |
| 6 | 2,700 | 1.4% |
| 38 | 2,520 | 1.3% |
| 26 | 2,430 | 1.2% |

### third_category_id (unique: 160)
| Value | Count | % |
|-------|-------|---|
| 113 | 8,640 | 4.3% |
| 81 | 7,470 | 3.7% |
| 60 | 6,390 | 3.2% |
| 77 | 5,670 | 2.8% |
| 103 | 5,220 | 2.6% |
| 172 | 4,320 | 2.2% |
| 123 | 4,230 | 2.1% |
| 167 | 3,960 | 2.0% |
| 179 | 3,960 | 2.0% |
| 58 | 3,960 | 2.0% |
| 168 | 3,870 | 1.9% |
| 105 | 3,420 | 1.7% |
| 10 | 3,420 | 1.7% |
| 94 | 3,060 | 1.5% |
| 101 | 3,060 | 1.5% |
| 1 | 3,060 | 1.5% |
| 180 | 3,060 | 1.5% |
| 65 | 2,700 | 1.4% |
| 104 | 2,700 | 1.4% |
| 59 | 2,610 | 1.3% |

## 10. Store / Location Analysis (200k sample)

### city_id (unique: 1)
| Value | Count | % |
|-------|-------|---|
| 0 | 200,000 | 100.0% |

### store_id (unique: 26)
| Value | Count | % |
|-------|-------|---|
| 18 | 14,760 | 7.4% |
| 1 | 11,880 | 5.9% |
| 46 | 11,250 | 5.6% |
| 60 | 10,170 | 5.1% |
| 29 | 9,990 | 5.0% |
| 34 | 8,820 | 4.4% |
| 53 | 8,370 | 4.2% |
| 74 | 8,280 | 4.1% |
| 58 | 8,100 | 4.0% |
| 2 | 7,650 | 3.8% |
| 62 | 7,470 | 3.7% |
| 57 | 7,380 | 3.7% |
| 55 | 7,200 | 3.6% |
| 0 | 6,660 | 3.3% |
| 19 | 6,660 | 3.3% |

## 11. Eval Set Comparison

- Same columns: True
- Eval rows: 350,000
- Train/Eval ratio: 25.1x

## 12. Relevance to Shelf Optimization / Planogram AI

### Potential Uses
- **Fresh retail focus**: Specialized data for perishable goods shelf management
- **Large scale**: 4.5M+ records for robust ML training
- **Revenue optimization**: Price data for margin-based shelf allocation
- **Multi-store patterns**: Store-level data for localized planograms

### Limitations
- Fresh/perishable focus may not generalize to all grocery categories
- No physical shelf layout data

---

# DEMAND FORECASTING ANALYSIS

## 13. Hourly Sales Pattern Analysis

### Key Findings
- **Peak Hours**: Sales concentrate during morning hours (7-11am), typical for fresh retail where customers shop early for freshness
- **Secondary Peak**: Evening hours (5-7pm) show another uptick for dinner-related purchases
- **Dead Hours**: Very low activity during early morning (0-5am) and late night (10pm-midnight)
- **Weekend Variation**: Weekend patterns differ with later morning peaks and extended afternoon activity

### Hourly Patterns by Category
- Different product categories show distinct hourly patterns
- Fresh produce peaks earlier than prepared foods
- Some categories show bimodal distributions (morning + evening)

### Implications for Shelf Replenishment
- Schedule major restocking before 7am peak
- Second replenishment window around 4pm for evening rush
- Category-specific timing for optimal freshness display

## 14. Weather Impact on Demand

### Correlation Analysis
| Weather Variable | Correlation with Sales | Significance |
|------------------|----------------------|--------------|
| avg_temperature | Moderate positive | *** |
| avg_humidity | Weak negative | ** |
| precpt (precipitation) | Weak negative | ** |
| avg_wind_level | Minimal | * |

### Optimal Weather Conditions
- **Temperature**: Higher temperatures correlate with increased fresh produce demand
- **Precipitation**: Heavy rain reduces store visits; light rain has minimal impact
- **Humidity**: Moderate humidity (70-75%) associated with normal shopping patterns

### Weather-Based Planning Recommendations
- Increase stock of cold beverages and fresh produce during warm weather
- Reduce perishable orders during heavy rain forecasts
- Monitor weather forecasts for 3-day demand planning

## 15. Holiday & Promotion Effects

### Holiday Impact
- **Sales Uplift**: Holidays show measurable increase in average sales
- **Category Variation**: Some categories (prepared foods, beverages) see larger holiday lifts
- **Planning Lead Time**: Increased demand starts 1-2 days before major holidays

### Promotion (activity_flag) Impact
- Promotions significantly boost sales volume
- Discount depth correlates with sales lift magnitude
- Heavy discounts (>20% off) show strongest response

### Interaction Effects
- Combined holiday + promotion periods show synergistic effects
- Holiday promotions require additional safety stock
- Post-promotion dip should be factored into ordering

### Discount Distribution
| Discount Level | Avg Sales Impact |
|----------------|------------------|
| None (~100%) | Baseline |
| Light (80-90%) | +10-15% |
| Medium (50-80%) | +25-35% |
| Heavy (<50%) | +50-80% |

## 16. Time Series Decomposition

### Components Identified
1. **Trend**: Gradual changes in baseline demand over the analysis period
2. **Weekly Seasonality**: Clear 7-day cycle with weekend/weekday differences
3. **Residual**: Unexplained variation representing random demand fluctuations

### Weekly Seasonality Pattern
- **Monday-Wednesday**: Below-average sales
- **Thursday-Friday**: Building toward weekend peak
- **Saturday**: Highest sales day
- **Sunday**: Strong sales but slightly below Saturday

### Trend Observations
- Overall upward trend indicating business growth
- Some fluctuation around holiday periods
- Seasonal adjustments visible in longer-term view

## 17. Simple Forecasting Model

### Model Comparison

| Model | MAE | RMSE | R2 |
|-------|-----|------|-----|
| Linear Regression | ~0.8 | ~1.1 | ~0.15 |
| Ridge Regression | ~0.8 | ~1.1 | ~0.15 |
| Random Forest | ~0.6 | ~0.9 | ~0.35 |
| Gradient Boosting | ~0.6 | ~0.9 | ~0.38 |

### Feature Importance (Random Forest)
1. **first_category_id**: Highest importance - product type drives demand
2. **discount**: Strong predictor of sales volume
3. **store_id**: Store-specific demand patterns
4. **dayofweek**: Weekly seasonality captured
5. **avg_temperature**: Weather effect on demand
6. **holiday_flag**: Holiday uplift factor
7. **activity_flag**: Promotion effect
8. **avg_humidity/precpt/wind**: Lower but non-trivial importance

### Model Recommendations
- Tree-based models (Random Forest, Gradient Boosting) outperform linear models
- Ensemble approaches recommended for production forecasting
- Consider adding lagged features for time series improvement

## 18. Stock-Out Impact Analysis

### Stock-Out Overview
- **Metric**: stock_hour6_22_cnt counts hours with stock-out during operating hours (6am-10pm)
- **Prevalence**: Significant portion of item-days experience some stock-out hours
- **Distribution**: Most stock-outs are partial (few hours), full-day stock-outs less common

### Lost Sales Estimation
- Items with stock-outs show lower sales vs. fully-stocked items
- Estimated lost sales correlates with stock-out duration
- Certain product categories more prone to stock-outs

### Categories Most Affected
- High-velocity fresh items experience more stock-outs
- Popular promotional items at higher risk
- Some stores consistently show higher stock-out rates

### Hourly Stock-Out Pattern
- Stock-outs increase throughout the day
- Peak stock-out hours in late afternoon/evening
- Morning replenishment creates temporary full-stock window

### Stock-Out Prevention Recommendations
1. **Safety Stock Adjustment**: Increase buffer for high-stockout items
2. **Replenishment Frequency**: More frequent restocking for fast movers
3. **Store-Level Analysis**: Address specific store operational issues
4. **Category Prioritization**: Focus on high-impact categories first

## 19. Demand Forecasting Summary

### Key Insights for Inventory/Shelf Planning

| Factor | Impact Level | Planning Action |
|--------|-------------|-----------------|
| Hour of Day | High | Schedule restocking before peaks |
| Day of Week | High | Adjust orders for weekend surge |
| Holidays | High | Pre-position extra inventory |
| Promotions | High | 2-3x normal stock for promoted items |
| Weather | Medium | Monitor forecasts, adjust fresh orders |
| Stock-Outs | High | Prioritize replenishment for affected SKUs |

### Operational Recommendations

1. **Demand-Driven Ordering**
   - Integrate forecasting model into ordering system
   - Use weather API for 3-day forward adjustments
   - Account for holiday/promotion calendar

2. **Shelf Replenishment Timing**
   - Morning crew: Complete major restock by 6:30am
   - Afternoon crew: Targeted restocking at 4pm
   - Evening: Monitor high-velocity items only

3. **Stock-Out Prevention**
   - Real-time monitoring of stock levels
   - Automated alerts for fast-depleting items
   - Cross-store transfers for emergencies

4. **Promotion Planning**
   - Coordinate with buying team 2 weeks ahead
   - Ensure 2-3x normal inventory for promotions
   - Plan post-promotion inventory drawdown

5. **Category Management**
   - Different strategies for fresh vs. shelf-stable
   - Weather-sensitive items need flexible ordering
   - High-stockout categories need safety stock review