"""with open("recorses\datapoints.csv" "r") as file:
    content = file.readlines()
    print(content)"""


"""with open("Labs\\Labb_2_Maskin\\recorses\datapoints.csv", "r") as file:
    content = file.read()
    print(content)"""
    
import csv

pocnon = []

with open("Labs\\Labb_2_Maskin\\recorses\datapoints.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["width (cm)"])
        """pocnon.append({"width (cm)": row["width (cm)"], "height (cm)": row["height (cm)"],
                          "label (0-pichu, 1-pikachu)": row["label (0-pichu, 1-pikachu)"]})
print(pocnon)"""
