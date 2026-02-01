## Grocery Chain Sales EDA – Questions, Answers, and Project Relevance

This EDA is for `grocery_chain_data.csv` (~1,980 rows) from a 9‑store grocery chain (11 aisles, 18 products) spanning 2023–2025. It is designed to:

- Understand **store & aisle performance**
- Diagnose **data quality issues** (missing values, negative amounts, string quantities)
- Extract features and insights that can support:
  - Store comparison and benchmarking
  - Promotion and discount optimization
  - Inventory & product mix decisions
  - Customer value and loyalty analysis

---

### Question 1: What is the basic structure, data quality, and missingness profile of the grocery dataset?

**Detailed answer (what to do)**  
- Inspect dataset shape, column types, and date ranges (`transaction_date`).  
- Check for missing values in core fields (`store_name`, `aisle`, `product_name`, `quantity`, `unit_price`, `total_amount`, `discount_amount`, `final_amount`, `loyalty_points`).  
- Look for obvious inconsistencies:  
  - `quantity` stored as string with mixed formats (`"2"` vs `"2.0"`).  
  - Negative `final_amount` due to large discounts.  
  - Cases where `total_amount ≠ quantity × unit_price` (after converting quantity).  

**Why this is important for our project**  
- We need **clean, trustworthy inputs** before building any store/aisle performance models or promotion analytics.  
- The small but realistic size makes this dataset a good sandbox to design **data cleaning pipelines** that can later be scaled to larger POS data (like your Nielsen and retail datasets).  

**What we get from this analysis**  
- A clear list of **data quality issues** to fix (type casting, negative values, missing store/aisle info).  
- A validated schema that underpins all subsequent analysis and model features.  

---

### Question 2: How do overall sales trends evolve over time (2023–2025)?

**Detailed answer (what to do)**  
- Parse `transaction_date` as a date and derive `year`, `month`, `year_month`.  
- Aggregate `final_amount` (and optionally `total_amount`) per month and per year.  
- Plot monthly total sales and average transaction value over time.  

**Why this is important for our project**  
- Time trends reveal **growth or decline** in the chain’s performance and can highlight seasonality or structural shifts (e.g., after a new promotion strategy or store opening).  
- For decision platforms and scenario simulators, knowing the **baseline trajectory** helps evaluate whether AI‑driven changes are actually improving results.  

**What we get from this analysis**  
- A **sales time series** (by month) for the chain and each store.  
- A baseline to compare future or simulated performance (e.g., after implementing optimized planograms or promotions).  

---

### Question 3: Which stores perform best in terms of revenue, discount usage, and loyalty points?
  at achieve good sales with fewer promotions.  
- Store‑level features (e.g., average discount rate, average loyalty points per transaction) that can be used in benchmarking or clustering.  

---

### Question 4: How do aisles (product categories) contribute to revenue and margin?

**Detailed answer (what to do)**  
- Group by `aisle` to compute:  
  - Total `final_amount` and average transaction value per aisle.  
  - Share of chain revenue per aisle (category mix).  
  - Average discount rate per aisle (how promotional each category is).  
- Plot top aisles by total revenue and by discount rate.  

**Why this is important for our project**  
- Aisles are the **natural units** for planogram optimization and assortment planning (e.g., Produce, Dairy, Snacks & Candy).  
- Knowing which aisles are high revenue vs highly promotional vs low‑performing helps prioritize **which categories deserve prime space and attention**.  

**What we get from this analysis**  
- A ranked list of aisles by contribution to chain revenue.  
- Indicators of which aisles are **margin‑sensitive** (large discounts) vs relatively full‑price.  
- Inputs for category‑level performance scores that can link back to your broader AI planogram engine.  

---

### Question 5: Which products drive sales, and how do price and quantity patterns look?

**Detailed answer (what to do)**  
- Group by `product_name` (and optionally by `aisle`) to compute:  
  - Total `final_amount`, total `quantity`, and average `unit_price`.  
  - Number of transactions per product.  
- Plot top products by revenue and by units sold.  
- Examine distribution of `unit_price` by aisle and product to see positioning (value vs premium).  

**Why this is important for our project**  
- This identifies **hero SKUs** versus long‑tail items. Hero SKUs are candidates for eye‑level placement, cross‑promotions, and availability guarantees.  
- Understanding unit price and quantity distributions supports **pricing strategy** and **pack-size decisions**.  

**What we get from this analysis**  
- A ranked list of products by revenue and volume.  
- Clarity on which SKUs are **key drivers** of each aisle’s performance.  
- Product‑level features that can feed into SKU scoring and facings optimization.  

---

### Question 6: How do discounts impact transaction value and store/aisle performance?

**Detailed answer (what to do)**  
- Compute `discount_rate = discount_amount / total_amount` (handling division by zero and missing values).  
- Analyze distribution of `discount_rate` (histogram, summary stats).  
- Compare `final_amount` and `quantity` between:  
  - Transactions with no discount vs with discount  
  - High vs low discount tiers (e.g., 0–10%, 10–30%, 30%+).  
- Check which stores/aisles rely most on high discounts.  

**Why this is important for our project**  
- Discounts are a double‑edged sword: they can increase volume but erode margin. Your decision platform should know **where promotions actually create profitable uplift** and where they just give away value.  
- Helps calibrate **promotion rules** and constraints in any optimization engine (e.g., don’t combine deep discounts with already low‑margin categories).  

