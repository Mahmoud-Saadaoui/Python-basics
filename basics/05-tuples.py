# 📌 Déclaration de base
colors = ("rouge", "vert", "bleu")
print("Tuple de colors :", colors)

# 📌 Accès aux éléments
print("Première couleur :", colors[0])
print("Dernière couleur :", colors[-1])

# 📌 Longueur d’un tuple
print("Nombre de colors :", len(colors))

# 📌 Parcourir un tuple
print("Les colors disponibles :")
for couleur in colors:
    print("-", couleur)

# 📌 Vérification de la présence d’un élément
if "vert" in colors:
    print("Vert est dans le tuple.")

# 📌 Tuples avec types mélangés
info = ("Alice", 30, True)
print("Tuple mixte :", info)

# 📌 Tuple imbriqué
coordonnées = ((0, 0), (1, 2), (2, 4))
print("Deuxième coordonnée :", coordonnées[1])

# 📌 Un tuple avec un seul élément (⚠️ la virgule est obligatoire)
solo = ("unique",)
print("Tuple avec un seul élément :", solo)
print("Type de solo :", type(solo))

# 📌 Déballage (unpacking) d’un tuple
nom, age, actif = info
print(f"Nom : {nom}, Âge : {age}, Actif : {actif}")