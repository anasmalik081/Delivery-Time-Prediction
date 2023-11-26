from delivery_time_prediction.logger import logging
from delivery_time_prediction.exception import CustomException
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV
import os, sys
import pickle

def save_object(filepath, obj):
    try:
        dir_path = os.path.dirname(filepath)
        os.makedirs(dir_path, exist_ok=True)

        with open(filepath, 'wb') as file_obj:
            pickle.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_model(X_train, y_train, X_test, y_test, models):
    try:
        report = {}

        for name, model in models.items():
            model = model
            model.fit(X_train, y_train)

            # predicting
            y_test_pred = model.predict(X_test)

            test_model_score = r2_score(y_test, y_test_pred)
            print(name, test_model_score)

            report[name] = test_model_score
        
        return report

    except Exception as e:
        raise CustomException(e, sys)