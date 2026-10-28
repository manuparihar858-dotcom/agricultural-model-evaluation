# Week 5: Model Evaluation and Reporting Strategy

This project provides an assignment report and reusable reporting assets for evaluating a hypothetical agricultural yield prediction model.

## Contents
- `reports/Week5_Model_Evaluation_and_Reporting_Strategy.docx` — detailed editable report.
- `src/make_evaluation_charts.py` — script to recreate example charts from the illustrative metrics.
- `data/illustrative_model_metrics.csv` — explicitly hypothetical example metrics, not real model results.
- `figures/` — example charts included in the report.

## Important note
All numerical results and plots in this project are illustrative examples created to demonstrate reporting methods. They are not measured results from a real agricultural dataset and must not be presented as empirical findings.

## Recreate the metrics chart
Requires Python 3.10+ and the packages listed in `requirements.txt`.

```bash
pip install -r requirements.txt
python src/make_evaluation_charts.py
```

## Evaluation approach in brief
1. Define the forecast target, unit, forecast date, and business use.
2. Keep training, validation, and test sets separate; use time-aware splits for future-season forecasts.
3. Compare candidate models against a simple baseline.
4. Report MAE and RMSE in yield units and R² as a complementary fit statistic.
5. Inspect actual-versus-predicted and residual plots.
6. Report performance by crop, region, season, and forecast horizon.
7. Explain limitations, uncertainty, and next steps in plain language.
