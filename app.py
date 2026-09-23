from flask import Flask, render_template, request, jsonify

from src.predict import predict_churn


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    data = request.form.to_dict()

    try:
        # Convert numeric fields from strings to appropriate types
        data["Tenure"] = float(data["Tenure"])
        data["WarehouseToHome"] = float(data["WarehouseToHome"])
        data["NumberOfDeviceRegistered"] = int(data["NumberOfDeviceRegistered"])
        data["SatisfactionScore"] = int(data["SatisfactionScore"])
        data["NumberOfAddress"] = int(data["NumberOfAddress"])
        data["Complain"] = int(data["Complain"])
        data["DaySinceLastOrder"] = float(data["DaySinceLastOrder"])
        data["CashbackAmount"] = float(data["CashbackAmount"])

        prediction, probability = predict_churn(data)

        result = "Likely to Churn" if prediction == 1 else "Not Likely to Churn"

        return jsonify({
            "prediction": int(prediction),
            "result": result,
            "probability": round(probability * 100, 2)
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 400


if __name__ == "__main__":
    app.run(debug=True)