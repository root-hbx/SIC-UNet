import os

def rename_jpg_to_png(directory_path):
    """
    Renames all .jpg files in the specified directory to .png files.

    Args:
    directory_path (str): The path to the directory containing the images.
    """
    # Check if the directory exists
    if not os.path.isdir(directory_path):
        print(f"Error: Directory '{directory_path}' not found.")
        return

    print(f"Scanning directory: '{directory_path}'")
    
    # Iterate over all files in the directory
    for filename in os.listdir(directory_path):
        # Check if the file ends with .jpg
        if filename.lower().endswith('.jpg'):
            # Construct the full old and new file paths
            old_file_path = os.path.join(directory_path, filename)
            base_filename = os.path.splitext(filename)[0]
            new_filename = base_filename + '.png'
            new_file_path = os.path.join(directory_path, new_filename)

            # Perform the renaming operation
            try:
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: '{filename}' -> '{new_filename}'")
            except OSError as e:
                print(f"Error renaming '{filename}': {e}")

    print("\nAll .jpg files have been successfully renamed to .png.")


def rename_png_to_jpg(directory_path):
    """
    Renames all .png files in the specified directory to .jpg files.

    Args:
    directory_path (str): The path to the directory containing the images.
    """
    # Check if the directory exists
    if not os.path.isdir(directory_path):
        print(f"Error: Directory '{directory_path}' not found.")
        return

    print(f"Scanning directory: '{directory_path}'")
    
    # Iterate over all files in the directory
    for filename in os.listdir(directory_path):
        # Check if the file ends with .png
        if filename.lower().endswith('.png'):
            # Construct the full old and new file paths
            old_file_path = os.path.join(directory_path, filename)
            base_filename = os.path.splitext(filename)[0]
            new_filename = base_filename + '.jpg'
            new_file_path = os.path.join(directory_path, new_filename)

            # Perform the renaming operation
            try:
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: '{filename}' -> '{new_filename}'")
            except OSError as e:
                print(f"Error renaming '{filename}': {e}")

    print("\nAll .png files have been successfully renamed to .jpg.")


if __name__ == '__main__':
    # Set the target directory
    target_directory_image = './Dataset/Image'
    target_directory_mask = './Dataset/Mask'
    
    rename_png_to_jpg(target_directory_image)
    rename_jpg_to_png(target_directory_mask)


