import random
import time
import sys
from termcolor import colored
import main_menu_logic as main3
from db_logic import *


lib1 = Engine('proj_lib1')


def show_register_menu():  # Функция, выводящая основное меню
    a = '\n''------ Меню регистрации -----'
    b = '\n''1 - Зарегесрироваться'
    c = '\n''2 - Помощь'
    d = '\n''3 - В основное меню'
    e = '\n''4 - Выход'
    f = '\n''-----------------------------'
    result = a + b + c + d + e + f
    return result


def run_register_menu():

    while True:

        choise_reg_menu = 0
        reg_menu_number = [1, 2, 3, 4]

        while choise_reg_menu not in reg_menu_number:

            print(show_register_menu())

            try:

                choise_reg_menu = int(input('\nВыберите пункт меню регистрации: '))  # Выбор пункта меню
                #  регистрации

                if choise_reg_menu == 1:  # Регистрация персонажа

                    name_user = input('\nВведите имя персонажа: ')
                    name_user = name_user.capitalize()

                    if lib1.find_user_name(name_user) == True:
                        return colored('\nИмя уже занято!', 'red')


                    if lib1.find_user_name(name_user) == False:
                        choise_class = 0
                        fighters_number = [1, 2, 3]

                        while choise_class not in fighters_number:

                            choise_class = int(
                                input('\nВыберите класс персонажа:\n1 - Воин\n2 - Лучник\n3 - Маг\nВыбор: '))

                            try:
                                if choise_class in fighters_number:

                                    if choise_class == 1:  # Если выбрали воина, распределяем хар-ки hp, strg, arm, luck
                                        choise_class = "war"
                                        lib1.reg_user(name_user, choise_class, 15, 4, 4, 0)
                                        return '\nПоздравляю с регистрацией! ' + name_user + ' !'

                                    if choise_class == 2:  # Если выбрали лучника, распределяем хар-ки hp, strg, arm, luck
                                        choise_class = "arc"
                                        lib1.reg_user(name_user, choise_class, 11, 3, 3, 2)
                                        return '\nПоздравляю с регистрацией ' + name_user + ' !'

                                    if choise_class == 3:  # Если выбрали мага, распределяем хар-ки hp, strg, arm, luck
                                        choise_class = "mag"
                                        lib1.reg_user(name_user, choise_class, 8, 6, 1, 5)
                                        return '\nПоздравляю с регистрацией ' + name_user + ' !'

                                if choise_class not in fighters_number:
                                    print(colored('\nВведенного бойца нет в списке!', 'red'))
                                    time.sleep(1)

                            except ValueError:
                                print(colored('\nВвод разрешен только числами', 'red'))
                                time.sleep(1)

                if choise_reg_menu == 2:  # Регистрация
                    print(colored('\nПомощь: ',
                                  'green') + 'Вам нужно ввести имя вашего персонажа и выбрать класс'
                                             '\n1 - Воин / 2 - Лучник / 3 - Маг')
                    time.sleep(1)

                if choise_reg_menu == 3:  # Возврат к главному меню игры
                    print(main3.run_main_menu())

                if choise_reg_menu == 4:  # Завершение цикла
                    print(colored('\nДо свидания!', 'blue'))
                    time.sleep(1)
                    sys.exit()

                elif choise_reg_menu not in reg_menu_number:

                    print(('\nДанного пункта нет в списке!', 'red'))
                    time.sleep(1)

            except ValueError:
                print(colored('\nВвод разрешен только числами', 'red'))
                time.sleep(1)


'''
while True:

    choise_reg_menu = 0
    reg_menu_number = [1, 2, 3]

    while choise_reg_menu not in reg_menu_number:

        print(show_register_menu())

        try:

            choise_reg_menu = int(input('\nВыберите пункт меню регистрации: '))

            if choise_reg_menu == 1:
                print(register())

            if choise_reg_menu == 2:
                print(colored('\nПомощь: ', 'green' )+ 'Вам нужно ввести имя вашего персонажа и выбрать класс'
                                                       '\n1 - Воин / 2 - Лучник / 3 - Маг')
                time.sleep(1)

            if choise_reg_menu == 3:
                print(colored('\nДо свидания!', 'blue'))
                time.sleep(1)
                sys.exit()

            elif choise_reg_menu not in reg_menu_number:

                print(('\nДанного пункта нет в списке!', 'red'))
                time.sleep(1)

        except ValueError:
            print(colored('\nВвод разрешен только числами', 'red'))
            time.sleep(1)

'''
# Добавить проверку на уникальность имени
