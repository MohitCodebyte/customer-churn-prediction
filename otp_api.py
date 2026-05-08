from flask import Flask, request, jsonify
from flask_cors import CORS
from twilio.rest import Client
import os

app = Flask(__name__)

CORS(app)

# -----------------------------
# TWILIO CONFIG
# -----------------------------

import os

account_sid = os.environ.get("AC51bb9b8b4a18e36cd00ac2535e93799e")

auth_token = os.environ.get("22543ec70cecd32e778dd41ac236e597")

verify_service_sid = os.environ.get("VA887236c8f24673ab9d390ea8e4ac153f")

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