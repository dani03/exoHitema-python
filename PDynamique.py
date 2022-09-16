tab = [7, 10, 12, 7, 9, 14]

def programmationDinamique(tab)-> int:
  newTab = []
  somme = 0
  for i in range(len(tab)):
    num_to_add = tab[i]
    if(i > 1):
      
      j = i - 2
      somme = newTab[j] + tab[i]
      if(somme > newTab[i-1]):
        num_to_add = somme
      else:
        num_to_add = newTab[i-1]
    else:
        num_to_add = tab[i]
    newTab.append(num_to_add)
  print(newTab)
  return newTab[-1];
  
  
print(programmationDinamique(tab))