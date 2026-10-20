import streamlit as st
import pandas as pd
import joblib

# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="HeartCare AI | Cardiovascular Risk Screening",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CUSTOM PROFESSIONAL LIGHT-WHITE & MATTE-BLACK DESIGN SYSTEM
# Clean medical-grade white background (#FFFFFF / #F8FAFC),
# professional high-contrast matte-black action buttons (#0F172A / #000000),
# refined slate typography, subtle borders, and modern shadows.
# =========================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

/* App Canvas - Pure White & Subtle Slate */
.stApp {
    background-color: #F8FAFC;
    color: #0F172A;
}

.block-container {
    max-width: 1180px;
    padding-top: 1.5rem;
    padding-bottom: 4rem;
}

/* Header bar blur */
header[data-testid="stHeader"] {
    background: rgba(248, 250, 252, 0.85);
    backdrop-filter: blur(12px);
    border-bottom: 1px solid #E2E8F0;
}

/* Sidebar styling */
section[data-testid="stSidebar"] {
    background-color: #FFFFFF !important;
    border-right: 1px solid #E2E8F0 !important;
}

section[data-testid="stSidebar"] .stRadio label {
    color: #0F172A !important;
    font-weight: 500;
}

/* Hero Header */
.hero-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 20px;
    padding: 34px 38px;
    margin-bottom: 28px;
    position: relative;
    overflow: hidden;
    box-shadow: 0 4px 20px -2px rgba(15, 23, 42, 0.05), 0 2px 6px -1px rgba(15, 23, 42, 0.03);
}

.hero-pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: #0F172A;
    color: #FFFFFF;
    padding: 6px 14px;
    border-radius: 9999px;
    font-size: 12.5px;
    font-weight: 700;
    letter-spacing: 0.6px;
    text-transform: uppercase;
    margin-bottom: 14px;
}

.hero-pulse {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background-color: #E11D48;
    box-shadow: 0 0 8px rgba(225, 29, 72, 0.6);
    animation: pulse-ring 2s infinite;
}

@keyframes pulse-ring {
    0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(225, 29, 72, 0.7); }
    70% { transform: scale(1.1); box-shadow: 0 0 0 8px rgba(225, 29, 72, 0); }
    100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(225, 29, 72, 0); }
}

.hero-card h1 {
    color: #0F172A;
    font-size: 34px;
    font-weight: 800;
    margin: 4px 0 10px 0;
    letter-spacing: -0.5px;
}

.hero-card p {
    color: #475569;
    font-size: 16px;
    line-height: 1.55;
    margin: 0;
    max-width: 680px;
}

/* Feature & Section Containers */
.section-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 18px;
    padding: 26px;
    margin-bottom: 22px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04), 0 6px 18px rgba(15, 23, 42, 0.02);
    transition: all 0.2s ease;
}

.section-card:hover {
    border-color: #CBD5E1;
    box-shadow: 0 4px 20px rgba(15, 23, 42, 0.06);
}

.section-title {
    display: flex;
    align-items: center;
    gap: 12px;
    color: #0F172A;
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 6px;
}

.section-desc {
    color: #64748B;
    font-size: 14px;
    margin-bottom: 18px;
    line-height: 1.5;
}

/* Informational & Guidance Boxes */
.tip-box {
    background: #F1F5F9;
    border-left: 4px solid #0F172A;
    border-radius: 12px;
    padding: 16px 20px;
    margin-bottom: 22px;
    font-size: 14px;
    color: #334155;
    line-height: 1.55;
}

.tip-box b {
    color: #0F172A;
}

.guide-pill {
    background: #F8FAFC;
    border: 1px solid #E2E8F0;
    border-radius: 10px;
    padding: 12px 16px;
    font-size: 13px;
    color: #475569;
    margin-top: 8px;
}

/* Clean Input Styling */
div[data-baseweb="input"] > div, 
div[data-baseweb="select"] > div {
    background-color: #FFFFFF !important;
    border: 1px solid #CBD5E1 !important;
    border-radius: 12px !important;
    color: #0F172A !important;
    transition: all 0.2s ease !important;
}

div[data-baseweb="input"] > div:hover, 
div[data-baseweb="select"] > div:hover {
    border-color: #94A3B8 !important;
}

div[data-baseweb="input"] > div:focus-within, 
div[data-baseweb="select"] > div:focus-within {
    border-color: #0F172A !important;
    box-shadow: 0 0 0 2px rgba(15, 23, 42, 0.15) !important;
}

input {
    color: #0F172A !important;
    font-family: inherit !important;
}

label p {
    color: #1E293B !important;
    font-weight: 600 !important;
    font-size: 14px !important;
}

