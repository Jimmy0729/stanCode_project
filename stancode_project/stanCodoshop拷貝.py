"""
File: stanCodoshop.py
Name: 鄭翔澤
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage
import math


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    color_distance = math.sqrt((pow(red-pixel.red, 2))+(pow(blue-pixel.blue, 2))+(pow(green-pixel.green, 2)))

    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    '''
    Use for loop to plus the sum of rgb in the list and then divide the
    length of list so we can get a average pixel
    '''
    red_pixel = 0
    blue_pixel = 0
    green_pixel = 0
    for i in range(len(pixels)):
        red_pixel += pixels[i].red
        blue_pixel += pixels[i].blue
        green_pixel += pixels[i].green
    red_pixel = red_pixel // len(pixels)
    blue_pixel = blue_pixel // len(pixels)
    green_pixel = green_pixel // len(pixels)
    average_pixel = [red_pixel, green_pixel, blue_pixel]
    return average_pixel


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    '''
    First, we get the average of pixel and then use the list[0] be the first distance be counted and then
    compare to other element in list, so we can know which element is closest to the average point
    '''
    avg = get_average(pixels)
    min_distance = get_pixel_dist(pixels[0], avg[0], avg[1], avg[2])
    best_pixel = pixels[0]

    for i in range(1, len(pixels)):
        distance = get_pixel_dist(pixels[i], avg[0], avg[1], avg[2])
        if distance < min_distance:
            min_distance = distance
            best_pixel = pixels[i]

    return best_pixel



def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    pixel_package = []
    # It is a list to load every picture points

    for i in range(images[0].width):
        for j in range(images[0].height):
            for k in range(len(images)):
                pixel_package.append(images[k].get_pixel(i, j))
            best_pixel = get_best_pixel(pixel_package)
            new_pixel = result.get_pixel(i, j)
            new_pixel.red = best_pixel.red
            new_pixel.green = best_pixel.green
            new_pixel.blue = best_pixel.blue
            pixel_package = []
            # This list need to be empty so next time it can load new pixel from other ways of picture

    # Write code to populate image and create the 'ghost' effect
    # green_pixel = SimpleImage.blank(20, 20, 'green').get_pixel(0, 0)
    # red_pixel = SimpleImage.blank(20, 20, 'red').get_pixel(0, 0)
    # blue_pixel = SimpleImage.blank(20, 20, 'blue').get_pixel(0, 0)
    # best1 = get_best_pixel([green_pixel, blue_pixel, blue_pixel])
    # print(best1.red, best1.green, best1.blue)

    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()



def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
