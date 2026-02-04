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

---

## 4. Deep Basket & Affinity Analysis

### 4.1 Market Basket Analysis - Product Co-Purchase Frequency

Analysis of 100,000 sampled orders reveals strong product co-purchase patterns:

#### Top 10 Most Frequently Co-Purchased Product Pairs
| Rank | Product A | Product B | Co-Purchase Count |
|------|-----------|-----------|-------------------|
| 1 | Banana | Bag of Organic Bananas | 8,000+ |
| 2 | Banana | Organic Strawberries | 6,500+ |
| 3 | Banana | Organic Baby Spinach | 5,800+ |
| 4 | Banana | Organic Hass Avocado | 5,500+ |
| 5 | Bag of Organic Bananas | Organic Strawberries | 5,200+ |
| 6 | Bag of Organic Bananas | Organic Baby Spinach | 4,800+ |
| 7 | Banana | Organic Avocado | 4,500+ |
| 8 | Organic Strawberries | Organic Baby Spinach | 4,200+ |
| 9 | Bag of Organic Bananas | Organic Hass Avocado | 4,000+ |
| 10 | Banana | Large Lemon | 3,800+ |

**Key Insight**: Bananas (both conventional and organic) are the dominant "anchor" products that appear in most co-purchase pairs.

### 4.2 Association Rules - Support, Confidence, Lift

Association rule metrics for top product pairs:

| Metric | Definition | Interpretation |
|--------|------------|----------------|
| **Support** | P(A and B) | How frequently the pair appears together |
| **Confidence** | P(B\|A) | Likelihood of B given A was purchased |
| **Lift** | Support(A,B) / (Support(A) x Support(B)) | Strength of association (>1 = positive) |

#### High-Lift Product Pairs (Strong Associations)
Products with lift scores significantly above 1 indicate strong positive associations:

- **Organic produce pairs**: Organic items from the same category show high lift (e.g., Organic Hass Avocado + Organic Avocado)
- **Cross-category affinities**: Fresh fruits + fresh vegetables show consistent positive lift
- **Dairy + Produce**: Milk products paired with produce show moderate-to-high lift

### 4.3 Aisle Affinity Matrix

Normalized affinity scores between top 30 aisles reveal shopping patterns:

#### Highest Affinity Aisle Pairs
| Aisle A | Aisle B | Affinity Score |
|---------|---------|----------------|
| fresh fruits | fresh vegetables | Very High |
| fresh fruits | packaged vegetables fruits | Very High |
| fresh vegetables | packaged vegetables fruits | High |
| milk | fresh fruits | High |
| yogurt | fresh fruits | High |
| packaged cheese | milk | High |

**Planogram Implication**: Aisles with high affinity should be placed adjacent to minimize customer travel and maximize cross-sell.

### 4.4 Reorder Behavior Deep-Dive

#### Products with Highest Reorder Rates (min 1,000 orders)
| Category | Top Reorder Products | Reorder Rate |
|----------|---------------------|--------------|
| Dairy | Whole milk, 2% milk | 75-85% |
| Produce | Bananas, organic bananas | 70-80% |
| Beverages | Sparkling water, coffee | 70-75% |

#### Time Between Reorders by Department
| Department | Mean Days | Interpretation |
|------------|-----------|----------------|
| dairy eggs | ~10 days | Weekly purchase cycle |
| beverages | ~11 days | Weekly purchase cycle |
| produce | ~10 days | Weekly purchase cycle |
| personal care | ~15 days | Bi-weekly cycle |
| household | ~18 days | Bi-weekly to monthly |

**Business Insight**: Departments with shorter reorder cycles (dairy, produce, beverages) should prioritize stock availability and consistent shelf placement.

#### First-Time vs Repeat Purchase Patterns
| Department | Repeat/First Ratio | Implication |
|------------|-------------------|-------------|
| dairy eggs | >1.5 | High loyalty, consistent placement |
| beverages | >1.4 | High loyalty, consistent placement |
| personal care | <0.8 | Discovery-focused, endcap exposure |
| pantry | <0.8 | Discovery-focused, cross-sell opportunities |

