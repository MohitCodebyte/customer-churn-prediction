# import streamlit as st
# import pickle
# import numpy as np

# # ---------------- PAGE CONFIG ----------------
# st.set_page_config(
#     page_title="Customer Churn Prediction",
#     page_icon="📊",
#     layout="wide"
# )

# # ---------------- CSS STYLING ONLY ----------------
# st.markdown("""
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600&family=DM+Mono:wght@400;500&display=swap');

# .stApp {
#     background: #060a10 !important;
#     font-family: 'Space Grotesk', sans-serif;
# }

# #MainMenu, footer, header { visibility: hidden; }

# [data-testid="stSidebar"] {
#     background: #0c131d !important;
#     border-right: 1px solid #1a2535;
# }

# label, .stSelectbox label, .stNumberInput label {
#     color: #94a3b8 !important;
#     font-size: 13px !important;
#     font-weight: 500 !important;
# }

# div[data-baseweb="select"] > div {
#     background-color: #080e17 !important;
#     border: 1px solid #1e2d42 !important;
#     border-radius: 8px !important;
#     color: #e2e8f0 !important;
# }

# div[data-baseweb="input"] > div {
#     background-color: #080e17 !important;
#     border: 1px solid #1e2d42 !important;
#     border-radius: 8px !important;
# }
# div[data-baseweb="input"] input {
#     color: #e2e8f0 !important;
#     font-family: 'DM Mono', monospace !important;
# }

# .stButton > button {
#     background: linear-gradient(90deg, #00e5a0, #0070f3) !important;
#     color: #000 !important;
#     font-family: 'Space Grotesk', sans-serif !important;
#     font-size: 15px !important;
#     font-weight: 700 !important;
#     border: none !important;
#     border-radius: 10px !important;
#     height: 52px !important;
#     width: 100% !important;
# }
# .stButton > button:hover { opacity: 0.88 !important; }

# [data-testid="stMetric"] {
#     background: #0c131d !important;
#     border: 1px solid #1a2535 !important;
#     border-radius: 10px !important;
#     padding: 12px 16px !important;
# }
# [data-testid="stMetricLabel"] p {
#     color: #64748b !important;
#     font-size: 11px !important;
#     letter-spacing: 0.8px !important;
#     text-transform: uppercase !important;
# }
# [data-testid="stMetricValue"] {
#     color: #f1f5f9 !important;
#     font-family: 'DM Mono', monospace !important;
# }
# </style>
# """, unsafe_allow_html=True)

# # ---------------- LOAD MODEL ----------------
# @st.cache_resource
# def load_model():
#     model  = pickle.load(open(r'churn_model.pkl', 'rb'))
#     scaler = pickle.load(open(r'scaler.pkl', 'rb'))
#     return model, scaler

# model, scaler = load_model()

# # ---------------- SIDEBAR ----------------
# with st.sidebar:
#     st.markdown("### 📌 Navigation")
#     st.divider()
#     st.info("This AI model predicts whether a customer is likely to churn or stay based on their profile.")
#     st.success("✅ Model Accuracy: 84%")
#     st.divider()
#     st.caption("Built with Machine Learning + Streamlit")

# # ---------------- HEADER ----------------
# st.markdown("""
# <div style='display:flex;align-items:center;gap:16px;padding:1rem 0 1.5rem;border-bottom:1px solid #1e2a3a;margin-bottom:2rem;'>
#     <div style='width:48px;height:48px;background:linear-gradient(135deg,#00e5a0,#0070f3);border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:22px;'>📊</div>
#     <div>
#         <div style='font-size:22px;font-weight:600;color:#f1f5f9;'>Customer Churn Prediction</div>
#         <div style='font-size:13px;color:#64748b;margin-top:2px;'>ML-powered churn risk assessment · Telecom dataset</div>
#     </div>
#     <div style='margin-left:auto;background:#0d2a1a;border:1px solid rgba(0,229,160,0.4);color:#00e5a0;font-size:11px;font-family:monospace;padding:5px 12px;border-radius:6px;'>Accuracy: 84%</div>
# </div>
# """, unsafe_allow_html=True)

# # ---------------- INPUTS ----------------
# col1, col2 = st.columns(2)

