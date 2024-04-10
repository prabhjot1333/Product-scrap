# import csv
# import requests
# from bs4 import BeautifulSoup
#
# csv_filename = 'data.csv'
# output_csv_filename = 'output_data.csv'
#
# name = []
# product = []
# key = []
#
# with open(csv_filename, 'r') as file:
#     reader = csv.reader(file)
#     next(reader)
#     for row in reader:
#         name.append(row[0])
#         product.append(row[1])
#         key.append(row[2])
#
# they_say = []
# ingredients = []
#
# for n in range(len(name)):
#     response = requests.get(f"https://skinskoolbeauty.com/product/{product[n]}/{name[n]}{key[n]}")
#     soup = BeautifulSoup(response.text, 'html.parser')
#     say = soup.find(name='p', class_='hidden')
#     if say:
#         they_say.append(say.text.strip())
#     else:
#         they_say.append("N/A")
#
#     ingred = soup.find_all(name='p', class_='leading-relaxed')
#     # Check if any ingredients are found
#     if ingred:
#         items = ingred[-1].text.strip()  # Get the text of the last 'p' tag
#     else:
#         items = "N/A"  # If no ingredients are found, set to "N/A"
#
#     ingredients.append(items)
#
# # Write the data to a new CSV file
# with open(output_csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['They Say', 'Ingredients'])  # Header row
#     writer.writerows(zip(they_say, ingredients))
#
# for n in range(len(name)):
#     response = requests.get(f"https://skinskoolbeauty.com/product/{product[n]}/{name[n]}{key[n]}")
#     soup = BeautifulSoup(response.text, 'html.parser')
#     say = soup.find(name='span', class_='hidden')
#     they_say.append([say.text.strip()])
#
# with open('theysay.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['They say'])  # Header row
#     writer.writerows(they_say)
#
#
# link_list = []
#
# for n in range(len(name)):
#     # Replace empty spaces with hyphens in the URL
#     link = f"https://skinskoolbeauty.com/product/{product[n].replace(' ', '-')}/{name[n].replace(' ', '-')}-{key[n]}"
#     link_list.append([link])
#
# with open('linklist.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['Link'])  # Header row
#     writer.writerows(link_list)
#


import csv
import requests
from bs4 import BeautifulSoup

csv_filename = 'data.csv'
output_csv_filename = 'output_data.csv'

data = []

with open(csv_filename, 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        name = row[0]
        product = row[1]
        key = row[2]

        response = requests.get(f"https://skinskoolbeauty.com/product/{product}/{name.replace(' ', '-')}-{key}")
        soup = BeautifulSoup(response.text, 'html.parser')

        say = soup.find(name='p', class_='hidden')
        they_say_text = say.text.strip() if say else "N/A"

        ingred = soup.find_all(name='p', class_='leading-relaxed')
        items = ingred[-1].text.strip() if ingred else "N/A"

        link = f"https://skinskoolbeauty.com/product/{product}/{name.replace(' ', '-')}-{key}"

        data.append([they_say_text, items, link])

# Write the data to a new CSV file
with open(output_csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['They Say', 'Ingredients', 'Link'])  # Header row
    writer.writerows(data)
