from delivery_time_prediction.constants import *
from delivery_time_prediction.config.configuration import *
import os, sys
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from delivery_time_prediction.logger import logging
from delivery_time_prediction.exception import CustomException


@dataclass
class DataIngestionConfig:
    raw_file_path: str = RAW_FILE_PATH
    train_data_path: str = TRAIN_FILE_PATH
    test_data_path: str = TEST_FILE_PATH

class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        try:
            logging.info("Reading Dataset")
            df = pd.read_csv(DATASET_PATH)
            logging.info("Succesfully Read the dataset")

            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_file_path), exist_ok=True)

            logging.info("Saving raw dataset")
            df.to_csv(self.data_ingestion_config.raw_file_path, index=False)
            logging.info("Successfully saved raw data")

            train_set, test_set = train_test_split(df, test_size=0.20, random_state=42)

            os.makedirs(os.path.dirname(self.data_ingestion_config.train_data_path), exist_ok=True)
            os.makedirs(os.path.dirname(self.data_ingestion_config.test_data_path), exist_ok=True)

            logging.info("Saving Train & Test data")
            train_set.to_csv(self.data_ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.data_ingestion_config.test_data_path, index=False, header=True)
            logging.info("Successfully Saved Train & Test data")

            return (
                self.data_ingestion_config.train_data_path,
                self.data_ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)