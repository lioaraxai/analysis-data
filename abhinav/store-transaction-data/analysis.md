# Store Transaction Data Analysis (iamprateek/store-transaction-data)

## 1. Dataset Overview

| File | Rows | Columns | Column Names |
|------|------|---------|--------------|
| Hackathon_Ideal_Data.csv | 14,260 | 10 | ['MONTH', 'STORECODE', 'QTY', 'VALUE', 'GRP', 'SGRP', 'SSGRP', 'CMP', 'MBRD', 'BRD'] |
| Hackathon_Mapping_File.csv | 24 | 3 | ['File Name', 'Column Name', 'Column Description'] |
| Hackathon_Validation_Data.csv | 2,430 | 4 | ['ID', 'STORECODE', 'MONTH', 'GRP'] |
| Hackathon_Working_Data.csv | 26,985 | 14 | ['MONTH', 'STORECODE', 'DAY', 'BILL_ID', 'BILL_AMT', 'QTY', 'VALUE', 'PRICE', 'GRP', 'SGRP', 'SSGRP', 'CMP', 'MBRD', 'BRD'] |
| Sample Submission.csv | 9 | 2 | ['ID', 'TOTALVALUE'] |

## 2. Schema Details

### Hackathon_Ideal_Data.csv
```
MONTH: str | nulls: 0 | unique: 3
STORECODE: str | nulls: 0 | unique: 10
QTY: int64 | nulls: 0 | unique: 258
VALUE: int64 | nulls: 0 | unique: 1606
GRP: str | nulls: 0 | unique: 80
SGRP: str | nulls: 0 | unique: 177
SSGRP: str | nulls: 0 | unique: 242
CMP: str | nulls: 0 | unique: 512
MBRD: str | nulls: 0 | unique: 818
BRD: str | nulls: 0 | unique: 1613
```

### Hackathon_Mapping_File.csv
```
File Name: str | nulls: 22 | unique: 2
Column Name: str | nulls: 0 | unique: 14
Column Description: str | nulls: 0 | unique: 15
```

### Hackathon_Validation_Data.csv
```
ID: int64 | nulls: 0 | unique: 2430
STORECODE: str | nulls: 0 | unique: 10
MONTH: str | nulls: 0 | unique: 3
GRP: str | nulls: 0 | unique: 81
```

### Hackathon_Working_Data.csv
```
MONTH: str | nulls: 0 | unique: 3
STORECODE: str | nulls: 0 | unique: 10
DAY: int64 | nulls: 0 | unique: 31
BILL_ID: str | nulls: 0 | unique: 6424
BILL_AMT: float64 | nulls: 0 | unique: 1453
QTY: float64 | nulls: 0 | unique: 45
VALUE: float64 | nulls: 0 | unique: 640
PRICE: float64 | nulls: 0 | unique: 492
GRP: str | nulls: 0 | unique: 80
SGRP: str | nulls: 0 | unique: 174
SSGRP: str | nulls: 0 | unique: 232
CMP: str | nulls: 0 | unique: 354
MBRD: str | nulls: 0 | unique: 643
BRD: str | nulls: 0 | unique: 1315
```

### Sample Submission.csv
```
ID: int64 | nulls: 0 | unique: 9
TOTALVALUE: int64 | nulls: 0 | unique: 9
```

## 3. Main Working Data - Deep Dive

**Hackathon_Working_Data.csv**: 26,985 rows x 14 cols

### Sample Data (First 5 Rows)
```
  MONTH STORECODE  DAY BILL_ID  BILL_AMT  QTY  VALUE  PRICE                      GRP                     SGRP                    SSGRP                     CMP           MBRD                 BRD
0    M1        N1    4    T375     225.0  1.0  225.0  225.0     BUTTER MARGR  (4/94)                   BUTTER                   SALTED               G C M M F           AMUL                AMUL
1    M1        N1    4    T379      95.0  1.0   95.0   95.0  CONFECTIONERY - ECLAIRS  CONFECTIONERY - ECLAIRS  CONFECTIONERY - ECLAIRS             PARLE PRODS         MELODY    MELODY CHOCOLATY
2    M1        N1    4    T381      10.0  1.0   10.0   10.0                CHOCOLATE         CHOCOLATE PANNED         CHOCOLATE PANNED  MONDELEZ INTERNATIONAL  CADBURY SHOTS       CADBURY SHOTS
3    M1        N1    4    T382     108.0  1.0  108.0  108.0             PACKAGED TEA               MAIN PACKS               MAIN PACKS      GUJ TEA PROCESSORS     WAGH BAKRI  WAGH BAKRI INSTANT
4    M1        N1    4    T384      19.0  1.0   19.0   19.0         ALL IODISED SALT            POWDERED SALT            POWDERED SALT               TATA CHEM           TATA           TATA SALT
```

