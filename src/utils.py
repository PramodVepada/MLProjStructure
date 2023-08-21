import os
import sys 
import numpy as np 
import pandas as pd 
import dill
from sklearn.metrics import r2_score
from src.exception import CustomException 

def save_object(file_path,obj):
    try :
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok = True)

        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)
    

def evaluate_models(X_train,y_train,X_test,y_test,models):
    try:
        report = {}
        for i in range(len(models)):
            model = list(models.values())[i]
            model.fit(X_train,y_train)
            y_pred_train = model.predict(X_train)
            y_pred_test = model.predict(X_test)
            r2_score_train = r2_score(y_train,y_pred_train)
            r2_score_test = r2_score(y_test,y_pred_test)

            report[list(models.keys())[i]] = r2_score_test

        return report
    
    except Exception as e:
        raise CustomException(e,sys)
    

        



