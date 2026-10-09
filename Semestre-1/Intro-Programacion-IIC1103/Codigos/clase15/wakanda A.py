def costo(m):
  # ESCRIBE TU CÓDIGO AQUÍ
  mayor = 0
  contador = 0
  for i in range(len(m)):
    if m[i]=='-':
      contador+=1
    else:
      if contador>mayor:
        mayor=contador
      contador = 0
  return mayor*10

def costo(m):
  for i in range(len(m)-2,0,-1):
    rejaposible = '-'*i
    if rejaposible in m:
      return i*10
  return 0