# Image Steganography using Python

An effective menu driven GUI made using Tkinter which takes in an image and returns a new image with the text data encoded in the pixels.In this, we hide the data in image as a secret message and only decode it when we type the correct password.

## Dependencies

1. Pillow: Used for reading/modifying image files.

## Installation

1. Use the following command to install the requirements.

`pip install -r requirements.txt`

> Note: The program works only for `.png` files. Reason being image extensions like `.jpeg` uses lossy compressions which means the image pixel data is not preserved.
