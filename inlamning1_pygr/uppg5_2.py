import csv

# Read the CSV file and get the data
def read_file(file_name):
    data = []
    with open(file_name, 'r', newline='') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            data.append(row)
    return data

# Function to extract columns starting with 'SE' and name the lists accordingly
def extract_SE_columns(file_name):
    data = read_file(file_name)
    se_columns = {}

    # Check for columns starting with 'SE' and add them to se_columns dictionary
    for idx, column in enumerate(data[0]):
        if column.startswith('SE'):
            se_columns[column] = [float(row[idx]) for row in data[1:]]

    return se_columns



# Read the file and extract SE columns
lghpriser_file = 'lghpriser.csv'
villapriser_file = 'villapriser.csv'

lgh_SE_columns = extract_SE_columns(lghpriser_file)
villa_SE_columns = extract_SE_columns(villapriser_file)

# Function to calculate statistics (min, max, mean) for SE columns
def calculate_statistics(se_columns):
    statistics = {}

    # Calculate statistics for each SE column
    for column_name, column_data in se_columns.items():
        min_value = min(column_data)
        max_value = max(column_data)
        mean_value = sum(column_data) / len(column_data)
        statistics[column_name] = {
            'min': min_value,
            'max': max_value,
            'mean': mean_value
        }

        # Print statistics for each SE column
        print(f"Statistics for {column_name}:")
        print(f"Min: {min_value}")
        print(f"Max: {max_value}")
        print(f"Mean: {mean_value}\n")

    return statistics

# Function to filter highest, lowest, and mean values for each SE column based on price type
def filter_statistics_by_price_type(se_columns):
    filtered_statistics = {}

    # Iterate through each SE column
    for column_name, column_data in se_columns.items():
        SE_number = column_name.split('-')[0][-1]  # Extract the SE number from the column name
        price_type = column_name.split(':')[-1].strip()  # Extract the price type

        # Check if the price type matches the desired ones
        if price_type in ["Fast pris 1 ar", "Fast pris 3 ar", "Rorligt pris"]:
            # Calculate statistics for the selected price type
            min_value = min(column_data)
            max_value = max(column_data)
            mean_value = sum(column_data) / len(column_data)

            # Store the statistics in a dictionary based on SE number and price type
            if SE_number not in filtered_statistics:
                filtered_statistics[SE_number] = {}

            filtered_statistics[SE_number][price_type] = {
                'min': min_value,
                'max': max_value,
                'mean': mean_value
            }

            # Print statistics for the selected price type
            print(f"Statistics for SE{SE_number}-{price_type}:")
            print(f"Min: {min_value}")
            print(f"Max: {max_value}")
            print(f"Mean: {mean_value}\n")

    return filtered_statistics

def filter_statistics(se_columns):
    for se_number in range(1, 5):
        for pris_type in ["Fast pris 1 ar", "Fast pris 3 ar", "Rorligt pris"]:
            column_name = f"SE{se_number}-{pris_type}"
            if column_name in se_columns:
                min_value = min(se_columns[column_name])
                max_value = max(se_columns[column_name])
                mean_value = sum(se_columns[column_name]) / len(se_columns[column_name])

                print(f"Statistics for {column_name}:")
                print(f"Min - {min_value}")
                print(f"Max - {max_value}")
                print(f"Mean - {mean_value}\n")

def filter_and_print_statistics(se_columns):
    for pris_type in ["Fast pris 1 ar", "Fast pris 3 ar", "Rorligt pris"]:
        print(f"Lägsta-, högsta- och medelvärden av elpriserna under tidsperioden 2018-2023 för {pris_type} avtal.\n")
        print("Prisomr. lägsta — år mån — högsta år — mån medel")
        print("-" * 51)

        for se_number in range(1, 5):
            column_name = f"SE{se_number}-{pris_type}"
            if column_name in se_columns:
                min_value = min(se_columns[column_name])
                max_value = max(se_columns[column_name])
                mean_value = sum(se_columns[column_name]) / len(se_columns[column_name])

                # Replace this section with logic to extract the years and months from the data
                # Extracting year and month for min and max values for now
                min_year = '2020'
                min_month = 'Apr'
                max_year = '2022'
                max_month = 'Dec'

                print(f"SE{se_number} {min_value:.2f} {min_year} {min_month}  {max_value:.2f} {max_year} {max_month} {mean_value:.2f}")

        print("=" * 51)

# Filter statistics for lgh and villa SE columns based on price type
lgh_filtered_statistics = filter_statistics_by_price_type(lgh_SE_columns)
villa_filtered_statistics = filter_statistics_by_price_type(villa_SE_columns)

# Calculate statistics for lgh and villa SE columns
lgh_statistics = calculate_statistics(lgh_SE_columns)
villa_statistics = calculate_statistics(villa_SE_columns)

# Printing the calculated statistics for lgh and villa SE columns
print("Statistics for lgh SE columns:")
for column_name, stats in lgh_statistics.items():
    print(f"{column_name}: Min - {stats['min']}, Max - {stats['max']}, Mean - {stats['mean']}")

print("\nStatistics for villa SE columns:")
for column_name, stats in villa_statistics.items():
    print(f"{column_name}: Min - {stats['min']}, Max - {stats['max']}, Mean - {stats['mean']}")

# Printing filtered statistics for lgh and villa SE columns
print("\nFiltered Statistics for lgh SE columns:")
for SE_number, prices in lgh_filtered_statistics.items():
    for price_type, stats in prices.items():
        print(f"Statistics for SE{SE_number}-{price_type}:")
        print(f"Min - {stats['min']}, Max - {stats['max']}, Mean - {stats['mean']}")

print("\nFiltered Statistics for villa SE columns:")
for SE_number, prices in villa_filtered_statistics.items():
    for price_type, stats in prices.items():
        print(f"Statistics for SE{SE_number}-{price_type}:")
        print(f"Min - {stats['min']}, Max - {stats['max']}, Mean - {stats['mean']}")

print("Filtered Statistics for lgh SE columns:")
filter_statistics(lgh_SE_columns)

print("\nFiltered Statistics for villa SE columns:")
filter_statistics(villa_SE_columns)

# Filter and print statistics for lgh and villa SE columns
print("Filtered Statistics for lgh SE columns:")
filter_and_print_statistics(lgh_SE_columns)

print("\nFiltered Statistics for villa SE columns:")
filter_and_print_statistics(villa_SE_columns)