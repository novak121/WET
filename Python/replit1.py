import random

odpoved = random.randint(1, 7) 

otazka = input("Na co se chces zeptat?\n")

if odpoved == 1:
  print("Ano")
if odpoved == 2:
  print("Jednoznačně")
if odpoved == 3:
  print("Na 100%")
if odpoved == 4:
  print("YESSIR")
if odpoved == 5:
  print("ANO PANE")
if odpoved == 6:
  print("asi ne")

odpovedi = "Ano","Jednoznačně", "Na 100%","YESSIR", "ANO PANE", "asi ne" 