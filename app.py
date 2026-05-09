import streamlit as st
import pickle
import plotly.graph_objects as go
import pandas as pd
import os
from streamlit_lottie import st_lottie
import requests
from streamlit_option_menu import option_menu
from datetime import datetime
import pyrebase

firebaseConfig = {

    "apiKey": "AIzaSyCe5Nr685KG-ZpxadJVK1UVsRz0ws2d7HQ",

    "authDomain": "customer-churn-predictio-53a2f.firebaseapp.com",

    "projectId": "customer-churn-predictio-53a2f",

    "storageBucket": "customer-churn-predictio-53a2f.firebasestorage.app",

    "messagingSenderId": "755866665641",

    "appId": "1:755866665641:web:14f3d0c360f4680789dfb8",

    "databaseURL": ""

}

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()

# ------------------------------------------------------------------ #
#  PAGE CONFIG
# ------------------------------------------------------------------ #
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# ------------------------------------------------------------------ #
# LOGIN SYSTEM
# ------------------------------------------------------------------ #

# ------------------------------------------------------------------ #
# FIREBASE AUTH SYSTEM
# ------------------------------------------------------------------ #

if "user" not in st.session_state:
    st.session_state.user = None

if "email" not in st.session_state:
    st.session_state.email = None

if st.session_state.user is None:

    st.markdown(
        "<h1 style='text-align:center;'>🔐 Customer Churn AI</h1>",
        unsafe_allow_html=True
    )

    auth_mode = option_menu(
        None,
        ["Login", "Signup"],
        icons=["box-arrow-in-right", "person-plus"],
        orientation="horizontal"
    )

    email = ""
    password = ""
    
    login_method = st.radio(
    "Select Login Method",
    ["Email Login", "Mobile OTP"]
)

    if login_method == "Email Login":

        email = st.text_input("📧 Email")

        password = st.text_input(
            "🔑 Password",
            type="password"
        )

    else:

        st.markdown("### 📱 Mobile OTP Login")

        phone = st.text_input(
            "Enter Mobile Number",
            placeholder="enter here"
        )

        otp = st.text_input(
            "Enter OTP",
            placeholder="6 digit OTP"
        )

        col1, col2 = st.columns(2)

        with col1:

            if st.button("📩 Send OTP"):

                try:

                    response = requests.post(
                        "https://customer-churn-prediction-4-qh3a.onrender.com/send_otp",
                        json={"phone": phone}
                    )

                    data = response.json()

                    if data["success"]:

                        st.success("✅ OTP Sent Successfully")

                    else:

                        st.error(data["message"])

                except Exception as e:

                    st.error(f"Server Error: {e}")

        with col2:

            if st.button("✅ Verify OTP"):

                try:

                    response = requests.post(
                        "https://customer-churn-prediction-4-qh3a.onrender.com/verify_otp",
                        json={
                            "phone": phone,
                            "otp": otp
                        }
                    )

                    data = response.json()

                    if data["success"]:

                        st.session_state.user = phone

                        st.session_state.email = phone

                        st.success("✅ Login Successful")

                        st.rerun()

                    else:

                        st.error("❌ Invalid OTP")

                except Exception as e:

                    st.error(f"Server Error: {e}")
    # ---------------- SIGNUP ---------------- #

    st.markdown("---")

    st.markdown("### 📧 Email OTP Login")

    email_otp = st.text_input(
        "Enter Email",
        placeholder="example@gmail.com"
    )

    email_otp_code = st.text_input(
        "Enter Email OTP",
        placeholder="6 digit OTP"
    )

    ecol1, ecol2 = st.columns(2)

    with ecol1:

        if st.button("📩 Send Email OTP"):

            try:

                with st.spinner("Sending Email OTP..."):

                    response = requests.post(
                        "https://email-otp-churn-pred.onrender.com/send_email_otp",
                        json={"email": email_otp},
                        timeout=120
                    )

                    data = response.json()

                    if data.get("success"):

                        st.success("✅ Email OTP Sent Successfully")

                    else:

                        st.error(data.get("message", "Unknown Error"))

            except requests.exceptions.Timeout:

                st.error("⏳ Server took too long to respond. Try again.")

            except requests.exceptions.RequestException as e:

                st.error(f"🌐 Network Error: {e}")

            except Exception as e:

                st.error(f"❌ Server Error: {e}")

    with ecol2:

        if st.button("✅ Verify Email OTP"):

            try:

                with st.spinner("Verifying OTP..."):

                    response = requests.post(
                        "https://email-otp-churn-pred.onrender.com/verify_email_otp",
                        json={
                            "email": email_otp,
                            "otp": email_otp_code
                        },
                        timeout=30
                    )

                    data = response.json()

                    if data["success"]:

                        st.session_state.user = email_otp

                        st.session_state.email = email_otp

                        st.success("✅ Email Login Successful")

                        st.rerun()

                    else:

                        st.error("❌ Invalid Email OTP")

            except Exception as e:

                st.error(f"Server Error: {e}")

    if auth_mode == "Signup":

        if st.button("Create Account"):

            try:

                auth.create_user_with_email_and_password(
                    email,
                    password
                )

                st.success("✅ Account created successfully!")

            except Exception as e:
                st.error(f"❌ Signup failed: {e}")

    # ---------------- LOGIN ---------------- #

    if auth_mode == "Login":

        if st.button("Login"):

            try:

                user = auth.sign_in_with_email_and_password(
                    email,
                    password
                )

                st.session_state.user = user
                st.session_state.email = email

                st.success("✅ Login successful!")

                st.rerun()

            except Exception as e:
                st.error(f"❌ Login failed: {e}")

    st.stop()

