from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

app = Flask(__name__)

CORS(app)

# -----------------------------
# EMAIL CONFIG
# -----------------------------

EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")

EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")

# -----------------------------
# STORE OTP
# -----------------------------

otp_storage = {}

# -----------------------------
# SEND OTP
# -----------------------------

# Render cold start ke liye ping endpoint
@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"status": "awake", "message": "Server is running"})

@app.route("/send_email_otp", methods=["POST"])
def send_email_otp():

    data = request.get_json()

    email = data.get("email")

    if not email:

        return jsonify({
            "success": False,
            "message": "Email required"
        })

    otp = str(random.randint(100000, 999999))

    otp_storage[email] = otp

    try:

        msg = MIMEMultipart()

        msg["From"] = "Mitansh <kushwahmitansh@gmail.com>"

        msg["To"] = email

        msg["Subject"] = "Your OTP Code"

        body = f"Your OTP is: {otp}"

        msg.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP("smtp-relay.brevo.com", 587, timeout=10)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        
        

        return jsonify({
            "success": True,
            "message": "OTP sent successfully"
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        })

# -----------------------------
# VERIFY OTP
# -----------------------------

@app.route("/verify_email_otp", methods=["POST"])
def verify_email_otp():

    data = request.get_json()

    email = data.get("email")

    otp = data.get("otp")

    saved_otp = otp_storage.get(email)

    if saved_otp == otp:

        return jsonify({
            "success": True,
            "message": "OTP verified"
        })

    else:

        return jsonify({
            "success": False,
            "message": "Invalid OTP"
        })

# -----------------------------
# RUN SERVER
# -----------------------------

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port
    )