The goal of this project was to simulate a real-world scenario of an end-to-end 
machine learning project, going from data extraction via SQL to model 
deployment and documentation. Below are the key conclusions drawn from the 
project: 

## ✨Key lessons learned 

- **SQL for data extraction**: Using SQL for data extraction is a powerful 
yet simple way to handle large datasets. In personal projects, the data 
often comes in CSV format, but in a real-world scenario, data is usually 
stored in a database. Being able to extract data directly from a database 
using SQL is a valuable skill. 

- **Strong baselines matter**: Sometimes, even a simple model can yield good 
results. In this project, using a simple XGBoost with default hyperparameters 
achieved acceptable results, and tracking the model's performance enabled to 
track the improvement obtained with hyperparameter tuning. 

- **Hyperparameter tuning strategy**: It is a good idea to start the 
hyperparameter tuning with a simple grid search, as it allows to quickly 
identify possible hyperparameter combinations that yield good results. If 
the performance is yet not satisfactory, a more advanced hyperparameter tuning 
method can be used, focused on the best performing region. 

- **Explainability with SHAP**: Using SHAP to analyze the model's predictions 
is a great way to understand how and why the model is making certain 
predictions. Using this tool in all the dataset enables to identify key 
patterns in the model's behavior. In addition, SHAP values analysis can also 
be used to identify potential biases in the model, which is important to 
ensure that the model is fair and not biased towards certain groups of 
applicants. 

## Further improvements 

Even though the project has reached a satisfactory conclusion, there is still 
room for improvement. Here are some ideas for further improvements: 

- **Try alternative models**: The model implemented here was XGBoost, but 
algorithms such as Random Forest or LightGBM could also be tested. 

- **Refine the estimator range**: The number of estimators obtained by the 
hyperparameter tuning process was 200. However, a more detailed search on 
this hyperparameter could yield better results. The grid search only 
contemplated 100 and 200, so maybe there is a value between those two that 
yields equal results with less computational cost. 

- **Incorporate class imbalance handling**: The model implemented didn't need 
any class imbalance handling, but it could be useful to test if the application
of techniques such as SMOTE could improve the model's performance. 