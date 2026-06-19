# Task 3: Heart Disease Prediction
### DevelopersHub Corporation — AI/ML Engineering Internship



>  Task Objective
Build a machine learning model to predict whether a patient is at risk of heart disease based on clinical health data such as age, cholesterol level, chest pain type, and more.



> Dataset
- Name: Heart Disease UCI Dataset
- Source: [Kaggle](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset)
- File: `heart.csv`
- Size: 1025 rows × 14 columns
- Target Column: `target` (1 = Heart Disease, 0 = No Disease)



> Libraries Used
| Library | Purpose |
|---------|---------|
| `pandas` | Data loading and manipulation |
| `numpy` | Numerical computations |
| `matplotlib` | Data visualization |
| `seaborn` | Statistical plots |
| `scikit-learn` | Model training and evaluation |



> Model Applied
- Algorithm: Logistic Regression
- Preprocessing: StandardScaler (feature normalization)
- Split: 80% Training / 20% Testing (stratified)



> Key Results & Findings

| Metric | Value |
|--------|-------|
| Accuracy | ~83% |
| ROC-AUC Score | ~0.90 |

> Top Predictive Features:
1. `cp` (Chest Pain Type) — strongest predictor
2. `thal` (Thalassemia) — major clinical indicator
3. `ca` (Number of Major Vessels) — more vessels = higher risk
4. `oldpeak` (ST Depression) — higher = more risk
5. `thalach` (Max Heart Rate) — higher = lower risk



> Project Structure

Task3_Heart_Disease_Prediction/
│
├── Task3_Heart_Disease_Prediction.ipynb   ← Main notebook
├── heart.csv                              ← Dataset (download from Kaggle)
├── README.md                              ← This file
├── plot1_target_distribution.png
├── plot2_age_gender_analysis.png
├── plot3_feature_boxplots.png
├── plot4_correlation_heatmap.png
├── plot5_model_evaluation.png
└── plot6_feature_importance.png


> How to Run

1. Download `heart.csv` from [Kaggle](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset)
2. Place `heart.csv` in the same folder as the notebook
3. Open `Task3_Heart_Disease_Prediction.ipynb` in VS Code
4. Select Python kernel → Run All Cells (`Ctrl+Shift+P` → "Run All")

> Install dependencies:
   bash
pip install pandas numpy matplotlib seaborn scikit-learn ipykernel




> Submission Checklist
- [1] Clear problem statement and goal
- [2] Dataset loading and preprocessing
- [3] Missing value and duplicate handling
- [4] Data visualization and EDA (6 plots)
- [5] Model training (Logistic Regression)
- [6] Evaluation: Accuracy, ROC Curve, Confusion Matrix
- [7] Feature importance analysis
- [8] Final insights and conclusions
- [9] Clean, commented, modular code



*DevelopersHub Corporation — AI/ML Engineering Internship | Due: 26th June 2026*
## *Author by:* 
## *Muhammad Abdullah*
## *(DHC-8675)*

