import string

CHARS = string.ascii_uppercase


# zum eintragen eines neuen Rankingplatzes
def neuer_eintrag(name, punkte):
    eintraege = auslesen_eintrag()

    eintraege.append(name + " " + punkte)

    rangliste = open("rankinglist.txt", "w")
    for eintrag in eintraege:
        rangliste.write(eintrag + "\n")

    rangliste.close()


# liest die rankinglist aus
def auslesen_eintrag():
    with open("rankinglist.txt") as f:
        lines = f.read().splitlines()
    f.close()
    return lines


# Alphabeth für die Buchstaben
def char_eintrag(charindex):
    return CHARS[charindex]


# sortiert die Liste vor dem Ausgeben
def sorter_extra():
    alte_liste = auslesen_eintrag()
    gesplittete_liste = []

    for eintrag in alte_liste:
        gesplittete_liste.append(eintrag.split())

    def takeSecond(elem):
        return int(elem[1])

    neue_liste = sorted(gesplittete_liste, key=takeSecond, reverse=True)

    rangliste = open("rankinglist.txt", "w")
    for i in range(0, 8):
        clear_line = str(neue_liste[i]).replace("[", "").replace("]", "").replace("'", "").replace(",", "")
        rangliste.write(clear_line + "\n")

    rangliste.close()

# if __name__ == '__main__':
# sorter_extra()