/* PROFESSIONAL MATTE BLACK BUTTONS */
div.stButton > button {
    background: #0F172A !important;
    color: #FFFFFF !important;
    font-size: 16.5px !important;
    font-weight: 700 !important;
    border: 1px solid #000000 !important;
    border-radius: 14px !important;
    padding: 14px 28px !important;
    box-shadow: 0 4px 14px rgba(15, 23, 42, 0.16) !important;
    transition: all 0.2s ease !important;
    letter-spacing: 0.2px !important;
}

div.stButton > button:hover {
    background: #1E293B !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 22px rgba(15, 23, 42, 0.25) !important;
    border-color: #1E293B !important;
}

div.stButton > button:active {
    background: #000000 !important;
    transform: translateY(0px) !important;
}

/* Result Cards */
.result-card-danger {
    background: #FFF1F2;
    border: 2px solid #FECDD3;
    border-radius: 20px;
    padding: 28px;
    text-align: center;
    box-shadow: 0 6px 20px rgba(225, 29, 72, 0.08);
    margin-top: 24px;
}

.result-card-safe {
    background: #F0FDF4;
    border: 2px solid #BBF7D0;
    border-radius: 20px;
    padding: 28px;
    text-align: center;
    box-shadow: 0 6px 20px rgba(22, 163, 74, 0.08);
    margin-top: 24px;
}

.result-icon {
    font-size: 46px;
    margin-bottom: 12px;
}

.result-title-danger {
    color: #BE123C;
    font-size: 25px;
    font-weight: 800;
    margin-bottom: 8px;
}

.result-title-safe {
    color: #15803D;
    font-size: 25px;
    font-weight: 800;
    margin-bottom: 8px;
}

.result-desc {
    color: #334155;
    font-size: 16px;
    line-height: 1.6;
    max-width: 600px;
    margin: 0 auto 16px auto;
}

/* Meter / Gauge Card */
.metric-container {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 16px;
    padding: 20px;
    text-align: center;
    margin-top: 14px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
}

.metric-number {
    font-size: 38px;
    font-weight: 800;
    letter-spacing: -1px;
}

.metric-label {
    font-size: 13px;
    color: #64748B;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    font-weight: 700;
}

/* Contributing Factor Pill */
.factor-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 8px 14px;
    border-radius: 10px;
    font-size: 13px;
    font-weight: 600;
    margin: 4px;
}

.factor-elevated {
    background: #FEE2E2;
    color: #B91C1C;
    border: 1px solid #FECACA;
}

.factor-normal {
    background: #DCFCE7;
    color: #15803D;
    border: 1px solid #BBF7D0;
}

/* Custom separator */
hr {
    border: 0;
    height: 1px;
    background: #E2E8F0;
    margin: 28px 0;
}

/* Radio buttons horizontal styling */
div[role="radiogroup"] {
    gap: 14px;
}

