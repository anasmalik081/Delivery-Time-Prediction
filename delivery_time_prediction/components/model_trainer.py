from delivery_time_prediction.logger import logging
from delivery_time_prediction.exception import CustomException
from delivery_time_prediction.utils import evaluate_model, save_object
from delivery_time_prediction.constants import *
import os, sys
from delivery_time_prediction.config.configuration import *
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

@dataclass
class ModelTrainerConfig:
    train_model_file_path: str = MODEL_FILE_PATH

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    
    def initiate_model_trainer(self, train_arr, test_arr):
        try:
            logging.info("Splitting data into dependent and independent variables")
            X_train, y_train, X_test, y_test = (
                train_arr[:,:-1], train_arr[:,-1],
                test_arr[:, :-1], test_arr[:,-1]
            )

            models = {
                'Ridge': Ridge(),
                'DecisionTree': DecisionTreeRegressor(),
                'RandomForest': RandomForestRegressor(),
                'GradientBoosting': GradientBoostingRegressor(),
                'xgboost': XGBRegressor(),
                'svm': SVR()
            }

            model_report: dict = evaluate_model(X_train, y_train, X_test, y_test, models)
            print(model_report)

            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model = models[best_model_name]

            print(f"Best Model Found, Model name: {best_model_name}, R2 Score: {best_model_score}")

            save_object(
                filepath=self.model_trainer_config.train_model_file_path,
                obj=best_model
            )

            return best_model_score
            

        except Exception as e:
            raise CustomException(e, sys)