# ------------------------------------------------------------------ #
#  SOCIAL LINKS
# ------------------------------------------------------------------ #
GITHUB_URL   = "https://github.com/Mohitcodebyte"
LINKEDIN_URL = "https://www.linkedin.com/in/mohitcodebyte"

GITHUB_SVG = """<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' width='22' height='22' fill='white'>
<path d='M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577
0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7
c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305
3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38
1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399
3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12
3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22
0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297
c0-6.627-5.373-12-12-12'/></svg>"""

LINKEDIN_SVG = """<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' width='22' height='22' fill='white'>
<path d='M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136
2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267
5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063
1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452z
M22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24
23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z'/></svg>"""

# ------------------------------------------------------------------ #
#  CSS
# ------------------------------------------------------------------ #
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600&family=DM+Mono:wght@400;500&display=swap');

.stApp { background:#060a10 !important; font-family:'Space Grotesk',sans-serif; }
#MainMenu, footer, header { visibility:hidden; }

[data-testid="stSidebar"] {
    background:#0c131d !important;
    border-right:1px solid #1a2535;
}

label, .stSelectbox label, .stNumberInput label {
    color:#94a3b8 !important; font-size:13px !important; font-weight:500 !important;
}

div[data-baseweb="select"] > div {
    background-color:#080e17 !important; border:1px solid #1e2d42 !important;
    border-radius:8px !important; color:#e2e8f0 !important;
}
div[data-baseweb="input"] > div {
    background-color:#080e17 !important; border:1px solid #1e2d42 !important;
    border-radius:8px !important;
}
div[data-baseweb="input"] input {
    color:#e2e8f0 !important; font-family:'DM Mono',monospace !important;
}

/* Predict button */
.stButton > button {
    background:linear-gradient(90deg,#00e5a0,#0070f3) !important;
    color:#000 !important; font-family:'Space Grotesk',sans-serif !important;
    font-size:15px !important; font-weight:700 !important;
    border:none !important; border-radius:10px !important;
    height:52px !important; width:100% !important;
    transition:transform .2s ease, box-shadow .2s ease !important;
}
.stButton > button:hover {
    transform:scale(1.03) !important;
    box-shadow:0 6px 24px rgba(0,229,160,.28) !important;
}

/* Download button */
[data-testid="stDownloadButton"] > button {
    background:#0c131d !important; color:#00e5a0 !important;
    border:1px solid rgba(0,229,160,.4) !important; border-radius:9px !important;
    font-family:'Space Grotesk',sans-serif !important; font-size:13px !important;
    font-weight:600 !important; padding:10px 20px !important;
    transition:transform .2s ease, box-shadow .2s ease !important;
}
[data-testid="stDownloadButton"] > button:hover {
    transform:scale(1.04) !important;
    box-shadow:0 6px 20px rgba(0,229,160,.2) !important;
}

/* Metric cards */
[data-testid="stMetric"] {
    background:#0c131d !important; border:1px solid #1a2535 !important;
    border-radius:10px !important; padding:14px 18px !important;
    transition:transform .22s ease, border-color .22s ease, box-shadow .22s ease !important;
}
[data-testid="stMetric"]:hover {
    transform:scale(1.06) !important; border-color:#3b82f6 !important;
    box-shadow:0 8px 28px rgba(59,130,246,.18) !important;
}
[data-testid="stMetricLabel"] p {
    color:#64748b !important; font-size:11px !important;
    letter-spacing:.8px !important; text-transform:uppercase !important;
}
[data-testid="stMetricValue"] {
    color:#f1f5f9 !important; font-family:'DM Mono',monospace !important;
}

/* Alert hover */
div[data-testid="stAlert"] {
    transition:transform .22s ease, box-shadow .22s ease !important;
    border-radius:10px !important;
}
div[data-testid="stAlert"]:hover {
    transform:scale(1.02) !important;
    box-shadow:0 8px 28px rgba(255,255,255,.07) !important;
}

/* Social buttons */
.social-btn {
    display:inline-flex; align-items:center; gap:10px;
    padding:10px 20px; border-radius:10px;
    text-decoration:none !important; cursor:pointer;
    font-family:'Space Grotesk',sans-serif; font-size:14px; font-weight:600;
    transition:transform .2s ease, box-shadow .2s ease;
}
.social-btn:hover { transform:scale(1.06); text-decoration:none !important; }
.github-btn {
    background:#161b22; color:#e2e8f0 !important;
    border:1px solid #30363d;
}
.github-btn:hover {
    background:#21262d;
    box-shadow:0 6px 22px rgba(255,255,255,.1);
}
.linkedin-btn {
    background:#0a66c2; color:#fff !important;
    border:1px solid #0a66c2;
}
.linkedin-btn:hover {
    background:#0958a8;
    box-shadow:0 6px 22px rgba(10,102,194,.4);
}

/* Sidebar social */
.sidebar-social {
    display:flex; flex-direction:column; gap:10px; margin-top:10px;
}
.sidebar-social .social-btn { justify-content:center; }
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------ #
#  LOAD MODEL
# ------------------------------------------------------------------ #
@st.cache_resource
def load_model():
    model  = pickle.load(open(r'churn_model.pkl', 'rb'))
    scaler = pickle.load(open(r'scaler.pkl', 'rb'))
    return model, scaler

model, scaler = load_model()

# ------------------------------------------------------------------ #
#  SIDEBAR
# ------------------------------------------------------------------ #
with st.sidebar:
    
    if st.button("🚪 Logout"):

        st.session_state.user = None
        st.session_state.email = None

        st.rerun()

    st.divider()

    st.markdown("### 📌 Navigation")

    st.divider()

    st.success(f"👤 Logged in as:\n{st.session_state.email}")

    st.info(
        "This AI model predicts whether a customer is likely to churn or stay based on their profile."
    )

    st.success("✅ Model Accuracy: 84%")

    st.divider()

    st.markdown("### 📊 Dashboard Features")

    st.markdown("""
    ✅ AI Churn Prediction  
    ✅ Firebase Authentication  
    ✅ Prediction History  
    ✅ Interactive Charts  
    ✅ Downloadable Reports  
    """)

    st.divider()

    st.markdown("**🔗 Connect with me**")

    st.markdown(f"""
    <div class='sidebar-social'>

        <a href='{GITHUB_URL}'
           target='_blank'
           class='social-btn github-btn'>

            {GITHUB_SVG}&nbsp; GitHub

        </a>

        <a href='{LINKEDIN_URL}'
           target='_blank'
           class='social-btn linkedin-btn'>

            {LINKEDIN_SVG}&nbsp; LinkedIn

        </a>

    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.caption("🚀 Built with Machine Learning + Firebase + Streamlit")   

# ------------------------------------------------------------------ #
#  HEADER
# ------------------------------------------------------------------ #
st.markdown("""
<div style='display:flex;align-items:center;gap:16px;padding:1rem 0 1.2rem;
            border-bottom:1px solid #1e2a3a;margin-bottom:1.2rem;'>
    <div style='width:48px;height:48px;background:linear-gradient(135deg,#00e5a0,#0070f3);
                border-radius:12px;display:flex;align-items:center;
                justify-content:center;font-size:22px;'>📊</div>
    <div>
        <div style='font-size:22px;font-weight:600;color:#f1f5f9;'>Customer Churn Prediction</div>
        <div style='font-size:13px;color:#64748b;margin-top:2px;'>
            ML-powered churn risk assessment · Telecom dataset
        </div>
    </div>
    <div style='margin-left:auto;background:#0d2a1a;border:1px solid rgba(0,229,160,.4);
                color:#00e5a0;font-size:11px;font-family:monospace;
                padding:5px 12px;border-radius:6px;'>Accuracy: 84%</div>
</div>
""", unsafe_allow_html=True)

def load_lottie(url):

    r = requests.get(url)

    if r.status_code != 200:
        return None

    return r.json()

lottie_ai = load_lottie(
    "https://assets5.lottiefiles.com/packages/lf20_49rdyysj.json"
)

if lottie_ai:

    st_lottie(
        lottie_ai,
        height=220,
        key="ai"
    )

else:

    st.info("🤖 AI Dashboard Loaded Successfully")

# Social buttons below header
st.markdown(f"""
<div style='display:flex;gap:12px;flex-wrap:wrap;margin-bottom:1.8rem;'>
    <a href='{GITHUB_URL}' target='_blank' class='social-btn github-btn'>
        {GITHUB_SVG}&nbsp; GitHub Profile
    </a>
    <a href='{LINKEDIN_URL}' target='_blank' class='social-btn linkedin-btn'>
        {LINKEDIN_SVG}&nbsp; LinkedIn Profile
    </a>
</div>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------ #
#  INPUTS
# ------------------------------------------------------------------ #
col1, col2 = st.columns(2)

with col1:
    st.markdown("<p style='color:#3b82f6;font-size:11px;font-weight:600;letter-spacing:1.2px;text-transform:uppercase;margin-bottom:8px;'>👤 Demographics</p>", unsafe_allow_html=True)
    gender     = st.selectbox("Gender", ["Male", "Female"])
    senior     = st.selectbox("Senior Citizen", [0, 1], format_func=lambda x: "Yes" if x else "No")
    partner    = st.selectbox("Partner",    [0, 1], format_func=lambda x: "Yes" if x else "No")
    dependents = st.selectbox("Dependents", [0, 1], format_func=lambda x: "Yes" if x else "No")
    tenure     = st.number_input("Tenure (months)", min_value=0, max_value=100, value=12)

    st.markdown("<br><p style='color:#3b82f6;font-size:11px;font-weight:600;letter-spacing:1.2px;text-transform:uppercase;margin-bottom:8px;'>🔒 Add-ons</p>", unsafe_allow_html=True)
    device_protection = st.selectbox("Device Protection", [0,1], format_func=lambda x:"Yes" if x else "No")
    tech_support      = st.selectbox("Tech Support",      [0,1], format_func=lambda x:"Yes" if x else "No")
    streaming_tv      = st.selectbox("Streaming TV",      [0,1], format_func=lambda x:"Yes" if x else "No")
    streaming_movies  = st.selectbox("Streaming Movies",  [0,1], format_func=lambda x:"Yes" if x else "No")

with col2:
    st.markdown("<p style='color:#3b82f6;font-size:11px;font-weight:600;letter-spacing:1.2px;text-transform:uppercase;margin-bottom:8px;'>📱 Services</p>", unsafe_allow_html=True)
    phone_service    = st.selectbox("Phone Service",    [0,1], format_func=lambda x:"Yes" if x else "No")
    multiple_lines   = st.selectbox("Multiple Lines",   [0,1], format_func=lambda x:"Yes" if x else "No")
    internet_service = st.selectbox("Internet Service", ["DSL","Fiber Optic","No Internet"])
    online_security  = st.selectbox("Online Security",  [0,1], format_func=lambda x:"Yes" if x else "No")
    online_backup    = st.selectbox("Online Backup",    [0,1], format_func=lambda x:"Yes" if x else "No")

    st.markdown("<br><p style='color:#3b82f6;font-size:11px;font-weight:600;letter-spacing:1.2px;text-transform:uppercase;margin-bottom:8px;'>💳 Billing & Contract</p>", unsafe_allow_html=True)
    contract  = st.selectbox("Contract Type",    ["Month-to-month","One year","Two year"])
    paperless = st.selectbox("Paperless Billing",[0,1], format_func=lambda x:"Yes" if x else "No")
    payment   = st.selectbox("Payment Method", [
        "Electronic check","Mailed check",
        "Bank transfer (automatic)","Credit card (automatic)"
    ])
    monthly = st.number_input("Monthly Charges ($)", min_value=0.0, value=70.0, step=0.01)
    total   = st.number_input("Total Charges ($)",   min_value=0.0, value=1000.0, step=0.01)

# ------------------------------------------------------------------ #
#  PREDICT BUTTON
# ------------------------------------------------------------------ #
st.markdown("<br>", unsafe_allow_html=True)
predict_clicked = st.button("⚡  Predict Churn Risk")

# ------------------------------------------------------------------ #
#  PREDICTION
# ------------------------------------------------------------------ #
if predict_clicked:

    gender_val         = 1 if gender == "Male" else 0
    internet_fiber     = 1 if internet_service == "Fiber Optic" else 0
    internet_no        = 1 if internet_service == "No Internet" else 0
    contract_one       = 1 if contract == "One year"            else 0
    contract_two       = 1 if contract == "Two year"            else 0
    payment_credit     = 1 if "Credit card" in payment          else 0
    payment_electronic = 1 if "Electronic"  in payment          else 0
    payment_mailed     = 1 if "Mailed"      in payment          else 0

    input_data = pd.DataFrame({

        'gender': [gender_val],

        'SeniorCitizen': [senior],

        'Partner': [partner],

        'Dependents': [dependents],

        'tenure': [tenure],

        'PhoneService': [phone_service],

        'PaperlessBilling': [paperless],

        'MonthlyCharges': [monthly],

        'TotalCharges': [total],

        'MultipleLines_No phone service': [0],

        'MultipleLines_Yes': [multiple_lines],

        'InternetService_Fiber optic':
            [1 if internet_service == "Fiber Optic" else 0],

        'InternetService_No':
            [1 if internet_service == "No Internet" else 0],

        'OnlineSecurity_No internet service':
            [1 if internet_service == "No Internet" else 0],

        'OnlineSecurity_Yes':
            [online_security],

        'OnlineBackup_No internet service':
            [1 if internet_service == "No Internet" else 0],

        'OnlineBackup_Yes':
            [online_backup],

        'DeviceProtection_No internet service':
            [1 if internet_service == "No Internet" else 0],

        'DeviceProtection_Yes':
            [device_protection],

        'TechSupport_No internet service':
            [1 if internet_service == "No Internet" else 0],

        'TechSupport_Yes':
            [tech_support],

        'StreamingTV_No internet service':
            [1 if internet_service == "No Internet" else 0],

        'StreamingTV_Yes':
            [streaming_tv],

        'StreamingMovies_No internet service':
            [1 if internet_service == "No Internet" else 0],

        'StreamingMovies_Yes':
            [streaming_movies],

        'Contract_One year':
            [1 if contract == "One year" else 0],

        'Contract_Two year':
            [1 if contract == "Two year" else 0],

        'PaymentMethod_Credit card (automatic)':
            [1 if payment == "Credit card (automatic)" else 0],

        'PaymentMethod_Electronic check':
            [1 if payment == "Electronic check" else 0],

        'PaymentMethod_Mailed check':
            [1 if payment == "Mailed check" else 0]

    })

    with st.spinner("🤖 AI model is processing telecom customer patterns..."):

        sample_scaled = scaler.transform(input_data)

        pred = model.predict(sample_scaled)

        prob = model.predict_proba(sample_scaled)

        churn_prob = round(prob[0][1] * 100, 1)

        stay_prob = round(prob[0][0] * 100, 1)

        is_churn = pred[0] == 1

    # ---------- Result Badge ----------
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<p style='color:#3b82f6;font-size:11px;font-weight:600;letter-spacing:1.2px;text-transform:uppercase;'>📌 Prediction Result</p>", unsafe_allow_html=True)

    if is_churn:

        st.error(
            "⚠️  High Churn Risk — This customer is likely to leave the service."
        )

    else:

        st.success(
            "✅  Low Churn Risk — This customer is likely to stay."
        )

    # ---------- Risk Level Badge ----------

    risk_level = (
        "🔴 High Risk" if churn_prob >= 70
        else "🟠 Medium Risk" if churn_prob >= 40
        else "🟢 Low Risk"
    )

    st.info(f"Risk Level: {risk_level}")

    st.markdown("<br>", unsafe_allow_html=True)

    # ---------- Progress Bars ----------
    st.markdown(f"<p style='color:#94a3b8;font-size:13px;margin-bottom:4px;'>🔴 Churn Probability &nbsp;<b style='color:#f87171;font-family:monospace;'>{churn_prob}%</b></p>", unsafe_allow_html=True)
    st.progress(int(churn_prob))
    st.markdown(f"<p style='color:#94a3b8;font-size:13px;margin-bottom:4px;margin-top:8px;'>🟢 Retention Probability &nbsp;<b style='color:#34d399;font-family:monospace;'>{stay_prob}%</b></p>", unsafe_allow_html=True)
    st.progress(int(stay_prob))

    st.markdown("<br>", unsafe_allow_html=True)

    # ---------- Charts ----------
    CARD_BG      = "#0c131d"
    TEXT_COL     = "#94a3b8"
    FONT_FAM     = "Space Grotesk, sans-serif"
    needle_color = "#f87171" if is_churn else "#34d399"

    chart_col1, chart_col2 = st.columns(2)

    # Gauge Chart
    with chart_col1:
        gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=churn_prob,
            number={'font':{'size':42,'color':needle_color,'family':FONT_FAM},'suffix':'%'},
            title={'text':"Churn Risk Score",'font':{'size':14,'color':TEXT_COL,'family':FONT_FAM}},
            gauge={
                'axis':{'range':[0,100],'tickwidth':1,'tickcolor':'#1a2535',
                        'tickfont':{'color':TEXT_COL,'size':11,'family':FONT_FAM}},
                'bar':{'color':needle_color,'thickness':0.25},
                'bgcolor':CARD_BG,'borderwidth':0,
                'steps':[
                    {'range':[0,40],  'color':'#052e16'},
                    {'range':[40,70], 'color':'#2d2000'},
                    {'range':[70,100],'color':'#2a0f0f'},
                ],
                'threshold':{'line':{'color':needle_color,'width':3},'thickness':0.8,'value':churn_prob}
            }
        ))
        gauge.update_layout(
            paper_bgcolor=CARD_BG, plot_bgcolor=CARD_BG,
            font={'family':FONT_FAM}, margin=dict(t=60,b=20,l=30,r=30), height=280
        )
        st.plotly_chart(gauge, use_container_width=True, config={'displayModeBar':False})

    # Donut Chart
    with chart_col2:
        pie_fig = go.Figure(go.Pie(
            labels=["Churn","Stay"],
            values=[churn_prob, stay_prob],
            hole=0.62,
            marker=dict(colors=["#ef4444","#22c55e"], line=dict(color=CARD_BG, width=3)),
            textinfo='label+percent',
            textfont=dict(size=13, color="#e2e8f0", family=FONT_FAM),
            hovertemplate="<b>%{label}</b><br>%{value}%<extra></extra>"
        ))
        pie_fig.update_layout(
            paper_bgcolor=CARD_BG, plot_bgcolor=CARD_BG,
            font={'family':FONT_FAM,'color':'#e2e8f0'},
            legend=dict(font=dict(color='#94a3b8',size=12),bgcolor='rgba(0,0,0,0)'),
            margin=dict(t=30,b=20,l=20,r=20), height=280,
            annotations=[dict(
                text=f"<b>{churn_prob}%</b>",
                x=0.5, y=0.5, font_size=22,
                font_color=needle_color, font_family=FONT_FAM, showarrow=False
            )]
        )
        st.plotly_chart(pie_fig, use_container_width=True, config={'displayModeBar':False})

    # ---------- Confidence Explanation ----------

    st.markdown("<br>", unsafe_allow_html=True)

    if churn_prob >= 80:
        st.error("🚨 Customer shows extremely strong churn behavior patterns.")

    elif churn_prob >= 60:
        st.warning("⚠️ Customer has moderate churn risk indicators.")

    elif churn_prob >= 40:
        st.info("📊 Customer has balanced retention/churn behavior.")

    else:
        st.success("💚 Customer retention probability is very high.")

    # ---------- Metric Cards ----------
    st.markdown("<br>", unsafe_allow_html=True)
    m1, m2, m3 = st.columns(3)
    m1.metric("🎯 Risk Score",      f"{churn_prob}%")
    m2.metric("💰 Monthly Charges", f"${monthly:.0f}")
    m3.metric("📅 Tenure",          f"{tenure} mo")

# ---------- Download Report ----------
    st.markdown("<br>", unsafe_allow_html=True)
    report = f"""CUSTOMER CHURN REPORT
    {'='*40}
    Prediction      : {'HIGH CHURN RISK' if is_churn else 'LIKELY TO STAY'}
    Churn Prob      : {churn_prob}%
    Retention Prob  : {stay_prob}%

    --- Customer Details ---
    Gender          : {gender}
    Senior Citizen  : {'Yes' if senior else 'No'}
    Partner         : {'Yes' if partner else 'No'}
    Dependents      : {'Yes' if dependents else 'No'}
    Tenure          : {tenure} months
    Internet Svc    : {internet_service}
    Contract        : {contract}
    Monthly Charges : ${monthly}
    Total Charges   : ${total}
    Payment Method  : {payment}
    {'='*40}
    """
    # ---------- Save Prediction History ----------

    # ---------- USER-WISE PREDICTION HISTORY ----------

    user_email = st.session_state.email

    safe_email = user_email.replace("@", "_").replace(".", "_")

    history_file = f"{safe_email}_history.csv"

    history_data = pd.DataFrame([{

        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

        "User": user_email,

        "Gender": gender,

        "SeniorCitizen": senior,

        "Tenure": tenure,

        "MonthlyCharges": monthly,

        "TotalCharges": total,

        "ChurnProbability": churn_prob,

        "Prediction": "Churn" if is_churn else "Stay"

    }])

    if os.path.exists(history_file):

        history_data.to_csv(
            history_file,
            mode='a',
            header=False,
            index=False
        )

    else:

        history_data.to_csv(
            history_file,
            index=False
        )

    # ---------- Download Report ----------

    st.download_button(
        label="📄 Download Report",
        data=report,
        file_name="churn_report.txt",
        mime="text/plain"
    )


    # ---------- Prediction History ----------

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <p style='color:#3b82f6;
    font-size:11px;
    font-weight:600;
    letter-spacing:1.2px;
    text-transform:uppercase;'>
    🗂 Prediction History
    </p>
    """, unsafe_allow_html=True)

    history_df = pd.read_csv(history_file)

    st.dataframe(
        history_df.tail(10),
        use_container_width=True
    )

    # ---------- Download Full CSV ----------

    csv = history_df.to_csv(index=False).encode('utf-8')

    st.download_button(
        "📥 Download Full History CSV",
        csv,
        f"{safe_email}_prediction_history.csv",
        "text/csv"
    )
    # ---------- Feature Importance ----------

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <p style='color:#3b82f6;
    font-size:11px;
    font-weight:600;
    letter-spacing:1.2px;
    text-transform:uppercase;'>
    📈 Feature Importance
    </p>
    """, unsafe_allow_html=True)

    feature_df = pd.DataFrame({
        "Feature": [
            "Contract",
            "MonthlyCharges",
            "Tenure",
            "TechSupport",
            "InternetService",
            "PaymentMethod"
        ],
        "Importance": [0.29, 0.22, 0.19, 0.14, 0.11, 0.05]
    })

    feature_chart = go.Figure()

    feature_chart.add_trace(go.Bar(
        x=feature_df["Importance"],
        y=feature_df["Feature"],
        orientation='h',
        text=feature_df["Importance"],
        textposition='outside'
    ))

    feature_chart.update_layout(
        paper_bgcolor="#0c131d",
        plot_bgcolor="#0c131d",
        font=dict(color="#e2e8f0"),
        height=350
    )

    st.plotly_chart(
        feature_chart,
        use_container_width=True,
        config={'displayModeBar':False}
    )
    
    # ---------- Footer Branding ----------

    st.markdown("""

    <hr style='border:1px solid #1a2535;'>

    <div style='text-align:center;
                color:#64748b;
                font-size:13px;
                padding:10px;'>

    Built with ❤️ using Machine Learning, Firebase & Streamlit

    </div>

    """, unsafe_allow_html=True)