# with col1:
#     st.markdown("<p style='color:#3b82f6;font-size:11px;font-weight:600;letter-spacing:1.2px;text-transform:uppercase;margin-bottom:8px;'>👤 Demographics</p>", unsafe_allow_html=True)
#     gender     = st.selectbox("Gender", ["Male", "Female"])
#     senior     = st.selectbox("Senior Citizen", [0, 1], format_func=lambda x: "Yes" if x else "No")
#     partner    = st.selectbox("Partner", [0, 1], format_func=lambda x: "Yes" if x else "No")
#     dependents = st.selectbox("Dependents", [0, 1], format_func=lambda x: "Yes" if x else "No")
#     tenure     = st.number_input("Tenure (months)", min_value=0, max_value=100, value=12)

#     st.markdown("<br><p style='color:#3b82f6;font-size:11px;font-weight:600;letter-spacing:1.2px;text-transform:uppercase;margin-bottom:8px;'>🔒 Add-ons</p>", unsafe_allow_html=True)
#     device_protection = st.selectbox("Device Protection", [0, 1], format_func=lambda x: "Yes" if x else "No")
#     tech_support      = st.selectbox("Tech Support", [0, 1], format_func=lambda x: "Yes" if x else "No")
#     streaming_tv      = st.selectbox("Streaming TV", [0, 1], format_func=lambda x: "Yes" if x else "No")
#     streaming_movies  = st.selectbox("Streaming Movies", [0, 1], format_func=lambda x: "Yes" if x else "No")

# with col2:
#     st.markdown("<p style='color:#3b82f6;font-size:11px;font-weight:600;letter-spacing:1.2px;text-transform:uppercase;margin-bottom:8px;'>📱 Services</p>", unsafe_allow_html=True)
#     phone_service    = st.selectbox("Phone Service", [0, 1], format_func=lambda x: "Yes" if x else "No")
#     multiple_lines   = st.selectbox("Multiple Lines", [0, 1], format_func=lambda x: "Yes" if x else "No")
#     internet_service = st.selectbox("Internet Service", ["DSL", "Fiber Optic", "No Internet"])
#     online_security  = st.selectbox("Online Security", [0, 1], format_func=lambda x: "Yes" if x else "No")
#     online_backup    = st.selectbox("Online Backup", [0, 1], format_func=lambda x: "Yes" if x else "No")

#     st.markdown("<br><p style='color:#3b82f6;font-size:11px;font-weight:600;letter-spacing:1.2px;text-transform:uppercase;margin-bottom:8px;'>💳 Billing & Contract</p>", unsafe_allow_html=True)
#     contract  = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
#     paperless = st.selectbox("Paperless Billing", [0, 1], format_func=lambda x: "Yes" if x else "No")
#     payment   = st.selectbox("Payment Method", [
#         "Electronic check", "Mailed check",
#         "Bank transfer (automatic)", "Credit card (automatic)"
#     ])
#     monthly = st.number_input("Monthly Charges ($)", min_value=0.0, value=70.0, step=0.01)
#     total   = st.number_input("Total Charges ($)", min_value=0.0, value=1000.0, step=0.01)

# # ---------------- PREDICT BUTTON ----------------
# st.markdown("<br>", unsafe_allow_html=True)
# predict_clicked = st.button("⚡  Predict Churn Risk")

# # ---------------- PREDICTION ----------------
# if predict_clicked:

#     gender_val         = 1 if gender == "Male" else 0
#     internet_fiber     = 1 if internet_service == "Fiber Optic" else 0
#     internet_no        = 1 if internet_service == "No Internet" else 0
#     contract_one       = 1 if contract == "One year" else 0
#     contract_two       = 1 if contract == "Two year" else 0
#     payment_credit     = 1 if "Credit card" in payment else 0
#     payment_electronic = 1 if "Electronic" in payment else 0
#     payment_mailed     = 1 if "Mailed" in payment else 0

#     sample = np.zeros((1, 30))
#     sample[0][0]  = gender_val
#     sample[0][1]  = senior
#     sample[0][2]  = partner
#     sample[0][3]  = dependents
#     sample[0][4]  = tenure
#     sample[0][5]  = phone_service
#     sample[0][6]  = paperless
#     sample[0][7]  = monthly
#     sample[0][8]  = total
#     sample[0][9]  = multiple_lines
#     sample[0][10] = internet_fiber
#     sample[0][11] = internet_no
#     sample[0][12] = online_security
#     sample[0][13] = online_backup
#     sample[0][14] = device_protection
#     sample[0][15] = tech_support
#     sample[0][16] = streaming_tv
#     sample[0][17] = streaming_movies
#     sample[0][18] = contract_one
#     sample[0][19] = contract_two
#     sample[0][20] = payment_credit
#     sample[0][21] = payment_electronic
#     sample[0][22] = payment_mailed

