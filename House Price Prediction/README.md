# Task 6: House Price Prediction
### DevelopersHub Corporation — AI/ML Engineering Internship



>  Task Objective
Predict house sale prices using property features such as living area size, number of bedrooms, overall quality, garage capacity, and year built. We compare two regression models. Linear Regression and Gradient Boosting  and evaluate them using MAE and RMSE.



>  Dataset
| Property | Details |
|----------|---------|
| Name | House Prices — Advanced Regression Techniques |
| Source | [Kaggle](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data) |
| File Used | `train.csv` |
| Size | 1460 rows × 81 columns |
| Target Column | `SalePrice` |
| Price Range | $34,900 — $755,000 |



>  Libraries Used
| Library | Purpose |
|---------|---------|
| `pandas` | Data loading and manipulation |
| `numpy` | Numerical computations |
| `matplotlib` | Plotting and visualization |
| `seaborn` | Statistical visualizations |
| `scikit-learn` | Preprocessing, model training, evaluation |



>>  Models Applied

> 1. Linear Regression (Baseline)
- Simple, fast, and highly interpretable
- Uses 9 engineered features scaled with StandardScaler
- Good for understanding linear relationships

> 2. Gradient Boosting Regressor (Advanced)
- Ensemble of 200 decision trees
- Captures non-linear feature relationships
- Generally more accurate than Linear Regression



>>  Key Results & Findings

| Metric | Linear Regression | Gradient Boosting |
|--------|:-----------------:|:-----------------:|
| MAE | ~$22,000 | ~$16,000 |
| RMSE | ~$35,000 | ~$24,000 |
| R² Score | ~0.82 | ~0.91 |

>> Top Features by Importance:
1. `OverallQual` — Overall material & finish quality (strongest predictor)
2. `GrLivArea` — Above-ground living area (sq ft)
3. `YearBuilt` — Year of original construction
4. `GarageCars` — Garage car capacity
5. `TotalBsmtSF` — Total basement area (sq ft)

>> EDA Insights:
- Sale prices are right-skewed; log transformation improves model fit
- Quality rating has the clearest linear relationship with price
- Newer houses and larger living areas consistently command higher prices



>>  Project Structure

Task6_House_Price_Prediction/
│
├── Task6_House_Price_Prediction.ipynb    ← Main notebook
├── train.csv                             ← Dataset (download from Kaggle)
├── README.md                             ← This file
├── plot1_price_distribution.png
├── plot2_feature_relationships.png
├── plot3_price_by_quality_bedrooms.png
├── plot4_correlation_heatmap.png
├── plot5_actual_vs_predicted.png
├── plot6_residuals_analysis.png
├── plot7_model_comparison.png
└── plot8_feature_importance.png




>>  How to Run

>1. Download the dataset
- Go to: https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data
- Download and extract the zip file
- Place `train.csv` in the same folder as the notebook

> 2. Install dependencies
   bash
pip install pandas numpy matplotlib seaborn scikit-learn ipykernel


> 3. Open in VS Code
- Open the folder in VS Code
- Click `Task6_House_Price_Prediction.ipynb`
- Select Python kernel (top right)
- Press `Ctrl+Shift+P` → Run All

All 8 plots will generate and save automatically.



>>  Submission Checklist
- [1] Clear problem statement and goal
- [2] Dataset loading and preprocessing (missing value handling, feature selection)
- [3] Statistical summary and EDA
- [4] Data visualization (8 professional plots)
- [5] Feature scaling with StandardScaler
- [6] Two models trained: Linear Regression + Gradient Boosting
- [7] Evaluation with MAE and RMSE
- [8] Actual vs Predicted price visualization
- [9] Residuals analysis
- [10] Feature importance analysis
- [11] Final insights and conclusion
- [12] Clean, modular, fully commented code



*DevelopersHub Corporation — AI/ML Engineering Internship | Due: 26th June 2026*
## *Author by:* 
## *Muhammad Abdullah*
## *(DHC-8675)*

