import csv
import matplotlib.pyplot as plt

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
villaData = read_file(lghpriser)

# Funktion som genererar listor for varje ar
def generate_year_lists(start_year, end_year, data, column_index):
    year_lists = {}
    for year in range(start_year, end_year + 1):
        if year == 2017:
            # For ar 2017, fyll m 0 for jan-nov och anvand jan 2018 for Dec (FF jan-18 = 0)
            jan_2018_value = float(data[1][column_index['R']])
            year_lists[year] = [0] * 11 + [jan_2018_value]
        elif year == 2018:
            # For 2018, skapa lista m varden jan-dec
            year_lists[year] = [
                float(data[row][column_index['R']]) for row in range(1, 13)
                ]
        elif year == 2023:
            start_row = (year - 2018) * 12 + 1
            end_row = start_row + 6  # 2023 har bara data till juli
    		# Generera lista for 2023 m data jan-juli
            year_lists[year] = [
                float(data[row][column_index['R']]) 
                for row in range(start_row, end_row + 1)] + [0] * 5  # Months 8-12 set to 0
            year_lists[year][7] = year_lists[year][6]  # Satt samma data for aug som juli
        else:
            start_row = (year - 2018) * 12 + 1
            end_row = start_row + 11
            # Generera listor for ovriga ar
            year_lists[year] = [
                float(data[row][column_index['R']]) 
                for row in range(start_row, end_row + 1)
                ]
    return year_lists

# Funkrtion for att berakna forandringsfaktor
def calculate_change_factors(year_lists):
    change_factors = {}
    for year, values in year_lists.items():
        change_factors[year] = []
        for i in range(len(values)):
            if year == 2017 and i == 0:
                # Skippa jan 2017
                continue
            elif i == 0:
                # Rakna forandringsfaktor for jan jamfort m dec foregaende ar
                prev_month_value = year_lists[year - 1][-1]
            else:
                # Berakna forandringsfaktor for ovriga manader
                prev_month_value = values[i - 1]                
            current_value = values[i]            
            # Satt forandringsfaktor for aug-dec 2023 till 0.00
            if year == 2023 and i >= 7:
                change_factors[year].append(0.00)
                continue 
            if prev_month_value == 0:  # Hantera nolldivision
                change_factor = 0
            else:
                change_factor = (
                    (current_value - prev_month_value) / prev_month_value) * 100
            change_factors[year].append(change_factor)
    return change_factors

# Funktion for att plotta bar graph
def plot_change_factor_bar_graph(year_input, area_input, category_text, 
                                 agreement_input, change_factors):
    change_factors_year = change_factors[year_input]
    months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", 
              "aug", "sep", "oct", "nov", "dec"]
    category_text = {
        'V': 'villakund', 'L': 'lagenhetskund'}.get(category_text, category_text)
    agreement_input = {
        'R': 'rörligt', 'F1': 'Fast 1 år', 'F3': 'Fast 3 år'}.get(agreement_input, agreement_input)

    plt.figure(figsize=(10, 6))
    plt.bar(months, change_factors_year, color='red', width=0.4)
    plt.title(f'Månatlig förändring av elpriset för {category_text} i prisområde SE{area_input} år {year_input}')
    plt.xlabel('månad')
    plt.ylabel('förändring [%]')
    plt.xticks(rotation=90)
    plt.ylim(-75, 150) 
    plt.yticks(range(-50, 126, 25))
    plt.tight_layout()
    plt.grid(True)
    plt.legend([f'{agreement_input}'])
    plt.show()

category_input = input("Lägenhetskund (L) eller villakund (V)? : ").upper()
agreement_input = input("Ange prisavtal (R/F1/F3): ").upper()
area_input = int(input("Ange prisområde (1-4): "))
year_input = int(input("Ange önskat årtal (2018-2023): "))

data = lghData if category_input == 'L' else villaData

column_index = {
    'R': 13 if area_input == 4 else 4 * (area_input - 1) + 4,
    'F1': 13 if area_input == 4 else 4 * (area_input - 1) + 2,
    'F3': 13 if area_input == 4 else 4 * (area_input - 1) + 3
}
year_lists = generate_year_lists(2017, 2023, data, column_index)
change_factors = calculate_change_factors(year_lists)
plot_change_factor_bar_graph(year_input, area_input, category_input, 
                             agreement_input, change_factors)