# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. 
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. 
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь. 
# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

from random import choice as rnch

NUMBER_QUEENS = 8
NUMBER_RASTONOVOK = 4

queen1 = [1, 1]
queen2 = [2, 7]
queen3 = [3, 4]
queen4 = [4, 6] 
queen5 = [5, 8] 
queen6 = [6, 2] 
queen7 = [7, 5] 
queen8 = [8, 3] 


def possible_moves(queen: list[int, int]) -> list[list[int, int]]:
    possible_moves_queen = []
    a, b = queen[0], queen[1]
    while a < 8:
        a += 1
        possible_moves_queen.append([a, b])
    a, b = queen[0], queen[1]
    while a > 1:
        a -= 1
        possible_moves_queen.append([a, b])
    a, b = queen[0], queen[1]
    while b > 1:
        b -= 1
        possible_moves_queen.append([a, b])   
    a, b = queen[0], queen[1]
    while b < 8:
        b += 1
        possible_moves_queen.append([a, b])
    a, b = queen[0], queen[1]
    while a < 8 and b < 8:
        a += 1
        b += 1
        possible_moves_queen.append([a, b])   
    a, b = queen[0], queen[1]
    while a < 8 and b > 1:
        a += 1
        b -= 1
        possible_moves_queen.append([a, b])
    a, b = queen[0], queen[1]
    while a > 1  and b > 1:
        a -= 1
        b -= 1
        possible_moves_queen.append([a, b])    
    a, b = queen[0], queen[1]
    while a > 1 and b < 8:
        a -= 1
        b += 1
        possible_moves_queen.append([a, b]) 

    return possible_moves_queen
    

def check (*queen: list[int, int]) -> bool:
    possible_moves1 = {}
    for i in queen:
        possible_moves1[str(i)] = possible_moves(i)
        for key, value in possible_moves1.items():
            if i in value:
                return False 
    return True


def placement(num: int):
    all_cells = []
    for i in range(1,9):
        for j in range(1,9):
            all_cells.append([i, j])
    placement = [rnch(all_cells)]
    all_cells.remove(placement[-1])
    while len(placement) < num:
        placement.append(rnch(all_cells))
        all_cells.remove(placement[-1])
        while check(*(placement)) == False:
            placement.pop()
            placement.append(rnch(all_cells))
            all_cells.remove(placement[-1])
    return placement


def function():	
  try:
    print(f'Растановка ферзей: {placement(NUMBER_QUEENS)}')
  except IndexError:
    function()
 

if __name__ == '__main__':
    print(check(queen1,queen2,queen3,queen4,queen5,queen6,queen7,queen8))
    for _ in range(NUMBER_RASTONOVOK):
        function()