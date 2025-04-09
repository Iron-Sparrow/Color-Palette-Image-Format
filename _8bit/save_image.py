import numpy as np
from pathlib import Path

def save_image_to_8bit_color_palette_image_file_format(pixel_array:np.ndarray[dtype], output_image_path:None|Path=None, limit_palette_size: int | np.uint8 | np.uint16 | np.uint32 = None):
    """
        ...
    """