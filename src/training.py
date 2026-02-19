import subprocess

def train_model(dataset_id, config="2d", fold=0):
    cmd = f"nnUNetv2_train {dataset_id} {config} {fold}"
    subprocess.run(cmd, shell=True, check=True)
