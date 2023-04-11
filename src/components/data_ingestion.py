import os
import sys

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# Importing modules from the project's source code
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.utils import BASE_DIR
from src.exception import CustomException
from src.logger import logging

# Creating a dataclass to store the configuration for data ingestion
@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join(BASE_DIR, 'data', "train.csv")
    test_data_path: str = os.path.join(BASE_DIR, 'data', "test.csv")
    raw_data_path: str = os.path.join(BASE_DIR, 'data', "data.csv")

# Creating a class for data ingestion
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            # Reading an Excel file as a pandas dataframe
            df = pd.read_excel(os.path.join(BASE_DIR, 'data', 'DS_assessment.xlsx'), sheet_name='Data')
            logging.info('Read the dataset as dataframe')

            # Renaming columns of the dataframe
            logging.info('Renaming the columns')
            df = df.rename(columns={'ID': 'id',
                                    'Age': 'age',
                                    'Experience': 'experience',
                                    'Income': 'income',
                                    'Postal Code': 'postal_code',
                                    'Family Size': 'family_size',
                                    'CCAvgSpending': 'creditc_avg_spent',
                                    'Education': 'education',
                                    'Mortgage': 'mortgage',
                                    'Investment Account': 'investment_account',
                                    'Deposit Account': 'deposit_account',
                                    'InternetBanking': 'internet_banking',
                                    'Personal Loan': 'personal_loan'})

            # Creating directory to store the train data file
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Writing the dataframe to a csv file as raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            # Splitting the data into train and test sets
            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Saving the train and test data as csv files
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            # Returning paths to the train and test data
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            # Raising a custom exception in case of errors
            raise CustomException(e, sys)


if __name__ == "__main__":
    # Initializing data ingestion
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    # Initializing data transformation
    data_transformation = DataTransformation()
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data)

    # Initializing model training
    modeltrainer = ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr, test_arr))
