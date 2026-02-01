## Retail Sales & Customer Behavior EDA – Questions, Answers, and Project Relevance

This EDA is for `retail_data.csv` (≈1M rows, 100+ columns) and is designed to support two main predictive goals:

- **Regression**: predict `total_sales` (customer-level revenue)
- **Classification**: predict `churned` (Yes/No)

All questions below are framed to (1) extract business insight and (2) feed useful features into models that support your broader project (AI planogram, merchandising co‑pilot, loyalty optimization, etc.).

---

### Question 1: What is the overall structure, data quality, and missingness profile of the dataset?

**Detailed answer (what to do)**  
- Inspect column dtypes (`customer_id`, `transaction_id`, dates, numeric vs categorical).  
- Compute missing value counts and percentages per column.  
- Check basic statistics for key numeric fields (`total_sales`, `total_transactions`, `avg_purchase_value`, `purchase_frequency`, etc.).  
- Validate obvious relationships (e.g., `total_sales ≥ 0`, `quantity ≥ 0`, `membership_years ≥ 0`).  

**Why this is important for our project**  
- You need to know **which features are trustworthy** and which need cleaning or imputation before feeding them into sales/churn models.  
- Some high‑leakage or redundant features (e.g., `customer_lifetime_value` or `churn_risk_score`) may already encode target information; you must decide whether to use them, regularize them, or hold them out depending on your modeling strategy.  

**What we get from this analysis**  
- A **data dictionary with health flags** (OK / needs cleaning / high missingness).  
- A shortlist of **candidate features** for modeling and a list of columns to drop or treat carefully.  
- Early detection of schema issues before you build any downstream pipelines.

---

### Question 2: What do our customers look like demographically, and how does that relate to sales and churn?

**Detailed answer (what to do)**  
- Profile distributions of `age`, `gender`, `income_bracket`, `marital_status`, `number_of_children`, `education_level`, `occupation`.  
- For each demographic group, compute:  
  - Average and median `total_sales`  
  - Churn rate (% of `churned = Yes`)  
- Visualize (bar plots/box plots) `total_sales` and churn rate across income brackets, age bands, and other key demographics.

**Why this is important for our project**  
- Demographics influence both **basket size** and **propensity to churn**.  
- For an AI planogram/merchandising engine, understanding which segments over‑index on which categories/brands allows better localized assortment and promotion targeting.  

**What we get from this analysis**  
- A clear view of **high‑value segments** (e.g., high‑income, mid‑age, loyalty members) and **at‑risk segments** for churn.  
- Features like age band, income segment, and household composition that can be used in both **sales uplift** and **churn prevention** models.  

---

### Question 3: How does loyalty program participation and tenure relate to sales and churn?

**Detailed answer (what to do)**  
- Compare `total_sales`, `purchase_frequency`, and `churned` between `loyalty_program = Yes` vs `No`.  
- Analyze `membership_years` vs `total_sales` and churn rate (e.g., buckets: <1, 1–3, 3–5, 5+ years).  
- Check how derived fields like `loyalty_score` correlate with `total_sales` and `churned`.  

**Why this is important for our project**  
- Loyalty status is central to **customer lifetime value** and **retention strategy**.  
- For your merchandiser dashboard, knowing which loyalty tiers are most profitable (and at what churn risk) informs where to allocate promotions, new products, and shelf visibility.  

**What we get from this analysis**  
- Evidence of **loyalty ROI** (do loyalty members buy more and churn less?).  
- Potential **cut‑offs** for defining VIP customers for special treatment and targeted recommendations.  
- A validated `loyalty_score` feature that can directly feed both regression and classification models.

---

### Question 4: What are the key RFM (Recency, Frequency, Monetary) patterns and how do they link to churn and sales?

**Detailed answer (what to do)**  
- Use `last_purchase_date`, `days_since_last_purchase`, `purchase_frequency`, `total_transactions`, and `total_sales` to construct RFM‑style scores.  
- Examine how churn probability (`churned`) varies by:  
  - `days_since_last_purchase`  
  - `purchase_frequency` (e.g., Daily/Weekly/Monthly/Yearly or numeric equivalent)  
  - `total_sales` buckets.  
- Visualize as heatmaps or grouped bar charts (e.g., high/medium/low frequency vs high/medium/low monetary).  

**Why this is important for our project**  
- RFM is the **foundation of churn modeling** and CLV estimation.  
- Your decision engine (recommendations, promotions, planogram changes) will benefit from understanding **who is at risk**, **who is growing**, and **who is stable**.  

