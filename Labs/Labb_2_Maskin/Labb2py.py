"""with open("recorses\datapoints.csv" "r") as file:
    content = file.readlines()
    print(content)"""

pocnon = []
with open("Labs\\Labb_2_Maskin\\recorses\datapoints.csv", "r") as file:
    pocnon = [file.read()]
    for i in pocnon:
        print(i)
pocnon_pika = []
poccnon_pich = []

for i in pocnon:
    if pocnon:
        if pocnon[::-1] == 1:
            poccnon_pich.append(pocnon)
        elif pocnon[::-1] == 0:
            pocnon_pika.append(pocnon)
for i in poccnon_pich:
    print("pich")
    print(i)



    
"""import csv

pocnon = []

with open("Labs\\Labb_2_Maskin\\recorses\datapoints.csv") as file:
    reader = csv.DictReader(file)
#print(reader)

    for row in reader:
        #print(row["width (cm)"])
        pocnon.append({"width (cm)": row["width (cm)"], "height (cm)": row["height (cm)"],
                          "label (0-pichu, 1-pikachu)": row["label (0-pichu, 1-pikachu)"]})
print(pocnon)"""
