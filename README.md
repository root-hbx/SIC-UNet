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
├── metadata.csv                 # A CSV file linking the images to their respective masks
├── flood_segmentation.ipynb     # Jupyter notebook with the model code
├── README.md                    # Project description and instructions
```
## Model Architecture
The model used in this project is a U-Net, a popular architecture for image segmentation tasks.
### U-Net Architecture
-**Encoder**: A series of convolutional layers and max pooling layers that capture the context of the input image.
-**Bottleneck**: The deepest part of the network where high-level features are learned.
-**Decoder**: A series of up-sampling layers and convolutional layers that help reconstruct the spatial dimensions of the input image.
-**Connections**: Links between encoder and decoder layers to retain fine details.
The U-Net model is trained to predict flood areas from the input images.

## Requirements
To run this project, you'll need the following libraries:
Python 3.x
TensorFlow
NumPy
Matplotlib
Pandas

## Results

Here is an example of the results from the model:

![Model Results](Dataset/Predicted%20Mask%20BW.png)
