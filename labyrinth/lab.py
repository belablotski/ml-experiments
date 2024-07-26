import random

class Labyrinth(object):

    WALL = 999

    def __init__(self, rows, cols, walls_prc = 0.35) -> None:
        super().__init__()
        self.__rows = rows
        self.__cols = cols
        self.__start_row = self.__start_col = 0
        self.__exit_row = self.__rows - 1
        self.__exit_col = self.__cols - 1
        self.__lab = [[self.WALL if random.random() <= walls_prc else 0 for _ in range(self.__cols)] for _ in range(self.__rows)]
        self.__lab[self.__start_row][self.__start_col] = 0
        self.__lab[self.__exit_row][self.__exit_col] = 0

    def print(self) -> None:
        for row in self.__lab:
            for cell in row:
                print(f'{cell:5}', end='')
            print()

    def __find_exit_backwards(self, row, col, distance) -> int:
        achievable_distances = []

        if self.__lab[row][col] > distance or self.__lab[row][col] == 0:
            self.__lab[row][col] = distance

            if (row, col) == (self.__start_row, self.__start_col):
                return distance

            next_steps = [(row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)]

            for next_step in next_steps:
                (r, c) = next_step
                if 0 <= r < self.__rows and 0 <= c < self.__cols:
                    if self.__lab[r][c] != self.WALL:
                        achievable_distance = self.__find_exit_backwards(r, c, distance + 1)
                        if achievable_distance > 0:
                            achievable_distances.append(achievable_distance)

        return min(achievable_distances) if achievable_distances else -1
    
    def find_exit(self) -> bool:
        return self.__find_exit_backwards(self.__exit_row, self.__exit_col, 1)

lab = Labyrinth(6, 8)
lab.print()
print(f'\nExit path lenght: {lab.find_exit()}\n')
lab.print()
