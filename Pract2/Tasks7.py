import gvgen as gv
import sys


# для координат
UP = ["UP", "north", "NORTH", "+", "up"]  # Север
DOWN = ["DOWN", "south", "SOUTH", "-", "down"]  # Юг
RIGHT = ["RIGHT", "east", "EAST", "->", "right"]  # Восток
LEFT = ["LEFT", "west", "WEST", "<-", "left"]  # Запад

_directions = [UP, DOWN, RIGHT, LEFT]


class RoomConfig:
    def __init__(self, name: str, description: str,
                 room_connections: list,
                 move_set: list, dir_desc: list):
        self.name = name
        self.description = description
        self.move_set = []

        for _ in move_set:
            for index in range(0, 4):
                if _ in _directions[index]:
                    self.move_set.append(_directions[index][0])

        self.directions = list(zip(self.move_set, room_connections, dir_desc))
        # print(self.directions)

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getMoves(self):
        return self.move_set

    def getDirections(self):
        return self.directions

    def printRoomData(self):
        # ["UP", "north", "NORTH", "+", "up"] -> Север
        # ["DOWN", "south", "SOUTH", "-", "down"] -> Юг
        # ["RIGHT", "east", "EAST", "->", "right"] -> Восток
        # ["LEFT", "west", "WEST", "<-", "left"] -> Запад
        print(self.name, '\n', self.description)
        # print(self.directions)
        for index in range(0, len(self.directions)):
            if self.directions[index][0] == "UP":
                print(index + 1, "\b. Проход на Север.",
                      self.directions[index][2])
            elif self.directions[index][0] == "DOWN":
                print(index + 1, "\b. Проход на Юг.",
                      self.directions[index][2])
            elif self.directions[index][0] == "RIGHT":
                print(index + 1, "\b. Проход на Восток.",
                      self.directions[index][2])
            elif self.directions[index][0] == "LEFT":
                print(index + 1, "\b. Проход на Запад.",
                      self.directions[index][2])
            else:
                raise Exception("Wrong directions added "
                                "to room config. "
                                "Check room creation process.")

    def inputProcessing(self, inp: int):
        if inp < 1:
            raise Exception("Bad number.")
        return self.directions[inp - 1][1] - 1


