import random
import time
import sys
from termcolor import colored
from register_logic import *


print('\nБоевые коты  (ノಠ益ಠ)ノ彡\n')  # Приветсвие


def show_main_menu():  # Функция, выводящая основное меню
    a = '\n''------ Меню игры -----'
    b = '\n''1 - Регистрация'
    c = '\n''2 - Вход'
    d = '\n''2 - Об игре'
    e = '\n''3 - Выход'
    f = '\n''----------------------'
    result = a + b + c + d + e + f
    return result


while True:

    choise_main_menu = 0
    main_menu_number = [1, 2, 3]

    while choise_main_menu not in main_menu_number:

        print(show_main_menu())

        try:

            choise_main_menu = int(input('\nВыберите пункт основного меню: '))  # Выбор пункта основного меню

            if choise_main_menu == 1:  # Пункт основного меню - Регистрация

                print(show_register_menu())

                while True:

                    choise_reg_menu = 0
                    reg_menu_number = [1, 2, 3, 4]

                    while choise_reg_menu not in reg_menu_number:

                        print(show_register_menu())

                        try:

                            choise_reg_menu = int(input('\nВыберите пункт меню регистрации: '))  # Выбор пункта меню
                            #  регистрации

                            if choise_reg_menu == 1:  # Пункт меню регистрации - Вход
                                print(register())

                            if choise_reg_menu == 2:  # Пункт меню регистрации - Регистрация
                                print(colored('\nПомощь: ',
                                              'green') + 'Вам нужно ввести имя вашего персонажа и выбрать класс'
                                                         '\n1 - Воин / 2 - Лучник / 3 - Маг')
                                time.sleep(1)

                            if choise_reg_menu == 3:  # Пункт меню регистрации - Якобы выход в основное меню
                                break

                            if choise_reg_menu == 4:  # Пункт меню регистрации - Завершение цикла
                                print(colored('\nДо свидания!', 'blue'))
                                time.sleep(1)
                                sys.exit()

                            elif choise_reg_menu not in reg_menu_number:

                                print(('\nДанного пункта нет в списке!', 'red'))
                                time.sleep(1)

                        except ValueError:
                            print(colored('\nВвод разрешен только числами', 'red'))
                            time.sleep(1)

                    break

            if choise_main_menu == 2:  # Пункт основного меню - Вход
                print(colored('\nВход:', 'green'))

            if choise_main_menu == 3:  # Пункт основного меню - Инфо об игре
                print(colored('\nОб игре:', 'green'))

            if choise_main_menu == 4:  # Пункт основного меню - Завершение цикла
                print(colored('\nДо свидания!', 'blue'))
                time.sleep(1)
                sys.exit()

            elif choise_main_menu not in main_menu_number:

                print(('\nДанного пункта нет в списке!', 'red'))
                time.sleep(1)

        except ValueError:
            print(colored('\nВвод разрешен только числами', 'red'))
            time.sleep(1)

    # Добавить пункт "ВХОД", с нормальной функциональностью, добавить арену с pvp и pve (предварительно добавить функции
            #  добавления ботов в бд)
    # Сделать БД, добавить возможность создания игрока и создания ботов с хар-ми
    # Создать классы: игрок и бот +
    # Разбить игру на 3-и разных файла .py и импортировать их в центральный файл игры, и вызывать по необходимости
    # Добавить меню : 1) Начало игры 2) Правила 3) Выход +
    # Добавить функцию - выводящую список бойцов на выбор  +
    # Добавить бесконечный цикл, в котором нужно обязательно выбрать бойца +
