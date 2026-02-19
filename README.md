# Stroke Lesion Segmentation using nnU-Net

## Project Overview
This project focuses on automatic stroke lesion segmentation from medical images using the nnU-Net framework.  
The goal is to train a deep learning model that can identify and segment stroke lesions accurately.

The entire workflow was first implemented in a Jupyter/Google Colab notebook and later converted into a clean, modular GitHub project.

---

## What This Project Does
- Verifies the medical imaging dataset
- Preprocesses the data using nnU-Net tools
- Trains a **2D nnU-Net model**
- Generates segmentation predictions
- Validates the output shapes to ensure correctness

---

## Model Configuration
- **Framework:** nnU-Net v2  
- **Training Mode:** 2D  
- **Task Type:** Medical image segmentation (stroke lesions)

The same configuration (`2d`) is used for both training and inference to ensure valid results.

---

## Project Structure

Stroke-Lesion-nnUNet/
│
├── notebooks/
│ └── Stroke_Lesion_nnUNet.ipynb
│
├── src/
│ ├── dataset_setup.py
│ ├── preprocessing.py
│ ├── training.py
│ ├── inference.py
│ └── evaluation.py
│
├── scripts/
│ └── run_pipeline.py
│
├── outputs/
│ ├── predictions/
│
├── requirements.txt
└── README.md

## How to Run the Project

1. Install the required packages:
```bash
pip install -r requirements.txt
```

## Outputs

Predicted segmentation masks are saved in the outputs/predictions folder
Shape verification ensures that input images, ground truth, and predictions match correctly