**What we get from this analysis**  
- Intuitive and powerful **RFM‑based features** for churn and sales models.  
- A clear picture of which RFM segments to target with proactive interventions (e.g., upsell, win‑back campaigns).  

---

### Question 5: How do online vs in‑store behavior and channel preferences affect sales and churn?

**Detailed answer (what to do)**  
- Compute online vs offline mix:  
  - `online_purchases`, `in_store_purchases`, and their ratios.  
  - `preferred_store` and its relation to `store_location`.  
- Analyze `total_sales` and churn by dominant channel (online‑heavy vs store‑heavy vs balanced).  
- Check if online‑dominant customers respond differently to promotions or have different `avg_transaction_value`.  

**Why this is important for our project**  
- Channel preference affects **how** we should reach and retain customers (e.g., app vs in‑store promotions).  
- For planogram and store layout optimization, understanding in‑store‑dominant customers helps fine‑tune physical merchandising; online‑heavy customers may be more impacted by recommendation algorithms and digital shelf.  

**What we get from this analysis**  
- Segmentation into **channel personas** (store‑centric, omni‑channel, online‑centric).  
- Features representing channel mix to enhance both **total_sales predictions** and **churn models**.  

---

### Question 6: Which product categories, brands, and products drive revenue and returns?

**Detailed answer (what to do)**  
- Aggregate by `product_category`, `product_brand`, and `product_id` to compute:  
  - `total_sales`, `total_items_purchased`, `product_return_rate`, `product_review_count`, `avg(product_rating)`.  
- Rank categories and brands by revenue contribution and return rate.  
- Identify SKUs with **high sales + high returns** vs **high sales + low returns**.  

**Why this is important for our project**  
- High‑sales, low‑return products are **ideal candidates** for premium shelf space and recommendations.  
- High‑returns products may indicate quality or expectation mismatches and should be treated cautiously in both assortment and promotion planning.  

**What we get from this analysis**  
- A list of **hero categories/brands/SKUs** and **problematic ones**.  
- Strong input for a **SKU performance scoring engine** (important for planogram optimization and inventory decisions).  

---

### Question 7: How do promotions (type, channel, timing) affect customer behavior and sales uplift?

**Detailed answer (what to do)**  
- Link `promotion_id` and `promotion_type/channel` to transactions and customers.  
- For each promotion, compute:  
  - Change in sales vs a pre‑promotion baseline (per customer, per category).  
  - Customer acquisition vs retention effects (did it attract new vs existing customers?).  
- Compare promotion effectiveness across `promotion_channel` (Online, In‑store, Social Media).  

**Why this is important for our project**  
- Promotions directly affect **short‑term sales** and **long‑term behavior** (e.g., deal‑seekers vs loyal buyers).  
- Your decision platform needs to know **which promotion levers actually work** and avoid over‑discounting where it doesn’t move the needle.  

**What we get from this analysis**  
- An empirical view of **promotion ROI** by type and channel.  
- Features such as customer sensitivity to promotions (`avg_discount_used`, response to past promos) for improved churn and sales prediction.  

---

### Question 8: How does geography (distance to store, city, state) influence sales and churn?

**Detailed answer (what to do)**  
- Analyze `total_sales`, `total_transactions`, `churned` by `customer_city`, `customer_state`, and by binned `distance_to_store`.  
- Compare store‑side geography (`store_city`, `store_state`) to customer geography to see which stores are drawing from a wide vs local catchment area.  
- Visualize sales and churn across distance buckets (e.g., 0–2km, 2–5km, 5–10km, 10km+).  

**Why this is important for our project**  
- Distance and locality shape **visit frequency**, **channel usage**, and how strongly a physical planogram change can influence behavior.  
- For localized assortment or pricing strategies, you need to know which regions or store catchments behave differently.  

**What we get from this analysis**  
- Geographic features (region, distance band) that can feed models and inform **store clustering**.  
- Evidence for **localized intelligence** in your platform (e.g., different recommendations in urban vs suburban areas).  

---

### Question 9: What seasonal, holiday, and weekend patterns do we see in sales and churn?

**Detailed answer (what to do)**  
- Use `transaction_date`, `season`, `holiday_season`, and `weekend` to analyze:  
  - Sales uplift during holidays vs non‑holidays.  
  - Differences in `avg_transaction_value` and basket size on weekends vs weekdays.  
  - Seasonal trends in churn (e.g., churn spikes after holidays/promotions).  

