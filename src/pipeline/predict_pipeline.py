import os
import sys

import pandas as pd
import numpy as np

from src.exception import CustomException
from src.utils import load_object, BASE_DIR


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = os.path.join(BASE_DIR, 'model', 'model.pkl')
            preprocessor_path = os.path.join(BASE_DIR, 'model', 'preprocessor.pkl')
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            print("Model and preprocessor loaded")
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            preds = "Will take Personal Loan" if preds[0] == 1 else "Will NOT take Personal Loan"
            return preds

        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(self,
                 education: str,
                 investment_account: int,
                 income: float,
                 family_size,
                 creditc_avg_spent: float,
                 mortgage: float):

        self.education = education

        self.investment_account = investment_account

        self.income = np.nan if income == '' else income

        self.family_size = np.nan if family_size == '' else family_size

        self.creditc_avg_spent = creditc_avg_spent

        self.mortgage = mortgage

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "education": [self.education],
                "investment_account": [self.investment_account],
                "income": [self.income],
                "family_size": [self.family_size],
                "creditc_avg_spent": [self.creditc_avg_spent],
                "mortgage": [self.mortgage]
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)
