import numpy as np
from pathlib import Path
from typing import Final, Union, Optional
import zstandard as zstd


def return_palette_and_indexed_image(pixel_array: np.ndarray, max_palette_size: Optional[int] = None) -> tuple[
    np.ndarray, np.ndarray]:
    """
    Extract a color palette from the pixel array and return both the palette and an indexed version of the image.

    :param pixel_array: Input image as a 2D array with shape (n, 3) where each row is an RGB color value
    :param max_palette_size: Optional maximum number of colors in the palette
    :return: A tuple containing (palette, indexed_image)
             - palette: numpy array of unique colors, shape (palette_size, 3)
             - indexed_image: numpy array where each value is an index into the palette
    """
    # Get the shape of the original image
    height, width, _ = pixel_array.shape

    # Reshape the pixel array to be a list of RGB values
    pixels = pixel_array.reshape(-1, 3)

    # Find unique colors to create the palette
    unique_colors, inverse_indices = np.unique(pixels, axis=0, return_inverse=True)

    # If max_palette_size is specified and we have more unique colors than allowed
    if max_palette_size is not None and len(unique_colors) > max_palette_size:
        # Use a simple frequency-based approach to reduce the palette
        # Count occurrences of each color
        color_counts = np.zeros(len(unique_colors), dtype=np.int32)
        for idx in inverse_indices:
            color_counts[idx] += 1

        # Get indices of the most frequent colors
        most_frequent_indices = np.argsort(color_counts)[-max_palette_size:]
        palette = unique_colors[most_frequent_indices]

        # For remaining colors, find closest match in the reduced palette
        indexed_image = np.zeros(len(pixels), dtype=np.uint8)
        for i, color in enumerate(pixels):
            # Find closest color in the reduced palette
            distances = np.sqrt(np.sum((palette - color) ** 2, axis=1))
            closest_idx = np.argmin(distances)
            indexed_image[i] = closest_idx
    else:
        # No need to reduce palette, use all unique colors
        palette = unique_colors
        indexed_image = inverse_indices

    # Reshape indexed image back to 2D (height x width)
    indexed_image = indexed_image.reshape(height, width)

    return palette, indexed_image


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
