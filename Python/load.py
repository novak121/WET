import csv
file_path = "H:\\programování\\Python\\data.csv"
bludistaci = {}
with open(file_path, "r", newline="") as f:
    reader = csv.reader(f,delimiter=";")
    for x in reader:
       bludistaci[radek[0]] = int(radek[1])