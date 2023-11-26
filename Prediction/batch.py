from delivery_time_prediction.constants import *
from delivery_time_prediction.config.configuration import *
from delivery_time_prediction.logger import logging
from delivery_time_prediction.exception import CustomException
from delivery_time_prediction.utils import load_model
from sklearn.pipeline import Pipeline
import os, sys
import pandas as pd
import pickle


PREDICTION_FOLDER = 'batch_prediction'
PREDICTION_CSV = 'prediction_csv'
PREDICTION_FILE = 'output.csv'

FEATURE_ENGG_FOLDER = 'feature_engg'

ROOT_DIR = os.getcwd()
BATCH_PREDICTION = os.path.join(
    ROOT_DIR,
    PREDICTION_FOLDER,
    PREDICTION_CSV
)
FEATURE_ENGG = os.path.join(
    ROOT_DIR,
    FEATURE_ENGG_FOLDER
)


class BatchPrediction:
    def __init__(
            self,
            input_file_path,
            model_file_path,
            transformer_file_path,
            feature_engg_file_path
    )->None:
        self.input_file_path = input_file_path
        self.model_file_path = model_file_path
        self.transformer_file_path = transformer_file_path
        self.feature_engg_file_path = feature_engg_file_path

    def start_batch_prediction(self):
        try:
            # load feature engg pipeline path
            with open(self.feature_engg_file_path, 'r') as f:
                feature__pipeline = pickle.load(f)

            # load data transformation path
            with open(self.transformer_file_path, 'r') as f:
                processor = pickle.load(f)

            # load model separately
            model = load_model(self.model_file_path)

            # create feature engineering pipeline
            feature_engg_pipeline = Pipeline(steps=[
                ('feature_engg', feature__pipeline)
            ])
            
            # loading dataset
            df = pd.read_csv(self.input_file_path)
            df.to_csv('zomato_delivery_time_prediction')

            # apply feature engineering
            df = feature__pipeline.transform(df)

            feature_engg_path = FEATURE_ENGG
            os.makedirs(feature_engg_path, exist_ok=True)

            file_path = os.path.join(feature_engg_path, 'batch_feature_eng.csv')
            df.to_csv(file_path, index=False)

            # time taken
            df = df.drop('Time_taken (min)', axis=1)
            

            transformed_data = processor.transform(df)

            file_path = os.path.join(feature_engg_path, 'processor.csv')

            predictions = model.predict(transformed_data)

            df_prediction = pd.DataFrame(predictions, columns=['predictions'])

            batch_prediction_path = BATCH_PREDICTION
            os.makedirs(batch_prediction_path, exist_ok=True)
            csv_path = os.path.join(batch_prediction_path, 'output.csv')

            df_prediction.to_csv(csv_path, index=False)
            logging.info("Batch prediction Done")

        except Exception as e:
            raise CustomException(e, sys)

