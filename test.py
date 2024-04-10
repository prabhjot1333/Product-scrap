import csv
import requests
from bs4 import BeautifulSoup

csv_filename = 'data.csv'
name = []
product = []
key = []

with open(csv_filename, 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        name.append(row[0])
        product.append(row[1])
        key.append(row[2])

main_texts = []
sub_texts = []


for n in range(len(name)):
    response = requests.get(f"https://skinskoolbeauty.com/product/{product[n]}/{name[n].replace(' ', '-')}-{key[n]}")
    soup = BeautifulSoup(response.text, 'html.parser')
    tag1 = soup.find(name='div', class_="categories col-span-5 lg:col-span-6 flex flex-wrap gap-4")
    tag2 = soup.find(name='div', class_="pm-row-3 attributes flex-wrap gap-2 flex")
    main_text = tag1.text.strip().split('\n\n\n\n') if tag1 else None
    sub_text = tag2.text.strip().split('\n\n\n\n') if tag2 else None
    main_texts.append(main_text)
    sub_texts.append(sub_text)

output_filename = 'scraped_data.csv'

with open(output_filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Main Text', 'Sub Text'])
    for main_text, sub_text in zip(main_texts, sub_texts):
        writer.writerow([main_text, sub_text])

print(f"Scraped data saved to '{output_filename}' successfully.")
