"""with open("recorses\datapoints.csv" "r") as file:
    content = file.readlines()
    print(content)"""
x = 0
test1 = 0
test2 = ""
with open("Labs\\Labb_2_Maskin\\recorses\datapoints.csv", "r") as file:
    pocnon = file.read()
    """Dra ner i spilt[""\n] lägg i lista med split[,] apend to new list"""

pocnon_pika = []
poccnon_pich = []
pocnon_list = pocnon.split("\n")

for index, pokemon in enumerate(pocnon_list):
    print(f"{index}: {pokemon}")
for i in pocnon_list:
    if i[-1] == "1":
        pocnon_pika.append(i)
        test1 = i
    elif i[-1]== "0":
        test2 = i
        poccnon_pich.append(i)
for index, pokemon in enumerate(poccnon_pich):
    print(f"{index}: {pokemon}")
print("\n")
for index, pokemon in enumerate(pocnon_pika):
    print(f"{index}: {pokemon}")