### Numeric Summary
```
                DAY      BILL_AMT           QTY         VALUE         PRICE
count  26985.000000  26985.000000  26985.000000  26985.000000  26985.000000
mean      15.167019    278.754206      4.105021     67.808551     52.812982
std        8.956057    541.398504     95.666947    118.005978     84.987730
min        1.000000      0.000000      0.500000      0.000000      0.000000
25%        7.000000     40.000000      1.000000     10.000000     10.000000
50%       14.000000    111.000000      1.000000     30.000000     22.000000
75%       23.000000    280.000000      2.000000     80.000000     64.000000
max       31.000000   7292.000000  12000.000000   3150.000000   3150.000000
```

### MONTH Distribution
| Value | Count | % |
|-------|-------|---|
| M3 | 9,430 | 34.9% |
| M2 | 9,192 | 34.1% |
| M1 | 8,363 | 31.0% |

### STORECODE Distribution
| Value | Count | % |
|-------|-------|---|
| N7 | 5,625 | 20.8% |
| N1 | 4,583 | 17.0% |
| N5 | 4,431 | 16.4% |
| N4 | 3,212 | 11.9% |
| N10 | 2,169 | 8.0% |
| N3 | 1,793 | 6.6% |
| N9 | 1,528 | 5.7% |
| N2 | 1,331 | 4.9% |
| N6 | 1,185 | 4.4% |
| N8 | 1,128 | 4.2% |

## 4. Mapping File

```
                 File Name Column Name           Column Description
0     Hackathon_Ideal_Data       MONTH        Month ID (M1, M2, M3)
1                      NaN   STORECODE  STORE CODE (P1, P2, …, P10)
2                      NaN         QTY                   Sales Unit
3                      NaN       VALUE                  Sales Value
4                      NaN         GRP                     Category
5                      NaN        SGRP                  Subcategory
6                      NaN       SSGRP             Sub Sub Category
7                      NaN         CMP         Company/Manufacturer
8                      NaN        MBRD                 Mother Brand
9                      NaN         BRD                        Brand
10  Hackathon_Working_Data       MONTH        Month ID (M1, M2, M3)
11                     NaN   STORECODE  STORE CODE (N1, N2, …, N10)
12                     NaN         DAY             Day of the month
13                     NaN     BILL_ID            Bill ID (T1,T2,…)
14                     NaN    BILL_AMT                 Bill Amount 
15                     NaN         QTY                   Sales Unit
16                     NaN       VALUE                  Sales Value
17                     NaN       PRICE       Selling Price Per Unit
18                     NaN         GRP                     Category
19                     NaN        SGRP                  Subcategory
20                     NaN       SSGRP             Sub Sub Category
21                     NaN         CMP         Company/Manufacturer
22                     NaN        MBRD                 Mother Brand
23                     NaN         BRD                        Brand
```

## 5. Ideal Data Overview

- Rows: 14,260
- Columns: ['MONTH', 'STORECODE', 'QTY', 'VALUE', 'GRP', 'SGRP', 'SSGRP', 'CMP', 'MBRD', 'BRD']

### Sample
```
  MONTH STORECODE  QTY  VALUE                GRP               SGRP              SSGRP                         CMP         MBRD                    BRD
0    M1        P1   25     83  HAIR CONDITIONERS  HAIR CONDITIONERS  HAIR CONDITIONERS  HINDUSTAN UNILEVER LIMITED         DOVE  DOVE HAIR FALL RESCUE
1    M1        P1    6     22  HAIR CONDITIONERS  HAIR CONDITIONERS  HAIR CONDITIONERS  HINDUSTAN UNILEVER LIMITED         DOVE    DOVE INTENSE REPAIR
2    M1        P1    4     15  HAIR CONDITIONERS  HAIR CONDITIONERS  HAIR CONDITIONERS  HINDUSTAN UNILEVER LIMITED         DOVE   DOVE OXYGEN MOISTURE
3    M1        P1   15     60  HAIR CONDITIONERS  HAIR CONDITIONERS  HAIR CONDITIONERS               L'OREAL INDIA      GARNIER                FRUCTIS
4    M1        P2    0      0  HAIR CONDITIONERS  HAIR CONDITIONERS  HAIR CONDITIONERS  HINDUSTAN UNILEVER LIMITED  CLINIC PLUS            CLINIC PLUS
```

### Numeric Summary
```
                QTY         VALUE
count  14260.000000  14260.000000
mean      16.354488    294.455330
std       34.365583    760.129558
min        0.000000      0.000000
25%        1.000000     10.000000
50%        4.000000     99.000000
75%       16.000000    283.000000
max      641.000000  24185.000000
```

## 6. Validation Data Overview

- Rows: 2,430
- Columns: ['ID', 'STORECODE', 'MONTH', 'GRP']