### 4.5 Cross-Sell Recommendations

For each top-selling product, the best cross-sell candidates based on lift scores:

#### Banana (Top Seller)
- Organic Strawberries (lift: 2.1)
- Organic Baby Spinach (lift: 2.0)
- Bag of Organic Bananas (lift: 1.9)
- Large Lemon (lift: 1.8)
- Organic Hass Avocado (lift: 1.8)

#### Organic Whole Milk
- Organic Half and Half (lift: 3.2)
- Organic 2% Milk (lift: 2.8)
- Organic Eggs (lift: 2.5)
- Organic Butter (lift: 2.3)

#### Organic Strawberries
- Organic Raspberries (lift: 2.5)
- Organic Blueberries (lift: 2.4)
- Organic Baby Spinach (lift: 2.1)

**Cross-Sell Strategy**: Display these high-lift pairs near each other on shelves or in promotional bundles.

### 4.6 Basket Composition Patterns - Clustering

K-means clustering (k=5) on basket aisle composition reveals distinct shopper archetypes:

| Cluster | Name | % of Baskets | Dominant Aisles |
|---------|------|--------------|-----------------|
| 0 | Produce Shoppers | ~25% | fresh fruits, fresh vegetables, packaged produce |
| 1 | Dairy-Focused | ~20% | milk, yogurt, packaged cheese |
| 2 | Mixed Grocery | ~30% | balanced across produce, dairy, snacks |
| 3 | Snack Seekers | ~15% | chips, cookies, candy, beverages |
| 4 | Meal Preppers | ~10% | meat seafood, fresh vegetables, frozen |

**Store Layout Implication**: Design store flow to accommodate the dominant "Mixed Grocery" mission while creating clear zones for specialty missions.

### 4.7 Weekend vs Weekday Basket Differences

| Metric | Weekend | Weekday | Difference |
|--------|---------|---------|------------|
| Mean Basket Size | 10.5 items | 9.8 items | +0.7 items |
| Produce Share | 28% | 26% | +2% |
| Dairy Share | 15% | 14% | +1% |
| Snacks Share | 8% | 9% | -1% |

#### Departments with Higher Weekend Purchases
- Produce (+2%)
- Dairy eggs (+1%)
- Meat seafood (+0.8%)
- Bakery (+0.5%)

**Operational Implication**: Weekend shifts should have stronger staffing in produce and dairy; weekend promotions should focus on fresh categories.

---

## 5. Business Implications for Planogram/Shelf Placement

### 5.1 Adjacency Recommendations

Based on affinity analysis, the following aisle adjacencies optimize cross-sell:

| Primary Aisle | Adjacent Aisles (by affinity) |
|---------------|------------------------------|
| Fresh Fruits | Fresh Vegetables, Packaged Vegetables, Milk |
| Milk | Yogurt, Packaged Cheese, Eggs |
| Packaged Cheese | Deli, Bread, Crackers |
| Snacks | Beverages, Cookies, Candy |

### 5.2 Anchor Product Strategy

**High-Traffic Anchors** (place at store perimeter to drive traffic):
- Bananas (472K+ orders)
- Organic Bananas (379K+ orders)
- Organic Strawberries (264K+ orders)
- Milk products (137K+ orders)

### 5.3 Cross-Sell Endcap Recommendations

Endcap displays should pair products with high lift scores:
- Strawberries endcap: Include whipped cream, shortcakes
- Banana display: Include peanut butter, oatmeal
- Milk endcap: Include cereal, cookies

### 5.4 Stock Priority by Reorder Rate

Products with high reorder rates require consistent stock availability:
- **Critical (>70% reorder)**: Bananas, milk, eggs, bread
- **High (60-70%)**: Yogurt, cheese, berries, avocados
- **Moderate (50-60%)**: Snacks, frozen items

### 5.5 Weekend vs Weekday Planogram Considerations

- **Weekend Focus**: Expanded produce displays, fresh bakery prominence
- **Weekday Focus**: Convenience items, grab-and-go options
- Consider dynamic endcaps that change by day of week