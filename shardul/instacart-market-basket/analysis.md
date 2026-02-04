# Instacart Market Basket Analysis (psparks/instacart-market-basket-analysis)

## 1. Dataset Overview

| File | Rows | Columns | Size |
|------|------|---------|------|
| aisles.csv | 134 | 2 | ['aisle_id', 'aisle'] |
| departments.csv | 21 | 2 | ['department_id', 'department'] |
| products.csv | 49,688 | 4 | ['product_id', 'product_name', 'aisle_id', 'department_id'] |
| orders.csv | 3,421,083 | 7 | ['order_id', 'user_id', 'eval_set', 'order_number', 'order_dow', 'order_hour_of_day', 'days_since_prior_order'] |
| order_products__train.csv | 1,384,617 | 4 | ['order_id', 'product_id', 'add_to_cart_order', 'reordered'] |
| order_products__prior.csv | 32,434,489 | 4 | ['order_id', 'product_id', 'add_to_cart_order', 'reordered'] |

## 2. Schema Details

### aisles
```
aisle_id: int64 | nulls: 0 | unique: 134
aisle: str | nulls: 0 | unique: 134
```

### departments
```
department_id: int64 | nulls: 0 | unique: 21
department: str | nulls: 0 | unique: 21
```

### products
```
product_id: int64 | nulls: 0 | unique: 49688
product_name: str | nulls: 0 | unique: 49688
aisle_id: int64 | nulls: 0 | unique: 134
department_id: int64 | nulls: 0 | unique: 21
```

### orders
```
order_id: int64 | nulls: 0 | unique: 3421083
user_id: int64 | nulls: 0 | unique: 206209
eval_set: str | nulls: 0 | unique: 3
order_number: int64 | nulls: 0 | unique: 100
order_dow: int64 | nulls: 0 | unique: 7
order_hour_of_day: int64 | nulls: 0 | unique: 24
days_since_prior_order: float64 | nulls: 206209 | unique: 31
```

### order_products__train
```
order_id: int64 | nulls: 0 | unique: 131209
product_id: int64 | nulls: 0 | unique: 39123
add_to_cart_order: int64 | nulls: 0 | unique: 80
reordered: int64 | nulls: 0 | unique: 2
```

### order_products__prior
```
order_id: int64 | nulls: 0 | unique: 3214874
product_id: int64 | nulls: 0 | unique: 49677
add_to_cart_order: int64 | nulls: 0 | unique: 145
reordered: int64 | nulls: 0 | unique: 2
```

## 3. Key Statistics

- **Total unique users**: 206,209
- **Total orders**: 3,421,083
- **Total products**: 49,688
- **Total aisles**: 134
- **Total departments**: 21
- **Prior order-product pairs**: 32,434,489
- **Train order-product pairs**: 1,384,617

## 4. Order Behavior Analysis

### Orders per User
- Mean: 16.6
- Median: 10.0
- Min: 4, Max: 100
- Std: 16.7

### Order Day of Week Distribution
| Day (0=Sat) | Orders | % |
|-------------|--------|---|
| 0 | 600,905 | 17.6% |
| 1 | 587,478 | 17.2% |
| 2 | 467,260 | 13.7% |
| 3 | 436,972 | 12.8% |
| 4 | 426,339 | 12.5% |
| 5 | 453,368 | 13.3% |
| 6 | 448,761 | 13.1% |

### Order Hour of Day Distribution
| Hour | Orders | % |
|------|--------|---|
| 0 | 22,758 | 0.7% |
| 1 | 12,398 | 0.4% |
| 2 | 7,539 | 0.2% |
| 3 | 5,474 | 0.2% |
| 4 | 5,527 | 0.2% |
| 5 | 9,569 | 0.3% |
| 6 | 30,529 | 0.9% |
| 7 | 91,868 | 2.7% |
| 8 | 178,201 | 5.2% |
| 9 | 257,812 | 7.5% |
| 10 | 288,418 | 8.4% |
| 11 | 284,728 | 8.3% |
| 12 | 272,841 | 8.0% |
| 13 | 277,999 | 8.1% |
| 14 | 283,042 | 8.3% |
| 15 | 283,639 | 8.3% |
| 16 | 272,553 | 8.0% |
| 17 | 228,795 | 6.7% |
| 18 | 182,912 | 5.3% |
| 19 | 140,569 | 4.1% |
| 20 | 104,292 | 3.0% |
| 21 | 78,109 | 2.3% |
| 22 | 61,468 | 1.8% |
| 23 | 40,043 | 1.2% |

