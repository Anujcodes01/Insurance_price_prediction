from src.constant import *
from src.config.configuration import *
import os,sys
import pandas as pd
import numpy as np
from src.logger import logging 
from src.exception import CustomException
import joblib
from src.utils import load_model
from sklearn.pipeline import Pipeline


PREDICTION_FOLDER = 'Batch_prediction'
PREDICTION_CSV = 'Prediction_csv'
PREDICTION_FILE = "output.csv"
TRANFORM_DATA = 'Processed_transformation'
ROOT_DIR = os.getcwd()
TRANFORM_PROCESSED = os.path.join(ROOT_DIR,PREDICTION_FOLDER,TRANFORM_DATA)
BATCH_PREDICTION = os.path.join(ROOT_DIR,PREDICTION_FOLDER,PREDICTION_CSV)

class BatchPrediction(object):
    def __init__(self,input_file,
                 model_file_path,
                 transformer_file_path,)->None:
        
        self.input_file = input_file
        self.model_file_path = model_file_path
        self.transformer_file_path = transformer_file_path
        
    
    def start_batch_prediction(self):
        try:
            # load the data transformation pipeline file path
            with open(self.transformer_file_path,'rb') as f:
                processed = joblib.load(f)
                
            # load the model sepratly
            model = load_model(file_path=self.model_file_path)
            
            # loading the csv
            
            df = pd.read_csv(self.input_file)
            
            # Data transformation 
            transformed_data = processed.transform(df)
            
            file_path = os.path.join(TRANFORM_PROCESSED,"processed.csv")
            prediction = model.predict(transformed_data) 
            
            df_prediction = pd.DataFrame(prediction,columns=['prediction'])
            
            BATCH_PREDICTION_PATH = BATCH_PREDICTION
            os.makedirs(BATCH_PREDICTION_PATH,exist_ok=True)
            csv_path = os.path.join(BATCH_PREDICTION_PATH,PREDICTION_CSV)
            df_prediction.to_csv(index=False)
            
            
            logging.info("Batch Prediction successfully completed")
                       
                       
        
        except Exception as e:
            CustomException(e,sys)