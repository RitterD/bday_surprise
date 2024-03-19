import time


def aufgabe_1():
    # Aufgabenstellung
    print(f'Aufgabe 1 also ok ok...\n'
          f'Wir fangen erstmal ganz easy an und zwar: '
          f'Was ist dein absolutes Lieblingsessen?\n'
          f'Falls du einen Tipp brauchst tippe "hint" ein oder "exit" um eine andere Aufgabe zu machen!')
    solution = None
    solved = False

    while True:
        print(f'Lösung bitte: ', end='')
        solution = input()
        if solution == 'schweineleder':  # Erste if condtion immer richtige Antwort
            print('Sehr gut sehr gut Manneli, immer weiter so!!')
            time.sleep(3)
            # Hier Antwort in config file schreiben
            solved = True
            break
        elif solution == 'hint':  # Hint Case
            print(f'Du brauchst also einen Tipp... traurig...\n'
                  f'Hint: Oink Oink\n')
            continue
        elif solution == 'exit':
            print(f'Zu schwer was?... Naja dann gibts halt kein Geschenk für dich ¯\_(°.°)_/¯')
            time.sleep(3)
            solved = False
            break
        else:
            print('Faaaaaaalsch!! Versuchs nochmal!')
    return solved
