def main():
    cecka = {
        "Jakub": 0,
        "Vašek": 2,
        "Ema": 2
    }
    jmeno = input("Napiš jméno ").capitalize()
    kolik_cecek(cecka)

def kolik_cecek(seznam):
    jmeno = input("Napiš jméno ").capitalize()
    if jmeno in seznam:
        print(seznam[jmeno])

def pridej_studenta(seznam):
    jmeno = input("Napiš jméno ").capitalize()
    seznam[jmeno] = 1


if __name__ == "__main__":
    main()
