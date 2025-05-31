
This section explains how the baseline model was built. It is a simple XGBoost model
with default hyperparameters. Even though it is not optimized, and hyperparameter 
tuning is an essential step in the machine learning pipeline, it is a good starting 
point. Also, with some metrics obtained by this model, one can keep track of the 
improvement of the model after hyperparameter tuning and feature engineering. 

The first step is to load the data from the database. For this project, the data 
was loaded as follows: 

```python
import pandas as pd 
import sqlite3 

conn = sqlite3.connect("german_credit.db")

extract_query = """
SELECT * FROM credit;
"""
data = pd.read_sql_query(extract_query, conn)
x = data.drop(columns=["Target"])
for col in x.select_dtypes(include="object").columns:
    x[col] = x[col].astype("category")
y = data["Target"]
```

Now, `x` is a DataFrame containing all the examples and features, and `y` contains 
the target variable for each example. 

For the baseline model, the `XGBoostClassifier` from the `xgboost` library was used. 
This model does not require any preprocessing of the data, as it can handle both 
numerical and categorical features. The model was trained with the default hyperparameters, 
using a cross-validation strategy to evaluate via `StratifiedKFold` with 5 folds.

```python 
from sklearn.metrics import accuracy_score, recall_score, f1_score, roc_auc_score
from sklearn.model_selection import StratifiedKFold
import xgboost as xgb

model = xgb.XGBClassifier(
    objective="binary:logistic",
    eval_metric="logloss",
    enable_categorical=True,
    random_state=42
)

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
acc_scores, recall_scores, f1_scores, auc_scores = [], [], [], []
for fold, (train_idx, test_idx) in enumerate(skf.split(x, y), 1):
    x_train, x_test = x.iloc[train_idx], x.iloc[test_idx]
    y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]

    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    y_proba = model.predict_proba(x_test)[:, 1]

    acc_scores.append(accuracy_score(y_test, y_pred))
    recall_scores.append(recall_score(y_test, y_pred))
    f1_scores.append(f1_score(y_test, y_pred))
    auc_scores.append(roc_auc_score(y_test, y_proba))
```

The model obtained the following metrics, averaged across the 5 folds: 

| Metric       | Value  |
|--------------|--------|
| **Accuracy** | 0.7540 |
| **Recall**   | 0.8643 |
| **F1 Score** | 0.8310 |
| **AUC**      | 0.7630 |

Even though the model was a simple baseline with default hyperparameters, it is still
a good starting point. The model correctly classified 75.40% of the examples, while 
maintaining 86.43% of the true positives among all real positive cases. The AUC 
score of 0.7630 indicates that the model has a good ability to discriminate between 
the positive and negative classes. However, there is still room for improvement. 
In the next section, a hyperparameter tuning process will be carried out to further
improve the model's performance. 














