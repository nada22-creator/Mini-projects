import os
import logging
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
import matplotlib.pyplot as plt

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

# Paths
path = r"C:\Users\21653\Desktop\imgs"
pathOut = r"C:\Users\21653\Desktop\editedImgs"

# Create output folder if it doesn't exist
os.makedirs(pathOut, exist_ok=True)

def process_image(file_path, save_path):
    try:
        img = Image.open(file_path)

        # Resize for dataset consistency (e.g., 256x256)
        img = img.resize((256, 256))

        # Apply multiple edits
        edit = (
            img.filter(ImageFilter.DETAIL)    # Enhance details
               .convert('L')                  # Grayscale
               .rotate(-90)                   # Rotate
        )

        # Contrast adjustment
        factor = 1.8
        enhancer = ImageEnhance.Contrast(edit)
        edit = enhancer.enhance(factor)

        # Normalize pixels (ML preprocessing step)
        arr = np.array(edit) / 255.0  # Scale between 0 and 1
        norm_img = Image.fromarray((arr * 255).astype(np.uint8))

        # Save edited image
        norm_img.save(save_path)
        logging.info(f"Saved: {save_path}")

        # Plot histogram of pixel intensities (data insight)
        plt.hist(arr.flatten(), bins=50, color="gray")
        plt.title(f"Histogram - {os.path.basename(save_path)}")
        plt.xlabel("Pixel Intensity")
        plt.ylabel("Frequency")
        plt.savefig(save_path.replace(".jpg", "_hist.png"))
        plt.close()

    except Exception as e:
        logging.error(f"Failed to process {file_path}: {e}")

# Process all images
for filename in os.listdir(path):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        file_path = os.path.join(path, filename)
        clean_name = os.path.splitext(filename)[0]
        save_path = os.path.join(pathOut, f"{clean_name}_processed.jpg")
        process_image(file_path, save_path)
