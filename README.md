# RGB565 to RGB888 to PNG -> python
Convert array RGB565 to RGB888 and then to PNG in python

This algorithm is intended to assemble an image from an array that consists of pixel to pixel of an image.
The Format of the array contains a sequence of type RGB565. Where there are respectively 5 bits for the color red, 6 for the green color and 5 for the blue color.
The frame assembly process can be better explained at this site:

http://www.barth-dev.de/online/rgb565-color-picker/

Just call your array containing all the pixels. And set the width and height of the image.
I also left a test sequence to check if the pixel position is correct.
