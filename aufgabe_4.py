import time


def aufgabe_4():
    # Aufgabenstellung
    print(f'Aufgabe 4 ist eine Frage zu deiner großen Liebe den Comic-Büchern.\n'
          f'Welchen der Avangers hast du schon persönlich getroffen?\n'
          f'Falls du einen Tipp brauchst tippe "hint" ein oder "exit" um eine andere Aufgabe zu machen!')
    solution = None
    solved = False

    while True:
        print(f'Lösung, hallo bitte: ', end='')
        solution = input()
        if solution == 'hulk' or solution == 'Hulk' or solution == 'Bruce Banner':  # Erste if condtion immer richtige Antwort
            print('')
            print('Zu Comic-Büchern scheinst du wirklich alles zu wissen!!')
            print('')
            print('Drück Enter damit wir weiter machen können ;)')
            wait_for_eingabe = input()
            solved = True
            break
        elif solution == 'hint':  # Hint Case
            print('')
            print(f'Ein Tipp brauchst du also...\n'
                  f'Hint: Er hat einen 100er Bizeps, ist grün und er hasst Fahrräder!\n')
            continue
        elif solution == 'exit':  # Exit case
            print('')
            print(f'Zu schwer was?... Naja dann gibts halt kein Geschenk für dich ¯\_(°.°)_/¯')
            time.sleep(3)
            solved = False
            break
        else:
            print('Faaaaaaalsch!! Versuchs nochmal!')
    return solved