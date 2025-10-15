# Un set (ensemble) est une collection non ordonnée, non indexée, et sans doublons.

# ✅ Création d’un set
fruits = {"pomme", "banane", "orange"}
print(fruits)  # {'pomme', 'banane', 'orange'}

# 🔄 Conversion d'une liste en set pour supprimer les doublons
liste = [1, 2, 2, 3, 4, 4, 5]
unique = set(liste)
print(unique)  # {1, 2, 3, 4, 5}

# 🚫 Les éléments du set doivent être immuables (int, str, tuple...)
# set_invalide = {[1, 2], 3}  # ❌ Erreur car list est mutable

# 📌 Ajouter des éléments
fruits.add("kiwi")
print(fruits)  # {'pomme', 'banane', 'orange', 'kiwi'}

# 📌 Ajouter plusieurs éléments
fruits.update(["fraise", "raisin"])
print(fruits)  # {'pomme', 'banane', 'orange', 'kiwi', 'fraise', 'raisin'}

# 🧹 Supprimer des éléments
fruits.remove("orange")  # Supprime "orange" - Erreur si non trouvé
print(fruits)  # {'pomme', 'banane', 'kiwi', 'fraise', 'raisin'}

fruits.discard("mangue")  # Ne fait rien si l'élément n'existe pas
print(fruits)  # {'pomme', 'banane', 'kiwi', 'fraise', 'raisin'}

# Retirer un élément arbitraire
retire = fruits.pop()
print(retire)  # ex: 'pomme'
print(fruits)  # reste du set

# Vider complètement un set
fruits.clear()
print(fruits)  # set()

# ===============================
# 🔄 Opérations ensemblistes
# ===============================

a = {1, 2, 3}
b = {3, 4, 5}

# 🔗 Union
print(a | b)  # {1, 2, 3, 4, 5}
print(a.union(b))  # {1, 2, 3, 4, 5}

# 🔀 Intersection
print(a & b)  # {3}
print(a.intersection(b))  # {3}

# ➖ Différence
print(a - b)  # {1, 2}
print(a.difference(b))  # {1, 2}

# 🔄 Différence symétrique (éléments non communs)
print(a ^ b)  # {1, 2, 4, 5}
print(a.symmetric_difference(b))  # {1, 2, 4, 5}

# ===============================
# ✅ Méthodes utiles
# ===============================

x = {1, 2}
y = {1, 2, 3}

print(x.issubset(y))     # True
print(y.issuperset(x))   # True
print(x.isdisjoint({3})) # True si aucun élément en commun

# ===============================
# 🔄 Boucler sur un set
# ===============================
nombres = {1, 2, 3}
for n in nombres:
    print(n)  # 1 \n 2 \n 3 (ordre arbitraire)

# ===============================
# 📝 Copie de set
# ===============================
a = {1, 2, 3}
b = a.copy()
print(b)  # {1, 2, 3}
print(a is b)  # False

# ===============================
# ❗ Attention
# ===============================
# - Un set est non ordonné → pas d’index
# - Les doublons sont automatiquement ignorés
# - Les éléments doivent être immuables
# - Les sets sont très utiles pour les opérations mathématiques d'ensemble
