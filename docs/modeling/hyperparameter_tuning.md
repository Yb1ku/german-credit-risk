
The previous section introduced a baseline model with default hyperparameters. Now, 
the goal is to improve the model's performance by tuning its hyperparameters. This 
process has been carried out using a simple grid search strategy. It may not be the 
most complex or exhaustive method, but it is a good starting point for hyperparameter
tuning. If the model's performance is still not satisfactory, more advanced techniques
can be applied. 

The hyperparameter search has been performed as follows: 
```python 
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.metrics import make_scorer, f1_score
import xgboost as xgb

base_model = xgb.XGBClassifier(
    objective="binary:logistic",
    eval_metric="logloss",
    enable_categorical=True,
    random_state=42
)

param_grid = {
    "max_depth": [3, 5, 7],
    "learning_rate": [0.01, 0.1, 0.2],
    "n_estimators": [100, 200],
    "subsample": [0.8, 1],
    "colsample_bytree": [0.8, 1],
}

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

grid_search = GridSearchCV(
    estimator=base_model,
    param_grid=param_grid,
    scoring=make_scorer(f1_score),
    cv=cv,
    verbose=1,
    n_jobs=-1
)

grid_search.fit(x, y)
```
The optimal hyperparameters found are: 
```python
{
    'colsample_bytree': 0.8,
    'learning_rate': 0.1, 
    'max_depth': 3,
    'n_estimators': 200, 
    'subsample': 1
}
``` 

The model achieved the following performance metrics, averaged over the 5-fold 
cross-validation process: 

| Metric       | Value  |Improvement|
|--------------|--------|-----------|
| **Accuracy** | 0.8461 |+0.0921|
| **Recall**   | 0.9743 |+0.11|
| **F1 Score** | 0.9472 |+0.1162|
| **AUC**      | 0.9744 |+0.2114|


With this simple grid search, the model's performance has been significantly 
improved. The metrics show the model's performance is now much better than the 
baseline model. Even though there is still room for improvement, the extra boost in 
performance that could be achieved with more advanced hyperparameter tuning techniques 
and with feature engineering is not worth the extra time and complexity. It is good 
to boost the performance, but it is also important to keep the model nice and simple. 

The next section will focus on explaining the model's predictions using SHAP. 















