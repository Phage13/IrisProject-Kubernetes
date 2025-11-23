from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load("model.pkl")

@app.route("/healthz")
def healthz():
    return jsonify({"status": "ok"})

@app.route("/predict", methods=["POST"])
def predict():
    payload = request.get_json(force=True)
    df = pd.DataFrame([payload], columns=["sepal_length","sepal_width","petal_length","petal_width"])
    preds = model.predict(df)
    label_map = {0:"Iris-setosa",1:"Iris-versicolor",2:"Iris-virginica"}
    return jsonify({"prediction": label_map[int(preds[0])]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
