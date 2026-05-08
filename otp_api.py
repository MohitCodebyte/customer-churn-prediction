from flask import Flask, request, jsonify
from flask_cors import CORS
from twilio.rest import Client
import os

app = Flask(__name__)

CORS(app)

# -----------------------------
# TWILIO CONFIG
# -----------------------------

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")

auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

verify_service_sid = os.environ.get("VERIFY_SERVICE_SID")

client = Client(account_sid, auth_token)

# -----------------------------
# SEND OTP
# -----------------------------

@app.route("/send_otp", methods=["POST"])
def send_otp():

    data = request.get_json()

    phone = data.get("phone")

    if not phone:

        return jsonify({
            "success": False,
            "message": "Phone number required"
        })

    phone = "+91" + phone

    try:

        verification = client.verify \
            .v2 \
            .services(verify_service_sid) \
            .verifications \
            .create(
                to=phone,
                channel="sms",
            )
        print("Verification Status:", verification.status)

        return jsonify({
            "success": True,
            "message": "OTP Sent Successfully"
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        })


# -----------------------------
# VERIFY OTP
# -----------------------------

@app.route("/verify_otp", methods=["POST"])
def verify_otp():

    data = request.get_json()

    phone = "+91" + data.get("phone")

    otp = data.get("otp")

    try:

        verification_check = client.verify \
            .v2 \
            .services(verify_service_sid) \
            .verification_checks \
            .create(
                to=phone,
                code=otp
            )

        if verification_check.status == "approved":

            return jsonify({
                "success": True,
                "message": "OTP Verified Successfully"
            })

        else:

            return jsonify({
                "success": False,
                "message": "Invalid OTP"
            })

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
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