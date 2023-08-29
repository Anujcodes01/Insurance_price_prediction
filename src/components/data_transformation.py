from src.constant import *
from src.config.configuration import *
from src.logger import logging
from src.exception import CustomException
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.pipeline import Pipeline
import os,sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from src.utils import save_object


# data transformation class
@dataclass
class DataTransformationConfig():
    processed_obj_file_path = PREPROCESSING_OBJ_FILE
    transfrom_train_file_path = TRANSFORM_TRAIN_FILE_PATH
    transfrom_test_file_path = TRANSFORM_TEST_FILE_PATH
    
    

class DataTransformation:
    def __init__(self,):
        self.data_transformation_config = DataTransformationConfig()
        
    
    def get_data_transformation_obj(self):
        try:
            
            categorical_columns = ['sex','smoker','region']
            numerical_columns = ['age','bmi','children']
            
            # numerical pipeline
            Numerical_pipeline = Pipeline(steps=[
                ('impute',SimpleImputer(strategy='constant',fill_value=0)),
                ('scaler',StandardScaler(with_mean=False))
                
            ])
            
            #categorical pipeline
            Categorical_pipeline =  Pipeline(steps=[
                ('impute',SimpleImputer(strategy='most_frequent')),
                ('onehotencoder',OneHotEncoder(handle_unknown= 'ignore')),
                ('scaler',StandardScaler(with_mean=False))
                
            ])
            preprocessor = ColumnTransformer([
                ('Numerical_pipeline', Numerical_pipeline,numerical_columns),
                ('Categorical_pipeline',Categorical_pipeline,categorical_columns)]
            )
            logging.info('pipeline steps completed successfully')
            
            return preprocessor
        
           
               
            
              
        except Exception as e :
            raise CustomException(e,sys)       
        
        
    def inititate_data_transformation(self,train_path,test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            
            train_df.to_csv("traindata.csv")
            test_df.to_csv("testdata.csv")
            
            processing_obj = self.get_data_transformation_obj()
            target_column_name = 'expenses'
            
            logging.info(f'data splited into training and test data')
            X_train = train_df.drop(columns=target_column_name,axis=1)
            y_train = train_df[target_column_name]
            logging.info(f'xtrain shape is  {X_train.shape} and y_train shape is {y_train.shape}')
            
            
            
            X_test = test_df.drop(columns=target_column_name,axis=1)
            y_test = test_df[target_column_name]
            
            logging.info(f'xtrain shape is  {X_test.shape} and y_train shape is {y_test.shape}')
            
            X_train = processing_obj.fit_transform(X_train)
            logging.info("transformation on the x_train  data completed successfully")
            
            X_test = processing_obj.transform(X_test)
            logging.info("transformation on the x_test  data completed successfully")
            
            train_arr = np.c_[X_train,np.array(y_train)]# concatenated the x_train and y_train
            test_arr = np.c_[X_test,np.array(y_test)] #  concatenated the x_test and y_test
            
            df_train  = pd.DataFrame(train_arr)
            df_test  = pd.DataFrame(test_arr)
            
            
            logging.info('makeing the dir for saving the obj')
            
            os.makedirs(os.path.dirname(self.data_transformation_config.transfrom_train_file_path),exist_ok=True)
            df_train.to_csv(self.data_transformation_config.transfrom_train_file_path,index=False,header=True)
            
            
            os.makedirs(os.path.dirname(self.data_transformation_config.transfrom_test_file_path),exist_ok=True)
            df_test.to_csv(self.data_transformation_config.transfrom_test_file_path,index=False,header=True)
            
            
            save_object(filepath=self.data_transformation_config.processed_obj_file_path,obj=processing_obj)
            logging.info("save the preprocessed object as a file")
            
            return (train_arr
                    ,test_arr,
                    self.data_transformation_config.processed_obj_file_path)
        
        except Exception as e :
            CustomException(e,sys) 
        