#     sample_scaled = scaler.transform(sample)
#     pred          = model.predict(sample_scaled)
#     prob          = model.predict_proba(sample_scaled)
#     churn_prob    = round(prob[0][1] * 100, 1)
#     stay_prob     = round(prob[0][0] * 100, 1)
#     is_churn      = pred[0] == 1

#     st.markdown("<br>", unsafe_allow_html=True)
#     st.markdown("<p style='color:#3b82f6;font-size:11px;font-weight:600;letter-spacing:1.2px;text-transform:uppercase;'>📌 Prediction Result</p>", unsafe_allow_html=True)

#     if is_churn:
#         st.error(f"⚠️  High Churn Risk — This customer is likely to leave the service.")
#     else:
#         st.success(f"✅  Low Churn Risk — This customer is likely to stay.")

#     st.markdown("<br>", unsafe_allow_html=True)

#     st.markdown(f"<p style='color:#94a3b8;font-size:13px;margin-bottom:4px;'>🔴 Churn Probability &nbsp;&nbsp;<b style='color:#f87171;font-family:monospace;'>{churn_prob}%</b></p>", unsafe_allow_html=True)
#     st.progress(int(churn_prob))

#     st.markdown(f"<p style='color:#94a3b8;font-size:13px;margin-bottom:4px;margin-top:12px;'>🟢 Retention Probability &nbsp;&nbsp;<b style='color:#34d399;font-family:monospace;'>{stay_prob}%</b></p>", unsafe_allow_html=True)
#     st.progress(int(stay_prob))

#     st.markdown("<br>", unsafe_allow_html=True)

#     m1, m2, m3 = st.columns(3)
#     m1.metric("🎯 Risk Score",       f"{churn_prob}%")
#     m2.metric("💰 Monthly Charges",  f"${monthly:.0f}")
#     m3.metric("📅 Tenure",           f"{tenure} mo")



import streamlit as st
import pickle
import numpy as np

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# ---------------- CSS ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600&family=DM+Mono:wght@400;500&display=swap');

.stApp {
    background: #060a10 !important;
    font-family: 'Space Grotesk', sans-serif;
}

#MainMenu, footer, header { visibility: hidden; }

[data-testid="stSidebar"] {
    background: #0c131d !important;
    border-right: 1px solid #1a2535;
}

label, .stSelectbox label, .stNumberInput label {
    color: #94a3b8 !important;
    font-size: 13px !important;
    font-weight: 500 !important;
}

div[data-baseweb="select"] > div {
    background-color: #080e17 !important;
    border: 1px solid #1e2d42 !important;
    border-radius: 8px !important;
    color: #e2e8f0 !important;
}

div[data-baseweb="input"] > div {
    background-color: #080e17 !important;
    border: 1px solid #1e2d42 !important;
    border-radius: 8px !important;
}
div[data-baseweb="input"] input {
    color: #e2e8f0 !important;
    font-family: 'DM Mono', monospace !important;
}

