from PIL import Image
from PIL.ImageFile import ImageFile
from pathlib import Path


def convert_image_to_ppm(image_file_path: Path) -> Path:
    """
    Convert any image to the PPM format (8bit) to be used to convert into the Color Palette Image File Format.

    :param image_file_path:
    :return:
    """
    image = (Image.open(image_file_path)).convert("RGB")
    output_path: Path = image_file_path.with_suffix('.ppm')
    image.save(output_path, format='PPM')
    return output_path
