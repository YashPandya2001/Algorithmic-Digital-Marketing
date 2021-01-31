# **Assignment 1**

## Team Information

| Name | NEU ID 
| --- | --- 
|Prathamesh Shrikrishna Verlekar | 001376578 
|Yash Pandya | 001346162

## Dataset Kaggle link

https://www.kaggle.com/c/GiveMeSomeCredit/data

## Claat Link

https://codelabs-preview.appspot.com/?file_id=1XP5C_Dyq4n5XjUmAIwF9UN8vX6FeirDn2tEzlPGS0tI/edit?usp=sharing

# **Dashboard for Analysis**

**Main Dashboard:**
![Main Dashboard](https://user-images.githubusercontent.com/55213702/84539877-46d1aa00-acc2-11ea-8e5c-2070aa7ec3e7.jpeg)

**Detailed Dashboards:**
![Detailed Dashboard 1](https://user-images.githubusercontent.com/55213702/84539879-476a4080-acc2-11ea-9651-a211033868c6.jpeg)
![Detailed Dashboard 2](https://user-images.githubusercontent.com/55213702/84539880-476a4080-acc2-11ea-97c6-6bcd123f0f9e.jpeg)

## **About Dataset Features**

There are a total of 11 features in the dataset (SeriousDlqin2yrs, RevolvingUtilizationOfUnsecuredLines, age, NumberOfTime30-59DaysPastDueNotWorse, DebtRatio, MonthlyIncome, NumberOfOpenCreditLinesAndLoans, NumberOfTimes90DaysLate, NumberRealEstateLoansOrLines, NumberOfTime60-89DaysPastDueNotWorse, NumberOfDependents).

The dataset has 1.5 lakh observations.

The main feature is SeriousDlqin2yrs, which tells us whether the person experienced 90 days past due to delinquency or worse.

All the details of the borrowers are of the past two years only.

Two features(RevolvingUtilizationOfUnsecuredLines, DebtRatio) are of the data type percentage and monthly income is of data type real and the rest all are integers.

## **Formulations we have used**

Replaced mismatched Values in MonthlyIncome with them the median value of the Monthly Income Column.

Replaced mismatched Values in the Number Of Dependent Column with the mode.

Inner Joined two CSV files together with the common columns.

Created Custom category(Age Category) with three conditions where data is distributed age-wise.

Created Custom category(Income Category) with five conditions where data is distributed income-wise.

The debt ratio is calculated by the division of the Liability and monthly income of the person given in the table.

## **Running Jupyter Notebook**

 1. Create a folder in my drive with the name as Datasets 
 2. Inside it put all the dataset files
 3. Then run the kernel code
 
All the visualiztion from Google Colab, XSV's Scripts, Trifacta, Salesforce Einstein Analytics are in respected folders.

