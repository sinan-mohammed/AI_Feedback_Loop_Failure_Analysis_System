from src.dataset_setup import setup_dataset
from src.preprocessing import run_preprocessing
from src.training import train_model
from src.inference import run_inference

DATASET_ID = 1
CONFIG = "2d" 

setup_dataset(DATASET_ID)
run_preprocessing(DATASET_ID, CONFIG)
train_model(DATASET_ID, CONFIG)
run_inference(
    DATASET_ID,
    CONFIG,
    "data/processed/images",
    "outputs/predictions"
)
