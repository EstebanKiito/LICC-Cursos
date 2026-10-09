def ciegos(m,k):
  ########################
  # ESCRIBE TU CÓDIGO AQUÍ
  contador = 0
  for i in range(len(m)):
    trozo = m[i:i+k]
    if 'V' not in trozo:
      contador+=1
  return contador