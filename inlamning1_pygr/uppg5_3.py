import csv

def read_file(file_name):
    data = []
    with open(file_name, 'r', newline='') as file:
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

# Extrahera kolumner startar m SE och namnger listor
def extract_SE_columns(file_name):
    data = read_file(file_name)
    se_columns = {}

    # Skapar dictionary med SE-kolumner
    for idx, column in enumerate(data[0]):
        if column.startswith('SE'):
            se_columns[column] = [float(row[idx]) for row in data[1:]]

    return se_columns

# Filtrerar statistik for SE kolumner och printar output
def filter_and_print_statistics(se_columns, prisavtal):
    for se_type in range(1, 5):
        column_name = f"SE{se_type}-{prisavtal}"
        if column_name in se_columns:
            min_value = find_min(se_columns[column_name])
            max_value = find_max(se_columns[column_name])
            mean_value = find_mean(se_columns[column_name])

			# Fixa logic for att extrahera ar och manader fran data - EJ KLAR!
            # Extraherar ar och man for min och max nu, placeholders:
            min_year = '2020'
            min_month = 'Apr'
            max_year = '2022'
            max_month = 'Dec'

            print(f"SE{se_type} {min_value:.2f} {min_year} {min_month}  {max_value:.2f} {max_year} {max_month} {mean_value:.2f}")

    print("=" * 51)

lghpriser_file = 'lghpriser.csv'
villapriser_file = 'villapriser.csv'

lgh_SE_columns = extract_SE_columns(lghpriser_file)
villa_SE_columns = extract_SE_columns(villapriser_file)

# Get user input for prisavtal
prisavtal_input = input("Ange prisavtal (R, F1, F3): ").upper()

# Check user input and print statistics for villaData and lghData accordingly
if prisavtal_input == "R":
    print("\nKategori lagenhetskund:")
    filter_and_print_statistics(lgh_SE_columns, "Rorligt pris")

    print("\nKategori villakund:")
    filter_and_print_statistics(villa_SE_columns, "Rorligt pris")
elif prisavtal_input == "F1":
    print("\nKategori lagenhetskund:")
    filter_and_print_statistics(lgh_SE_columns, "Fast pris 1 ar")

    print("\nKategori villakund:")
    filter_and_print_statistics(villa_SE_columns, "Fast pris 1 ar")
elif prisavtal_input == "F3":
    print("\nKategori lagenhetskund:")
    filter_and_print_statistics(lgh_SE_columns, "Fast pris 3 ar")

    print("\nKategori villakund:")
    filter_and_print_statistics(villa_SE_columns, "Fast pris 3 ar")
else:
    print("Ogiltigt format. Var god ange R, F1, eller F3.")
