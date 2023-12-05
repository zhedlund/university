import matplotlib.pyplot as plt
import csv

# Funktion för att lasa data från en CSV-fil
def read_file(filename):
    data = []
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            data.append(row)
    return data

lghpriser = 'lghpriser.csv'
villapriser = 'villapriser.csv'

lghData = read_file(lghpriser)
villaData = read_file(villapriser)

# Funktion for att filtrera data for ett specifikt ar
def filter_data_by_year(data, year):
    return [entry for entry in data if entry[0] == str(year)]

# Funktion for att generera x axis labels
def prepare_month_labels(all_months, years):
    return [month[:3] for month in all_months * len(years)]

# Funktion for att plotta priser i linjediagram
def plot_prices(variable_prices_lgh, variable_prices_villa, fixed_prices_1year_lgh, fixed_prices_1year_villa, title, month_labels):
    plt.figure(figsize=(10, 6))
    plt.plot(month_labels, variable_prices_lgh, label='Rörligt - lgh')
    plt.plot(month_labels, variable_prices_villa, label='Rörligt - villa')
    plt.plot(month_labels, fixed_prices_1year_lgh, label='Fast 1 år - lgh')
    plt.plot(month_labels, fixed_prices_1year_villa, label='Fast 1 år - villa')
    plt.title(title)
    plt.xlabel('månad')
    plt.ylabel('pris (öre/kWh)')
    plt.grid(True)
    plt.legend()
    plt.xticks(ticks=range(len(month_labels)), labels=month_labels, rotation=90)
    plt.show()

prisomrade_input = input("Ange prisområde (1-4): ")
ar_input = input("Ange årtalet som ska presenteras (2018-2023): ")

# Felhantering genom att prova konvertering till heltal
try:
    prisomrade = int(prisomrade_input)
    year = int(ar_input)
except ValueError:
    print("Ogiltigt format. Ange prisområde som heltal 1-4 och år mellan 2018-2023.")
    exit()

# Kontrollerar om user input ar inom giltigt intervall och skapar titel till grafen
if 1 <= prisomrade <= 4 and 2018 <= year <= 2023:
    prisomrade_text = f"SE{prisomrade}"
    title = f"Elpriser prisområde {prisomrade_text} år {year}"

    # Filtrerar data for det angivet ar
    filtered_data_lgh = filter_data_by_year(lghData, year)
    filtered_data_villa = filter_data_by_year(villaData, year)

    # Kontrollerar om tillracklig data finns for att generera grafen
    if len(filtered_data_lgh) > 1 and len(filtered_data_villa) > 1:
        year_index = 0
        month_index = 1
        fixed_prices_1year_index = [2, 5, 8, 11]  # Satter index for kolumner
        variable_prices_index = [4, 7, 10, 13]
        all_months = [
            'januari', 'februari', 'mars', 'april', 'maj', 'juni',
            'juli', 'augusti', 'september', 'oktober', 'november', 'december'
        ]
        years = sorted(set(entry[year_index] for entry in filtered_data_lgh[1:]))  # Extraherar ar

        # Listor for prisdata som ska plottas
        variable_prices_lgh = []
        variable_prices_villa = []
        fixed_prices_1year_lgh = []
        fixed_prices_1year_villa = []

        # Loopar genom varje ar och manader for att hamta prisdata
        for year in years:
            year_data_lgh = {entry[month_index]: entry for entry in filtered_data_lgh if entry[year_index] == year}
            year_data_villa = {entry[month_index]: entry for entry in filtered_data_villa if entry[year_index] == year}

            for month in all_months:
                if month in year_data_lgh:
                    variable_prices_lgh.append(float(year_data_lgh[month][variable_prices_index[prisomrade - 1]]))
                    fixed_prices_1year_lgh.append(float(year_data_lgh[month][fixed_prices_1year_index[prisomrade - 1]]))
                else:
                    variable_prices_lgh.append(None)
                    fixed_prices_1year_lgh.append(None)

                if month in year_data_villa:
                    variable_prices_villa.append(float(year_data_villa[month][variable_prices_index[prisomrade - 1]]))
                    fixed_prices_1year_villa.append(float(year_data_villa[month][fixed_prices_1year_index[prisomrade - 1]]))
                else:
                    variable_prices_villa.append(None)
                    fixed_prices_1year_villa.append(None)

        # X axis labels genereras
        month_labels = prepare_month_labels(all_months, years)
        # Funktion anropas som plottar grafen
        plot_prices(variable_prices_lgh, variable_prices_villa, fixed_prices_1year_lgh, fixed_prices_1year_villa, title, month_labels)
    else:
        print(f"Ingen data finns för {prisomrade_text} och år {year}.")
else:
    print("Ogiltigt prisområde eller år. Programmet avslutas.")