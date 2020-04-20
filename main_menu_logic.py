import time
import sys
from termcolor import colored
from register_logic import *
from enter_logic import *


login_user = None  # Глобальная переменная для входа в игру


def show_main_menu():  # Функция, выводящая основное меню
    a = '\n''------ Меню игры -----'
    b = '\n''1 - Регистрация'
    c = '\n''2 - Вход'
    d = '\n''3 - Об игре'
    e = '\n''4 - Выход из аккаунта'
    f = '\n''5 - Выход из игры'
    g = '\n''----------------------'
    result = a + b + c + d + e + f + g
    return result


def run_main_menu():
    while True:

        choise_main_menu = 0
        main_menu_number = [1, 2, 3]

        while choise_main_menu not in main_menu_number:

            print(show_main_menu())

            try:

                choise_main_menu = int(input('\nВыберите пункт основного меню: '))  # Выбор пункта основного меню

                if choise_main_menu == 1:  # Регистрация
                    print(run_register_menu())

                elif choise_main_menu == 2:  # Вход в игру

                    if login_user is None:
                        print(run_enter_menu())
                    else:
                        print(colored('Вы уже выполнили вход!', 'red'))
                        time.sleep(1)

                elif choise_main_menu == 3:  # Инфо об игре
                    print(colored('\nОб игре:', 'green'))
                    print(login_user)
                    time.sleep(1)

                elif choise_main_menu == 4:  # Выход из аккаунта
                    print('Вы вышли из аккаунта: ', colored(login_user, 'blue'))
                    logout()
                    time.sleep(1)

                elif choise_main_menu == 5:  # Выход из игры
                    print(colored('\nДо свидания!', 'blue'))
                    time.sleep(1)
                    sys.exit()

                elif choise_main_menu not in main_menu_number:
                    print(colored('\nДанного пункта нет в списке!', 'red'))
                    time.sleep(1)

            except ValueError:
                print(colored('\nВвод разрешен только числами', 'red'))
                time.sleep(1)

    # Добавить пункт "ВХОД", с нормальной функциональностью, добавить арену с pvp и pve (предварительно добавить функции
            #  добавления ботов в бд)
    # Сделать БД, добавить возможность создания игрока и создания ботов с хар-ми
    # Создать классы: игрок и бот +
    # Разбить игру на 3-и разных файла .py и импортировать их в центральный файл игры, и вызывать по необходимости +
    # Добавить меню : 1) Начало игры 2) Правила 3) Выход +
    # Добавить функцию - выводящую список бойцов на выбор  +
    # Добавить бесконечный цикл, в котором нужно обязательно выбрать бойца +
