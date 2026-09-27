from xgboost import XGBClassifier
from catboost import CatBoostClassifier
from lightgbm import LGBMClassifier
import pandas as pd

train = pd.read_csv("adult_converted/adult_xgboost_train.csv")
test = pd.read_csv("adult_converted/adult_xgboost_test.csv")

X_train = train.drop(columns=["income"])
y_train = train["income"]
X_test = test.drop(columns=["income"])
y_test = test["income"]

model = XGBClassifier(
       n_estimators=500,
       max_depth=6,
       learning_rate=0.05,
       eval_metric="rmse",
)

model.fit(X_train, y_train)
print(model.score(X_test, y_test))