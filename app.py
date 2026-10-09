from flask import Flask, render_template, session, redirect, jsonify
import os
import json
from firebase_admin import credentials, firestore, initialize_app

app = Flask(__name__)

# Initialize Firestore DB
credentials = credentials.Certificate(
    "swiper-33762-firebase-adminsdk-hvnpd-4edacf361e.json"
)
firbase_app = initialize_app(credentials)
db = firestore.client()

# datatypes
db_accounts = db.collection("account")
db_chats = db.collection("chats")


@app.route("/", methods=["GET", "POST"])
def index():
    try:
        _id = "3"

        db_accounts.document(_id).set(
            {"email": "mail@gmail.com", "username": "lakshya", "password": "lakshya121", "profile_picture":"profilepic.link"}
        )
        # db_chats.document(_id).set(
        #     {"id":1,"sender":"username_1","reciver":"username_2", "message":"this is a test message", "datetime":"01/02/2023"}
        # )
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occurred: {e}"

    # if session and session['logdin']:
    #     return redirect('/dashboard')
    # else:
    #     return redirect('/signin')
    return render_template("index.html")


@app.route("/signin", methods=["GET", "POST"])
def SignIn():
    return render_template("sign-in.html")


@app.route("/signup", methods=["GET", "POST"])
def SignUp():
    return render_template("sign-up.html")


@app.route("/dashboard", methods=["GET", "POST"])
def Dashboard():
    # if session and session["logdin"]:
        return render_template("chat.html")

    # return redirect("/")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
