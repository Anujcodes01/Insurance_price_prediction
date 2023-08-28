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
