# Instacart Online Grocery Basket Analysis (yasserh/instacart-online-grocery-basket-analysis-dataset)

## 1. Dataset Comparison with instacart-market-basket

- Files in market-basket: ['aisles.csv', 'departments.csv', 'order_products__prior.csv', 'order_products__train.csv', 'orders.csv', 'products.csv']
- Files in grocery-basket: ['aisles.csv', 'departments.csv', 'order_products__prior.csv', 'order_products__train.csv', 'orders.csv', 'products.csv']

- aisles.csv: market-basket=2,603 bytes, grocery-basket=2,603 bytes — IDENTICAL
- departments.csv: market-basket=270 bytes, grocery-basket=270 bytes — IDENTICAL
- order_products__prior.csv: market-basket=577,550,706 bytes, grocery-basket=577,550,706 bytes — IDENTICAL
- order_products__train.csv: market-basket=24,680,147 bytes, grocery-basket=24,680,147 bytes — IDENTICAL
- orders.csv: market-basket=108,968,645 bytes, grocery-basket=108,968,645 bytes — IDENTICAL
- products.csv: market-basket=2,166,953 bytes, grocery-basket=2,166,953 bytes — IDENTICAL

> **CONCLUSION: These two datasets are IDENTICAL.** Same files, same sizes. They are the same Instacart dataset uploaded by different Kaggle users.

All analysis from `instacart-market-basket/analysis.md` applies directly to this dataset.

## 2. Dataset Overview (Confirming)

| File | Rows | Columns |
|------|------|---------|
| aisles.csv | 134 | 2 |
| departments.csv | 21 | 2 |
| products.csv | 49,688 | 4 |
| orders.csv | 3,421,083 | 7 |
| order_products__train.csv | 1,384,617 | 4 |
| order_products__prior.csv | 32,434,489 | 4 |

- **Total users**: 206,209
- **Total orders**: 3,421,083
- **Total products**: 49,688

## 3. Recommendation

Since this dataset is identical to `instacart-market-basket`, for analysis purposes:
- Use **one** of the two datasets (avoid duplicate processing)
- The `instacart-market-basket/analysis.md` contains the full detailed analysis
- This dataset can serve as a backup / validation copy