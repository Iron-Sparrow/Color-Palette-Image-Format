import numpy as np
from pathlib import Path
from typing import Final, Union, Optional
import zstandard as zstd


def return_palette_and_indexed_image(pixel_array: np.ndarray, max_palette_size: Optional[int] = None) -> tuple[
    np.ndarray, np.ndarray]:
    """

    :param pixel_array:
    :param max_palette_size:
    :return:
    """


def save_image_to_8bit_copiff(
        pixel_array: np.ndarray,
        output_image_path: Optional[Path] = None,
        limit_palette_size: Optional[int | np.uint8 | np.uint16 | np.uint32] = None,
        metadata: Optional[dict | bytes] = None):
    """

    :param pixel_array:
    :param output_image_path:
    :param limit_palette_size:
    :param metadata:
    :return:
    """
    if pixel_array.dtype != np.uint8:
        raise ValueError("Pixel array must be of type uint8")
    # the pixel aray must be 2D consisting of tuples of 3 uint8 values
    if pixel_array.ndim != 2 or pixel_array.shape[1] != 3:
        raise ValueError("Pixel array must be 2D with shape (n, 3)")

    bits_per_pixel: Final[int] = 8
    magic_number: Final[np.uint16] = np.uint16(0x01D7)
    major_version: Final[np.uint8] = np.uint8(0)
    minor_version: Final[np.uint8] = np.uint8(1)
    file_format_version: Final[tuple[np.uint8, np.uint8]] \
        = major_version, minor_version
