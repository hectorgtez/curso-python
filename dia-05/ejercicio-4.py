def es_primo(numero):
  if numero < 2:
    return False

  for i in range(2, numero):
     if  (numero % i) == 0:
        return False

  return True

def contar_primos(num):
    lista_primos = []

    for n in range(2, num+1):
        if es_primo(n):
            lista_primos.append(n)

    return len(lista_primos)

print( contar_primos(20) )