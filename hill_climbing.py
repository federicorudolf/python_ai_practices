# TSP con hill climbing

import random
from datos import distancia, coordenadas

# Calculate the distance covered by the route

def evalua_ruta(ruta):
  total = 0
  for i in range(0, len(ruta) - 1):
    ciudad1 = ruta[i]
    ciudad2 = ruta[i+1]
    total = total + distancia(coordenadas[ciudad1], coordenadas[ciudad2])
  ciudad1 = ruta[i + 1]
  ciudad2 = ruta[0]
  total = total + distancia(coordenadas[ciudad1], coordenadas[ciudad2])
  return total

def hill_climbing():
  # Ruta inicial aleatoria
  ruta = []
  for ciudad in coordenadas:
    ruta.append(ciudad)
  random.shuffle(ruta)

  mejora = True
  while mejora:
    mejora = False
    dist_actual = evalua_ruta(ruta)
    # Evaluar vecinos
    for i in range (0, len(ruta)):
      if mejora:
        break
      for j in range (0, len(ruta)):
        if i != j:
          ruta_temp = ruta[:]
          ciudad_temp = ruta_temp[i]
          ruta_temp[i] = ruta_temp[j]
          ruta_temp[j] = ciudad_temp
          dist = evalua_ruta(ruta_temp)
          if dist < dist_actual:
            # Encontrado vecino que mejora el resultado
            mejora = True
            ruta = ruta_temp[:]
            break
  
  return ruta

if __name__ == "__main__":
  ruta = hill_climbing()
  print(ruta)
  print("Distancia total: " + str(evalua_ruta(ruta)))

