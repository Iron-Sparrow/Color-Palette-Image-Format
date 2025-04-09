# Color Palette Image File Format (CoPIFF)

CoPIFF is a file format in order to store an image consisting of a color palette (non-redundant colors) followed by the pixels which contain the index of the color in the palette.

The file itself is binary for which gets compressed using Zstandard.

The CoPIFF files are using arrays of unsigned integers to store the color palette and the pixels.

## File Extension

The file extension for CoPIFF files is:
 - `.copiff` (recommended)
 - `.copif`

Although all of the presented file extensions are functional, the first one is recommended to be used. (Here it means `.8copiff`, `.16copiff`, `.32copiff`)

## File Structure

The CoPIFF file format is a file format that consists of a series of "magic numbers" which determine the characteristics of the file:
  - It begins with an unsigned integer, which is a confirmation that it is in fact a CoPIFF file. It is either `401` or `471`. (in hexadecimal: `0x191` or `0x1D7`)
  - 
