# suite de fibonacci
def fibo(num):
  nombre_1 = 0
  nombre_2 = 1
  total = nombre_1 + nombre_2
  for i in range(num+1):
    if i == 0 or i == 1:
      print("inside")
      nombre_1 = 0
      nombre_2 = 1
    else:
      print(f" debut : {nombre_1}, {nombre_2}, {total} \n")
      nombre_1 = nombre_2
      nombre_2  = total
      total = nombre_1 + nombre_2
      print(f" fin: {nombre_1}, {nombre_2}, {total} \n")
      
      
  print(total)
       
fibo(5)

def factorielle(n):
  last_i = 1
  val = 1
  response = ""
  for i in range(1, n+1):
    # response = f"{last_i} x {i}"
    print(response)
    val *=  i
    last_i = i
  print(val)

factorielle(4)

