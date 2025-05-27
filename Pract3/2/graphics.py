from typing import Sized

import matplotlib.pyplot as plt
import matplotlib as mpl
import random


def generate_symmetric_image(bounds_int=1):
    image = [[0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]
    for x in range(0, len(image)):
        for y in range(0, 5):
            image[x][y] = random.randint(0, bounds_int)
            image[x][len(image)-1-y] = image[x][y]
    return image

def generate_symmetric_image_with_border(bounds_int=1):
    image = [[0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0]]
    for x in range(1, len(image) - 1):
        for y in range(2, 6):
            image[x][y] = random.randint(0, bounds_int)
            image[x][len(image)-1-y] = image[x][y]
    return image

# 1

def first_image_preset():
    colors = ['black', 'white']
    bounds = [0, 1]

    cmap = mpl.colors.ListedColormap(colors)
    norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

    my_image = [[1, 1, 0, 1, 1],
                [0, 1, 1, 1, 0],
                [0, 0, 1, 0, 0],
                [1, 0, 0, 0, 1],
                [0, 0, 0, 0, 0]]

    plt.imshow(my_image, interpolation='none', cmap=cmap, norm=norm)
    plt.show()

def first_image_random():
    colors = ['black', 'white']
    bounds = [0, 1]

    cmap = mpl.colors.ListedColormap(colors)
    norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

    my_image = generate_symmetric_image()

    plt.imshow(my_image, interpolation='none', cmap=cmap, norm=norm)
    plt.show()

# 2

def get_x_image(image, size=7, bounds=1):
    for _ in range(0, size):
        image = [a + b for a, b in zip(generate_symmetric_image_with_border(bounds_int=bounds),
                                       image)]
    return image


def get_y_image(image, size=7, bounds=1):
    for _ in range(0, size):
        new_image = generate_symmetric_image_with_border(bounds_int=bounds)
        for y in range(0, 7):
            image.append(new_image[y])
    return image


def loads_of_images_as_one(size_x=20,size_y=10):
    colors = ['black', 'white']
    bounds = [0, 1]

    image = generate_symmetric_image_with_border()
    tmp = generate_symmetric_image_with_border()
    cmap = mpl.colors.ListedColormap(colors)
    norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

    image = get_x_image(image, size_x)
    for _ in range(0, size_y):
        tmp = get_x_image(tmp, size_x)
        for y in range(0, 7):
            image.append(tmp[y])
        tmp = generate_symmetric_image_with_border()

    plt.imshow(image, interpolation='none', cmap=cmap, norm=norm)
    plt.show()

# 3

def loads_of_images_as_one_colored(size_x=20,size_y=10):
    colors = [[0,0,0], [29, 43, 83], [126, 37, 83], [0, 135, 81],
              [171, 82, 54], [95, 87, 79], [194, 195, 199],
              [255, 241, 232], [255, 0, 77], [255, 163, 0],
              [255, 236, 39], [0, 228, 54], [41, 173, 255],
              [131, 118, 156], [255, 119, 168], [255, 204, 170],]
    bounds = []
    for _ in range(0, len(colors)):
        bounds.append(_)

    image = generate_symmetric_image_with_border(bounds_int=len(bounds))
    tmp = generate_symmetric_image_with_border(bounds_int=len(bounds))
    cmap = mpl.colors.ListedColormap(colors)
    norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

    image = get_x_image(image, size_x, bounds=len(bounds))
    for _ in range(0, size_y):
        tmp = get_x_image(tmp, size_x, bounds=len(bounds))
        for y in range(0, 7):
            image.append(tmp[y])
        tmp = generate_symmetric_image_with_border(bounds_int=len(bounds))

    plt.imshow(image, interpolation='nearest', cmap=cmap, norm=norm)
    plt.show()

# main

def main():
    inp = 1
    print("Enter 1 to launch 1st task\n"
          "Enter 2 to launch 2nd task\n"
          "Enter 3 to launch 3rd task\n"
          "Enter 0 to exit\n")
    while inp != 0:
        inp = int(input(">: "))
        if inp == 1:
            first_image_random()
        elif inp == 2:
            loads_of_images_as_one(size_x=20, size_y=10)
        elif inp == 3:
            loads_of_images_as_one_colored(size_x=20, size_y=10)


if __name__ == "__main__":
    main()
