import os
import random
import shutil

# Set your directories
raw_images_dir = '/localdata/szhoubx/med_video/dataset/CholecTrack20/yolo_dataset/img'  # Change this to your images directory
raw_labels_dir = '/localdata/szhoubx/med_video/dataset/CholecTrack20/yolo_dataset/label'  # Change this to your labels directory
train_images_dir = '/localdata/szhoubx/med_video/dataset/CholecTrack20/tool_detection/train/images'  # Output directory for training images
train_labels_dir = '/localdata/szhoubx/med_video/dataset/CholecTrack20/tool_detection/train/labels'  # Output directory for training labels
val_images_dir = '/localdata/szhoubx/med_video/dataset/CholecTrack20/tool_detection/val/images'      # Output directory for validation images
val_labels_dir = '/localdata/szhoubx/med_video/dataset/CholecTrack20/tool_detection/val/labels'      # Output directory for validation labels

# Create output directories if they don't exist
os.makedirs(train_images_dir, exist_ok=True)
os.makedirs(train_labels_dir, exist_ok=True)
os.makedirs(val_images_dir, exist_ok=True)
os.makedirs(val_labels_dir, exist_ok=True)

# Get all image files
image_files = [f for f in os.listdir(raw_images_dir) if f.endswith(('.jpg', '.png','.jpeg'))]

# Shuffle the files for randomness
random.shuffle(image_files)

# Define the split ratio
train_ratio = 0.8
train_size = int(len(image_files) * train_ratio)

# Function to copy files if they match
def copy_matching_files(file_list, src_images_dir, src_labels_dir, dest_images_dir, dest_labels_dir):
    for file in file_list:
        # Check if the image file has a corresponding label file
        label_file = os.path.splitext(file)[0] + '.txt'
        if os.path.exists(os.path.join(src_labels_dir, label_file)):
            # Copy image
            shutil.copy(os.path.join(src_images_dir, file), dest_images_dir)
            # Copy corresponding label file
            shutil.copy(os.path.join(src_labels_dir, label_file), dest_labels_dir)

# Split the data into training and validation sets
train_files = image_files[:train_size]
val_files = image_files[train_size:]

# Copy training files
copy_matching_files(train_files, raw_images_dir, raw_labels_dir, train_images_dir, train_labels_dir)

# Copy validation files
copy_matching_files(val_files, raw_images_dir, raw_labels_dir, val_images_dir, val_labels_dir)

print(f"Train files: {len(train_files)}, Validation files: {len(val_files)}")