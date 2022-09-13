nombre1 = input("entrez un premier nombre: ")
nombre2 = input("entrez un 2eme nombre: ")
while(int(nombre1) == 0 or int(nombre1) == 0):
  print("les nombres doivent être differents de 0\n")
  nombre1 = input("entrez un premier nombre: ")
  nombre2 = input("entrez un 2eme nombre: ")

produit = int(nombre1) * int(nombre2)
if produit >= 0:
  print(f"{produit} le produit est positif")
else:
  print(f"{produit} est negatif")

#additivité
nombre = int(input("entrez un nombre positif:"))
somme = 0
for i in range(nombre+1):
  somme += i

print(f"la somme est: {somme}")

#somme des elements d'un tableau

tab = [2, 1, 7, 0]
somme = 0
for i in tab:
  somme += i

print(f"la somme des element du tableau est :{somme}------")

#le plus grand nombre du tableau
tableau = [ -1,1, 30, 2, 3, 4, 9, 10]
maximum = max(tableau)
print(maximum)

# for i in tableau:
#   if i >= max:
#     max = i

# print(f"le plus grand nombre est : {max}")

