# Условие задачи: На столе лежит n-ное количество конфт. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем m конфет. Выигрывает игрок забравший последнюю конфету.
import os
import random
print('Условия игры')
initial_quantity = int(input('Введите начальное количество конфет: '))
max_step = int(input('Введите какое количество конфет можно взять за один ход: '))
game_mode = input('Выберите режим игры: \n 1 - игрок против игрока; \n 2 - игрок против компьютера (простой режим); \n 3 - игрок против компьютера (сложный режим).\n')
match game_mode:
    case '1':
        while initial_quantity > 0:
            os.system('CLS')
            print(f'Осталось конфет: {initial_quantity}')
            player_1 = int(input(f'ход игрока 1 (1-{max_step}):'))
            while player_1 < 1 or player_1 > max_step:
                player_1 = int(
                    input(f'не допустимое значение, ход игрока 1 (1-{max_step}): '))
            initial_quantity -= player_1
            if initial_quantity < 1:
                print('Игрок 1 победил')
            else:
                os.system('CLS')
                print(f'Осталось конфет: {initial_quantity}')
                player_2 = int(input(f'ход игрока 2 (1-{max_step}):'))
                while player_2 < 1 or player_2 > max_step:
                    player_2 = int(
                        input(f'не допустимое значение, ход игрока 2 (1-{max_step}): '))
                initial_quantity -= player_2
                if initial_quantity < 1:
                    print('Игрок 2 победил')
    case '2':
        toss = (random.randint(0, 1))
        if toss == 0:
            print('Первым ходит игрок')
        else:
            print('Первым ходит бот')
        input('Нажмите ввод для начала игры')
        os.system('CLS')
        while initial_quantity > 0:
            if toss == 0:
                print(f'Осталось конфет: {initial_quantity}')
                step_player = int(input(f'ход игрока (1-{max_step}):'))
                while step_player < 1 or step_player > max_step:
                    step_player = int(
                        input(f'не допустимое значение, ход игрока (1-{max_step}): '))
                initial_quantity -= step_player
                toss = 1
                if initial_quantity < 1:
                    print('Игрок победил')
            else:
                os.system('CLS')
                step_bot = (random.randint(1, max_step))
                initial_quantity -= step_bot
                toss = 0
                print(f'ход бота: {step_bot}')
                if initial_quantity < 1:
                    print('Бот победил')
    case '3':
        toss = (random.randint(0, 1))
        if toss == 0:
            print('Первым ходит игрок')
        else:
            print('Первым ходит бот')
        input('Нажмите ввод для начала игры')
        os.system('CLS')
        while initial_quantity > 0:
            if toss == 0:
                print(f'Осталось конфет: {initial_quantity}')
                step_player = int(input(f'ход игрока (1-{max_step}):'))
                while step_player < 1 or step_player > max_step:
                    step_player = int(
                        input(f'не допустимое значение, ход игрока (1-{max_step}): '))
                initial_quantity -= step_player
                toss = 1
                if initial_quantity < 1:
                    print('Игрок победил')
            else:
                os.system('CLS')
                if initial_quantity % (max_step+1) > 0:
                    step_bot = initial_quantity % (max_step+1)
                else:
                    step_bot = max_step - step_player + 1
                initial_quantity -= step_bot
                toss = 0
                print(f'ход бота: {step_bot}')
                if initial_quantity < 1:
                    print('Бот победил')