from flask import Flask, render_template, request, jsonify

from src.predict import predict_churn


app = Flask(__name__)


# =========================================================
# HOME / CUSTOMER PREDICTION PAGE
# =========================================================

@app.route("/")
def home():
    return render_template("index.html")


# =========================================================
# ANALYTICS DASHBOARD
# =========================================================

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# =========================================================
# DETAILED PREDICTION REPORT
# =========================================================

@app.route("/result")
def result():
    return render_template("result.html")


# =========================================================
# CUSTOMER CHURN PREDICTION
# =========================================================

@app.route("/predict", methods=["POST"])
def predict():

    data = request.form.to_dict()

    try:

        # -------------------------------------------------
        # Convert numeric fields to correct data types
        # -------------------------------------------------

        data["Tenure"] = float(
            data["Tenure"]
        )

        data["WarehouseToHome"] = float(
            data["WarehouseToHome"]
        )

        data["NumberOfDeviceRegistered"] = int(
            data["NumberOfDeviceRegistered"]
        )

        data["SatisfactionScore"] = int(
            data["SatisfactionScore"]
        )

        data["NumberOfAddress"] = int(
            data["NumberOfAddress"]
        )

        data["Complain"] = int(
            data["Complain"]
        )

        data["DaySinceLastOrder"] = float(
            data["DaySinceLastOrder"]
        )

        data["CashbackAmount"] = float(
            data["CashbackAmount"]
        )


        # -------------------------------------------------
        # Make prediction using trained XGBoost model
        # -------------------------------------------------

        prediction, probability = predict_churn(data)


        # -------------------------------------------------
        # Convert prediction to readable text
        # -------------------------------------------------

        result = (
            "Likely to Churn"
            if prediction == 1
            else "Not Likely to Churn"
        )


        # -------------------------------------------------
        # Return JSON response to JavaScript
        # -------------------------------------------------

        return jsonify({

            "prediction": int(prediction),

            "result": result,

            "probability": round(
                probability * 100,
                2
            )

        })


    except Exception as e:

        # -------------------------------------------------
        # Return error as JSON
        # -------------------------------------------------

        return jsonify({

            "error": str(e)

        }), 400


# =========================================================
# RUN FLASK APPLICATION
# =========================================================

if __name__ == "__main__":

    app.run(
        debug=True
    )