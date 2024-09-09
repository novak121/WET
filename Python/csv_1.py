import csv

# cesta = "H:\\programování\\Python\\data.csv"
# with open(cesta, "r") as f:
#    reader = csv.reader(f, delimiter=";")
#    for x in reader:
#        print(x)


cesta = "H:\\programování\\Python\\data.csv"
with open(cesta, "w", newline="") as f:
    jmeno = input("Zadej jméno: ")
    pocet = int(input("Zadej počet: "))
    writer = csv.writer(f, delimiter=";")
    writer.writerow([jmeno, pocet])
    