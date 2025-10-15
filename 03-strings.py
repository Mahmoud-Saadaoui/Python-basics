name = 'mahmoud saadaoui'

a = name[0] # 'm'
b = name[0:4] #'mah'
# name[0] = "M" # TypeError: object does not support item 
c = 'M' + name[1:] # 'Mahmoud saadaoui'
d = name[:-1] + "K"
print(d) # mahmoud saadaouK

print('a' in name) # True
print('D' in name) # False
print(len(name)) # 16
print(name.find('s')) # 8
print(name.find('a'))  # 1
print(name.find('y')) # -1 ==> introuvable

greet = f'Hello {name}' # Hello mahmoud saadaoui
