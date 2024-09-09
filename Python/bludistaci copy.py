import sys
import csv


cesta = "H:\\programování\\Python\\data.csv"

bludistaci = {
   "Božetěch": 1,
   "Želmíra": 3,
   "Andělín": 2,
   "Hvězdoslava": 1
}

def vypisBludistakyPro(bludistaci):
    jmeno = input("Koho chceš zkontrolovat?: ")
    if jmeno in bludistaci:
        pocet_bludistaku = bludistaci[jmeno]
        print(f"{jmeno} {pocet_bludistaku}")

def vypisVse(bludistaci):
    for jmeno, pocet_bludistaku in bludistaci.items():
        print(f"{jmeno} {pocet_bludistaku}")

def pridejBludistaka(bludistaci):
    jmeno = input("Komu chceš přidat bludšiťáka?: ")
    if jmeno in bludistaci:
        bludistaci[jmeno] += 1
    else:
        bludistaci[jmeno] = 1
    print(f"{jmeno} {bludistaci[jmeno]}")

def odeberBludistaka(bludistaci):
    jmeno = input("Komu chceš odebrat bludšiťáka?: ")
    if jmeno in bludistaci and bludistaci[jmeno] > 0:
        bludistaci[jmeno] -= 1
        print(f"{jmeno} {bludistaci[jmeno]}")
    else:
        print(f"{jmeno} nemá žádného bludišťáka k odebrání.")

def pridejStudenta(bludistaci):
    jmeno = input("Přidej studenta/ku: ")
    if jmeno not in bludistaci:
        bludistaci[jmeno] = 1
    else:
        bludistaci[jmeno] += 1
    print(f"{jmeno} {bludistaci[jmeno]}")

def nejvyssiSkore(bludistaci):
    if bludistaci:
        nejvyssi_student = max(bludistaci, key=bludistaci.get)
        pocet_bludistaku = bludistaci[nejvyssi_student]
        print(f"Nejvíce bludišťáků nasbíral/a:\n{nejvyssi_student} {pocet_bludistaku}")
    else:
        print("Žádní bludišťáci nejsou k dispozici.")

def main():
    print("Vítej uživateli")
    print("Zvol možnost")
    print("Pro vypsání všech Bludišťáků zvol 1")
    print("Pro vypsání jednoho studenta zvol 2")
    print("Pro přidání Bludišťáka zvol 3")
    print("Pro odebrání Bludišťáka zvol 4")
    print("Pro vypsání nejlepšího studenta zvol 5")
    print("Pro přidání studenta zvol 6")
    print("Pro ukončení zvolte 7")

    while True:
        try:
            zvolena_moznost = int(input())
            break
         except ValueError:
            print("Nezadal/a jsi číslo. Zadej číslo")

        
    match zvolena_moznost:
    case 1:
        zvolena_moznost == '1':
        vypisVse(bludistaci)
    case 2:
            zvolena_moznost == '2':
        vypisBludistakyPro(bludistaci)
    case 3:
            zvolena_moznost == '3':
        pridejBludistaka(bludistaci)
    case 4:
            zvolena_moznost == '4':
        odeberBludistaka(bludistaci)
    case 5:
            zvolena_moznost == '5':
        nejvyssiSkore(bludistaci)
    case 6:
              zvolena_moznost == '6':
        pridejStudenta(bludistaci)
    case 7:
              print("Bye")
              sys.exit()

if __name__ == "__main__":
    main()
