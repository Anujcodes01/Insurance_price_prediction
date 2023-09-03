import os,sys
from datetime import datetime

# artifact -> pipeline folder ->timestamp -> output

def get_current_timestamp():
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

CURRENT_TIME_STAMP = get_current_timestamp()

ROOT_DIR_KEY = os.getcwd()
DATA_DIR = 'Data'
DATA_DIR_KEY = 'insurance.csv'

#Insurance_price_prediction/DATA_DIR/DATA_DIR_KEY

ARTIFACT_DIR_KEY = 'Artifact'
# data ingestion related variables

DATA_INGESTION_KEY = 'Data_Ingestion'
DATA_INGESTION_RAW_DATA_DIR = 'raw_data_dir'
DATA_INGESTION_INGESTED_DATA_DIR_KEY = 'Ingested_Dir'
RAW_DATA_DIR_KEY = 'raw.csv'
TRAIN_DATA_DIR_KEY = 'train.csv'
TEST_DATA_DIR_KEY = 'test.csv'
# artifacts --> Data Ingestion --> current timestamp --> raw data dir/raw.csv --> Ingested Dir /train.csv and test.csv

# data transfromation related variables

DATA_TRANSFORMATION_ARTIFACT = 'Data_Transformation'
DATA_PREPROCESSED_DIR = "preprocessor"
DATA_TRANSFROMATION_PROCESSED_OBJ = "processed.pkl"
# DATA_TRANSFORMATION_FEATURES_ENN = 'feature_engg.pkl'
DATA_TRANSFORM_DIR = "transformation"
TRANFORM_TRAIN_DIR_KEY = "train.csv"
TRANFORM_TEST_DIR_KEY = "test.csv"

# artifacts - > data_transformation -> processor /preprocessor.pkl ->and transformation -> train.csv and test.csv

# model training

# model training
MODEL_TRAINER_KEY = 'model_trainer'
MODEL_OBJECT = 'model.pkl'

# batch prediction 


PREDICTION_FOLDER = 'Batch_Prediction'
PREDICTION_CSV = 'Prediction_csv'
PREDICTION_FILE = "output.csv"
TRANFORM_DATA = 'Processed_transformation'