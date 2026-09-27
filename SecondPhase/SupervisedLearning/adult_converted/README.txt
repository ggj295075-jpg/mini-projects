Adult Census dataset — converted for CatBoost and XGBoost

Files:
- adult_catboost_train.csv : 32,561 rows, categorical columns kept as text
- adult_catboost_test.csv  : 16,281 rows, categorical columns kept as text
- adult_xgboost_train.csv  : 32,561 rows, categorical columns one-hot encoded
- adult_xgboost_test.csv   : 16,281 rows, same numeric feature columns as train
- xgboost_feature_names.csv: feature names after one-hot encoding

Target:
- income = 0 for <=50K
- income = 1 for >50K

Missing categorical values:
- '?' was converted to 'Unknown' (important for CatBoost)

CatBoost example:
    from catboost import CatBoostClassifier
    import pandas as pd

    train = pd.read_csv("adult_catboost_train.csv")
    test = pd.read_csv("adult_catboost_test.csv")

    X_train = train.drop(columns=["income"])
    y_train = train["income"]
    X_test = test.drop(columns=["income"])
    y_test = test["income"]

    cat_cols = [
        "workclass", "education", "marital_status", "occupation",
        "relationship", "race", "sex", "native_country"
    ]

    model = CatBoostClassifier(
        iterations=500,
        depth=6,
        learning_rate=0.05,
        verbose=False
    )
    model.fit(X_train, y_train, cat_features=cat_cols)
    pred = model.predict(X_test)

XGBoost example:
    from xgboost import XGBClassifier
    import pandas as pd

    train = pd.read_csv("adult_xgboost_train.csv")
    test = pd.read_csv("adult_xgboost_test.csv")

    X_train = train.drop(columns=["income"])
    y_train = train["income"]
    X_test = test.drop(columns=["income"])
    y_test = test["income"]

    model = XGBClassifier(
        n_estimators=300,
        max_depth=6,
        learning_rate=0.05,
        eval_metric="logloss"
    )
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
