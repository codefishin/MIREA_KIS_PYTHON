# 1
# для координат
UP = ["UP", "north", "NORTH", "+", "up"]  # Север
DOWN = ["DOWN", "south", "SOUTH", "-", "down"]  # Юг
RIGHT = ["RIGHT", "east", "EAST", "->", "right"]  # Восток
LEFT = ["LEFT", "west", "WEST", "<-", "left"]  # Запад

_directions = [UP, DOWN, RIGHT, LEFT]


class RoomConfig:
    def __init__(self, name: str, description: str,
                 room_connections: list,
                 move_set: list):
        self.name = name
        self.description = description
        self.move_set = []
        self.room_connections = room_connections

        for _ in move_set:
            for index in range(0, 4):
                if _ in _directions[index]:
                    self.move_set.append(_directions[index][0])

        self.directions = list(zip(self.move_set, self.room_connections))


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
        #print(self.directions)
        for index in range(0, len(self.directions)):
            if self.directions[index][0] == "UP":
                print(index + 1, "\b. Travel towards North")
            elif self.directions[index][0] == "DOWN":
                print(index + 1, "\b. Travel towards South")
            elif self.directions[index][0] == "RIGHT":
                print(index + 1, "\b. Travel towards East")
            elif self.directions[index][0] == "LEFT":
                print(index + 1, "\b. Travel towards West")
            else:
                raise Exception("Wrong directions added to room config. Check room creation process.")


    def inputProcessing(self, user_input: int):
        if user_input < 1:
            raise Exception("User has entered a bad number.")
        #print(self.directions[user_input - 1][1])
        return self.directions[user_input - 1][1] - 1


def level_one():  # task 1
    # ["UP", "north", "NORTH", "+", "up"] -> Север
    # ["DOWN", "south", "SOUTH", "-", "down"] -> Юг
    # ["RIGHT", "east", "EAST", "->", "right"] -> Восток
    # ["LEFT", "west", "WEST", "<-", "left"] -> Запад
    rooms = [RoomConfig("Room 1", "You are in room 1", [2],["LEFT"]),  # goto 2
              RoomConfig("Room 2", "You are in room 2", [3, 1], ["west", "east"]),  # goto 3, 1
              RoomConfig("Room 3", "You are in room 3", [4, 2], ["north", "east"]),  # goto 4, 2
              RoomConfig("Room 4", "You are in room 4", [5, 3], ["north", "south"]),  # goto 5, 3
              RoomConfig("Room 5", "You are in room 5", [4, 6], ["south", "east"]),  # goto 4, 6
              RoomConfig("Room 6", "You are in room 6", [15, 7, 5, 11], ["north", "south", "east", "west"]),  # goto 15, 7, 5, 11
              RoomConfig("Room 7", "You are in room 7", [6, 8], ["north", "east"]),  # goto 6, 8
              RoomConfig("Room 8", "You are in room 8", [7, 9], ["west", "east"]),  # goto 7, 9
              RoomConfig("Room 9", "You are in room 9", [10, 8], ["south", "west"]),  # goto 10, 8
              RoomConfig("Room 10", "You are in room 10", [9], ["north"]),  # goto 9
              RoomConfig("Room 11", "You are in room 11", [6, 12], ["west", "east"]),  # goto 6, 12
              RoomConfig("Room 12", "You are in room 12", [13, 11], ["north", "west"]),  # goto 13, 11
              RoomConfig("Room 13", "You are in room 13", [12, 14], ["south", "west"]),  # goto 12, 14
              RoomConfig("Room 14", "You are in room 14", [13], ["east"]),  # goto 13
              RoomConfig("Room 15", "You are in room 15", [0, 6, 16], ["north", "south", "west"]),  # goto win, 6, 16
              RoomConfig("Room 16", "You are in room 16", [15], ["east"])]  # goto 15
    return rooms


# inputs_to_win = [1, 1, 1, 1, 2, 1, 1]


def play_level():
    rooms = level_one()
    current_room = 0
    while 1:
        current_room_data_dir = rooms[current_room].getDirections()
        rooms[current_room].printRoomData()
        userInput = int(input("> "))
        current_room = rooms[current_room].inputProcessing(userInput)
        if current_room == -1:
            print("You win!")
            break


def main():
    # ["UP", "north", "NORTH", "+", "up"] -> Север
    # ["DOWN", "south", "SOUTH", "-", "down"] -> Юг
    # ["RIGHT", "east", "EAST", "->", "right"] -> Восток
    # ["LEFT", "west", "WEST", "<-", "left"] -> Запад

    play_level()


if __name__ == "__main__":
    main()
