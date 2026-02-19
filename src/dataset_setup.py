import os
from nnunetv2.utilities.dataset_name_id_conversion import maybe_convert_to_dataset_name
from nnunetv2.experiment_planning.verify_dataset_integrity import verify_dataset_integrity

def setup_dataset(dataset_id):
    dataset_name = maybe_convert_to_dataset_name(dataset_id)
    print(f"Using dataset: {dataset_name}")
    verify_dataset_integrity(dataset_name)
