import csv

# Tar ett filnamn som argument och returnerar en lista med innehållet
def read_file(file_name):
    data = []
    with open(file_name, 'r', newline='') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            data.append(row)
    return data				

lghpriser = 'lghpriser.csv'	
villapriser = 'villapriser.csv'

lghData = read_file(lghpriser)
villaData = read_file(lghpriser)

print("Innehåll i lghData:")
for i in range(3):
    print(lghData[i])  # Skriver ut 3 forsta raderna

print("\nInnehåll i villaData:")
for i in range(3):
    print(villaData[i])

