import csv
import matplotlib.pyplot as plt

# Tar ett filnamn som argument och returnerar en lista med innehållet
def read_file(file_name):
    data = []
    with open(file_name, 'r', newline='') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            data.append(row)
    return data

# Läs in filerna med elpriser
lghpriser = 'lghpriser.csv'
villapriser = 'villapriser.csv'

lghData = read_file(lghpriser)
villaData = read_file(villapriser)

def categorize_data(prices, category):
    category_data = {
        'lagenhetskund': [],
        'villakund': []
    }
    for entry in prices:
        if entry[0].lower() == category.lower():
            category_data[entry[0].lower()].append(entry[1:])

    return category_data

# Funktion för att beräkna min, max och medelvärde av elpriser för ett prisavtal och en kundtyp
def calculate_stats(prices, agreement):
    year_index = 0
    pris_index = 0
    
    # Användare väljer prisavtal
    if agreement == "rörligt":
        pris_index = [4, 7, 10, 13]  # Indexter för rörligt pris i CSV-filen
    elif agreement == "fast 1 år":
        pris_index = [3, 6, 9, 12]  # Indexter för fast 1 år i CSV-filen
    elif agreement == "fast 3 år":
        pris_index = [2, 5, 8, 11]  # Indexter för fast 3 år i CSV-filen

    years = list(range(2018, 2024))
    prices_per_year = [[] for _ in range(len(years))]

    for i, year in enumerate(years):
        # Filtrerar data för det givna året och priset för det givna prisavtalet
        filtered_prices = [
            float(entry[pris_index[i % 4]]) for entry in prices if int(entry[year_index]) == year
        ]
        prices_per_year[i].extend(filtered_prices)

    # Beräkna min, max och medelvärde för varje år
    min_prices = [min(prices) for prices in prices_per_year]
    max_prices = [max(prices) for prices in prices_per_year]
    avg_prices = [sum(prices) / len(prices) for prices in prices_per_year]

    return min_prices, max_prices, avg_prices

# Läs in filerna med elpriser
lghpriser = 'lghpriser.csv'
villapriser = 'villapriser.csv'

lghData = read_file(lghpriser)
villaData = read_file(villapriser)

prisavtal_input = input("Ange prisavtal (R, F1, F3): ")
prisavtal_map = {
    "R": "rörligt",
    "F1": "fast 1 år",
    "F3": "fast 3 år"
}
if prisavtal_input.upper() in prisavtal_map:
    prisavtal = prisavtal_map[prisavtal_input.upper()]
else:
    print("Ogiltigt prisavtal. Ange 'R', 'F1' eller 'F3'.")
    exit()



# Beräkna statistik för lägenhetskunder och villakunder
min_lgh, max_lgh, avg_lgh = calculate_stats(lghData[1:], prisavtal)
min_villa, max_villa, avg_villa = calculate_stats(villaData[1:], prisavtal)

# Presentera tabell
print(f"{'År':<6}{'Lägsta':<10}{'Högsta':<10}{'Medel':<10}")
print("=" * 36)
for i, year in enumerate(range(2018, 2024)):
    print(f"{year:<6}{min_lgh[i]:<10.2f}{max_lgh[i]:<10.2f}{avg_lgh[i]:<10.2f}")

# Skapa punktdiagram för lägenhetskunder och villakunder
plt.figure(figsize=(10, 5))

# Diagram för lägenhetskunder
plt.subplot(1, 2, 1)
plt.scatter(range(1, 7), min_lgh, label='Lägsta')
plt.scatter(range(1, 7), max_lgh, label='Högsta')
plt.scatter(range(1, 7), avg_lgh, label='Medel')
plt.xlabel('Prisområde')
plt.ylabel('Pris (öre/kWh)')
plt.title('Lägenhetskund')
plt.legend()

# Diagram för villakunder
plt.subplot(1, 2, 2)
plt.scatter(range(1, 7), min_villa, label='Lägsta')
plt.scatter(range(1, 7), max_villa, label='Högsta')
plt.scatter(range(1, 7), avg_villa, label='Medel')
plt.xlabel('Prisområde')
plt.ylabel('Pris (öre/kWh)')
plt.title('Villakund')
plt.legend()

plt.tight_layout()
plt.show()

