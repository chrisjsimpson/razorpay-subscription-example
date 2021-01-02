from flask import Flask, render_template, request, redirect
from dotenv import load_dotenv
import os
import requests
from requests.auth import HTTPBasicAuth
import logging

load_dotenv()

logging.basicConfig(level=os.getenv("PYTHON_LOGLEVEL", "WARNING"))

app = Flask(__name__)

RAZOR_ENDPOINT_URL = os.getenv("RAZOR_ENDPOINT_URL")
RAZOR_PUBLIC_API_KEY = os.getenv("RAZOR_PUBLIC_API_KEY")
RAZOR_SECRET_API_KEY = os.getenv("RAZOR_SECRET_API_KEY")
RAZOR_PLAN_ID = os.getenv("RAZOR_PLAN_ID")


@app.route("/", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        """Take to checkout if entered email"""
        email = request.form.get("email", None)
        razor_subscription_object = create_subscription(email=email)

        # Redirect the user to Razor checkout
        return redirect(razor_subscription_object["short_url"])
    return render_template("sign_up.html")


def create_subscription(email=None):
    """Create a subscription object

    Returns: Json object of subscription object.
             See https://razorpay.com/docs/api/subscriptions/#create-a-subscription   # noqa: E501
             short_url, URL that can be used to make the
             authorization payment.
    """
    url = RAZOR_ENDPOINT_URL + "subscriptions"
    req = requests.post(
        url,
        auth=HTTPBasicAuth(RAZOR_PUBLIC_API_KEY, RAZOR_SECRET_API_KEY),
        json={
            "plan_id": RAZOR_PLAN_ID,
            "total_count": 12,
            "quantity": 1,
            "customer_notify": 1,
            "addons": [],
            "notes": {
                "email": email,
            },
        },
    )
    return req.json()
