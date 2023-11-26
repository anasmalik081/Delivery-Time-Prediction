import sys
from flask import Flask
from delivery_time_prediction.logger import logging
from delivery_time_prediction.exception import CustomException
from delivery_time_prediction.components.data_ingestion import DataIngestion
from delivery_time_prediction.components.data_transformation import DataTransformation
from delivery_time_prediction.components.model_trainer import ModelTrainer

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        raise Exception("Testing Exception file")
    except Exception as e:
        message = CustomException(e, sys)
        logging.info(message.error_message)
        return "Hello"
    
@app.route('/initiate', methods=['GET'])
def initiate():
    data_ingestion = DataIngestion()
    train_data, test_data = data_ingestion.initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_arr, test_arr, _ = data_transformation.inititate_data_transformation(train_data, test_data)

    model_trainer = ModelTrainer()
    model_trainer.initiate_model_trainer(train_arr, test_arr)
    return "Successfully Trained Model"

if __name__ == '__main__':
    app.run(debug=True)