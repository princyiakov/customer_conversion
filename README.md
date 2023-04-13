<img alt="customer_conversion" src="https://raw.githubusercontent.com/princyiakov/customer_conversion/main/resources/attract-customers.png">

# Customer Conversion

The bank wants to explore ways of converting its liability customers to personal loan customers (while retaining them 
as depositors). A campaign that the bank ran last year for liability customers showed a conversion rate of over 9% 
success. This has encouraged the retail marketing department to devise campaigns with better target marketing to 
increase the success ratio with minimal budget.

<!-- toc -->
- [Our Goal](#our-goal)
- [Notebook Files](#notebook-files)
- [Presentation File](#presentation-file)
- [How Were We Able To Predict The Progression](#how-were-we-able-to-predict-the-progression)
  - [Feature Engineering](#feature-engineering)
  - [Handling Missing Features](#handling-missing-features)
  - [Scaling](#scaling)
  - [Feature Selection](#feature-selection)
  - [Handling Imbalanced Data](#handling-imbalanced-data)
  - [Model Evaluation and Selection](#model-evaluation-and-selection)
- [Our Primary Target Audience](#our-primary-target-audience)
- [Web Application](#web-application)
- [Dockerfile](#dockerfile)
<!-- tocstop -->

## Our Goal
Using the Data set, help to build a Machine Learning Model which can predict if a Customer would take up Personal Loan 
if the targeted Marketing Campaign is done

## Notebook Files
Here is the link to the [EDA HTML](https://github.com/princyiakov/customer_conversion/blob/main/resources/task_1_Data_Cleaning_EDA.html) for better visualisation

Here is the link to the [EDA Notebook](https://github.com/princyiakov/customer_conversion/blob/main/notebooks/task_1_Data_Cleaning_EDA.ipynb)

Here is the link to the [Feature Selection & Modelling](https://github.com/princyiakov/customer_conversion/blob/main/notebooks/task_2_FeatureSelection_Modelling_Pipeline.ipynb)

## Presentation File
Here is the link to the [Presentation File](https://github.com/princyiakov/customer_conversion/blob/main/resources/Data_Scientist_Assignment.pdf)


## How Were We Able To Predict The Progression
Explored various models like Random Forest, Gradient Boosting, XGBClassifier, KNeighborsClassifier using different hyperparameters

### Feature Engineering
- Feature Engineered Experience  :
    - Featured engineered Experience feature to gain insights with the data but the Heat map of Correlation matrix showed Experience field is not a good feature to conside

### Handling Missing Features
- Categorical data :
  - Replace missing values with mode 
- Numerical Data :
  - Replace missing values with mean

### Scaling 
- Performed Standard Scaling on the features

### Feature Selection
Performed correlation matrix to check which features are the best 
<img alt="featureimp" src="https://raw.githubusercontent.com/princyiakov/customer_conversion/main/resources/correlation.png">


### Handling Imbalanced Data
I used SMOTE to improve the imbalanced data

### Model Evaluation and Selection

The following were the  performance metrics of the models
<img alt="evaluation" src="https://raw.githubusercontent.com/princyiakov/customer_conversion/main/resources/evaluation.png">


### Our Primary Target Audience
- Income ranging between 122k to 172k
- Credit card average spending ranging between 2.6k to 5.4k
- People with deposit account

### Web Application
<img alt="webapp" src="https://raw.githubusercontent.com/princyiakov/customer_conversion/main/resources/webapp.png">

### Dockerfile

If you have docker installed, run the following command to access the webapp on http://localhost:3000
```aidl
docker build -t customer_conversion .
docker run -p 3000:3000 customer_conversion

```