**Why this is important for our project**  
- Seasonality and holiday effects are crucial for **short‑term forecasting**, **stocking decisions**, and **planogram changes** (e.g., seasonal end‑caps).  
- Churn risk might increase after high‑promotion periods if regular prices feel too high, so understanding this dynamic helps plan proactive engagement.  

**What we get from this analysis**  
- Temporal features (season, holiday flag, weekend flag) for models.  
- Concrete multipliers for **promotion planning** (e.g., expected uplift during Diwali/Christmas vs regular weeks).  

---

### Question 10: How do customer interaction and engagement metrics relate to churn and value?

**Detailed answer (what to do)**  
- Examine distributions and correlations for `customer_support_calls`, `email_subscriptions`, `app_usage`, `website_visits`, `social_media_engagement`.  
- For each variable, compare:  
  - Churn rate by engagement level (e.g., high app usage vs low).  
  - `total_sales` by engagement level.  
- Check whether more support calls correlate with dissatisfaction and churn or with high‑value, high‑contact customers.  

**Why this is important for our project**  
- Engagement metrics are **actionable levers**: you can nudge email‑subscribed app users differently than low‑engagement customers.  
- For a co‑pilot dashboard, showing “high‑value, low‑engagement customers at risk” is extremely valuable to merchandisers and CRM teams.  

**What we get from this analysis**  
- Features capturing **engagement intensity** and **service friction** (e.g., many support calls).  
- Insight into which engagement channels actually correlate with retention vs those that just add noise.  

---

### Question 11: Are the derived scores (CLV, loyalty_score, churn_risk_score) consistent and predictive?

**Detailed answer (what to do)**  
- Validate distributions of `customer_lifetime_value`, `loyalty_score`, `churn_risk_score`.  
- Check monotonicity:  
  - Does higher `customer_lifetime_value` correspond to higher `total_sales`?  
  - Does higher `churn_risk_score` correspond to higher observed churn rate?  
- Correlate these scores with key raw features (RFM metrics, loyalty, engagement).  

**Why this is important for our project**  
- These scores are likely **pre‑engineered features** or outputs of legacy models.  
- You need to decide whether to *trust* them as strong features, use them as targets for calibration, or treat them cautiously to avoid leakage or double‑counting effects.  

**What we get from this analysis**  
- A clear sense of how **reliable** the existing scores are.  
- A decision on whether they become first‑class features in the new models or purely diagnostic KPIs.  

---

### Question 12: Can we segment customers into meaningful personas that link back to merchandising and planogram decisions?

**Detailed answer (what to do)**  
- Use a subset of clean features (demographics, RFM, channel mix, engagement) to run clustering (e.g., k‑means) or simpler rule‑based segmentation.  
- Characterize each segment by:  
  - Typical basket (categories/brands).  
  - Channel preference (online vs in‑store).  
  - Loyalty and churn risk.  
- Map segments to **assortment and layout strategies** (e.g., family shoppers, bargain hunters, premium convenience shoppers).  

**Why this is important for our project**  
- Your AI planogram and recommendation system need **clear customer archetypes** to optimize shelf space, promotions, and product adjacency for the dominant personas of each store.  
- Segments also inform **scenario builders** (“what if we push more healthy products to high‑income health‑conscious segments?”).  

**What we get from this analysis**  
- A set of **customer personas** that can be used throughout the product (dashboards, simulations, store‑level strategy).  
- Segment labels that augment raw features in downstream models and make outputs **more explainable** to business users.

---

## How This EDA Supports Our Project Goals

- **Better Imputation & Prediction**: Clean features, RFM metrics, engagement data, and validated scores improve `total_sales` and `churned` models.  
- **Explainable Recommendations**: Each question yields interpretable patterns (e.g., “high‑income loyalty members with weekly purchases rarely churn”), which you can surface as explanations alongside recommendations.  
- **Planogram & Merchandising Intelligence**: Category/brand performance, promotion effectiveness, channel and geo behavior directly feed into **SKU scoring**, **facings optimization**, and **scenario simulation** modules.  
- **Localized & Persona‑Driven Decisions**: Geo and segmentation insights help tailor strategies to each store’s catchment area and dominant customer personas.

You can now implement this EDA in a notebook or script (similar to `eda_store_transaction.py`) and log the outputs/figures per question, using this file as the master “questions & answers + why it matters” document.

