import numpy as np
import random


def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


def game_core_v2(number):
    """Функция принимает загаданное число и возвращает число попыток. Поиск числа осуществляется бинарным методом"""
    count = 1  # счетчик итераций поиска
    predict = 51  # разбиваем диапазон поиска пополам
    min_number = 0  # нижний предел диапазона
    max_number = 101  # верхний
    while number != predict:
        count += 1
        if number > predict:
            min_number = predict  # ограничиваем диапазон поиска снизу
            predict += (max_number - predict) // 2  # середина поиска
        elif number < predict:
            max_number = predict  # ограничиваем диапазон поиска сверху
            predict -= (predict - min_number) // 2
    return count  # выход из цикла, если угадали


score_game(game_core_v2)
