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
maximum = int(max(tableau))
print(maximum)

for i in tableau:
  if i >= maximum:
    maximum = i

print(f"le plus grand nombre est : {max}")

# 2.7 Ecrire un algorithme permettant d’effectuer la multiplication 
# de deux vecteurs de tailleNconnue `a l’avance et d’afficher le résultat.
def calcul_vecteur(tab1, tab2):
  new_list = []
  for i in range(len(tab1)):
    val = tab1[i] * tab2[i]
    new_list.append(val)
  print(new_list)

tableau = [1, 2, 3]
tableau2 = [4, 5, 3]
calcul_vecteur(tableau, tableau2)

#tri Ecrire un algorithme permettant de trier un tableau de taille n
tableau3 = [4, 5, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def tri(tab, mod):
  isIt = []
  imp = []
  for i in range(len(tableau3)):
    if tableau3[i] % mod :
      imp.append(tableau3[i])
    else:
      isIt.append(tableau3[i])
  print(f"pair: {isIt}, impair: {imp}")

tri(tableau3, 2)

#multiplication matricielle

a = [3, 4]
b = [2, 6]
c = []

for i in range(len(a)):
  produit = a[i] * b[i]
  c.append(produit)

print(c)
#########################


# #####################################
tableau = [1, 5, 20, 30] 
def calcul_moyenne(tableau):
  somme = 0
  index = 0
  while index < len(tableau) :
    somme += tableau[index]
    index += 1
  
  moyenne = somme / len(tableau)
  return moyenne
  
la_moyenne = calcul_moyenne(tableau)
older_moyenne = []

for element in tableau:
  if (element > la_moyenne):
    older_moyenne.append(element)

print(older_moyenne, la_moyenne)

def tab_max(arr) -> int:
  maximum = 0
  for i in arr:
    if i > maximum:
      maximum = i
  return maximum

tab1 = [1, 3, 5, 10]  
tab2 = [4, 20, 9, 5]

max_tab_1 = tab_max(tab1)  
max_tab_2 = tab_max(tab2)

total = max_tab_1 + max_tab_2

print(total)

############ 
tab1 = [-1, -3, -5, -10]  
tab2 = [-4, -20, -9, -5]

for i in range(0, len(tab1)):
  maximum = tab1[0]
  if maximum <  tab1[i]:
    maximum = tab1[i]
  else:
    maximum = tab1[i]

print(maximum)

#le temps d'arret

number = int(input("entrez une valeur: "))
somme = 0
all_values = []
while number > somme:
  somme += 1/i
  all_values.append(round(somme, 2))
  i+= 1

print(all_values)
print(i-1)


#progammation dynamique

  
    

