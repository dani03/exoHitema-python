tab1 = [1, 3, 4, 2]
tab2 = [4, 5, 6, 8]
num = 0
for i in tab1:
  for j in tab2:
    result = i * j
    num += result

print(num)


# calcule de vecteurs
resultat = 0
for i in range(len(tab1)):
  resultat += tab1[i] * tab2[i]

print(resultat)

# 2.5    Le plus grandEcrire un algorithme permettant
# `a l’utilisateur de renvoyer la plus grande valeurdu  tableau  passer 
# en  input  en  pr ́ecisant  quelle  position  elle  occupe  dans  letableau.

tableau = [2,4,6,32,8,10,12]

  
def get_max_and_position(tableau)-> str:
  maximum = tableau[0]
  position = 0
  for i in range(len(tableau)):
    if maximum < tableau[i]:
      maximum = tableau[i]
      position = i
  return (f"le maximum est :{maximum} sa position est {position}")

get_max_and_position(tableau)


# 2.6    Plus grand que la moyenne
# Ecrire un algorithme permettant `a l’utilisateur de renvoyer le nombre de valeursup ́erieures
# `a la moyenne d’un tableau pass ́e en input de taillen.

tableau = [ 7, 8, 2, 1,2]
nb = 0
moyenne = sum(tableau) / len(tableau)
for i in range(len(tableau)):
  if tableau[i] > moyenne:
    nb += 1