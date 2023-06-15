import csv

# Set the path and name for the new CSV file
output_file = 'countries.csv'

# Create a set to store unique country names
country_set = set()

# Read the CSV file with the appropriate encoding
with open('goalscorers.csv', 'r', encoding='cp1252') as file:
    reader = csv.DictReader(file)
    for row in reader:
        home_team = row['home_team']
        away_team = row['away_team']
        team = row['team']
        
        # Add the country names to the set
        country_set.add(home_team)
        country_set.add(away_team)
        country_set.add(team)

# Convert the set to a list
country_list = list(country_set)

# Sort the country list alphabetically
country_list.sort()

# Write the country names to the new CSV file
with open(output_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['country'])
    writer.writerows([[country] for country in country_list])

print(f"Successfully created '{output_file}' containing the list of countries.")
