from src.constant import *
from src.config.configuration import *
from src.logger import logging
from src.exception import CustomException
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.pipeline import Pipeline
import os,sys
from dataclasses import dataclass
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from src.utils import evaluate_model,save_obj

@dataclass
class ModelTrainerConfig :
    trainer_model_file_path = MODEL_FILE_PATH
    
class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
        
    def inititate_model_training(self,train_arr,test_arr):
        try:
            X_train,y_train ,X_test,y_test = (train_arr[:,:-1],train_arr[:,-1],
                                              test_arr[:,:-1],test_arr[:,-1])
            
            models={
            'SVR':SVR(),
            'DecisionTree':DecisionTreeRegressor(),
            'Gradient Boosting':GradientBoostingRegressor(),
            'Random Forest':RandomForestRegressor(),
            'XGB Regressor':XGBRegressor()
            
        }
        
            model_report:dict=evaluate_model(X_train,y_train,X_test,y_test,models)
            print(model_report)
            print('\n====================================================================================\n')
            logging.info(f'Model Report : {model_report}')

            # To get best model score from dictionary 
            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            
            best_model = models[best_model_name]

            print(f'Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_score}')
            print('\n====================================================================================\n')
            logging.info(f'Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_score}')

            save_obj(
                 filepath=self.model_trainer_config.trainer_model_file_path,
                 obj=best_model
            )
          
            logging.info("save the model object as a file")
            
            
        except Exception as e:
            CustomException(e,sys)