from delivery_time_prediction.constants import *
from delivery_time_prediction.logger import logging
from delivery_time_prediction.exception import CustomException
from delivery_time_prediction.config.configuration import *
import os, sys
from delivery_time_prediction.components.data_ingestion import DataIngestion
from delivery_time_prediction.components.data_transformation import DataTransformation
from delivery_time_prediction.components.model_trainer import ModelTrainer

class Train:
    def __init__(self):
        self.c = 0
        print(f"**********************{self.c}*************************")

    def main(self):
        data_ingestion = DataIngestion()
        train_data, test_data = data_ingestion.initiate_data_ingestion()

        data_transformation = DataTransformation()
        train_arr, test_arr, _ = data_transformation.inititate_data_transformation(train_data, test_data)

        model_trainer = ModelTrainer()
        model_trainer.initiate_model_trainer(train_arr, test_arr)