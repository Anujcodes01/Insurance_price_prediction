from src.constant import *
from src.logger import logging
from src.exception import CustomException
import os ,sys
from src.config.configuration import *
from src.utils import load_model
import pandas as pd

class PredictionPipeline():
    def __init__(self):
        pass
    
    def predict(self,features):
        try:
            preprocessor_path = PREPROCESSING_OBJ_FILE
            model_path = MODEL_FILE_PATH
            
            preprocessor = load_model(preprocessor_path)
            model = load_model(model_path)
            
            data_scaled = preprocessor.transform(features)
            
            pred = model.predict(data_scaled)
            return pred
        
        
        
        except Exception as e:
            logging.info('error occured while processing single prediction')
            CustomException(e,sys)
            
    
class CustomData :
    def __init__(self,sex:str,
                    smoker : str,
                    region:str,
                    age:int,
                    bmi:float,
                    children:int
                    ):
        """"categorical_columns = ['sex','smoker','region']
        numerical_columns = ['age','bmi','children']"""
        
        self.sex = sex
        self.smoker = smoker
        self.region = region
        self.age = age
        self.bmi = bmi
        self.children = children
    
    def  get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {'sex':[self.sex],
                                      'smoker':[self.smoker],
                                    'region':[self.region],
                                      'age':[self.age],
                                      'bmi':[self.bmi],
                                      'children':[self.children]
                                      }
            df = pd.DataFrame(custom_data_input_dict)
            
            return df
        
        
        except Exception as e:
            logging.info('error occured in custom pipeline')
            CustomException(e,sys) 
    
            
            