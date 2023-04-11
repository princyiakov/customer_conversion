import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder, StandardScaler
from imblearn.over_sampling import SMOTE

from src.exception import CustomException
from src.logger import logging
import os

from src.utils import save_object, BASE_DIR


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join(BASE_DIR, 'model', "preprocessor.pkl")


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        """
        This function is responsible for data transformation

        """
        try:
            numerical_columns = ['income', 'family_size','creditc_avg_spent', 'mortgage']
            categorical_columns = ['education', 'investment_account']

            num_pipeline = Pipeline([('imputer', SimpleImputer(strategy='mean', missing_values=np.nan)),
                                     ('scalar', StandardScaler())])

            cat_pipeline = Pipeline([('imputer', SimpleImputer(strategy='most_frequent', missing_values=np.nan)),
                                     ('ordinal', OrdinalEncoder())])

            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")

            preprocessor = ColumnTransformer(
                [
                    ("cat_pipelines", cat_pipeline, categorical_columns),
                    ("num_pipeline", num_pipeline, numerical_columns)

                ]

            )

            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self, train_path, test_path):

        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessing object")

            preprocessing_obj = self.get_data_transformer_object()

            target_column_name = "personal_loan"
            target_mapping = {'YES': 1, 'NO': 0}
            selected_column_names = ['education', 'investment_account','income', 'family_size','creditc_avg_spent', 'mortgage']

            input_feature_train_df = train_df.loc[:, selected_column_names]
            target_feature_train_df = train_df[target_column_name].map(target_mapping)

            input_feature_test_df = test_df.loc[:, selected_column_names]
            target_feature_test_df = test_df[target_column_name].map(target_mapping)

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )

            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            # Apply SMOTE resampling to balance the training data
            smote = SMOTE(random_state=42)
            input_feature_train_arr, target_feature_train_df = smote.fit_resample(input_feature_train_arr, target_feature_train_df)

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object.")

            save_object(

                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj

            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
        except Exception as e:
            raise CustomException(e, sys)
