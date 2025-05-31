## 📊 Exploratory Data Analysis (EDA) 

The exploratory data analysis (EDA) is the first step in a machine learning project, 
as it helps to understand the data one is working with. As an attempt to simulate a
real world scenario, the EDA has been performed with the dataset converted to a 
SQL database. The EDA is performed using SQL queries to extract the data and matplotlib 
to visualize it. For more details on the queries used please refer to the 
[queries]() section. 

Here are the graphs generated during the EDA: 

![EDA results](../assets/eda_result.png) 

## 📈 Key Findings 

The first thing to notice is the imbalance in the target variable. 70% of the 
applicants have a good credit risk, while 30% have a bad credit risk. This is 
a common scenario in real world datasets, where the positive class outnumbers the
negative one. When training the model, it will be important to keep this in mind, 
as class balancing techniques may be needed. Also, accuracy and recall analysis 
will be important to ensure that the model is not biased towards the majority 
class.

When looking at the credit amount, the mean amount is around 4.000 for bad risk 
applicants, and around 3.000 for good risk applicants. This suggests that credit 
amount could be a good feature to use in the model. 

The age most frequent age group in the dataset is the 25-34 segment, which is 
somewhat expected, as this is the age group that is most likely to apply for a 
credit. Looking at the personal status, the majority of the applicants are single 
men (A93). Something that stands out is the absence of A95 applicants(female, 
single). This suggests that, fore some reason, single men are more likely to 
apply for a credit than single women. However, this issue is not within the scope 
of this project. 

In terms of housing, the majority of the applicants are owners (A152). Being an 
owner may be a good indicator of good credit risk, as the majority of the 
applicants who fall into this category have a good credit risk. On the other hand, 
both A151 (renting) and A153 (for free) don't have enough data to draw any 
conclusions. 

50% of the applicants are type A32 in credit history, which means they have paid 
all their previous credits. This could be a good indicator of good credit risk, but
it would not be prudent to draw any conclusions based on this alone. 

Looking at the guarantor types, the distributions is quite even, so this variable 
is not likely to be a good indicator of credit risk. However, the variable could 
still be useful in the model. 

---

With this information, the next step is to build a base model and evaluate it. 
Even though the EDA has provided some insights, it can still be improved with 
further analysis. 
