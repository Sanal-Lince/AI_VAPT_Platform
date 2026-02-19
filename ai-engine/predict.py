import joblib

model = joblib.load("anomaly_model.pkl")

def predict_risk(features):
    result = model.predict([features])
    return "ANOMALY" if result[0]==-1 else "NORMAL"
