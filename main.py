import os
import time

from aufgabe_1 import aufgabe_1
from aufgabe_2 import aufgabe_2
from aufgabe_3 import aufgabe_3

aufgaben_not_solved: list = ['Aufgabe 1', 'Aufgabe 2', 'Aufgabe 3']


def intro() -> None:
    intro_str = str(f'Alles gute zum 30. Geburtstag Manu!!\n'
                    f'Bleib so wie du bist und vor allem gesund\n'
                    f'Hier kommt dein Geschenk!!!\n'
                    f'...\n'
                    f'...\n'
                    f'Verdammt... es scheint dein Geschenk ist von einer internationalen Hackerorganisation gestohlen worden...\n'
                    f'Du musst wohl die folgenden Aufgaben lösen um an dein Geschenk zu kommen... viel Glück!\n')
    for letter in intro_str:
        print(letter, end='', flush=True)
        # time.sleep(0.1)


if __name__ == '__main__':
    intro()

    while aufgaben_not_solved:
        for aufgabe in aufgaben_not_solved:
            print(aufgabe + '\n')
        print('Welche Aufgabe solls sein? ')
        selected_task = input()
        if selected_task == str(1) or 'Aufgabe 1' or 'aufgabe 1':
            os.system('cls')  # Clear CMD
            solved = aufgabe_1()
            if solved:
                aufgaben_not_solved.remove('Aufgabe 1')
            os.system('cls')  # Clear CMD
        elif selected_task == str(2) or 'Aufgabe 2' or 'aufgabe 2':
            os.system('cls')
            solved = aufgabe_2()
            if solved:
                aufgaben_not_solved.remove('Aufgabe 2')
            os.system('cls')  # Clear CMD
        elif selected_task == str(3) or 'Aufgabe 3' or 'aufgabe 3':
            os.system('cls')
            solved = aufgabe_3()
            if solved:
                aufgaben_not_solved.remove('Aufgabe 3')
            os.system('cls')  # Clear CMD
        else:
            print("Rly??? 1-5, ist das sooo schwer?")
