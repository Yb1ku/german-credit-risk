This section contains the queries used to explore the dataset 


#### Get the number of clients in the dataset

```sql
SELECT COUNT(*) FROM credit;
```

#### Get the number of clients with each credit rating

```sql 
SELECT Target, COUNT(*) as total
FROM credit
GROUP BY Target;
```

#### Average credit amount by credit rating

```sql 
SELECT Target, AVG(Credit_amount) AS mean_credit
FROM credit
GROUP BY Target;
```

#### Purpose of credit by credit rating

```sql 
SELECT Purpose, Target, COUNT(*) as total
FROM credit
GROUP BY Purpose, Target
```

#### Most frequent purpose of credit by credit rating

```sql
SELECT Purpose, Target, COUNT(*) AS total
FROM credit
GROUP BY Purpose, Target
HAVING total = (
    SELECT MAX(cnt)
    FROM (
        SELECT COUNT(*) AS cnt
        FROM credit AS c2
        WHERE c2.Target = credit.Target
        GROUP BY Purpose
    )
)
```


#### Housing type by credit rating

```sql
SELECT Housing, Target, COUNT(*) as total
FROM Credit
GROUP BY Housing, Target
```

#### Age distribution 

```sql 
SELECT
  CASE
    WHEN Age < 25 THEN '18-24'
    WHEN Age < 35 THEN '25-34'
    WHEN Age < 50 THEN '35-49'
    ELSE '50+'
  END AS age_group,
  COUNT(*) AS total
FROM credit
GROUP BY age_group
ORDER BY age_group;
```

#### Personal status distribution 

```sql
SELECT Personal_status_and_sex, Target, COUNT(*) as total
FROM credit
GROUP BY Personal_status_and_sex
ORDER BY total DESC
```

#### Credit history distribution 

```sql 
SELECT Credit_history, Target, COUNT(*) as total
FROM credit
GROUP BY Credit_history
ORDER BY total DESC
```

#### Duration of credit in months by credit rating

```sql 
SELECT Duration_in_month, AVG(Target) AS good_credit_rate
FROM credit
GROUP BY Duration_in_month
ORDER BY Duration_in_month ASC;
```





















