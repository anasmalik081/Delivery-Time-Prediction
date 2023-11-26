import sys
from flask import Flask
from delivery_time_prediction.logger import logging
from delivery_time_prediction.exception import CustomException
from delivery_time_prediction.components.data_ingestion import DataIngestion

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
    data_ingestion.initiate_data_ingestion()
    return "Successfully Data Ingestion Done"

if __name__ == '__main__':
    app.run(debug=True)