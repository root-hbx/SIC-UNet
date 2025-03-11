import os

# List files in the working directory
print("Files in current directory:", os.listdir())

# Check if the model file exists
model_path = "unet_model1.keras"
if os.path.exists(model_path):
    print(f"✅ Model file '{model_path}' found!")
else:
    print(f"❌ Model file '{model_path}' is missing!")