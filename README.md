<img alt="customer_conversion" src="https://raw.githubusercontent.com/princyiakov/customer_conversion/main/resources/attract-customers.png">

# Customer Conversion

The bank wants to explore ways of converting its liability customers to personal loan customers (while retaining them 
as depositors). A campaign that the bank ran last year for liability customers showed a conversion rate of over 9% 
success. This has encouraged the retail marketing department to devise campaigns with better target marketing to 
increase the success ratio with minimal budget.

<!-- toc -->
- [Our Goal](#our-goal)
- [Presentation File](#presentation-file)
- [Notebook Files](#notebook-files)
- [How Were We Able To Predict The Progression](#how-were-we-able-to-predict-the-progression)
  - [Feature Engineering](#feature-engineering)
  - [Handling Missing Features](#handling-missing-features)
  - [Scaling](#scaling)
  - [Feature Selection](#feature-selection)
  - [Handling Imbalanced Data](#handling-imbalanced-data)
  - [Model Evaluation and Selection](#model-evaluation-and-selection)
- [Our Primary Target Audience](#our-primary-target-audience)
- [Coding Scripts](#coding-scripts)
- [Web Application](#web-application)
- [Dockerfile](#dockerfile)
<!-- tocstop -->

## Our Goal
Using the Data set, help to build a Machine Learning Model which can predict if a Customer would take up Personal Loan 
if the targeted Marketing Campaign is done

## Presentation File
Here is the link to the [Presentation PDF](https://github.com/princyiakov/customer_conversion/blob/main/resources/Data_Scientist_Assignment.pdf)

## Notebook Files

Here is the link to the [EDA Notebook](https://github.com/princyiakov/customer_conversion/blob/main/notebooks/task_1_Data_Cleaning_EDA.ipynb)

Here is the link to the [Feature Selection & Modelling](https://github.com/princyiakov/customer_conversion/blob/main/notebooks/task_2_FeatureSelection_Modelling_Pipeline.ipynb)


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

### Coding Scripts
1. [data_ingestion.py](https://github.com/princyiakov/customer_conversion/blob/main/src/components/data_ingestion.py) : For ingesting train, test and raw data along with the trained model
2. [data_transformation.py](https://github.com/princyiakov/customer_conversion/blob/main/src/components/data_transformation.py) : For handling missing values, scaling and oversampling with SMOTE
3. [model_trainer.py](https://github.com/princyiakov/customer_conversion/blob/main/src/components/model_trainer.py) : For training different models on various hyper parameters and choosing the best based on ROC AUC Score
4. [predict_pipeline.py](https://github.com/princyiakov/customer_conversion/blob/main/src/pipeline/predict_pipeline.py) : To predict the data created using CustomData class
5. [app.py](https://github.com/princyiakov/customer_conversion/blob/main/app.py) : For running the front end application to predict if the person will take personal loan

Other Scipts include : 
1. [utils.py](https://github.com/princyiakov/customer_conversion/blob/main/src/utils.py) : For common function used in the project
2. [logger.py](https://github.com/princyiakov/customer_conversion/blob/main/src/logger.py) : For improved logging 
3. [exception.py](https://github.com/princyiakov/customer_conversion/blob/main/src/exception.py) : For logging errors along with line number of error along with file name

### Web Application
<img alt="webapp" src="https://raw.githubusercontent.com/princyiakov/customer_conversion/main/resources/webapp.png">

### Dockerfile

First clone the repo 
```
git clone https://github.com/princyiakov/customer_conversion.git
cd customer_conversion
```

If you have docker installed, run the following command to access the webapp on http://localhost:3000
```
docker build -t customer_conversion .
docker run -p 3000:3000 customer_conversion
```