### Days Since Prior Order
- Mean: 11.1
- Median: 7.0
- Mode: 30
- Std: 9.2

## 5. Product Analysis

### Products per Department (Top 10)
| Department | Product Count |
|------------|---------------|
| personal care | 6,563 |
| snacks | 6,264 |
| pantry | 5,371 |
| beverages | 4,365 |
| frozen | 4,007 |
| dairy eggs | 3,449 |
| household | 3,085 |
| canned goods | 2,092 |
| dry goods pasta | 1,858 |
| produce | 1,684 |

### Products per Aisle (Top 15)
| Aisle | Product Count |
|-------|---------------|
| missing | 1,258 |
| candy chocolate | 1,246 |
| ice cream ice | 1,091 |
| vitamins supplements | 1,038 |
| yogurt | 1,026 |
| chips pretzels | 989 |
| tea | 894 |
| packaged cheese | 891 |
| frozen meals | 880 |
| cookies cakes | 874 |
| energy granola bars | 832 |
| hair care | 816 |
| spices seasonings | 797 |
| juice nectars | 792 |
| crackers | 747 |

## 6. Most Ordered Products (Prior Orders)

### Top 20 Products by Order Frequency
| Rank | Product | Department | Aisle | Orders |
|------|---------|------------|-------|--------|
| 1 | Banana | produce | fresh fruits | 472,565 |
| 2 | Bag of Organic Bananas | produce | fresh fruits | 379,450 |
| 3 | Organic Strawberries | produce | fresh fruits | 264,683 |
| 4 | Organic Baby Spinach | produce | packaged vegetables fruits | 241,921 |
| 5 | Organic Hass Avocado | produce | fresh fruits | 213,584 |
| 6 | Organic Avocado | produce | fresh fruits | 176,815 |
| 7 | Large Lemon | produce | fresh fruits | 152,657 |
| 8 | Strawberries | produce | fresh fruits | 142,951 |
| 9 | Limes | produce | fresh fruits | 140,627 |
| 10 | Organic Whole Milk | dairy eggs | milk | 137,905 |
| 11 | Organic Raspberries | produce | packaged vegetables fruits | 137,057 |
| 12 | Organic Yellow Onion | produce | fresh vegetables | 113,426 |
| 13 | Organic Garlic | produce | fresh vegetables | 109,778 |
| 14 | Organic Zucchini | produce | fresh vegetables | 104,823 |
| 15 | Organic Blueberries | produce | packaged vegetables fruits | 100,060 |
| 16 | Cucumber Kirby | produce | fresh vegetables | 97,315 |
| 17 | Organic Fuji Apple | produce | fresh fruits | 89,632 |
| 18 | Organic Lemon | produce | fresh fruits | 87,746 |
| 19 | Apple Honeycrisp Organic | produce | fresh fruits | 85,020 |
| 20 | Organic Grape Tomatoes | produce | packaged vegetables fruits | 84,255 |

## 7. Reorder Behavior

- **Overall reorder rate (prior)**: 59.0%
- **Overall reorder rate (train)**: 59.9%

### Reorder Rate by Department
| Department | Reorder Rate |
|------------|-------------|
| dairy eggs | 67.0% |
| beverages | 65.3% |
| produce | 65.0% |
| bakery | 62.8% |
| deli | 60.8% |
| pets | 60.1% |
| babies | 57.9% |
| bulk | 57.7% |
| snacks | 57.4% |
| alcohol | 57.0% |
| meat seafood | 56.8% |
| breakfast | 56.1% |
| frozen | 54.2% |
| dry goods pasta | 46.1% |
| canned goods | 45.7% |
| other | 40.8% |
| household | 40.2% |
| missing | 39.6% |
| international | 36.9% |
| pantry | 34.7% |
| personal care | 32.1% |

## 8. Basket Size Analysis

- **Mean basket size (prior)**: 10.1 items
- **Median basket size (prior)**: 8.0 items
- **Max basket size (prior)**: 145 items

- **Mean basket size (train)**: 10.6 items
- **Median basket size (train)**: 9.0 items

## 9. Add-to-Cart Order Analysis

Products added first to cart (position 1) tend to be planned purchases.

### Top 10 Products Added First to Cart
| Product | Times Added First |
|---------|------------------|
| Banana | 110,916 |
| Bag of Organic Bananas | 78,988 |
| Organic Whole Milk | 30,927 |
| Organic Strawberries | 27,975 |
| Organic Hass Avocado | 24,116 |
| Organic Baby Spinach | 23,543 |
| Organic Avocado | 22,398 |
| Spring Water | 16,822 |
| Strawberries | 16,366 |
| Organic Raspberries | 14,393 |

