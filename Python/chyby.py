import sys

def kladne_zaporne(cislo):
    if cislo > 0:
        print("Číslo je kladné")
    elif cislo < 0:
        print("Čísl je záporné")
    else:
        print("Číslo je 0")



while True:
    try: 
        cislo = int(input("Zadej číslo: "))
        kladne_zaporne(cislo)
        break
    except KeyboardInterrupt:
        print("Program manuálně ukončen")
        sys.exit()
    except ValueError:
        print("Nastala chyba")
    else:
        print("Kód proběhl úspěšně")
    finally:
        print("Finally se píše vždy")