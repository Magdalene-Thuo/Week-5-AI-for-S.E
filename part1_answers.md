# 🔹 Part 1: Short Answer Questions

---

## 1. Problem Definition

**Problem**: Predicting student dropout rates in online universities

**Objectives**:
1. Identify high-risk students early.
2. Reduce dropout rates through interventions.
3. Support academic advisors.

**Stakeholders**: 
- Students  
- University admin

**KPI**: Dropout rate reduction (%)

---

## 2. Data Collection & Preprocessing

**Data Sources**:
- LMS logs
- Student records

**Bias**: Socioeconomic background may cause unfair risk classification.

**Preprocessing**:
1. Handle missing values
2. Normalize data
3. One-hot encode categories

---

## 3. Model Development

**Model**: Random Forest  
**Why**: Easy to interpret, handles missing/categorical values.

**Split**: 70% train, 15% validate, 15% test

**Hyperparameters**:
- `n_estimators` (controls tree count)
- `max_depth` (controls overfitting)

---

## 4. Evaluation & Deployment

**Metrics**:
- Recall (to catch most at-risk)
- F1 Score (balances errors)

**Concept Drift**: Model becomes outdated as student behavior changes. Monitor via live validation and retraining.

**Challenge**: Scalability in real-time platforms.
