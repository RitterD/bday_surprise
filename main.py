import os
import time
import codecs
import webbrowser
import socket
from aufgabe_1 import aufgabe_1
from aufgabe_2 import aufgabe_2
from aufgabe_3 import aufgabe_3
from aufgabe_4 import aufgabe_4

aufgaben_not_solved: list = ['Aufgabe 1', 'Aufgabe 2', 'Aufgabe 3', 'Aufgabe 4']
msg: bytes = b'User: Hackerman, PW: Alles_gute_zum_30'


def print_slow(text: str) -> None:
    """
    Prints text Buchstabe für Buchstabe
    :param text: intro und outro text
    """
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(0.15)


def intro() -> None:
    intro_str = str(f'Alles gute zum 30. Geburtstag Manu!!\n'
                    f'Bleib so wie du bist und vor allem gesund und uns noch lange erhalten.\n'
                    f'Jezt wollen wir dich aber nicht mehr weiter auf die Folter spannen!!\n'
                    f'Hier kommt dein Geschenk!!!\n'
                    f'...\n'
                    f'...\n'
                    f'Verdammt... es scheint dein Geschenk ist von einer internationalen Hackerorganisation gestohlen worden...\n'
                    f'Du musst wohl ein paar sehr tricky Aufgaben lösen um an dein Geschenk zu kommen... viel Glück bro!!\n')
    print_slow(intro_str)


def outro() -> None:
    file_path = os.path.abspath("ui/index.html")
    outro_str = str(f'Du hast es geschafft!! '
                    f'Du bist wohl einfach viel schlauer und deutlich attraktiver als die Hacker\n'
                    f'Jetzt ist es soweit, hier kommt dein Geschenk!!!\n'
                    f'.......\n'
                    f'.......\n'
                    f'Oh no! Die Hacker versenden gerade deinen Benutzernamen und dein Passwort per UDP!!\n'
                    f'Schnell öffne den Browser und Wireshark und log dich ein um sie aufzuhalten!!!')
    print_slow(outro_str)
    os.system("start " + file_path)


if __name__ == '__main__':

    intro()

    while aufgaben_not_solved:
        for aufgabe in aufgaben_not_solved:
            print(aufgabe + '\n')
        print('Welche Aufgabe solls sein? ')
        selected_task = input()
        if selected_task == str(1) or selected_task.upper() == 'AUFGABE 1':
            os.system('cls')  # Clear CMD
            solved = aufgabe_1()
            if solved:
                aufgaben_not_solved.remove('Aufgabe 1')
            os.system('cls')  # Clear CMD
        elif selected_task == str(2) or selected_task.upper() == 'AUFGABE 2':
            os.system('cls')
            solved = aufgabe_2()
            if solved:
                aufgaben_not_solved.remove('Aufgabe 2')
            os.system('cls')  # Clear CMD
        elif selected_task == str(3) or selected_task.upper() == 'AUFGABE 3':
            os.system('cls')
            solved = aufgabe_3()
            if solved:
                aufgaben_not_solved.remove('Aufgabe 3')
            os.system('cls')  # Clear CMD
        elif selected_task == str(4) or selected_task.upper() == 'AUFGABE 4':
            os.system('cls')
            solved = aufgabe_4()
            if solved:
                aufgaben_not_solved.remove('Aufgabe 4')
            os.system('cls')  # Clear CMD
        else:
            print(
                "Rly??? also wenns schon daran scheitert eine Zahl von 1-4 einzugeben brauchen wir hier gar nicht weitermachen....")
    outro()
    f = open("ui/index.html", 'r')
    filename = 'file:///' + os.getcwd() + '/' + 'ui/index.html'
    webbrowser.open_new_tab(filename)
    f.read()
    s_ = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        s_.sendto(msg, ('192.168.178.99', 5555))
        time.sleep(0.01)
