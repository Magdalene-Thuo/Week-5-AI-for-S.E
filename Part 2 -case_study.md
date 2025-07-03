# 🏥 Case Study: Predicting Patient Readmission Risk

---

## 1. Problem Scope

**Problem**: Predict if a patient will be readmitted within 30 days of discharge.

**Objectives**:
- Lower readmission rates
- Prioritize patients for follow-up

**Stakeholders**:
- Medical staff
- Hospital administrators

---

## 2. Data Strategy

**Data Sources**:
- EHRs
- Demographics
- Medication & vitals

**Ethical Concerns**:
1. Privacy breaches
2. Unintended bias toward minority patients

**Preprocessing Pipeline**:
- Drop PII
- Impute missing vitals
- Feature engineering: diagnosis codes, readmission flags, med counts

---

## 3. Model Development

**Model**: XGBoost  
**Why**: Performs well on tabular data, interpretable via SHAP.

**Confusion Matrix** (hypothetical):

|              | Predicted Yes | Predicted No |
|--------------|----------------|---------------|
| Actual Yes   | 18             | 7             |
| Actual No    | 5              | 70            |

**Precision** = 18 / (18 + 5) = 0.78  
**Recall** = 18 / (18 + 7) = 0.72

---

## 4. Deployment

**Integration**:
- API deployment
- EHR dashboard scoring
- Staff training

**Compliance**:
- Data encryption
- Access logs
- HIPAA checklist

---

## 5. Optimization

**Overfitting Fix**: Use early stopping or L2 regularization in XGBoost.