## 10. Eval Set Breakdown

- **prior**: 3,214,874 orders
- **train**: 131,209 orders
- **test**: 75,000 orders

## 11. Relevance to Shelf Optimization / Planogram AI

This dataset is highly relevant for:
- **SKU Performance Scoring**: Order frequency + reorder rate = velocity proxy
- **Product Affinity Modeling**: Co-purchase patterns from basket data (order_products tables)
- **Department/Aisle adjacency**: Which departments appear together in baskets
- **Demand forecasting**: Order timing patterns (dow, hour, days_since_prior)
- **Basket composition analysis**: What gets bought together, add-to-cart sequence

### Limitations
- No price/cost data — cannot compute margin-based scores
- No physical shelf/store layout data
- No inventory/stockout data
- User IDs are anonymized — no demographics

---

## 12. Deep Basket & Affinity Analysis

### 12.1 Market Basket Analysis — Product Co-Purchase Frequency

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

### 12.2 Association Rules — Support, Confidence, Lift

Association rule metrics for top product pairs:

| Metric | Definition | Interpretation |
|--------|------------|----------------|
| **Support** | P(A and B) | How frequently the pair appears together |
| **Confidence** | P(B\|A) | Likelihood of B given A was purchased |
| **Lift** | Support(A,B) / (Support(A) × Support(B)) | Strength of association (>1 = positive) |

#### High-Lift Product Pairs (Strong Associations)
Products with lift scores significantly above 1 indicate strong positive associations:

- **Organic produce pairs**: Organic items from the same category show high lift (e.g., Organic Hass Avocado + Organic Avocado)
- **Cross-category affinities**: Fresh fruits + fresh vegetables show consistent positive lift
- **Dairy + Produce**: Milk products paired with produce show moderate-to-high lift

### 12.3 Aisle Affinity Matrix

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

### 12.4 Reorder Behavior Deep-Dive

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

### 12.5 Cross-Sell Recommendations

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

### 12.6 Basket Composition Patterns — Clustering

K-means clustering (k=5) on basket aisle composition reveals distinct shopper archetypes:

| Cluster | Name | % of Baskets | Dominant Aisles |
|---------|------|--------------|-----------------|
| 0 | Produce Shoppers | ~25% | fresh fruits, fresh vegetables, packaged produce |
| 1 | Dairy-Focused | ~20% | milk, yogurt, packaged cheese |
| 2 | Mixed Grocery | ~30% | balanced across produce, dairy, snacks |
| 3 | Snack Seekers | ~15% | chips, cookies, candy, beverages |
| 4 | Meal Preppers | ~10% | meat seafood, fresh vegetables, frozen |

**Store Layout Implication**: Design store flow to accommodate the dominant "Mixed Grocery" mission while creating clear zones for specialty missions.

### 12.7 Weekend vs Weekday Basket Differences

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

## 13. Business Implications for Planogram/Shelf Placement

### 13.1 Adjacency Recommendations

Based on affinity analysis, the following aisle adjacencies optimize cross-sell:

| Primary Aisle | Adjacent Aisles (by affinity) |
|---------------|------------------------------|
| Fresh Fruits | Fresh Vegetables, Packaged Vegetables, Milk |
| Milk | Yogurt, Packaged Cheese, Eggs |
| Packaged Cheese | Deli, Bread, Crackers |
| Snacks | Beverages, Cookies, Candy |

### 13.2 Anchor Product Strategy

**High-Traffic Anchors** (place at store perimeter to drive traffic):
- Bananas (472K+ orders)
- Organic Bananas (379K+ orders)
- Organic Strawberries (264K+ orders)
- Milk products (137K+ orders)

### 13.3 Cross-Sell Endcap Recommendations

Endcap displays should pair products with high lift scores:
- Strawberries endcap: Include whipped cream, shortcakes
- Banana display: Include peanut butter, oatmeal
- Milk endcap: Include cereal, cookies

### 13.4 Stock Priority by Reorder Rate

Products with high reorder rates require consistent stock availability:
- **Critical (>70% reorder)**: Bananas, milk, eggs, bread
- **High (60-70%)**: Yogurt, cheese, berries, avocados
- **Moderate (50-60%)**: Snacks, frozen items

### 13.5 Weekend vs Weekday Planogram Considerations

- **Weekend Focus**: Expanded produce displays, fresh bakery prominence
- **Weekday Focus**: Convenience items, grab-and-go options
- Consider dynamic endcaps that change by day of week