import matplotlib.pyplot as plt
import csv

def read_file(filnamn):
    data = []
    with open(filnamn, 'r', newline='') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            data.append(row)
    return data

# Funktion for att hitta minsta varde
def find_min(prices):
    min_price = float('inf')
    for price in prices:
        if price < min_price:
            min_price = price
    return min_price

# Fuktion for att hitta max varde
def find_max(prices):
    max_price = float('-inf')
    for price in prices:
        if price > max_price:
            max_price = price
    return max_price

# Funktion for att hitta medelvarde
def find_mean(prices):
    total = sum(prices)
    mean = total / len(prices)
    return mean

# Funktion for att hitta medianvarde
def find_median(prices):
    sorted_prices = sorted(prices)
    n = len(sorted_prices)
    mid = n // 2
    if n % 2 == 0:
        median = (sorted_prices[mid - 1] + sorted_prices[mid]) / 2
    else:
        median = sorted_prices[mid]
    return median

# Läs in filerna och skapa listor
lghpriser = 'lghpriser.csv'
villapriser = 'villapriser.csv'

lghData = read_file(lghpriser)
villaData = read_file(villapriser)

# Programmets huvudfunktion, analyserar priser och printar tabell
def analyze_prices(prices, category, year):
    year_index = 0
    month_index = 1
    pris_index_rorligt = [4, 7, 10, 13]
    pris_index_fast_3year = [3, 6, 9, 12]
    
    print(f"              Analys av elpriserna för kategorin {category} år {year}")
    print("          rörligt pris (öre/kWh)                        fast pris 3 år (öre/kWh)")
    print("{:<12}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format(
        "Prisomr.", "min -- (mån)", "max -- (mån)", "medel", "median",
        "min -- (mån)", "max -- (mån)", "medel", "median"))
    print("=" * 100)

    prisomraden = []
    min_variable_prices = []
    max_variable_prices = []
    mean_variable_prices = []
    median_variable_prices = []
    min_fixed_3year_prices = []
    max_fixed_3year_prices = []
    mean_fixed_3year_prices = []
    median_fixed_3year_prices = []

    for prisomrade in range(1, 5):
        prisomrade_text = f"SE{prisomrade}"

        variable_prices = [
            float(entry[pris_index_rorligt[prisomrade - 1]]) for entry in prices 
            if entry[year_index] == str(year)
        ]
        fixed_prices_3year = [
            float(entry[pris_index_fast_3year[prisomrade - 1]]) for entry in prices 
            if entry[year_index] == str(year)
        ]
        min_variable = find_min(variable_prices)
        max_variable = find_max(variable_prices)
        mean_variable = find_mean(variable_prices)
        median_variable = find_median(variable_prices)

        min_fixed_3year = find_min(fixed_prices_3year)
        max_fixed_3year = find_max(fixed_prices_3year)
        mean_fixed_3year = find_mean(fixed_prices_3year)
        median_fixed_3year = find_median(fixed_prices_3year)
        
        min_month_variable = prices[variable_prices.index(min_variable) + 1][month_index]
        max_month_variable = prices[variable_prices.index(max_variable) + 1][month_index]
        min_month_fixed = prices[fixed_prices_3year.index(min_fixed_3year) + 1][month_index]
        max_month_fixed = prices[fixed_prices_3year.index(max_fixed_3year) + 1][month_index]

        prisomraden.append(prisomrade_text)
        min_variable_prices.append(min_variable)
        max_variable_prices.append(max_variable)
        mean_variable_prices.append(mean_variable)
        median_variable_prices.append(median_variable)
        min_fixed_3year_prices.append(min_fixed_3year)
        max_fixed_3year_prices.append(max_fixed_3year)
        mean_fixed_3year_prices.append(mean_fixed_3year)
        median_fixed_3year_prices.append(median_fixed_3year)

        print("{:<6}{:<10}{:<6}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format(
            prisomrade_text,
            f"{min_variable:.2f} {min_month_variable[:3]}", 
            f"{max_variable:.2f} {max_month_variable[:3]}", 
            f"{mean_variable:.2f}", f"{median_variable:.2f}",
            f"{min_fixed_3year:.2f} {min_month_fixed[:3]}", 
            f"{max_fixed_3year:.2f} {max_month_fixed[:3]}", 
            f"{mean_fixed_3year:.2f}", f"{median_fixed_3year:.2f}"
		))

	# Plottar bar graph Rorligt pris
    bar_width = 0.2
    bar_positions_min = list(range(1, 5))
    bar_positions_max = [pos + bar_width for pos in bar_positions_min]
    bar_positions_mean = [pos + 2 * bar_width for pos in bar_positions_min]
    bar_positions_median = [pos + 3 * bar_width for pos in bar_positions_min]

    plt.subplot(1, 2, 1)
    plt.bar(bar_positions_min, min_variable_prices, width=bar_width, label='rörligt min')
    plt.bar(bar_positions_max, max_variable_prices, width=bar_width, label='rörligt max')
    plt.bar(bar_positions_mean, mean_variable_prices, width=bar_width, label='rörligt medel')
    plt.bar(bar_positions_median, median_variable_prices, width=bar_width, label='rörligt median')
    plt.xticks(bar_positions_mean, prisomraden)
    plt.title(f'Elpriser rörligt för {category} i prisområden SE1-SE4 år {year}')
    plt.xlabel('prisområden')
    plt.ylabel('pris (öre/kWh)')
    plt.legend()

	# Bar graph for Fast pris 3 år
    bar_positions_min = list(range(1, 5))
    bar_positions_max = [pos + bar_width for pos in bar_positions_min]
    bar_positions_mean = [pos + 2 * bar_width for pos in bar_positions_min]
    bar_positions_median = [pos + 3 * bar_width for pos in bar_positions_min]

    plt.subplot(1, 2, 2)
    plt.bar(bar_positions_min, min_fixed_3year_prices, width=bar_width, label='fast 3 år - min')
    plt.bar(bar_positions_max, max_fixed_3year_prices, width=bar_width, label='fast 3 år - max')
    plt.bar(bar_positions_mean, mean_fixed_3year_prices, width=bar_width, label='fast 3 år - medel')
    plt.bar(bar_positions_median, median_fixed_3year_prices, width=bar_width, label='fast 3 år - median')
    plt.title(f'Elpriser fast 3 år för {category} i prisområden SE1-SE4 år {year}')
    plt.xlabel('prisområden')
    plt.ylabel('pris (öre/kWh)')
    plt.legend()
    plt.tight_layout()
    plt.show()

category_input = input("Lägenhetskund (L) eller villakund (V)? :").upper()
if category_input not in ['L', 'V']:
    print("Ogiltig kundkategori. Programmet avslutas.")
    exit()

year_input = input("Ange årtalet som ska presenteras (2018-2023): ")

try:
    year = int(year_input)
except ValueError:
    print("Ogiltigt format för årtal.")
    exit()
    
if not (2018 <= year <= 2023):
    print("Ogiltigt årtal. Programmet avslutas.")
    exit()

if category_input == 'L':
    prices = lghData
    category_text = "lägenhetskund"
elif category_input == 'V':
    prices = villaData
    category_text = "villakund"
else:
    print("Ogiltig kundkategori. Programmet avslutas.")
    exit()

# Analysera och printa priser
prisomraden = analyze_prices(prices, category_text, year)