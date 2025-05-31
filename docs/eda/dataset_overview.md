## 📇 DATASET OVERVIEW 

The data used in this project is the 
[German Credit Data](https://archive.ics.uci.edu/dataset/144/statlog+german+credit+data) 
dataset, which contains information about credit applicants and their credit risk 
classification. The dataset consists of 1000 samples. There are 2 variations of the 
dataset: 

- **German Data**: Contains both categorical and numerical features. 
- **German Data Numeric**: Categorical features are encoded as numerical values. 
Suitable for models that require numerical inputs. 

This project uses the original **German Data** with categorical features. 

## FEATURES 

The dataset contains 20 features and a target variable. The features are a mix of 
categorical and numerical variables: 

| Feature Name               | Type         | Description                                                                 |
|---------------------------|--------------|-----------------------------------------------------------------------------|
| Checking_account_status   | Categorical  | Status of existing checking account                                        |
| Duration_months           | Numerical    | Duration in months                                                         |
| Credit_history            | Categorical  | Credit history of the applicant                                            |
| Purpose                   | Categorical  | Purpose of the credit                                                      |
| Credit_amount             | Numerical    | Amount of credit                                                           |
| Savings_account_bonds     | Categorical  | Savings account or bonds                                                   |
| Employment_since          | Categorical  | Present employment duration                                                |
| Installment_rate          | Numerical    | Installment rate in % of disposable income                                 |
| Personal_status_sex       | Categorical  | Personal status and sex                                                    |
| Other_debtors_guarantors  | Categorical  | Other debtors or guarantors                                                |
| Residence_since           | Numerical    | Present residence duration in years                                        |
| Property                  | Categorical  | Type of property                                                           |
| Age_years                 | Numerical    | Age of the applicant                                                       |
| Other_installment_plans   | Categorical  | Other installment plans (e.g. bank, stores)                                |
| Housing                   | Categorical  | Type of housing                                                            |
| Existing_credits          | Numerical    | Number of existing credits at this bank                                    |
| Job                       | Categorical  | Job category                                                               |
| Maintenance_people        | Numerical    | Number of people liable for maintenance                                    |
| Telephone                 | Categorical  | Presence of telephone (registered under the customer's name or not)       |
| Foreign_worker            | Categorical  | Whether the applicant is a foreign worker                                  |

---

The next step is to perform exploratory data analysis (EDA) to understand the 
underlying patterns and relationships in the data. This will help in feature 
selection and model building stages. 