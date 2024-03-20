import time

def aufgabe_3():
    # Aufgabenstellung
    print(f'Aufgabe 3 es geht wieder um einen Ort.\n'
          f'Wo bist du nochmal mit einem, im wahrsten Sinne, blaune Auge davon gekommen?\n'
          f'Falls du einen Tipp brauchst tippe "hint" ein oder "exit" um eine andere Aufgabe zu machen!')
    solution = None
    solved = False

    while True:
        print(f'Lösung bitte: ', end='')
        solution = input()
        if solution == 'baggersee' or solution == 'Baggersee':  # Erste if condtion immer richtige Antwort
            print('')
            print('Du bist einfach eine Rätsellegende!')
            print('')
            print('Drück Enter damit wir weiter machen können ;)')
            wait_for_eingabe = input()
            # Hier Antwort in config file schreiben
            solved = True
            break
        elif solution == 'hint':  # Hint Case
            print('')
            print(f'Ein Tipp brauchst du also...\n'
                  f'Hint: Es war warm, feucht, dunkel und dich hat ein aggressives Bierfass angegriffen!\n')
            continue
        elif solution == 'exit':
            print('')
            print(f'Zu schwer was?... Naja dann gibts halt kein Geschenk für dich ¯\_(°.°)_/¯')
            time.sleep(3)
            solved = False
            break
        else:
            print('Faaaaaaalsch!! Versuchs nochmal!')
    return solved