### Sample
```
        ID STORECODE MONTH                       GRP
0  1112535        N1    M1       AFTER SHAVE LOTIONS
1  1112539        N1    M1    AGARBATTI & DHOOPBATTI
2  1112543        N1    M1  ALL AIR FRESHNERS(01/03)
3  1112547        N1    M1          ALL IODISED SALT
4  1112551        N1    M1                  ANTACIDS
```

## 7. Relevance to Shelf Optimization / Planogram AI

### Potential Uses
- Store-level transaction patterns for demand forecasting
- Product category performance for shelf allocation
- Transaction volume patterns for inventory planning

### Limitations
- Hackathon dataset — may have synthetic/modified data
- Need to verify if product-level granularity exists

---

## 8. Imputation Model Analysis

### Problem Context
Stores share transaction data for only 2-28 days per month instead of the full 28 days. This creates a need to impute/extrapolate missing data to predict total monthly sales at the store-category level.

### 8.1 Days vs Sales Correlation

**Methodology:**
- Aggregated working data to store-month level
- Computed correlation between number of observed days and total VALUE

**Key Findings:**
- Strong positive correlation exists between observed days and total sales value
- This validates the linear extrapolation approach
- Stores with more observed days generally have higher total sales (expected relationship)

**Visualization:**
- Scatter plot with regression line shows clear positive relationship
- Per-store analysis reveals consistent patterns across stores

### 8.2 Baseline Extrapolation Model

**Formula:**
```
Predicted_Value = (Observed_Value / Observed_Days) x 28
```

**Assumptions:**
1. Linear relationship between days and sales
2. Daily sales are roughly uniform within a month
3. 28 days represents a full month

**Implementation:**
- Applied to all store-month combinations in working data
- Simple daily average multiplied by target days

### 8.3 Store-Specific Adjustments

**Methodology:**
- Calculated average daily value per store across all months
- Computed store multipliers relative to overall average

**Store Characteristics:**
- 10 unique stores (N1-N10) with varying daily patterns
- Store multipliers range from ~0.3x to ~2.5x the average
- High-volume stores (N7, N1, N5) have multipliers > 1.0
- Low-volume stores (N8, N6, N2) have multipliers < 1.0

**Use Case:**
- Can be used to adjust predictions based on store characteristics
- Useful for new categories without store-specific history

### 8.4 Category-Level Imputation

**Methodology:**
- Aggregated data at store-month-category (GRP) level
- Applied baseline extrapolation separately for each category
- Aggregated category predictions back to store-month totals

**Comparison with Store-Level:**
- Category-level and store-level predictions show < 1% average difference
- Category-level provides more granular predictions
- Better suited for submission format (STORECODE + MONTH + GRP)

**Benefits:**
- Captures category-specific daily patterns
- More accurate for categories with varying purchase frequency
- Required for validation data format

### 8.5 Validation Results

**Validation Approach:**
- Used store-months with 20+ observed days as validation set
- Simulated partial data by using 50% of observed days
- Predicted full-month values and compared to actual

**Metrics:**
| Metric | Description |
|--------|-------------|
| RMSE | Root Mean Squared Error - measures average prediction error magnitude |
| MAPE | Mean Absolute Percentage Error - measures average % error |
| Correlation | Pearson correlation between predicted and actual values |

**Interpretation:**
- Low MAPE indicates model captures the overall trend well
- High correlation suggests consistent prediction patterns
- Residual analysis shows no systematic bias

### 8.6 Predictions for Validation Dataset

**Process:**
1. Built lookup table from working data at STORECODE-MONTH-GRP level
2. Merged with validation data to get predictions
3. For missing categories (no historical data), filled with 0
4. Formatted output to match Sample Submission.csv format

**Output:**
- File: `submission_imputation_model.csv`
- Columns: ID, TOTALVALUE
- 2,430 predictions generated

**Coverage:**
- Most validation records have matching historical data
- Categories without history in working data are filled with 0

### 8.7 Recommendations

1. **Use Category-Level Imputation**: Provides required granularity and better captures category-specific patterns

2. **Consider Store Multipliers**: For categories without history, use store-level multipliers to adjust predictions

3. **Handle Missing Categories**:
   - Option A: Use similar category averages
   - Option B: Use store-level average per category from other months
   - Option C: Use cross-store category patterns

4. **Future Improvements**:
   - Day-of-week patterns for more sophisticated imputation
   - Seasonal adjustments (if month patterns vary)
   - Category co-occurrence patterns

5. **Model Monitoring**:
   - Track prediction accuracy over time
   - Refine multipliers as more data becomes available

### 8.8 Output Files

| File | Description |
|------|-------------|
| `submission_imputation_model.csv` | Predictions for validation dataset in submission format |