def levelConfiguration():
    # ["UP", "north", "NORTH", "+", "up"] -> Север
    # ["DOWN", "south", "SOUTH", "-", "down"] -> Юг
    # ["RIGHT", "east", "EAST", "->", "right"] -> Восток
    # ["LEFT", "west", "WEST", "<-", "left"] -> Запад
    graph = gv.GvGen()  # В задаче не указано, чтобы генерация была нормальная
    # это пока сойдёт.
    node1 = graph.newItem("1")
    node2 = graph.newItem("2")
    _ = graph.newLink(node1, node2)
    _ = graph.newLink(node2, node1)
    node1 = graph.newItem("3")
    _ = graph.newLink(node1, node2)
    _ = graph.newLink(node2, node1)
    node2 = graph.newItem("4")
    _ = graph.newLink(node1, node2)
    _ = graph.newLink(node2, node1)
    node1 = graph.newItem("5")
    _ = graph.newLink(node1, node2)
    _ = graph.newLink(node2, node1)
    node2 = graph.newItem("6")  # keep track of
    _ = graph.newLink(node1, node2)
    _ = graph.newLink(node2, node1)
    node1 = graph.newItem("7")
    _ = graph.newLink(node1, node2)
    _ = graph.newLink(node2, node1)
    node3 = graph.newItem("8")
    _ = graph.newLink(node3, node1)
    _ = graph.newLink(node1, node3)
    node1 = graph.newItem("9")
    _ = graph.newLink(node3, node1)
    _ = graph.newLink(node1, node3)
    node3 = graph.newItem("10")
    _ = graph.newLink(node3, node1)
    _ = graph.newLink(node1, node3)
    node11 = graph.newItem("11")
    _ = graph.newLink(node2, node11)
    _ = graph.newLink(node11, node2)
    node12 = graph.newItem("12")
    _ = graph.newLink(node12, node11)
    _ = graph.newLink(node11, node12)
    node11 = graph.newItem("13")
    _ = graph.newLink(node12, node11)
    _ = graph.newLink(node11, node12)
    node12 = graph.newItem("14")
    _ = graph.newLink(node12, node11)
    _ = graph.newLink(node11, node12)
    node15 = graph.newItem("15")
    _ = graph.newLink(node2, node15)
    _ = graph.newLink(node15, node2)
    node16 = graph.newItem("16")
    _ = graph.newLink(node16, node15)
    _ = graph.newLink(node15, node16)
    node_end = graph.newItem("END")
    _ = graph.newLink(node15, node_end)
    stdout = sys.stdout  # сойдёт
    f = open("map.dot", "a")  # рофл
    sys.stdout = f
    graph.dot(fd=f)
    sys.stdout = stdout  # рофл окончен
    f.close()
    rooms = [RoomConfig("Комната #1", "Вы стоите у высоких, древних ворот, "
                                      "ведущих в лабиринт,"
                                      "чьи стены уходят в туман, "
                                      "скрывая его тайны."
                                      "Воздух здесь прохладный, "
                                      "и где-то вдалеке слышится "
                                      "эхо капающей воды. "
                                      "Сможете ли вы найти выход?",
                        [2], ["LEFT"],
                        dir_desc=["Ваши шаги эхом раздаются "
                                  "по коридору,"
                                  "уводящему вглубь "
                                  "лабиринта. (#2)"]),  # goto 2
             RoomConfig("Комната #2", "Вы находитесь в узкой, "
                                      "извилистой комнате, "
                                      "где стены украшены "
                                      "древними рунами, "
                                      "светящимися при "
                                      "слабом свете. "
                                      "Кажется, что каждая "
                                      "руна несёт своё сообщение.",
                        [3, 1],
                        ["west", "east"],
                        dir_desc=["Путь идёт дальше, "
                                  "скрываясь в тени. (#3)",
                                  "Вы можете вернуться назад. "
                                  "(#1)"]),  # goto 3, 1
             RoomConfig("Комната #3", "Эта комната "
                                      "напоминает подземное озеро. "
                                      "Вода мерцает зелёным светом, "
                                      "отражая странные формы на стенах. "
                                      "В центре комнаты стоит "
                                      "древний каменный алтарь.",
                        [4, 2],
                        ["north", "east"],
                        dir_desc=["Путь ведёт через пещеру, "
                                  "наполненную эхом "
                                  "капающей воды. (#4)",
                                  "Путь обратно "
                                  "к рунам. (#2)"]),  # goto 4, 2
             RoomConfig("Комната #4",
                        "Вы оказались в огромной зале, "
                        "поддерживаемой колоннами из чёрного камня. "
                        "В центре залы горит вечный огонь, "
                        "освещая древние фрески на стенах.",
                        [5, 3], ["north", "south"],
                        dir_desc=["Путь ведёт через таинственную "
                                  "дверь, украшенную символами. (#5)",
                                  "Вы можете вернуться к озеру. (#3)"]),
             RoomConfig("Комната #5",
                        "Эта комната наполнена странными звуками, "
                        "похожими на шёпот ветра. "
                        "На стенах висят старинные ковры, "
                        "изображающие сцены из легенд.",
                        [4, 6], ["south", "east"],
                        dir_desc=["Обратно к огню и фрескам. (#4)",
                                  "Путь ведёт через тёмный коридор. (#6)"]),
             RoomConfig("Комната #6",
                        "Вы находитесь в комнате, "
                        "где воздух наполнен запахом мёда и лаванды. "
                        "На стенах развешаны зеркала, "
                        "искажающие ваше отражение.",
                        [15, 7, 5, 11], ["north", "south", "east", "west"],
                        dir_desc=["Путь ведёт в неизвестное. (#15)",
                                  "Вниз, в комнату с коврами. (#7)",
                                  "Обратно к шёпоту. (#5)",
                                  "Путь ведёт через "
                                  "светлый коридор. (#11)"]),
             RoomConfig("Комната #7",
                        "Эта комната напоминает древний библиотекарский зал. "
                        "Полки, уходящие вверх, полны старинных "
                        "книг и свитков.",
                        [6, 8], ["north", "east"],
                        dir_desc=["Путь обратно к зеркалам. (#6)",
                                  "В комнату, где воздух "
                                  "наполнен ароматами. (#8)"]),  # goto 6, 8
             RoomConfig("Комната #8",
                        "Вы находитесь в комнате, напоминающей тронный зал. "
                        "В центре стоит пустой трон, "
                        "окружённый статуями древних стражей.",
                        [7, 9], ["west", "east"],
                        dir_desc=["Обратно к книгам. (#7)",
                                  "Путь ведёт через коридор "
                                  "с колоннами. (#9)"]),  # goto 7, 9
             RoomConfig("Комната #9",
                        "Эта комната полна звуков падающей воды. "
                        "В центре находится водопад, "
                        "падающий в подземное озеро, "
                        "его брызги создают радугу в воздухе.",
                        [10, 8], ["south", "west"],
                        dir_desc=["Путь ведёт вниз, к пещере. (#10)",
                                  "Обратно к тронному залу. (#8)"]),
             RoomConfig("Комната #10",
                        "Вы находитесь в пещере, "
                        "где воздух насыщен влагой. "
                        "На стенах видны следы древних наскальных рисунков.",
                        [9], ["north"],
                        dir_desc=["Обратно к водопаду. (#9)"]),  # goto 9
             RoomConfig("Комната #11",
                        "Эта комната напоминает сад, "
                        "выращенный в подземелье. "
                        # тут ошибка была в написании
                        "Растения здесь светятся мягким светом, "
                        "создавая атмосферу спокойствия.",
                        [6, 12], ["west", "east"],
                        dir_desc=["Обратно к зеркалам. (#6)",
                                  "Путь ведёт через "
                                  "светлый коридор. (#12)"]),  # goto 6, 12
             RoomConfig("Комната #12",
                        "Вы находитесь в комнате, "
                        "где стены украшены мозаиками, "
                        "изображающими сцены из древних легенд. "
                        "В центре стоит фонтан, "
                        "из которого течёт кристально "
                        "чистая вода.",
                        [13, 11], ["north", "west"],
                        dir_desc=["Путь ведёт через каменные двери. (#13)",
                                  "Обратно к саду. (#11)"]),  # goto 13, 11
             RoomConfig("Комната #13",
                        "Эта комната напоминает древний храм. "
                        "В центре стоит монолит, на котором "
                        "высечены странные символы. "
                        "Воздух здесь наэлектризован.",
                        [12, 14], ["south", "west"],
                        dir_desc=["Обратно к фонтану. (#12)",
                                  "Путь ведёт через тёмный коридор. (#14)"]),
             RoomConfig("Комната #14",
                        "Вы находитесь в комнате, "
                        "где стены покрыты мхом, "
                        "а воздух наполнен запахом земли. "
                        "В центре комнаты растёт древнее дерево, "
                        "корни которого уходят глубоко вниз.",
                        [13], ["east"],
                        dir_desc=["Путь обратно к храму. (#13)"]),  # goto 13
             RoomConfig("Комната #15",
                        "Вы находитесь в комнате, "
                        "наполненной светом, "
                        "исходящим из кристаллов на стенах. "
                        "В центре стоит портал, "
                        "светящийся ярким белым светом.",
                        [0, 6, 16], ["north", "south", "west"],
                        dir_desc=["Вы выбрались из лабиринта!",
                                  "Обратно к зеркалам. (#6)",
                                  "Путь ведёт через комнату "
                                  "с древними кристаллами. (#16)"]),
             RoomConfig("Комната #16",
                        "Вы находитесь в комнате, "
                        "где стены покрыты кристаллами, "
                        "издающими мелодичные звуки при прикосновении. "
                        "В центре комнаты стоит каменная плита, "
                        "на которой высечена карта лабиринта.",
                        [15], ["east"],
                        dir_desc=["Путь обратно к порталу. (#15)"])]
    return rooms


inputs_to_win = [1, 1, 1, 1, 2, 1, 1]


def playLevel(*, cheat=False):
    rooms = levelConfiguration()
    current_room = 0

    if cheat is True:
        for _ in inputs_to_win:
            rooms[current_room].printRoomData()
            print(">", _)
            current_room = rooms[current_room].inputProcessing(_)
            if current_room == -1:
                print("Игра окончена.")
                return -1

    while 1:
        rooms[current_room].printRoomData()
        user_input = int(input("> "))
        current_room = rooms[current_room].inputProcessing(user_input)
        if current_room == -1:
            print("Игра окончена.")
            return 1


def main():
    # ["UP", "north", "NORTH", "+", "up"] -> Север
    # ["DOWN", "south", "SOUTH", "-", "down"] -> Юг
    # ["RIGHT", "east", "EAST", "->", "right"] -> Восток
    # ["LEFT", "west", "WEST", "<-", "left"] -> Запад

    playLevel(cheat=True)


if __name__ == "__main__":
    main()
