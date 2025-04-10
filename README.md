# Color Palette Image File Format (CoPIFF)

CoPIFF is a file format in order to store an image consisting of a color palette (non-redundant colors) followed by the pixels which contain the index of the color in the palette.

The file itself is binary for which gets compressed using Zstandard.

The CoPIFF files are using arrays of unsigned integers to store the color palette and the pixels.

The palette itself may be limited to a certain number of colors, which if it is defined, will convert the least common pixels to the closest color in the palette.
This can be used in order to reduce file size at the cost of precision.

## File Extension

The file extension for CoPIFF files are:
 - `.copiff` (recommended)
 - `.copif`
 - `.CoPIFF` (not recommended but still correct)

## File Structure

The CoPIFF file format is a file format that consists of a series of "magic numbers" which determine the characteristics of the file:

  - It begins with an unsigned integer, which is a confirmation that it is in fact a CoPIFF file. It is either `401` or `471`. (in hexadecimal: `0x0191` or `0x01D7`)
  - Followed by 2 bytes which are representing the version of the file format. The first byte is the major version and the second byte is the minor version.
  - It is followed by a byte which is the number of bits per pixel. It can be either `8`, `16`, or `32`. (Currently only the 8 bit mode is supported)
  - It is then followed by 4-bytes which represent the palette length. It represents the amount of different colors there are in the palette (non-redundant colors of the RGB).
  - It is then followed by the size of the `x` axis and the size of the `y` axis. (4 bytes each which makes in total 8 bytes.)
  - It is then followed by 3 empty bytes which are reserved for future use.

Following these "magic numbers" comes the actual image data:

  - The palette consists of a series of unsigned integers of the length specified by the number of bits per pixel.<br>For now it only has support for 8 bits per pixel. The palette itself is a series of 3 bytes representing the RGB for each color in the palette. Every 3 bytes are one color.
  - When the last color of the palette is reached (thanks to the magic number indicating the palette length), it is followed by a series of unsigned integers which are the index of the required color in the palette.
  - The pixels are sorted into a flattened array with the `x` axis first and the `y` axis second. That means that the pixels are stored in a row-major order. The first pixel is the top-left pixel and the last pixel is the bottom-right pixel.<br>The array is arrange by rows which follow each other and every time we reach the size of the `x` axis, we increment the `y` axis.
  - Finally, at the end of the file, when we get out of the pixel array, we have metadata which is additional data that may be left there by other software or that indicate supplementary indications about the image. This metadata is not required and can be ignored by the software that reads the file. It is just there for additional information.<br>**BY DEFINITION, THE METADATA CANNOT BE EXECUTED AND CAN'T CONTAIN ANY CODE OR INFORMATION THAT COULD LEAD TO UNWANTED RESULTS.**

## Planned Features for future versions
- Support for 16 and 32 bits per pixel (unsigned integers).
- Support for 16, 32, and 64 bits per pixel (floating point).
- Support for `RGBA` format.
- Support for `BBR` format.
- Support for `BGRA` format.
- Support for `CMYK` format.
- Support for `HSV` format.
- Support for `HSL` format.
- Support for different Color Spaces/Color Profiles like `sRGB (1999)`, `Adobe RGB (1998)`, etc.