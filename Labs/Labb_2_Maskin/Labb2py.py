import numpy as np
import matplotlib.pyplot as plt

x = 0
test1 = 0
test2 = ""
with open("Labs\\Labb_2_Maskin\\recorses\datapoints.csv", "r") as file:
    pocnon = file.read()
    """Dra ner i spilt[""\n] lägg i lista med split[,] apend to new list"""

pocnon_pika = []
pocnon_pich = []
pocnon_list = pocnon.split("\n")
pich_x_axis = []
pich_y_axis = []
pich_axis = []
pich = []

for index, pokemon in enumerate(pocnon_list):
    print(f"{index}: {pokemon}")
for i in pocnon_list:
    if i[-1] == "1":
        pocnon_pika.append(i)
        test1 = i
    elif i[-1]== "0":
        test2 = i
        pocnon_pich.append(i)
for index, pokemon in enumerate(pocnon_pich):
    print(f"{index}: {pokemon}")
print("\n")
for index, pokemon in enumerate(pocnon_pika):
    print(f"{index}: {pokemon}")

for i in pocnon_pich:
    pich.append(i.split(','))

for index, pokemon in enumerate(pich):
    print(f"{index}: {pokemon}")

for index, pokemon in enumerate(pich):
    print(f"{index}: {pokemon}")
for i in pich:
    del pich[x][2]
    x += 1
for index, pokemon in enumerate(pich):
    print(f"{index}: {pokemon}")

x, y = pich.T
  
  
# plot our list in X,Y coordinates
plt.scatter(x, y)
plt.show()