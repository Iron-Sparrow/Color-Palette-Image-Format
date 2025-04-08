from PIL import Image
from pathlib import Path

def convert_image_to_ppm(image_file_path:Path|str):
    if type(image_file_path) == str:
        # Convert to path
    