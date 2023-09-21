# import matplotlib as plt

a = 0
b = 0
test1 = []
test2 = ""
pokemon = ""
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
pika = []

#for index, pokemon in enumerate(pocnon_list):
#    print(f"{index}: {pokemon}")
for i in pocnon_list:
    if i[-1] == "1":
        pocnon_pika.append(i)
        test1 = i
    elif i[-1]== "0":
        test2 = i
        pocnon_pich.append(i)

for i in pocnon_pich:
    pich.append(i.split(','))

for i in pich:
    del pich[a][2]
    del pika[a][2]
    a += 1

for i in pich:
    pich_x_axis.append(pich[b][0])
    b += 1
b = 0
for i in pich:
    pich_y_axis.append(pich[b][1])
    b += 1
print("X: ")
for index, pokemon in enumerate(pich_x_axis):
    print(f"{index}: {pokemon}")
print("Y: ")
for index, pokemon in enumerate(pich_y_axis):
    print(f"{index}: {pokemon}")

#for i in pich:
#    pokemon = pokemon + i
#pich_axis = pokemon.split(",")

#for index, pokemon in enumerate(pokemon):
#    print(f"{index}: {pokemon}")

#test1 = [p.strip("'") for p in pich_axis]
  
#for index, pokemon in enumerate(pich_axis):
#    print(f"{index}: {pokemon}")
# plot our list in X,Y coordinates
