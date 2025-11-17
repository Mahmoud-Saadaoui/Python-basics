# import module
# print(module.say_hello("Mahmoud"))

# import sys
# print(sys.path)

#import module
#print(module.__file__) # path complet de module.py

from module import Car, say_hello, names
for name in names:
    print(say_hello(name))
# print("#" * 100)
yaris = Car("Toyota Yaris", 2020)
# print(f"{yaris.model} was made in {yaris.date}")
# print(__name__)  # affiche le nom du module courant (ici __main__)