**What we get from this analysis**  
- A quantitative view of **discount penetration** and its effect on basket value.  
- Store/aisle level discount profiles that can be used in modeling and governance.  

---

### Question 7: Are there any anomalous or suspicious transactions (e.g., negative final_amount)?

**Detailed answer (what to do)**  
- Identify transactions with:  
  - `final_amount < 0`  
  - Extremely high `discount_amount` relative to `total_amount`  
  - `quantity` values outside the expected 1–5 range after type conversion.  
- Inspect these rows to determine if they represent:  
  - Refunds or returns  
  - Data entry errors  
  - Edge cases of promotions (e.g., free items).  

**Why this is important for our project**  
- Outliers can **distort averages and model training**, especially in a small dataset.  
- If negative `final_amount` rows are actually returns, we might treat them differently or separate them into a **returns dataset**.  

**What we get from this analysis**  
- A clear set of **outlier rules** (e.g., flag or exclude `final_amount < 0` unless modeling returns explicitly).  
- Cleaner input data for sales and margin analysis, and better trust in model outputs.  

---

### Question 8: How does customer behavior vary across stores and aisles (basic segmentation)?

**Detailed answer (what to do)**  
- For each `customer_id`, compute:  
  - Number of transactions, total `final_amount`, total `quantity`.  
  - Number of distinct stores visited and distinct aisles purchased from.  
- Analyze whether some customers are:  
  - **Store‑loyal** vs **store‑hoppers**  
  - Focused on specific aisles (e.g., mostly Produce) vs diverse shoppers.  

**Why this is important for our project**  
- Even in this small dataset, you can see patterns that map to **customer personas** (e.g., top‑up shoppers vs weekly basket shoppers).  
- These personas are the foundation for **targeted merchandising** and **promotion scenarios** in your broader platform.  

**What we get from this analysis**  
- Preliminary customer‑level features that later can be aligned with the much larger retail/customer datasets.  
- Insights on cross‑store and cross‑category behavior that inform assortment and layout decisions.  

---

### Question 9: What temporal patterns exist (by day, month, and season)?

**Detailed answer (what to do)**  
- Extract `day_of_week`, `month`, and approximate `season` from `transaction_date`.  
- Aggregate `final_amount` and `quantity` by these temporal keys:  
  - Sales by day of week (e.g., weekends vs weekdays)  
  - Sales by month (seasonality)  
- Visualize with line plots or bar charts.  

**Why this is important for our project**  
- Temporal patterns influence staffing, inventory, and **placement of impulse categories** (e.g., snacks near checkout on weekends).  
- They also help in building **short‑term demand forecasts** and calibrating simulation scenarios (“what if we move a key product to an end‑cap before weekends?”).  

**What we get from this analysis**  
- Simple but actionable temporal multipliers (e.g., weekend uplift factor).  
- Evidence for including time‑based features in any forecasting or promotion‑planning models.  

---

### Question 10: How do loyalty points relate to spending, discounts, and store/aisle preferences?

**Detailed answer (what to do)**  
- Analyze the distribution of `loyalty_points`.  
- Correlate `loyalty_points` with `final_amount`, `discount_amount`, and `quantity`.  
- Check differences in average loyalty points per transaction across stores and aisles.  

**Why this is important for our project**  
- Loyalty points reflect how the chain **rewards behavior** and can be a proxy for **customer value** or **promotion intensity**.  
- Linking points to aisles and products shows where loyalty mechanics are being used most (e.g., extra points on Health & Wellness).  

**What we get from this analysis**  
- Understanding whether loyalty points are **aligned with profitable behavior** or just being given away.  
- Features that could feed into future **customer‑level models** when combined with longer‑horizon data.  

---

### Question 11: How do stores compare on key KPIs (basket size, AOV, discount rate, loyalty points)?

**Detailed answer (what to do)**  
- For each `store_name`, compute:  
  - Average basket value (`final_amount` per transaction)  
  - Average items per basket (`quantity`)  
  - Average discount rate  
  - Average loyalty points per transaction  
- Present these KPIs in a comparison table and radar/bar charts.  

**Why this is important for our project**  
- This is a **mini performance dashboard** across the 9 stores. It is directly analogous to what your merchandiser dashboard would show at scale.  
- It surfaces which stores are over‑discounting, underperforming, or could learn from best‑in‑class peers.  

**What we get from this analysis**  
- A store comparison framework that you can later generalize to larger datasets and more KPIs.  
- Concrete KPIs to drive **store‑level experiments** and measure the impact of optimization recommendations.  

---

## How This EDA Supports Our Project Goals

- **Data Cleaning & Quality Playbook**: This small but realistic dataset is ideal to design and test cleaning rules (e.g., type conversion, handling negatives) before applying them to larger POS datasets.  
- **Store & Aisle Intelligence**: Store and aisle performance insights here mirror the needs of your Nielsen/retail projects, making it a good prototype for **planogram and merchandising KPIs**.  
- **Promotion & Loyalty Insights**: Discount and loyalty analysis supports promotion optimization and customer value strategies, concepts that transfer directly to your bigger datasets.  
- **Explainable KPIs**: The metrics and comparisons derived here can be reused as **explainable outputs** in dashboards and AI recommendation explanations.

You can use this document as the “questions + answers + why it matters” guide, and back it with a Python EDA script (see `eda_grocery_chain.py`) that generates figures and tables for each question.

