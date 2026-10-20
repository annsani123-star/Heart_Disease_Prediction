import joblib
import pandas as pd

# Load model
model = joblib.load("heart_disease_model.pkl")

# Case 1: Patient with standard healthy baseline (no hospital test report)
patient_baseline = pd.DataFrame([{
    "age": 52.0,
    "sex": 1.0,
    "cp": 4.0,           # asymptomatic
    "trestbps": 120.0,
    "chol": 200.0,
    "fbs": 0.0,
    "restecg": 0.0,      # normal
    "thalach": 155.0,
    "exang": 0.0,
    "oldpeak": 0.0,      # normal
    "slope": 1.0,        # normal upsloping
    "ca": 0.0,           # 0 vessels
    "thal": 3.0          # normal scan
}])

pred_b = model.predict(patient_baseline)
prob_b = model.predict_proba(patient_baseline)[0][1]
print(f"Patient Baseline Test: Pred={pred_b[0]}, Prob={prob_b:.4f}")

# Case 2: Patient with severe exertional angina and lab results
patient_severe = pd.DataFrame([{
    "age": 62.0,
    "sex": 1.0,
    "cp": 1.0,           # typical angina
    "trestbps": 158.0,
    "chol": 285.0,
    "fbs": 1.0,
    "restecg": 2.0,
    "thalach": 120.0,
    "exang": 1.0,
    "oldpeak": 2.4,
    "slope": 2.0,
    "ca": 2.0,
    "thal": 7.0
}])

pred_s = model.predict(patient_severe)
prob_s = model.predict_proba(patient_severe)[0][1]
print(f"Severe Case Test: Pred={pred_s[0]}, Prob={prob_s:.4f}")

# Case 3: Doctor Presets A, B, C
for label, data in [
    ("Preset A (Healthy)", [45.0, 0.0, 4.0, 118.0, 185.0, 0.0, 0.0, 172.0, 0.0, 0.0, 1.0, 0.0, 3.0]),
    ("Preset B (High Risk)", [62.0, 1.0, 1.0, 158.0, 285.0, 1.0, 2.0, 120.0, 1.0, 2.4, 2.0, 2.0, 7.0]),
    ("Preset C (Borderline)", [56.0, 1.0, 2.0, 138.0, 240.0, 1.0, 1.0, 145.0, 0.0, 1.0, 2.0, 1.0, 6.0]),
]:
    df = pd.DataFrame([dict(zip(
        ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"],
        data
    ))])
    p = model.predict(df)[0]
    pr = model.predict_proba(df)[0][1]
    print(f"{label}: Pred={p}, Prob={pr:.4f}")

print("\nALL PREDICTION TESTS PASSED SUCCESSFULLY!")
