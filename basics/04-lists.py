# Déclaration de base
ma_liste = [1, 2, 3, 2, 4]

# 📌 1. append(x) → Ajoute un élément à la fin
ma_liste.append(5)
print("append:", ma_liste)  # [1, 2, 3, 2, 4, 5]

# 📌 2. extend(iterable) → Étend la liste avec un autre iterable
ma_liste.extend([6, 7])
print("extend:", ma_liste)  # [1, 2, 3, 2, 4, 5, 6, 7]

# 📌 3. insert(i, x) → Insère x à la position i
ma_liste.insert(2, 99)
print("insert:", ma_liste)  # [1, 2, 99, 3, 2, 4, 5, 6, 7]

# 📌 4. remove(x) → Supprime la première occurrence de x
ma_liste.remove(2)
print("remove:", ma_liste)  # [1, 99, 3, 2, 4, 5, 6, 7]

# 📌 5. pop([i]) → Supprime et retourne l'élément à l’index i (dernier si pas précisé)
dernier = ma_liste.pop()
print("pop:", dernier, ma_liste)  # 7 [1, 99, 3, 2, 4, 5, 6]

# 📌 6. clear() → Vide la liste
temp = [1, 2, 3]
temp.clear()
print("clear:", temp)  # []

# 📌 7. index(x) → Retourne l’index de la première occurrence de x
print("index of 4:", ma_liste.index(4))  # 4

# 📌 8. count(x) → Nombre d’occurrences de x
print("count of 2:", ma_liste.count(2))  # 1

# 📌 9. sort() → Trie la liste (ordre croissant par défaut)
tri = [3, 1, 4, 2]
tri.sort()
print("sort:", tri)  # [1, 2, 3, 4]

# Tri décroissant
tri.sort(reverse=True)
print("sort reverse:", tri)  # [4, 3, 2, 1]

# 📌 10. reverse() → Inverse l’ordre des éléments
tri.reverse()
print("reverse:", tri)  # [1, 2, 3, 4]

# 📌 11. copy() → Crée une copie superficielle de la liste
copie = tri.copy()
print("copy:", copie)  # [1, 2, 3, 4]
  
# Recap
#  _________________________________________________________
# | Méthode        | Description                            |
# | -------------- | -------------------------------------- |
# | `append(x)`    | Ajoute un élément à la fin             |
# | `extend(it)`   | Ajoute tous les éléments d’un itérable |
# | `insert(i, x)` | Insère à l’index `i`                   |
# | `remove(x)`    | Supprime la **première** occurrence    |
# | `pop(i)`       | Supprime et retourne l’élément à `i`   |
# | `clear()`      | Vide la liste                          |
# | `index(x)`     | Renvoie l’index de `x`                 |
# | `count(x)`     | Nombre d’occurrences                   |
# | `sort()`       | Trie la liste                          |
# | `reverse()`    | Inverse la liste                       |
# | `copy()`       | Fait une copie                         |
