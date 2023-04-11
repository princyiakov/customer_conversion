import os
import sys

import pickle
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import GridSearchCV

from src.logger import logging
from src.exception import CustomException

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def save_object(file_path, obj):
    """
    This function saves the object to the mentioned file_path
    """
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)


def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    """
    This function evaluates the list of models based on ROC AUC Score
    """
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para = param[list(models.keys())[i]]
            logging.info(f'Initiating Grid Search for {model}')
            gs = GridSearchCV(model, para, cv=5)
            gs.fit(X_train, y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)
            logging.info(f'Initiating grid search and model fir completed for {model}')

            y_test_pred = model.predict(X_test)

            test_model_score = roc_auc_score(y_test, y_test_pred)
            logging.info(f'ROC AUC Score for {model} is {test_model_score}')

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)


def load_object(file_path):
    """
    This function loads the object from the mentioned file_path
    """
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)