.stButton > button {
    background: linear-gradient(90deg, #00e5a0, #0070f3) !important;
    color: #000 !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 15px !important;
    font-weight: 700 !important;
    border: none !important;
    border-radius: 10px !important;
    height: 52px !important;
    width: 100% !important;
    transition: transform 0.2s ease, box-shadow 0.2s ease !important;
}
.stButton > button:hover {
    transform: scale(1.03) !important;
    box-shadow: 0 6px 24px rgba(0, 229, 160, 0.25) !important;
}

/* ---- METRIC CARD HOVER ---- */
[data-testid="stMetric"] {
    background: #0c131d !important;
    border: 1px solid #1a2535 !important;
    border-radius: 10px !important;
    padding: 14px 18px !important;
    transition: transform 0.22s ease, border-color 0.22s ease, box-shadow 0.22s ease !important;
    cursor: default;
}
[data-testid="stMetric"]:hover {
    transform: scale(1.06) !important;
    border-color: #3b82f6 !important;
    box-shadow: 0 8px 28px rgba(59, 130, 246, 0.18) !important;
}
[data-testid="stMetricLabel"] p {
    color: #64748b !important;
    font-size: 11px !important;
    letter-spacing: 0.8px !important;
    text-transform: uppercase !important;
}
[data-testid="stMetricValue"] {
    color: #f1f5f9 !important;
    font-family: 'DM Mono', monospace !important;
}

/* ---- ALERT BOX HOVER ---- */
div[data-testid="stAlert"] {
    transition: transform 0.22s ease, box-shadow 0.22s ease !important;
    border-radius: 10px !important;
    cursor: default;
}
div[data-testid="stAlert"]:hover {
    transform: scale(1.02) !important;
    box-shadow: 0 8px 28px rgba(255,255,255,0.07) !important;
}

/* ---- PROGRESS BAR WRAPPER HOVER ---- */
.progress-wrap {
    transition: transform 0.22s ease;
    border-radius: 8px;
    padding: 6px 0;
}
.progress-wrap:hover {
    transform: scaleX(1.015);
    transform-origin: left;
}

/* Stray stProgress bar color */
.stProgress > div > div > div {
    border-radius: 4px !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_model():
    model  = pickle.load(open(r'D:\churn pred\churn_model.pkl', 'rb'))
    scaler = pickle.load(open(r'D:\churn pred\scaler.pkl', 'rb'))
    return model, scaler

model, scaler = load_model()

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown("### 📌 Navigation")
    st.divider()
    st.info("This AI model predicts whether a customer is likely to churn or stay based on their profile.")
    st.success("✅ Model Accuracy: 84%")
    st.divider()
    st.caption("Built with Machine Learning + Streamlit")

# ---------------- HEADER ----------------
st.markdown("""
<div style='display:flex;align-items:center;gap:16px;padding:1rem 0 1.5rem;border-bottom:1px solid #1e2a3a;margin-bottom:2rem;'>
    <div style='width:48px;height:48px;background:linear-gradient(135deg,#00e5a0,#0070f3);border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:22px;'>📊</div>
    <div>
        <div style='font-size:22px;font-weight:600;color:#f1f5f9;'>Customer Churn Prediction</div>
        <div style='font-size:13px;color:#64748b;margin-top:2px;'>ML-powered churn risk assessment · Telecom dataset</div>
    </div>
    <div style='margin-left:auto;background:#0d2a1a;border:1px solid rgba(0,229,160,0.4);color:#00e5a0;font-size:11px;font-family:monospace;padding:5px 12px;border-radius:6px;'>Accuracy: 84%</div>
</div>
""", unsafe_allow_html=True)

# ---------------- INPUTS ----------------
col1, col2 = st.columns(2)

with col1:
    st.markdown("<p style='color:#3b82f6;font-size:11px;font-weight:600;letter-spacing:1.2px;text-transform:uppercase;margin-bottom:8px;'>👤 Demographics</p>", unsafe_allow_html=True)
    gender     = st.selectbox("Gender", ["Male", "Female"])
    senior     = st.selectbox("Senior Citizen", [0, 1], format_func=lambda x: "Yes" if x else "No")
    partner    = st.selectbox("Partner", [0, 1], format_func=lambda x: "Yes" if x else "No")
    dependents = st.selectbox("Dependents", [0, 1], format_func=lambda x: "Yes" if x else "No")
    tenure     = st.number_input("Tenure (months)", min_value=0, max_value=100, value=12)

    st.markdown("<br><p style='color:#3b82f6;font-size:11px;font-weight:600;letter-spacing:1.2px;text-transform:uppercase;margin-bottom:8px;'>🔒 Add-ons</p>", unsafe_allow_html=True)
    device_protection = st.selectbox("Device Protection", [0, 1], format_func=lambda x: "Yes" if x else "No")
    tech_support      = st.selectbox("Tech Support", [0, 1], format_func=lambda x: "Yes" if x else "No")
    streaming_tv      = st.selectbox("Streaming TV", [0, 1], format_func=lambda x: "Yes" if x else "No")
    streaming_movies  = st.selectbox("Streaming Movies", [0, 1], format_func=lambda x: "Yes" if x else "No")

with col2:
    st.markdown("<p style='color:#3b82f6;font-size:11px;font-weight:600;letter-spacing:1.2px;text-transform:uppercase;margin-bottom:8px;'>📱 Services</p>", unsafe_allow_html=True)
    phone_service    = st.selectbox("Phone Service", [0, 1], format_func=lambda x: "Yes" if x else "No")
    multiple_lines   = st.selectbox("Multiple Lines", [0, 1], format_func=lambda x: "Yes" if x else "No")
    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber Optic", "No Internet"])
    online_security  = st.selectbox("Online Security", [0, 1], format_func=lambda x: "Yes" if x else "No")
    online_backup    = st.selectbox("Online Backup", [0, 1], format_func=lambda x: "Yes" if x else "No")

    st.markdown("<br><p style='color:#3b82f6;font-size:11px;font-weight:600;letter-spacing:1.2px;text-transform:uppercase;margin-bottom:8px;'>💳 Billing & Contract</p>", unsafe_allow_html=True)
    contract  = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
    paperless = st.selectbox("Paperless Billing", [0, 1], format_func=lambda x: "Yes" if x else "No")
    payment   = st.selectbox("Payment Method", [
        "Electronic check", "Mailed check",
        "Bank transfer (automatic)", "Credit card (automatic)"
    ])
    monthly = st.number_input("Monthly Charges ($)", min_value=0.0, value=70.0, step=0.01)
    total   = st.number_input("Total Charges ($)", min_value=0.0, value=1000.0, step=0.01)

# ---------------- PREDICT BUTTON ----------------
st.markdown("<br>", unsafe_allow_html=True)
predict_clicked = st.button("⚡  Predict Churn Risk")

# ---------------- PREDICTION ----------------
if predict_clicked:

    gender_val         = 1 if gender == "Male" else 0
    internet_fiber     = 1 if internet_service == "Fiber Optic" else 0
    internet_no        = 1 if internet_service == "No Internet" else 0
    contract_one       = 1 if contract == "One year" else 0
    contract_two       = 1 if contract == "Two year" else 0
    payment_credit     = 1 if "Credit card" in payment else 0
    payment_electronic = 1 if "Electronic" in payment else 0
    payment_mailed     = 1 if "Mailed" in payment else 0

    sample = np.zeros((1, 30))
    sample[0][0]  = gender_val
    sample[0][1]  = senior
    sample[0][2]  = partner
    sample[0][3]  = dependents
    sample[0][4]  = tenure
    sample[0][5]  = phone_service
    sample[0][6]  = paperless
    sample[0][7]  = monthly
    sample[0][8]  = total
    sample[0][9]  = multiple_lines
    sample[0][10] = internet_fiber
    sample[0][11] = internet_no
    sample[0][12] = online_security
    sample[0][13] = online_backup
    sample[0][14] = device_protection
    sample[0][15] = tech_support
    sample[0][16] = streaming_tv
    sample[0][17] = streaming_movies
    sample[0][18] = contract_one
    sample[0][19] = contract_two
    sample[0][20] = payment_credit
    sample[0][21] = payment_electronic
    sample[0][22] = payment_mailed

    sample_scaled = scaler.transform(sample)
    pred          = model.predict(sample_scaled)
    prob          = model.predict_proba(sample_scaled)
    churn_prob    = round(prob[0][1] * 100, 1)
    stay_prob     = round(prob[0][0] * 100, 1)
    is_churn      = pred[0] == 1

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<p style='color:#3b82f6;font-size:11px;font-weight:600;letter-spacing:1.2px;text-transform:uppercase;'>📌 Prediction Result</p>", unsafe_allow_html=True)

    # Alert box (has hover via CSS)
    if is_churn:
        st.error("⚠️  High Churn Risk — This customer is likely to leave the service.")
    else:
        st.success("✅  Low Churn Risk — This customer is likely to stay.")

    st.markdown("<br>", unsafe_allow_html=True)

    # Progress bars wrapped in hover div
    st.markdown(f"""
    <div class='progress-wrap'>
        <p style='color:#94a3b8;font-size:13px;margin-bottom:4px;'>
            🔴 Churn Probability &nbsp;&nbsp;
            <b style='color:#f87171;font-family:monospace;'>{churn_prob}%</b>
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.progress(int(churn_prob))

    st.markdown(f"""
    <div class='progress-wrap'>
        <p style='color:#94a3b8;font-size:13px;margin-bottom:4px;margin-top:8px;'>
            🟢 Retention Probability &nbsp;&nbsp;
            <b style='color:#34d399;font-family:monospace;'>{stay_prob}%</b>
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.progress(int(stay_prob))

    st.markdown("<br>", unsafe_allow_html=True)

    # Metric cards (hover via CSS on [data-testid="stMetric"])
    m1, m2, m3 = st.columns(3)
    m1.metric("🎯 Risk Score",      f"{churn_prob}%")
    m2.metric("💰 Monthly Charges", f"${monthly:.0f}")
    m3.metric("📅 Tenure",          f"{tenure} mo")