/* Footer */
.footer-text {
    text-align: center;
    color: #64748B;
    font-size: 13px;
    margin-top: 40px;
    padding-top: 20px;
    border-top: 1px solid #E2E8F0;
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# LOAD MACHINE LEARNING MODEL
# =========================================================

@st.cache_resource
def load_model():
    return joblib.load("heart_disease_model.pkl")

try:
    model = load_model()
except Exception as e:
    st.error(f"Error loading trained model: {e}")
    st.stop()


# =========================================================
# SIDEBAR NAVIGATION & APP INFO
# =========================================================

with st.sidebar:
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px;">
        <span style="font-size: 28px;">❤️</span>
        <div>
            <div style="font-size: 20px; font-weight: 800; color: #0F172A; letter-spacing: -0.5px;">HeartCare AI</div>
            <div style="font-size: 12px; color: #E11D48; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">Cardio Intelligence</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p style="font-size: 13px; color: #475569; line-height: 1.5; margin-bottom: 18px;">
    Modern risk screening platform powered by clinical machine learning. Designed for patients and medical professionals.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='margin: 14px 0;'>", unsafe_allow_html=True)

    role = st.radio(
        "Choose Dashboard Experience",
        [
            "👤 Patient View (Simple & Guided)",
            "🩺 Medical Professional View (Clinical & Detailed)"
        ],
        index=0
    )

    st.markdown("<hr style='margin: 18px 0;'>", unsafe_allow_html=True)

    st.markdown("""
    <div style="background: #F1F5F9; border: 1px solid #E2E8F0; border-radius: 12px; padding: 14px; font-size: 12px; color: #334155; line-height: 1.5;">
        <div style="font-weight: 700; color: #0F172A; margin-bottom: 4px; display: flex; align-items: center; gap: 6px;">
            <span>🛡️</span> Clinical Disclaimer
        </div>
        This application provides machine-learning assisted screening for informational and educational purposes. It does <b>not</b> replace a doctor's examination or clinical diagnosis.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.caption("v2.1 • Random Forest Classifier (Cleveland Dataset)")


# =========================================================
# HERO HEADER
# =========================================================

is_patient = "Patient" in role

header_pill = "Patient Self-Screening" if is_patient else "Clinical Decision Support"
header_title = "Cardiovascular Risk Assessment" if is_patient else "Clinical Evaluation Station"
header_desc = (
    "Check your heart risk easily using everyday terms and standard medical tests. "
    "Even if you don't have hospital scans, you can still get a personalized health evaluation."
    if is_patient else
    "Comprehensive binary classification workspace utilizing the 13-feature Cleveland Heart Disease Dataset. "
    "Examine risk probabilities, feature vectors, and clinical splits."
)

st.markdown(f"""
<div class="hero-card">
    <div class="hero-pill">
        <div class="hero-pulse"></div>
        {header_pill}
    </div>
    <h1>❤️ {header_title}</h1>
    <p>{header_desc}</p>
</div>
""", unsafe_allow_html=True)


# =========================================================
# 👤 PATIENT DASHBOARD (PATIENT-CENTRIC & JARGON-FREE)
# =========================================================

if is_patient:

    st.markdown("""
    <div class="tip-box">
        <b>👋 Welcome! You don't need a medical degree to use this tool.</b><br>
        Fill in the details you know below. We've written everything in clear, everyday language with 
        normal healthy reference ranges. If you haven't done specialized hospital scans yet, don't worry—our 
        system automatically handles them using standard healthy baselines!
    </div>
    """, unsafe_allow_html=True)

    # ---------------------------------------------------------
    # STEP 1: ABOUT YOU & BASIC VITALS
    # ---------------------------------------------------------
    st.markdown("""
    <div class="section-card">
        <div class="section-title">
            <span>👤</span> Step 1: About You & Basic Numbers
        </div>
        <div class="section-desc">
            Your age, biological sex, and everyday health numbers you can find from a routine clinic checkup or home monitor.
        </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        age = st.number_input(
            "Your Age (Years)",
            min_value=18,
            max_value=100,
            value=52,
            help="Age is one of the most reliable natural indicators of cardiovascular health."
        )

    with c2:
        sex_label = st.selectbox(
            "Biological Sex",
            ["Male", "Female"],
            help="Biological sex influences typical hormonal and cardiovascular risk patterns."
        )
        sex = 1 if sex_label == "Male" else 0

    st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

    c3, c4 = st.columns(2)
    with c3:
        st.markdown("**🩸 Resting Blood Pressure**")
        bp_mode = st.radio(
            "Do you know your typical blood pressure reading?",
            ["Yes, I know my number", "I'm not sure (Use standard normal: 120 mmHg)"],
            key="p_bp_choice"
        )
        if "Yes" in bp_mode:
            trestbps = st.number_input(
                "Top number / Systolic (mmHg)",
                min_value=80,
                max_value=220,
                value=128,
                help="The top number when measured while resting calmly. Normal is usually between 90 and 120 mmHg."
            )
            if trestbps >= 140:
                st.caption("⚠️ Note: Readings of 140 or higher indicate elevated pressure.")
            elif trestbps <= 120:
                st.caption("✅ Great: Within optimal healthy range (under 120 mmHg).")
            else:
                st.caption("ℹ️ Slightly elevated range (121 - 139 mmHg).")
        else:
            trestbps = 120.0
            st.caption("Using typical healthy resting baseline: 120 mmHg.")

    with c4:
        st.markdown("**🧪 Total Blood Cholesterol**")
        chol_mode = st.radio(
            "Do you know your total cholesterol level from a blood test?",
            ["Yes, I have my test result", "I'm not sure (Use standard average: 200 mg/dL)"],
            key="p_chol_choice"
        )
        if "Yes" in chol_mode:
            chol = st.number_input(
                "Total Cholesterol (mg/dL)",
                min_value=100,
                max_value=500,
                value=210,
                help="Found on your routine lipid blood panel. Desirable level is usually under 200 mg/dL."
            )
            if chol >= 240:
                st.caption("⚠️ High cholesterol range (240 mg/dL or above).")
            elif chol < 200:
                st.caption("✅ Desirable healthy range (below 200 mg/dL).")
            else:
                st.caption("ℹ️ Borderline high range (200 - 239 mg/dL).")
        else:
            chol = 200.0
            st.caption("Using typical standard baseline: 200 mg/dL.")

    st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

    c5, c6 = st.columns(2)
    with c5:
        st.markdown("**🍬 Morning Fasting Blood Sugar**")
        fbs_choice = st.selectbox(
            "Has a morning blood test shown fasting sugar higher than 120 mg/dL (or diagnosed diabetes)?",
            [
                "No — My blood sugar is normal (under 120 mg/dL)",
                "Yes — Elevated fasting sugar / Diabetic (over 120 mg/dL)",
                "I don't know (Assume normal healthy level)"
            ],
            help="Fasting blood sugar measures glucose after not eating overnight. Over 120 mg/dL can indicate diabetes risk."
        )
        if "Yes" in fbs_choice:
            fbs = 1
        else:
            fbs = 0

    with c6:
        st.markdown("**💓 Maximum Heart Rate Achieved**")
        hr_mode = st.radio(
            "Do you know your peak heart rate from exercise or a treadmill test?",
            ["Yes, I know it", "Calculate estimated peak for my age automatically"],
            key="p_hr_choice"
        )
        if "Yes" in hr_mode:
            thalach = st.number_input(
                "Peak Heart Rate (beats per minute)",
                min_value=60,
                max_value=220,
                value=155,
                help="The highest heart rate reached during strenuous exercise or a cardiology treadmill test."
            )
        else:
            # Standard physiological formula: 220 - age, scaled to ~85% for typical test
            estimated_thalach = max(90, int(220 - (age * 0.85)))
            thalach = float(estimated_thalach)
            st.caption(f"Estimated age-appropriate peak heart rate: ~{estimated_thalach} bpm.")

    st.markdown("</div>", unsafe_allow_html=True)

    # ---------------------------------------------------------
    # STEP 2: SYMPTOMS YOU FEEL IN DAILY LIFE
    # ---------------------------------------------------------
    st.markdown("""
    <div class="section-card">
        <div class="section-title">
            <span>❤️</span> Step 2: Everyday Sensations & Exercise
        </div>
        <div class="section-desc">
            How your chest and heart feel during your normal daily activities, walking, or physical exertion.
        </div>
    """, unsafe_allow_html=True)

    s1, s2 = st.columns(2)

    with s1:
        st.markdown("**Do you experience any chest discomfort or unusual sensations?**")
        cp_selection = st.selectbox(
            "Select the description that best matches your experience:",
            [
                "No chest pain or discomfort at all (Completely comfortable)",
                "Chest pressure, heaviness, or squeezing during physical effort or stress (Relieved by rest)",
                "Occasional unusual ache or mild tightness (Not directly tied to physical effort)",
                "Sharp, momentary twinges or pains unrelated to heart exertion (e.g., muscle/rib pain)"
            ],
            help="Angina is discomfort caused when heart muscles need more oxygenated blood during activity."
        )
        # Cleveland mapping:
        # 1 = typical angina (chest pressure with effort)
        # 2 = atypical angina (unusual chest ache)
        # 3 = non-anginal pain (sharp/momentary unrelated)
        # 4 = asymptomatic (no chest pain)
        if "No chest pain" in cp_selection:
            cp = 4.0
        elif "pressure, heaviness" in cp_selection:
            cp = 1.0
        elif "unusual ache" in cp_selection:
            cp = 2.0
        else:
            cp = 3.0

    with s2:
        st.markdown("**Exercise / Exertion Check**")
        exang_selection = st.selectbox(
            "Do you get chest pain or tightness when walking uphill, climbing stairs, or exercising?",
            [
                "No — I do not get chest discomfort when exercising",
                "Yes — I often feel tightness or ache during physical exertion",
                "I'm not sure / I rarely engage in vigorous activity"
            ]
        )
        if "Yes" in exang_selection:
            exang = 1.0
        else:
            exang = 0.0

    st.markdown("</div>", unsafe_allow_html=True)

    # ---------------------------------------------------------
    # STEP 3: SPECIALIZED MEDICAL TESTS (OPTIONAL / GUIDED)
    # ---------------------------------------------------------
    st.markdown("""
    <div class="section-card">
        <div class="section-title">
            <span>🩺</span> Step 3: Medical Test Reports (ECG & Hospital Scans)
        </div>
        <div class="section-desc">
            These are advanced tests done at a cardiology clinic or hospital (e.g. resting ECG, treadmill stress test, angiogram).
        </div>
    """, unsafe_allow_html=True)

    has_advanced_tests = st.radio(
        "Do you have a detailed cardiology or hospital lab report with ECG / Stress test results?",
        [
            "No — I don't have these hospital tests (Use standard healthy clinical baselines)",
            "Yes — I have my test report and want to enter specific results"
        ],
        horizontal=False
    )

    if "No" in has_advanced_tests:
        # Standard clinical healthy baselines for non-hospitalized individuals:
        restecg = 0.0   # Normal resting ECG
        oldpeak = 0.0   # No ST depression on stress test (healthy)
        slope = 1.0     # Normal upsloping ST segment
        ca = 0.0        # 0 major vessels blocked
        thal = 3.0      # Normal blood flow (score 3)

        st.markdown("""
        <div class="guide-pill" style="border-left: 3px solid #16A34A; background: #F0FDF4;">
            ✅ <b>Standard Healthy Baseline Applied:</b><br>
            • Resting ECG: Normal (0)<br>
            • Exercise ST Depression: None / 0.0 mm<br>
            • Major Blood Vessels Blocked: 0 vessels<br>
            • Cardiac Blood Flow: Normal scan (3)<br>
            <i>You can still assess your cardiovascular risk based on your lifestyle, vitals, age, and symptoms!</i>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.markdown("<p style='font-size:13px; color:#E11D48; font-weight:600;'>💡 Refer to the written values in your medical discharge summary or stress test report.</p>", unsafe_allow_html=True)

        t1, t2 = st.columns(2)
        with t1:
            restecg_choice = st.selectbox(
                "Resting Electrocardiogram (ECG) Result",
                [
                    "Normal ECG (Score 0)",
                    "ST-T Wave Changes / Mild rhythm variance (Score 1)",
                    "Ventricular Enlargement / Hypertrophy (Score 2)"
                ],
                help="A quick recording of the electrical activity of your heart while lying quietly."
            )
            restecg = 0.0 if "Normal" in restecg_choice else (1.0 if "Score 1" in restecg_choice else 2.0)

            oldpeak = st.number_input(
                "Exercise ST Depression (Oldpeak in mm)",
                min_value=0.0,
                max_value=6.5,
                value=0.5,
                step=0.1,
                help="Look under 'ST depression' in your treadmill exercise test report. 0.0 is completely normal."
            )

        with t2:
            ca_choice = st.selectbox(
                "Number of Major Vessels Blocked (from Fluoroscopy/Angiogram)",
                [
                    "0 Vessels blocked (Clear / Healthy arteries)",
                    "1 Major vessel affected",
                    "2 Major vessels affected",
                    "3 Major vessels affected"
                ],
                help="Determined during cardiac catheterization or fluoroscopy."
            )
            ca = float(ca_choice.split()[0])

            thal_choice = st.selectbox(
                "Heart Blood Flow Scan (Thallium Stress Test)",
                [
                    "Normal blood flow throughout heart (Score 3)",
                    "Fixed defect / Old scar tissue (Score 6)",
                    "Reversible defect / Reduced flow during stress (Score 7)"
                ],
                help="A nuclear medicine scan showing how well blood flows to your heart muscle during exercise and rest."
            )
            if "Normal" in thal_choice:
                thal = 3.0
            elif "Fixed" in thal_choice:
                thal = 6.0
            else:
                thal = 7.0

        slope_choice = st.selectbox(
            "Slope pattern of ECG during peak exercise",
            [
                "Upsloping — Healthy normal rise during exertion (Slope 1)",
                "Flat — Horizontal line during exertion (Slope 2)",
                "Downsloping — Dropping line during exertion (Slope 3)"
            ]
        )
        slope = 1.0 if "Upsloping" in slope_choice else (2.0 if "Flat" in slope_choice else 3.0)

    st.markdown("</div>", unsafe_allow_html=True)

    # ---------------------------------------------------------
    # PREDICTION TRIGGER
    # ---------------------------------------------------------
    st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

    run_check = st.button("🔍 Check My Heart Health Risk", use_container_width=True)

    if run_check:
        patient_data = pd.DataFrame([{
            "age": float(age),
            "sex": float(sex),
            "cp": float(cp),
            "trestbps": float(trestbps),
            "chol": float(chol),
            "fbs": float(fbs),
            "restecg": float(restecg),
            "thalach": float(thalach),
            "exang": float(exang),
            "oldpeak": float(oldpeak),
            "slope": float(slope),
            "ca": float(ca),
            "thal": float(thal)
        }])

        pred = model.predict(patient_data)[0]
        prob = model.predict_proba(patient_data)[0][1]
        risk_pct = round(prob * 100, 1)

        # ---------------------------------------------------------
        # RESULT VISUALIZATION
        # ---------------------------------------------------------
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown("## 📊 Your Risk Assessment Report")

        if pred == 1 or risk_pct >= 50.0:
            card_class = "result-card-danger"
            title_class = "result-title-danger"
            status_title = "Elevated Heart Disease Risk Detected"
            status_icon = "⚠️"
            status_desc = (
                f"Based on your responses, the machine learning model calculated an estimated **{risk_pct}% risk likelihood**. "
                "This indicates factors that warrant a comprehensive review with a cardiologist or your primary physician."
            )
            accent_color = "#E11D48"
        else:
            card_class = "result-card-safe"
            title_class = "result-title-safe"
            status_title = "Lower Predicted Cardiovascular Risk"
            status_icon = "✅"
            status_desc = (
                f"Based on your responses, the machine learning model calculated an estimated **{risk_pct}% risk likelihood**. "
                "Your entered parameters currently align with lower risk patterns for coronary heart disease."
            )
            accent_color = "#16A34A"

        st.markdown(f"""
        <div class="{card_class}">
            <div class="result-icon">{status_icon}</div>
            <div class="{title_class}">{status_title}</div>
            <div class="result-desc">{status_desc}</div>
        </div>
        """, unsafe_allow_html=True)

        # Meter Gauge & Metrics Grid
        m1, m2, m3 = st.columns(3)

        with m1:
            st.markdown(f"""
            <div class="metric-container">
                <div class="metric-number" style="color: {accent_color};">{risk_pct}%</div>
                <div class="metric-label">Estimated Risk Score</div>
            </div>
            """, unsafe_allow_html=True)

        with m2:
            category_text = "High Risk" if risk_pct >= 65 else ("Moderate Risk" if risk_pct >= 40 else "Optimal / Low Risk")
            st.markdown(f"""
            <div class="metric-container">
                <div class="metric-number" style="color: #0F172A; font-size: 28px; padding-top: 6px;">{category_text}</div>
                <div class="metric-label">Risk Category</div>
            </div>
            """, unsafe_allow_html=True)

        with m3:
            baseline_status = "Custom Hospital Lab" if "Yes" in has_advanced_tests else "Standard Normal Baseline"
            st.markdown(f"""
            <div class="metric-container">
                <div class="metric-number" style="color: #334155; font-size: 22px; padding-top: 10px;">{baseline_status}</div>
                <div class="metric-label">Evaluation Mode</div>
            </div>
            """, unsafe_allow_html=True)

        # Contributing Factors Breakdown
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("### 🔍 Key Factors in Your Profile")

        factor_html = "<div style='display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 20px;'>"

        # BP
        if trestbps >= 140:
            factor_html += f"<span class='factor-badge factor-elevated'>⚠️ Resting BP ({int(trestbps)} mmHg - Elevated)</span>"
        else:
            factor_html += f"<span class='factor-badge factor-normal'>✅ Resting BP ({int(trestbps)} mmHg - Healthy)</span>"

        # Cholesterol
        if chol >= 240:
            factor_html += f"<span class='factor-badge factor-elevated'>⚠️ Cholesterol ({int(chol)} mg/dL - High)</span>"
        elif chol >= 200:
            factor_html += f"<span class='factor-badge factor-elevated'>⚠️ Cholesterol ({int(chol)} mg/dL - Borderline)</span>"
        else:
            factor_html += f"<span class='factor-badge factor-normal'>✅ Cholesterol ({int(chol)} mg/dL - Optimal)</span>"

        # Sugar
        if fbs == 1:
            factor_html += "<span class='factor-badge factor-elevated'>⚠️ Fasting Blood Sugar > 120 mg/dL</span>"
        else:
            factor_html += "<span class='factor-badge factor-normal'>✅ Fasting Blood Sugar Normal</span>"

        # Chest Pain / Exertion
        if cp == 1.0 or exang == 1.0:
            factor_html += "<span class='factor-badge factor-elevated'>⚠️ Exertional Chest Discomfort Reported</span>"
        else:
            factor_html += "<span class='factor-badge factor-normal'>✅ No Exertional Chest Pain</span>"

        factor_html += "</div>"
        st.markdown(factor_html, unsafe_allow_html=True)

        # Actionable Next Steps
        st.markdown("""
        <div class="section-card" style="background: #FFFFFF;">
            <div class="section-title"><span>📋</span> Plain-Language Next Steps</div>
            <div style="font-size: 14.5px; color: #334155; line-height: 1.6;">
                <ul>
                    <li><b>Discuss with your doctor:</b> Take these numbers to your next checkup. Ask your physician: <i>"Should we check a formal lipid panel, ECG, or cardiac calcium score?"</i></li>
                    <li><b>Daily heart care:</b> Maintain regular moderate exercise (like 30 minutes of brisk walking), minimize trans-fats and excess sodium, and stay well hydrated.</li>
                    <li><b>When to seek immediate emergency care:</b> If you ever feel sudden crushing chest pressure, shortness of breath, radiating pain to your left arm or jaw, or unexplained fainting, call emergency services (e.g. 911 or local emergency) immediately.</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)

        with st.expander("📄 View & Copy Summary for Your Doctor Appointment", expanded=False):
            summary_text = (
                f"HeartCare AI - Patient Screening Summary\n"
                f"-----------------------------------------\n"
                f"• Age: {int(age)} | Biological Sex: {sex_label}\n"
                f"• Estimated Cardiovascular Risk: {risk_pct}% ({category_text})\n"
                f"• Resting Blood Pressure: {int(trestbps)} mmHg\n"
                f"• Total Cholesterol: {int(chol)} mg/dL\n"
                f"• Fasting Blood Sugar: {'> 120 mg/dL' if fbs == 1 else 'Normal (< 120 mg/dL)'}\n"
                f"• Peak Heart Rate: {int(thalach)} bpm\n"
                f"• Chest Discomfort: {cp_selection}\n"
                f"• Exertional Symptoms: {'Reported with exercise' if exang == 1 else 'None'}\n"
                f"• Hospital Test Mode: {'Specialized Cardiology Tests Provided' if 'Yes' in has_advanced_tests else 'Standard Population Baselines Applied'}\n"
            )
            st.code(summary_text, language="markdown")
            st.caption("Tip: You can copy this summary to your notes or show it directly to your doctor.")


# =========================================================
# 🩺 MEDICAL PROFESSIONAL DASHBOARD (CLINICAL & DETAILED)
# =========================================================

else:
    st.markdown("""
    <div class="tip-box" style="border-left-color: #0F172A;">
        <b>🩺 Clinical Decision Support Mode:</b><br>
        Direct access to the 13 clinical predictors from the Cleveland Heart Disease Dataset. 
        You can use 1-click presets to populate patient cases or manually configure any feature vector.
    </div>
    """, unsafe_allow_html=True)

    # 1-Click Clinical Case Presets
    st.markdown("### ⚡ Quick Clinical Presets")
    p_col1, p_col2, p_col3 = st.columns(3)

    preset_name = None
    with p_col1:
        if st.button("🧪 Preset A: Healthy 45yo Screening", use_container_width=True):
            preset_name = "preset_a"
    with p_col2:
        if st.button("⚠️ Preset B: 62yo High-Risk Angina", use_container_width=True):
            preset_name = "preset_b"
    with p_col3:
        if st.button("⚖️ Preset C: 56yo Borderline Diabetic", use_container_width=True):
            preset_name = "preset_c"

    # Set default values based on chosen preset or standard defaults
    if preset_name == "preset_a":
        def_age, def_sex, def_cp, def_bp, def_chol = 45, 0, 4, 118, 185
        def_thalach, def_fbs, def_restecg, def_exang = 172, 0, 0, 0
        def_oldpeak, def_slope, def_ca, def_thal = 0.0, 1, 0, 3
    elif preset_name == "preset_b":
        def_age, def_sex, def_cp, def_bp, def_chol = 62, 1, 1, 158, 285
        def_thalach, def_fbs, def_restecg, def_exang = 120, 1, 2, 1
        def_oldpeak, def_slope, def_ca, def_thal = 2.4, 2, 2, 7
    elif preset_name == "preset_c":
        def_age, def_sex, def_cp, def_bp, def_chol = 56, 1, 2, 138, 240
        def_thalach, def_fbs, def_restecg, def_exang = 145, 1, 1, 0
        def_oldpeak, def_slope, def_ca, def_thal = 1.0, 2, 1, 6
    else:
        def_age, def_sex, def_cp, def_bp, def_chol = 54, 1, 2, 130, 235
        def_thalach, def_fbs, def_restecg, def_exang = 150, 0, 0, 0
        def_oldpeak, def_slope, def_ca, def_thal = 1.0, 1, 0, 3

    st.markdown("""
    <div class="section-card">
        <div class="section-title"><span>🧑‍⚕️</span> Clinical Predictor Vector (13 Features)</div>
        <div class="section-desc">Cleveland Heart Disease standard categorical & continuous variables.</div>
    """, unsafe_allow_html=True)

    # Row 1: Demographics & Hemodynamics
    r1, r2, r3, r4 = st.columns(4)
    with r1:
        doc_age = st.number_input("Age (years)", 20, 100, def_age, key="doc_age")
    with r2:
        doc_sex = st.selectbox("Sex", [1, 0], format_func=lambda x: "Male (1)" if x == 1 else "Female (0)", index=0 if def_sex == 1 else 1, key="doc_sex")
    with r3:
        doc_cp = st.selectbox(
            "Chest Pain Type (cp)",
            [1, 2, 3, 4],
            format_func=lambda x: {
                1: "1: Typical Angina",
                2: "2: Atypical Angina",
                3: "3: Non-Anginal Pain",
                4: "4: Asymptomatic"
            }[x],
            index=[1, 2, 3, 4].index(def_cp),
            key="doc_cp"
        )
    with r4:
        doc_trestbps = st.number_input("Resting BP (trestbps mm Hg)", 80, 220, def_bp, key="doc_trestbps")

    # Row 2: Metabolic & Stress Vitals
    r5, r6, r7, r8 = st.columns(4)
    with r5:
        doc_chol = st.number_input("Cholesterol (chol mg/dl)", 100, 600, def_chol, key="doc_chol")
    with r6:
        doc_fbs = st.selectbox(
            "Fasting Blood Sugar > 120 (fbs)",
            [0, 1],
            format_func=lambda x: "fbs = 0 (Normal / < 120)" if x == 0 else "fbs = 1 (> 120 mg/dl)",
            index=def_fbs,
            key="doc_fbs"
        )
    with r7:
        doc_thalach = st.number_input("Max Heart Rate (thalach)", 60, 220, def_thalach, key="doc_thalach")
    with r8:
        doc_exang = st.selectbox(
            "Exercise Angina (exang)",
            [0, 1],
            format_func=lambda x: "No (0)" if x == 0 else "Yes (1)",
            index=def_exang,
            key="doc_exang"
        )

    # Row 3: Diagnostic Electrocardiography & Scans
    r9, r10, r11, r12 = st.columns(4)
    with r9:
        doc_restecg = st.selectbox(
            "Resting ECG (restecg)",
            [0, 1, 2],
            format_func=lambda x: {
                0: "0: Normal",
                1: "1: ST-T Abnormality",
                2: "2: LV Hypertrophy"
            }[x],
            index=def_restecg,
            key="doc_restecg"
        )
    with r10:
        doc_oldpeak = st.number_input("ST Depression (oldpeak)", 0.0, 7.0, float(def_oldpeak), step=0.1, key="doc_oldpeak")
    with r11:
        doc_slope = st.selectbox(
            "Peak ST Slope (slope)",
            [1, 2, 3],
            format_func=lambda x: {
                1: "1: Upsloping",
                2: "2: Flat",
                3: "3: Downsloping"
            }[x],
            index=[1, 2, 3].index(def_slope),
            key="doc_slope"
        )
    with r12:
        doc_ca = st.selectbox(
            "Major Vessels Fluro (ca)",
            [0, 1, 2, 3],
            index=def_ca,
            key="doc_ca"
        )

    # Row 4: Nuclear Perfusion Scintigraphy
    doc_thal = st.selectbox(
        "Thallium Heart Scintigraphy (thal)",
        [3, 6, 7],
        format_func=lambda x: {
            3: "3: Normal Perfusion",
            6: "6: Fixed Defect (Previous Infarct)",
            7: "7: Reversible Defect (Ischemia)"
        }[x],
        index=[3, 6, 7].index(def_thal),
        key="doc_thal"
    )

    st.markdown("</div>", unsafe_allow_html=True)

    # Analyze Button
    doc_predict = st.button("🩺 Execute Clinical Model Analysis", use_container_width=True)

    if doc_predict:
        doc_patient = pd.DataFrame([{
            "age": float(doc_age),
            "sex": float(doc_sex),
            "cp": float(doc_cp),
            "trestbps": float(doc_trestbps),
            "chol": float(doc_chol),
            "fbs": float(doc_fbs),
            "restecg": float(doc_restecg),
            "thalach": float(doc_thalach),
            "exang": float(doc_exang),
            "oldpeak": float(doc_oldpeak),
            "slope": float(doc_slope),
            "ca": float(doc_ca),
            "thal": float(doc_thal)
        }])

        pred = model.predict(doc_patient)[0]
        prob = model.predict_proba(doc_patient)[0][1]

        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown("## 📋 Model Diagnostic Output")

        res_c1, res_c2, res_c3 = st.columns(3)
        with res_c1:
            class_str = "CAD Disease Predicted (1)" if pred == 1 else "No Disease Predicted (0)"
            class_color = "#E11D48" if pred == 1 else "#16A34A"
            st.markdown(f"""
            <div class="metric-container">
                <div class="metric-number" style="color: {class_color}; font-size: 26px; padding-top: 6px;">{class_str}</div>
                <div class="metric-label">Predicted Classification</div>
            </div>
            """, unsafe_allow_html=True)

        with res_c2:
            st.markdown(f"""
            <div class="metric-container">
                <div class="metric-number" style="color: #0F172A;">{prob * 100:.1f}%</div>
                <div class="metric-label">Posterior Probability P(Disease)</div>
            </div>
            """, unsafe_allow_html=True)

        with res_c3:
            st.markdown("""
            <div class="metric-container">
                <div class="metric-number" style="color: #2563EB; font-size: 26px; padding-top: 6px;">Random Forest</div>
                <div class="metric-label">Model Architecture (85% Accuracy)</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("### 🔬 Patient Feature Vector")
        st.dataframe(doc_patient, use_container_width=True)

        # Feature Importance Insights
        if hasattr(model, "feature_importances_"):
            st.markdown("### 📈 Model Feature Weighting")
            feat_df = pd.DataFrame({
                "Feature": ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"],
                "Importance": model.feature_importances_
            }).sort_values("Importance", ascending=False)
            st.bar_chart(feat_df.set_index("Feature"))


# =========================================================
# GLOBAL FOOTER
# =========================================================

st.markdown("""
<div class="footer-text">
    ❤️ <b>HeartCare AI</b> • Intelligent Cardiovascular Screening Platform<br>
    Built with Streamlit & Scikit-Learn • Cleveland Heart Disease Clinical Cohort • For Educational & Evaluative Use Only
</div>
""", unsafe_allow_html=True)