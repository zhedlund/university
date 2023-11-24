import matplotlib.pyplot as plt
import csv

def read_file(filnamn):
    data = []
    with open(filnamn, 'r', newline='') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            data.append(row)
    return data

lghpriser = 'lghpriser.csv'
villapriser = 'villapriser.csv'

lghData = read_file(lghpriser)
villaData = read_file(villapriser)

# Funktion som extraherar data och plottar elpriser i linjediagram
def plot_prices(prices_lgh, prices_villa, title, prisomrade):
    # Definierar index for respektive tabell i csv-filer
    year_index = 0
    month_index = 1
    fixed_prices_1year_index = [2, 5, 8, 11]
    variable_prices_index = [4, 7, 10, 13]
    months = [entry[month_index][:3] for entry in prices_lgh[1:]]

	# Extraherar data for fast och rorligt elpris for lgh respektive villa
    variable_prices_lgh = [
        float(entry[variable_prices_index[prisomrade - 1]])
        for entry in prices_lgh[1:]
        if entry[year_index] == str(year)
        ]
    variable_prices_villa = [
        float(entry[variable_prices_index[prisomrade - 1]]) 
        for entry in prices_villa[1:] 
        if entry[year_index] == str(year)
        ]
    fixed_prices_1year_lgh = [
        float(entry[fixed_prices_1year_index[prisomrade - 1]]) 
        for entry in prices_lgh[1:] 
        if entry[year_index] == str(year)
        ]
    fixed_prices_1year_villa = [
        float(entry[fixed_prices_1year_index[prisomrade - 1]]) 
        for entry in prices_villa[1:] 
        if entry[year_index] == str(year)
        ]

    # Plottar ut elpriser for lgh respektive villa
    plt.figure(figsize=(10, 6))
    plt.plot(months, variable_prices_lgh, label='Rörligt - lgh')
    plt.plot(months, variable_prices_villa, label='Rörligt - villa')
    plt.plot(months, fixed_prices_1year_lgh, label='Fast 1 år - lgh')
    plt.plot(months, fixed_prices_1year_villa, label='Fast 1 år - villa')
    
	# Justerar rubriker och utseende
    plt.title(title)
    plt.xlabel('månad')
    plt.ylabel('pris (öre/kWh)')
    plt.grid(True)
    plt.legend()
    plt.xticks(rotation=90)  # Roterar titeln pa x-axeln
    plt.show()

prisomrade_input = input("Ange prisområde (1-4): ")
ar_input = input("Ange årtalet som ska presenteras (2018-2023): ")

# Felhantering user input
try:
    prisomrade = int(prisomrade_input)
    year = int(ar_input)
except ValueError:
    print("Ogiltigt format. Ange prisområde som heltal 1-4 och år mellan 2018-2023.")
    exit()

if 1 <= prisomrade <= 4 and 2018 <= year <= 2023:
    prisomrade_text = f"SE{prisomrade}"
    title = f"Elpriser för {prisomrade_text} år {year}"
    
    # Skapar nya listor med data filtrerad utifran ar
    filtered_data_lgh = [
        entry for entry in lghData 
        if entry[0] == str(year)
        ]
    filtered_data_villa = [
        entry for entry in villaData 
        if entry[0] == str(year)
        ]
    
    if len(filtered_data_lgh) > 1 and len(filtered_data_villa) > 1:
        plot_prices(filtered_data_lgh, filtered_data_villa, title, prisomrade)
    else:
        print(f"Ingen data finns för {prisomrade_text} och år {year}.")
else:
    print("Ogiltigt prisområde eller år. Programmet avslutas.")