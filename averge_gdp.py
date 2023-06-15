import csv

def calculate_average_gdp(input_csv, output_csv):
    country_gdp = {}

    with open("gdp.csv", 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            country = row['Country']
            gdp_values = [float(row[year].replace(',', '')) for year in reader.fieldnames[1:]]
            average_gdp = sum(gdp_values) / len(gdp_values)
            country_gdp[country] = average_gdp

    with open(output_csv, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Country', 'Average GDP'])
        for country, average_gdp in country_gdp.items():
            writer.writerow([country, average_gdp])

csv_file = 'your_file.csv'  # Replace with the actual file name/path
output_csv_file = 'output_file.csv'  # Replace with the desired output file name/path

calculate_average_gdp(csv_file, output_csv_file)
