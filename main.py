from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import csv

chrome_option = webdriver.ChromeOptions()

# Adding argument to disable the AutomationControlled flag
chrome_option.add_argument("--disable-blink-features=AutomationControlled")

# Exclude the collection of enable-automation switches
chrome_option.add_experimental_option("excludeSwitches", ["enable-automation"])

# Turn-off userAutomationExtension
chrome_option.add_experimental_option("useAutomationExtension", False)

chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)

driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

base_url = 'https://skinskoolbeauty.com/discover'

driver.get(url=base_url)
sleep(4)

options = ['Acne and Blemishes', 'Bath and Body', 'Cleansers', 'Eyes and Lips', 'Hair', 'Makeup', 'Masks', 'Moisturizers', 'Sunscreens', 'Treatments and Serums']

option_value = [11, 3, 8, 7, 10, 9, 12, 6, 4, 5]

option_type = [['Acne Cleanser', 'Acne Lotion, Serums and Cream', 'Acne Spot Treatment (incl Gels and stickers)', 'Acne Toner, Pads, Solutions'],
               ['Body Exfoliants and Scrubs', 'Body Lotions and Creams', 'Body Oils', 'Body Washes and Bath/Shower Oils', 'Shaving Products'],
               ['AHA Exfoliants', 'Bar and Stick Cleansers', 'BHA Exfoliants', 'Cleansers', 'Cleansing Cloths', 'Exfoliants', 'Facial Scrubs and Polishers', 'Makeup Removers', 'Toners'],
               ['Eye Lash / Eye Brow', 'Eye Moisturizers', 'Lip Products (Including Lip Exfoliators)', 'Lipsticks', 'Mascaras'],
               ['Hair Colour', 'Hair Conditioners', 'Hair Dry Shampoos', 'Hair Heat Protection', 'Hair Masks', 'Hair Oils and Serums', 'Hair Regrowth', 'Hair Scalp Treatment', 'Hair Shampoos', 'Hair Styling Products', 'Hair Treatment'],
               ['BB, CC Creams and Primers', 'Blush', 'Foundation (incl Cream, Cushion, Stick)', 'Foundation Powder (incl Loose and Setting)', 'Foundation Spray', 'Self-Tanners', 'Setting and Primer Sprays'],
               ['Facial Masks', 'Sheet Masks'],
               ['Face Oils', 'Mists and Essences', 'Moisturizers With Sunscreen', 'Moisturizers Without Sunscreen'],
               ['Sunscreens (Chemical)', 'Sunscreens (Mineral)', 'Sunscreens (Spray)', 'Sunscreens - Sticks (Chemical)', 'Sunscreens - Sticks (Mineral)'],
               ['Serums']]

option_type_value = [[61, 64, 62, 63], [6, 4, 33, 5, 23], [1, 42, 3, 7, 38, 8, 20, 14, 28], [43, 9, 13, 56, 57], [47, 40, 39, 70, 68, 69, 49, 50, 37, 44, 46], [34, 79, 45, 52, 77, 21, 75], [11, 36], [10, 35, 16, 17], [26, 59, 60, 73, 74], [22]]

product_list = []
brand_list = []
unique_key = []
category_list = []
sub_category_list = []

for i in range(len(options)):
    for k in range(len(option_type[i])):
        for page_number in range(1, 12):
            driver.get(f'https://skinskoolbeauty.com//discover?categories={option_type_value[i][k]}&category_id={option_value[i]}&page={page_number}')
            sleep(3)
            try:
                for product_number in range(1, 13):
                    product_name = driver.find_element(By.XPATH, f'//*[@id="pagination-top"]/div/div[{product_number}]/div[2]/div/p[1]/a')
                    product_brand = driver.find_element(By.XPATH, f'//*[@id="pagination-top"]/div/div[{product_number}]/div[2]/div/p[2]')
                    href_value = product_name.get_attribute('href').split('/')[-1][:8]
                    product_list.append(product_name.text)
                    brand_list.append(product_brand.text)
                    unique_key.append(href_value)
                    category_list.append(options[i])
                    sub_category_list.append(option_type[i][k])
            except:
                print("No more products")


csv_file_path = 'data.csv'

rows = zip(product_list, brand_list, unique_key, category_list, sub_category_list)

with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Product', 'Brand', 'Key', 'Category', 'Sub Category'])  # Header row
    writer.writerows(rows)
