import json

with open("data.json", "r") as data_file:
    data = json.load(data_file)
    for el in data:
        print(el["country"])

# print(data)



# import fileinput

# with fileinput.input(files=("africa.txt", "asia.txt")) as files:
#     index = 1
#     for line in files:
#         if fileinput.isfirstline():
#             print(f'\n---- Reading {fileinput.filename()} ----')
#             index = 1
#         print(f'{index}- {line}', end='')
#         index += 1
# ----------------------------------------------
# Result
# ----------------------------------------------
# ---- Reading africa.txt ----
# 1- South Africa
# 2- Tunisia
# 3- Egypt
# 4- Algeria
# 5- Somalia
# 6- Uganda
# 7- Senegal
# 6- Uganda
# 7- Senegal
# 7- Senegal
# 8- Tchad
# 9- Sudan
# 10- Mauritania
# 10- Mauritania
# ---- Reading asia.txt ----
# 1- Palestine
# 2- Iraq
# 3- Malisia
# 4- Indonisia
# 5- Yemen
# 6- Qatar
# 7- Arabic Saoudi
# 8- Jordan
# 9- Syria
# 10- Afghanistan
# 11- Bakistan
# 12- Japon