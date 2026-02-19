import subprocess

def run_inference(dataset_id, config, input_dir, output_dir):
    cmd = (
        f"nnUNetv2_predict "
        f"-d {dataset_id} "
        f"-c {config} "
        f"-i {input_dir} "
        f"-o {output_dir}"
    )
    subprocess.run(cmd, shell=True, check=True)
