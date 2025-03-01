import sys
import math
import tkinter as tk
import random

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


class PacManShader: # 4.3
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


def pseudoRandom(x, y):
    # Простая хеш-функция на основе координат
    n = x * 73856093 + y * 19349663
    n = n ^ (n >> 13)
    n = n * 83492791
    n = n & 0xFFFFFFFF  # Ограничиваем 32 битами

    # Преобразуем в значение от 0 до 1
    return (n % 1000000) / 1000000.0


def noiseShader(master): # 4.4
    w = 512
    h = 512
    canvas = tk.Canvas(master, width=w, height=h)
    canvas.pack()
    for y in range(w):
        for x in range(h):
            noise_value = pseudoRandom(x, y)
            color_value = int(noise_value * 255)
            color = f'#{color_value:02x}{color_value:02x}{color_value:02x}'
            canvas.create_line(x, y, x + 1, y, fill=color)

    master.update()

# <------------- val noise ----------------->

def interpolate(a, b, t): return a + (b - a) * t


def valNoiseShader(master, scale=16):
    w = 512 # width
    h = 512 # height
    # я просто сдался уже использовать mainShader для этого всего
    canvas = tk.Canvas(master, width=w, height=h)
    canvas.pack()

    grid_width = w // scale + 1
    grid_height = h // scale + 1

    grid = [[random.randint(0,255) for _ in range(grid_width)]
            for _ in range(grid_height)] # сетка
    # эмммм в задании 4.4 сказано не использовать random :nerd:
    # зато в задании 4.5 не сказано не использовать random

    for y in range(h):
        for x in range(w):
            grid_x = x // scale # как бы сетка для интер чё-то там слово сложное оно должно
            # быть МЕНЬШЕ общего размера и как бы у нас есть настройка чтобы размер уменьшался (параметр scale)
            grid_y = y // scale

            local_x = (x % scale) / scale # для интер чёто там ну слово сложное
            local_y = (y % scale) / scale

            top_left = grid[grid_y][grid_x] # создание углов для вывода пикселя
            top_right = grid[grid_y][grid_x + 1]
            bottom_left = grid[grid_y + 1][grid_x]
            bottom_right = grid[grid_y + 1][grid_x + 1]

            # bilinear штука
            top = interpolate(top_left, top_right, local_x)
            bottom = interpolate(bottom_left, bottom_right, local_x)
            value = interpolate(top, bottom, local_y)
            # копирка из noise
            color_value = int(value)
            color = f'#{color_value:02x}{color_value:02x}{color_value:02x}'
            canvas.create_line(x, y, x + 1, y, fill=color)


def cloudShader(x, y): # 4.6 TODO
    return x, y, 0


# 4.7 делать не буду

# 5.1
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


# 5.3
def union(*obj):
    objs = list(obj)
    return min(objs)


def intersect(x, y):
    return max(x, y)


def difference(x, y):
    return max(x, -y)


def sdf_square_dif(x, y):
    d = intersect(square(x - 0.5, y - 0.5, 0.4),
                   circle(x - 0.5, y - 0.5, 0.3))
    return d > 0, abs(d) * 3, 0

# 5.4

def sdf_freddy_fazbear(x, y):  # пойдёт
    d = union(circle(x - 0.25, y - 0.25, 0.15),
              circle(x - 0.75, y - 0.25, 0.15),
              circle(x - 0.5, y - 0.5, 0.35))
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
            elif task == "3": # я не буду это делать через mainShader
                root = tk.Tk()
                PacManShader(root)
                root.mainloop()
            elif task == "4": # и это тоже, дальше подозреваю тоже
                root = tk.Tk()
                noiseShader(root)
                root.mainloop()
            elif task == "5":
                root = tk.Tk()
                root.title("qr-code looking aah")
                valNoiseShader(root, scale=16) # scale можно не вводить
                root.mainloop()
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
                mainShader(sdf_freddy_fazbear) # TODO
            elif task == "5":
                mainShader(sdf_square) # TODO
        else:
            print("Такого варианта нет.\n")


if __name__ == '__main__':
    main()
