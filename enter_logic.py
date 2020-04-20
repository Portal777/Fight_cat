import time
from termcolor import colored
import sys
import main_menu_logic as main2
from db_logic import *


lib1 = Engine('proj_lib1')


def show_enter_menu():
    a = '\n''------ Меню входа -----'
    b = '\n''1 - Ввод имени персонажа для входа'
    c = '\n''2 - Вывод доступных персонажей'
    d = '\n''3 - Выход в основное меню'
    e = '\n''4 - Заверщение игры'
    f = '\n''----------------------'
    result = a + b + c + d + e + f
    return result


def run_enter_menu():
    while True:

        choise_enter_menu = 0
        enter_menu_number = [1, 2, 3]

        while choise_enter_menu not in enter_menu_number:

            print(show_enter_menu())

            try:

                choise_enter_menu = int(input('\nВыберите пункт основного меню: '))  # Выбор пункта основного меню

                if choise_enter_menu == 1:  # Вход по имени персонажа
                    choise_user_name = input('\nВведите имя персонажа для входа: ')
                    choise_user_name = choise_user_name.capitalize()

                    if lib1.find_user_name(choise_user_name) == False:
                        print(colored('\nТакого персонажа на существует', 'red'))

                    elif lib1.find_user_name(choise_user_name) == True:
                        main2.login_user = choise_user_name
                        print(colored('\nГотово ', 'green'), colored(main2.login_user + ' !', 'blue'))
                        time.sleep(1)
                        print(main2.run_main_menu())

                if choise_enter_menu == 2:  # Вывод всех персонажей в базе данных
                    print(colored('\nДоступные персонажы для входа:', 'green'))
                    lib1.print_all_user()
                    time.sleep(1)

                if choise_enter_menu == 3:  # Возврат к главному меню игры
                    print(main2.run_main_menu())

                if choise_enter_menu == 4:  # Выход из игры
                    print(colored('\nДо свидания!', 'blue'))
                    time.sleep(1)
                    sys.exit()

                if choise_enter_menu not in enter_menu_number:  # Ввывод, при ошибочном вводе числа меню
                    print(('\nДанного пункта нет в списке!', 'red'))
                    time.sleep(1)

            except ValueError:
                print(colored('\nВвод разрешен только числами', 'red'))
                time.sleep(1)


def logout():
     main2.login_user = None
