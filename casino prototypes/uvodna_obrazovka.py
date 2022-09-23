import kocky
from testfightgame import fightgame2


def menu():
    print("Vitajte v kasíne. Môžte tu vyskúšať množstvo jednoduchých hier.")
    hra = (input ("Akú hru by ste si chceli zahrať ? Možnosti sú :\n 1)Kocky\n 2)Fightgame\n "))
    if hra == "1":
        kocky.kocky()
    elif hra== "2":
        fightgame2.fightgame2()


if __name__ == "__main__":
    menu()