cesta = "H:\\programování\\Python\\data.txt"

with open(cesta, "r") as soubor:
    print(soubor.read())

with open(cesta, "a") as soubor:
    text = "\nBye"
    soubor.write(text)
