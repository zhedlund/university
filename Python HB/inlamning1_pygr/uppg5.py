import csv
import matplotlib.pyplot as plt

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

def print_header(prisavtal):
    print ("=" * 80, "\n\n")
    print(f"              Lägsta- högsta- och medelvärde av elpriserna")
    print(f"              under tidsperioden 2018-2023 for {prisavtal}\n\n")
    print("{:<12}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format(
        "Prisomr.", "lägsta", "år", "mån", "högsta",
        "år", "mån", "medel"))
    print("-" * 80)

# Filtrerar statistik for SE kolumner och printar output
def filter_and_print_statistics(se_columns, prisavtal, data):
    for se_type in range(1, 5):
        column_name = f"SE{se_type}-{prisavtal}"
        if column_name in se_columns:
            min_value = find_min(se_columns[column_name])
            max_value = find_max(se_columns[column_name])
            mean_value = find_mean(se_columns[column_name])
            
            # Extrahera row index min, max, medel i dataset
            min_row_index = se_columns[column_name].index(min_value) + 1  # Skippa header row
            max_row_index = se_columns[column_name].index(max_value) + 1 
            
            # Hitta ar och manad
            min_year = data[min_row_index][0]
            min_month = data[min_row_index][1]
            max_year = data[max_row_index][0]
            max_month = data[max_row_index][1]

            print("{:<12}{:<10.2f}{:<10}{:<10}{:<10.2f}{:<10}{:<10}{:<10.2f}".format(
                f"SE{se_type}", min_value, min_year, min_month[:3], 
                max_value, max_year, max_month[:3], mean_value))

lghpriser_file = 'lghpriser.csv'
villapriser_file = 'villapriser.csv'

lgh_SE_columns = extract_SE_columns(lghpriser_file)
villa_SE_columns = extract_SE_columns(villapriser_file)

lghData = read_file(lghpriser_file)
villaData = read_file(villapriser_file)

# Get user input for prisavtal
prisavtal_input = input("Ange prisavtal (R, F1, F3): ").upper()

# Check user input and print statistics for villaData and lghData accordingly
if prisavtal_input == "R":
    print_header("rörligt avtal")
    print("\nKategori lägenhetskund:")
    filter_and_print_statistics(lgh_SE_columns, "Rorligt pris", lghData)
    print("\nKategori villakund:")
    filter_and_print_statistics(villa_SE_columns, "Rorligt pris", villaData)
    print ("=" * 80)
elif prisavtal_input == "F1":
    print_header("fast pris 1 år")
    print("\nKategori lägenhetskund:")
    filter_and_print_statistics(lgh_SE_columns, "Fast pris 1 ar", lghData)
    print("\nKategori villakund:")
    filter_and_print_statistics(villa_SE_columns, "Fast pris 1 ar", villaData)
    print ("=" * 80)
elif prisavtal_input == "F3":
    print_header("fast pris 3 år")
    print("\nKategori lägenhetskund:")
    filter_and_print_statistics(lgh_SE_columns, "Fast pris 3 ar", lghData)
    print("\nKategori villakund:")
    filter_and_print_statistics(villa_SE_columns, "Fast pris 3 ar", villaData)
    print ("=" * 80)
else:
    print("Ogiltigt format. Var god ange R, F1, eller F3.")
