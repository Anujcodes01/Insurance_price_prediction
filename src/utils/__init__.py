import pickle
from src.logger import logging
from src.exception import CustomException
import os,sys
def save_object(filepath,obj):
    try:
        dir_path = os.path.dirname(filepath)
        os.makedirs(dir_path,exist_ok=True)
        
        with open(filepath,'wb') as file_obj:
            pickle.dump(obj,file_obj)
        
    except Exception as e:
        CustomException(e,sys)