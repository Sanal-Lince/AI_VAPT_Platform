import pandas as pd
from ai_engine.model import *

data=pd.read_csv("client_data.csv")
data=data.dropna()
print("training...")
