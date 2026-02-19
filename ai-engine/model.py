import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

data = pd.read_csv("training_data.csv")

model = IsolationForest(contamination=0.02)
model.fit(data)

joblib.dump(model,"anomaly_model.pkl")
print("AI model trained")
