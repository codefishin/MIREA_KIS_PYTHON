import sys
import math
import tkinter as tk
from doctest import master


def draw(shader, width, height):
    image = bytearray((0, 0, 0) * width * height)
    for y in range(height):
        for x in range(width):
            pos = (width * y + x) * 3
            color = shader(x / width, y / height)
            normalized = [max(min(int(c * 255), 255), 0) for c in color]
            image[pos:pos + 3] = normalized
    header = bytes(f'P6\n{width} {height}\n255\n', 'ascii')
    return header + image


def mainShader(shader):
    label = tk.Label()
    img = tk.PhotoImage(data=draw(shader, 256, 256)).zoom(2, 2)
    label.pack()
    label.config(image=img)
    tk.mainloop()


def blackSquareShader(x, y): # 4.1
    return 0, 0, 0 # rgb

def circleShader(x, y): # 4.2
    s = 0.6
    d = 0.53
    d2 = 1 - d
    r2 = ((x - d2) ** 2 + (y - d2) ** 2) * 2 - (s ** 2)
    r1 = ((x - d) ** 2 + (y - d) ** 2) * 2 - (s ** 2)
    return -r1 - (r1 * 2), -r2 + (-r2 * 2), 0


class pacManShader: # 4.3
    def __init__(self, mast):
        self.master = mast
        self.canvas = tk.Canvas(mast, width=400, height=400, bg="black")
        self.canvas.pack()
        self.draw_pacman(200, 200, 120, 45)

    def draw_pacman(self, x, y, radius, angle):
        self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="yellow", outline="black")
        self.canvas.create_oval(240, 110, 200, 150, fill="black")
        # Вычисляем координаты для треугольника
        points = [
            (x, y),  # центр
            (x + radius * math.cos(math.radians(angle)) + x * 0.2, y - radius * math.sin(math.radians(angle))),  # точка на границе
            (x + radius * math.cos(math.radians(-angle)) + x * 0.2, y - radius * math.sin(math.radians(-angle))),  # другая точка на границе
        ]
        # Рисуем треугольник Pac-Man
        self.canvas.create_polygon(points, fill="black")


def noiseShader(x, y): # 4.4 TODO
    return x, y, 0


def valNoiseShader(x, y): # 4.5 TODO
    return x, y, 0


def cloudShader(x, y): # 4.6 TODO
    return x, y, 0


# 4.7 делать не буду

### ниже задание 5 ###

### 5.1
def circle(x, y, r):
    return x ** 2 + y ** 2 - r ** 2


def sdf_circle(x, y):
    d = circle(x - 0.5, y - 0.5, 0.45)
    return d > 0, abs(d) * 3, 0


### 5.2
def square(x, y, s):
    return max(abs(x), abs(y)) - s


def sdf_square(x, y):
    d = square(x - 0.5, y - 0.5, 0.4)
    return d > 0, abs(d) * 3, 0


# 5.3 FIXME func: difference

def union(x, y):
    return x + y


def intersect(x, y):
    return max(x, y) - min(x, y)

def difference(x, y):
    return min(x, y) * max(x, y) # где цвет))

def sdf_square_dif(x, y):
    d = difference(square(x - 0.5, y - 0.5, 0.4), circle(x - 0.5, y - 0.5, 0.3))
    return d > 0, abs(d) * 3, 0



def main():
    while 1:
        choice = input("Введите номер задания (от 4 до 5): ")
        if choice == "4":
            task = (input("Введите подраздел задания (от 1 до 6): "))
            if task == "1":
                mainShader(blackSquareShader)
            elif task == "2":
                mainShader(circleShader)
            elif task == "3":
                root = tk.Tk()
                pacManShader(root) # я не буду это делать через mainShader
                root.mainloop()
            elif task == "4":
                mainShader(noiseShader)
            elif task == "5":
                mainShader(valNoiseShader)
            elif task == "6":
                mainShader(cloudShader)

        elif choice == "5":
            task = (input("Введите подраздел задания (от 1 до 5): "))
            if task == "1":
                mainShader(sdf_circle)
            elif task == "2":
                mainShader(sdf_square)
            elif task == "3":
                mainShader(sdf_square_dif)
            elif task == "4":
                mainShader(sdf_square) # TODO
            elif task == "5":
                mainShader(sdf_square) # TODO
        else:
            print("Такого варианта нет.\n")


if __name__ == '__main__':
    main()
