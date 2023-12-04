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
    year_index = 0
    month_index = 1
    fixed_prices_1year_index = [2, 5, 8, 11]
    variable_prices_index = [4, 7, 10, 13]
    years = sorted(set(entry[year_index] for entry in prices_lgh[1:]))  # Extraherar artal
    all_months = [
        'januari', 'februari', 'mars', 'april', 'maj', 'juni',
        'juli', 'augusti', 'september', 'oktober', 'november', 'december'
    ]
    # Skapar listor for datan som ska plottas
    variable_prices_lgh = []
    variable_prices_villa = []
    fixed_prices_1year_lgh = []
    fixed_prices_1year_villa = []
	# Loopar igenom varje ar
    for year in years:
        year_data_lgh = {  # Filtrerar data for lghpriser aktuellt ar
            entry[month_index]: entry 
            for entry in prices_lgh 
            if entry[year_index] == year
            }
        year_data_villa = {  # Filtrerar data for villapriser aktuellt ar
            entry[month_index]: entry 
            for entry in prices_villa 
            if entry[year_index] == year
            }
        # Loopar igenom alla manader, kollar om data for aktuell manad existerar
        for month in all_months:
            if month in year_data_lgh:
                variable_prices_lgh.append(  # Laggs till i listan
                    float(year_data_lgh[month][variable_prices_index[prisomrade - 1]]))
                fixed_prices_1year_lgh.append( 
                    float(year_data_lgh[month][fixed_prices_1year_index[prisomrade - 1]]))
            else:
                variable_prices_lgh.append(None)  # Om data saknas for aktuell manad
                fixed_prices_1year_lgh.append(None)
            # Upprepar samma procedur for villa
            if month in year_data_villa:
                variable_prices_villa.append(
                    float(year_data_villa[month][variable_prices_index[prisomrade - 1]]))
                fixed_prices_1year_villa.append(
                    float(year_data_villa[month][fixed_prices_1year_index[prisomrade - 1]]))
            else:
                variable_prices_villa.append(None)
                fixed_prices_1year_villa.append(None)
    
	#  Skapar labels till x-axeln genom att korta ned manader till 3 tecken
    month_labels = [month[:3] for month in all_months * len(years)]
    
    # Plottar diagram
    plt.figure(figsize=(10, 6))
    plt.plot(all_months * len(years), variable_prices_lgh, label='Rörligt - lgh')
    plt.plot(all_months * len(years), variable_prices_villa, label='Rörligt - villa')
    plt.plot(all_months * len(years), fixed_prices_1year_lgh, label='Fast 1 år - lgh')
    plt.plot(all_months * len(years), fixed_prices_1year_villa, label='Fast 1 år - villa')
    plt.title(title)
    plt.xlabel('månad')
    plt.ylabel('pris (öre/kWh)')
    plt.grid(True)
    plt.legend()
    plt.xticks(ticks=range(len(month_labels)), labels=month_labels, rotation=90)
    plt.xticks(rotation=90)
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
    title = f"Elpriser prisområde {prisomrade_text} år {year}"
    
    # Skapar nya listor med data filtrerad utifran angivet ar och prisomrade
    filtered_data_lgh = [
        entry for entry in lghData 
        if entry[0] == str(year)
        ]
    filtered_data_villa = [
        entry for entry in villaData 
        if entry[0] == str(year)
        ]
    #  Om data existerar i listorna, kallas funktion som skapar diagram
    if len(filtered_data_lgh) > 1 and len(filtered_data_villa) > 1:
        plot_prices(filtered_data_lgh, filtered_data_villa, title, prisomrade)
    else:
        print(f"Ingen data finns för {prisomrade_text} och år {year}.")
else:
    print("Ogiltigt prisområde eller år. Programmet avslutas.")