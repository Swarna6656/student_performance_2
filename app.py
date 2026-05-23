from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle
import sys

app = Flask(__name__)

# Load model
try:
    model = pickle.load(open("Model.pkl", "rb"))
    print("Model loaded successfully")

except Exception as e:
    er_type, er_msg, er_line = sys.exc_info()
    print(f"Error loading model: Line {er_line.tb_lineno} : {er_type} : {er_msg}")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get input from form
        hours_studied = float(request.form["hours_studied"])
        previous_scores = float(request.form["previous_scores"])
        sleep_hours = float(request.form["sleep_hours"])
        sample_papers = float(request.form["sample_papers"])

        # ✅ FIXED: use DataFrame instead of numpy array (removes warning)
        features = pd.DataFrame([[
            hours_studied,
            previous_scores,
            sleep_hours,
            sample_papers
        ]], columns=[
            "Hours Studied",
            "Previous Scores",
            "Sleep Hours",
            "Sample Question Papers Practiced"
        ])

        # Prediction
        prediction = model.predict(features)[0]

        return render_template(
            "index.html",
            prediction_text=f"Performance Index: {prediction:.2f}"
        )

    except Exception as e:
        er_type, er_msg, er_line = sys.exc_info()
        return render_template(
            "index.html",
            prediction_text=f"Error in Line {er_line.tb_lineno}: {er_msg}"
        )


if __name__ == "__main__":
    app.run(debug=True)