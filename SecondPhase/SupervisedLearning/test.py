import pandas as pd
from lightgbm import LGBMClassifier
from xgboost import XGBClassifier

train = pd.read_csv("Datasets/train_shuttle.csv")
print(train.head())
