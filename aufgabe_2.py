import time


def aufgabe_2():
    # Aufgabenstellung
    print(f'Aufgabe 2 wird nicht so einfach wie die erste\n'
          f'Wo war dein größter doppelter "Absturz"?\n'
          f'Falls du einen Tipp brauchst tippe "hint" ein oder "exit" um eine andere Aufgabe zu machen!')
    solution = None
    solved = False

    while True:
        print(f'Lösung bitte: ', end='')
        solution = input()
        if solution == 'heidelberg' or solution == 'Heidelberg':  # Erste if condtion immer richtige Antwort
            print('')
            print('Die zweite au richtig! Beeindruckend!')
            print('')
            print('Drück Enter damit wir weiter machen können ;)')
            wait_for_eingabe = input()
            # Hier Antwort in config file schreiben
            solved = True
            break
        elif solution == 'hint':  # Hint Case
            print('')
            print(f'Du brauchst also einen Tipp... traurig...\n'
                  f'Hint: apache\n')
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