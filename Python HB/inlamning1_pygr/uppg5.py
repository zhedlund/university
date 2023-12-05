import csv
import matplotlib.pyplot as plt

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
villaData = read_file(villapriser)

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

# Extrahera kolumner startar m SE och namnger listor
def extract_SE_columns(file_name):
    data = read_file(file_name)
    se_columns = {}
    # Skapar dictionary med SE-kolumner
    for idx, column in enumerate(data[0]):
        if column.startswith('SE'):
            se_columns[column] = [float(row[idx]) for row in data[1:]]
    return se_columns

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

# Filtrerar statistik for SE kolumner och printar output samt lagger till varden i listor
def filter_and_print_statistics(se_columns, prisavtal, data, statistics_list):
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
            min_month = data[min_row_index][1][:3]
            max_year = data[max_row_index][0]
            max_month = data[max_row_index][1][:3]

            # Lagger till dictionary med key-value pairs till lista, for att anvanda till diagrammen
            statistics_list.append({
                'SE_Type': f"SE{se_type}",
                'Min_Value': min_value,
                'Max_Value': max_value,
                'Mean_Value': mean_value
            })
            # Printar tabellen
            print("{:<12}{:<10.2f}{:<10}{:<10}{:<10.2f}{:<10}{:<10}{:<10.2f}".format(
                f"SE{se_type}", min_value, min_year, min_month, 
                max_value, max_year, max_month, mean_value))

# Meta-funktion for att fa diagrammen bredvid varandra. Fick inte till det med subplot av nagon anledning, sa detta blev en workaround.
def create_side_by_side_scatter_plots(lgh_statistics, villa_statistics, prisavtal):
    def create_scatter_plot(ax, statistics, customer_type):
        SE_types = [entry['SE_Type'] for entry in statistics]
        min_values = [entry['Min_Value'] for entry in statistics]
        max_values = [entry['Max_Value'] for entry in statistics]
        mean_values = [entry['Mean_Value'] for entry in statistics]

        ax.scatter(SE_types, min_values, label='lägsta elpris', marker='o')
        ax.scatter(SE_types, max_values, label='högsta elpris', marker='o')
        ax.scatter(SE_types, mean_values, label='medelvärde', marker='o')
        ax.set_title(f"Elpriser\nLägsta-, högsta- och medelvärde under tidsperioden 2018-2023\nKategori {customer_type} - {prisavtal}")
        ax.set_xlabel('prisområden')
        ax.set_ylabel('pris (öre/kWh)')
        ax.legend()
        ax.grid(True)
        ax.set_xticks(range(len(SE_types)))
        ax.set_xticklabels(SE_types, rotation=90)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    create_scatter_plot(ax1, lgh_statistics, 'lägenhetskund') 
    create_scatter_plot(ax2, villa_statistics, 'villakund')
    plt.tight_layout()
    plt.show()

lgh_SE_columns = extract_SE_columns(lghpriser)
villa_SE_columns = extract_SE_columns(villapriser)

# Listor for berakningar som gors i filter_and_print_statistics, som sedan anvands till diagrammen
lgh_statistics = []
villa_statistics = []

prisavtal_input = input("Ange prisavtal (R, F1, F3): ").upper()

# Anvands till rubriken i diagrammen
if prisavtal_input in ["R", "F1", "F3"]:
    if prisavtal_input == "R":
        prisavtal_text = "rörligt avtal"
    elif prisavtal_input == "F1":
        prisavtal_text = "fast pris 1 år"
    else:
        prisavtal_text = "fast pris 3 år"

# Kollar user input och printar statistik utifran det
if prisavtal_input == "R":
    print_header("rörligt avtal")
    print("\nKategori lägenhetskund:")
    filter_and_print_statistics(lgh_SE_columns, "Rorligt pris", lghData, lgh_statistics)
    print("\nKategori villakund:")
    filter_and_print_statistics(villa_SE_columns, "Rorligt pris", villaData, villa_statistics)
    print ("=" * 80)
elif prisavtal_input == "F1":
    print_header("fast pris 1 år")
    print("\nKategori lägenhetskund:")
    filter_and_print_statistics(lgh_SE_columns, "Fast pris 1 ar", lghData, lgh_statistics)
    print("\nKategori villakund:")
    filter_and_print_statistics(villa_SE_columns, "Fast pris 1 ar", villaData, villa_statistics)
    print ("=" * 80)
elif prisavtal_input == "F3":
    print_header("fast pris 3 år")
    print("\nKategori lägenhetskund:")
    filter_and_print_statistics(lgh_SE_columns, "Fast pris 3 ar", lghData, lgh_statistics)
    print("\nKategori villakund:")
    filter_and_print_statistics(villa_SE_columns, "Fast pris 3 ar", villaData, villa_statistics)
    print ("=" * 80)
else:
    print("Ogiltigt format. Var god ange R, F1, eller F3.")
    
# Skapar diagram
create_side_by_side_scatter_plots(lgh_statistics, villa_statistics, prisavtal_text)