
tab = [[1,2],[3,4],[5,6],[7,8]]

# (1,2)  (5,6)  (12 24)
# (3,4)  (7,8)  (42 52)

# conaitre la taille de la liste
i_moit_tab =int( len(tab) / 2)
index_2 = i_moit_tab
index = 0

for i in range(len(tab)):
  for j in range(len(tab[i])):
    result = tab[index][j] * tab[index_2][j]
    print(result)
    