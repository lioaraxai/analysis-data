# Quick Start Guide: EDA for Store Transaction Data

## What This EDA Does

This EDA analyzes store transaction data to understand:
- How incomplete the data is (stores share 2-28 days instead of full month)
- What patterns exist that can help impute missing data
- Which features are most useful for imputation models

## Quick Run

```bash
# Navigate to the directory
cd Store_Transaction_data

# Run the EDA script
python eda_store_transaction.py
```

## What You'll Get

### Console Output
- Dataset statistics
- Key findings for each question
- Correlation values
- Summary statistics

### Visualizations (in `figures/` folder)
- `q2_days_per_store_month.png` - Shows data completeness
- `q3_sales_distribution.png` - Sales across stores
- `q4_category_contribution.png` - Top categories
- `q5_days_sales_relationship.png` - **KEY**: Days vs Sales correlation
- `q6_daily_value_consistency.png` - Daily value patterns
- `q7_data_completeness.png` - Completeness heatmap
- `q8_company_contribution.png` - Market share
- `q9_transaction_relationship.png` - Transaction patterns
- `q10_temporal_patterns.png` - Day-of-week patterns
- `q11_validation_requirements.png` - What needs prediction

## Key Questions & Answers

| Question | Key Finding | Implication for Imputation |
|---------|------------|---------------------------|
| Q2: Days per store? | 2-28 days, varies | Need extrapolation |
| Q5: Days-Sales relationship? | Strong correlation | Extrapolation is feasible |
| Q6: Daily value consistency? | Moderate consistency | Can use as baseline |
| Q9: Transaction patterns? | Strong correlation | Useful feature |
| Q10: Temporal patterns? | Day-of-week patterns exist | Use temporal features |

## Top 3 Insights for Model Building

1. **Extrapolation Works**: Days and sales are strongly correlated → Use `(Value/Days) × 28`
2. **Store-Specific**: Stores differ significantly → Include store features
3. **Category Matters**: Categories have different patterns → Consider category-level imputation

## Next Steps After EDA

1. Build baseline: Average daily value × 28 days
2. Enhance with features: Store, category, temporal features
3. Test on validation set
4. Iterate and improve

## Files Structure

```
Store_Transaction_data/
├── eda_store_transaction.py    # Main EDA script
├── README_EDA.md               # Detailed documentation
├── EDA_SUMMARY.md              # Summary of findings
├── QUICK_START.md              # This file
├── figures/                    # Generated visualizations
└── [CSV data files]            # Original datasets
```

## Troubleshooting

**Issue**: Module not found errors
**Solution**: Install required packages:
```bash
pip install pandas numpy matplotlib seaborn
```

**Issue**: Figures not saving
**Solution**: Ensure `figures/` directory exists (script creates it automatically)

**Issue**: Memory errors with large datasets
**Solution**: The script uses sampling for large scatter plots to manage memory

## Questions?

Refer to:
- `README_EDA.md` for detailed question explanations
- `EDA_SUMMARY.md` for model-building recommendations
- Code comments in `eda_store_transaction.py` for implementation details
