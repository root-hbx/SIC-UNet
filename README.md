# Flood Area Segmentation Using U-Net

This project involves flood area segmentation using a U-Net model. The goal of the project is to train a model to predict flood areas from images using a U-Net architecture. The dataset contains flood images, corresponding masks for the flood areas, and a CSV file that links images with their masks.

## Project Structure

The project contains the following components:

- **Image Dataset**: The input images used for training and validation.
- **Mask Dataset**: The corresponding segmentation masks indicating flood areas.
- **CSV File**: A CSV file linking the images to their respective masks.
- **Jupyter Notebook**: Contains the full workflow for loading the data, training the U-Net model, validating it, and visualizing the predictions.

### Directory Structure

```bash
├── datasets/
│   ├── images/                 # Folder containing the flood images
│   ├── masks/                  # Folder containing the segmentation masks
│   └── links.csv               # CSV file linking images to masks
├── flood_segmentation.ipynb     # Jupyter notebook with the model code
├── README.md                    # Project description and instructions
└── .gitignore                   # Ignored files and folders (e.g., dataset, system files)
