from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model safely
model = joblib.load('CellPricePrediction.pkl')

@app.route("/",methods=['GET'])
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def dopredict():
        # Collect inputs
        ram = int(request.form["ram"])
        battery_power = int(request.form["battery_power"])
        px_height = int(request.form["px_height"])
        px_width = int(request.form["px_width"])
        three_g = int(request.form["three_g"])  # 0 or 1
        four_g = int(request.form["four_g"])    # 0 or 1

        # Build feature vector (order should match training)
        features = ([[ram, battery_power, px_height, px_width, three_g, four_g]])

        # Make prediction
        prediction = model.predict(features)[0]
        prediction = int(prediction)  # fix numpy.int64 issue

        # Map to label
        price_ranges = {
            0: "Low Cost",
            1: "Medium Cost",
            2: "High Cost", 
            3: "Very High Cost"
        }

        result = price_ranges.get(prediction, "Unknown")
        return render_template("index.html", prediction_text=f"Predicted Price Range: {result}",predict = prediction)
    
    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
