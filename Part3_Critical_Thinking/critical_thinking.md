# ⚖️ Part 3: Critical Thinking

---

## Ethics & Bias

**Impact of Bias**:  
If historical care has been unequal, the model may underpredict risk in underserved populations, worsening outcomes.

**Mitigation Strategy**:
- Rebalance training samples by gender, race, and income level.
- Use fairness constraints in model objectives.

---

## Interpretability vs Accuracy

**Trade-off**:
- High accuracy (neural nets) = less transparency
- High interpretability (logistic regression) = less predictive power

**Resource Constraints**:
If compute is limited, prefer:
- Logistic regression
- Decision trees with capped depth
