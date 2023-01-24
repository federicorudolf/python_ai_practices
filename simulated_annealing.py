# TSP con templado simulado

import math
import random
from datos import coordenadas, evalua_ruta

def simulated_annealing(ruta):
  T = 20
  T_MIN = 0
  v_enfriamiento = 100

  while T > T_MIN:
    dist_actual = evalua_ruta(ruta)
    for i in range(1, v_enfriamiento):
      # Intercambiamos dos ciudades aleatoriamente
      i = random.randint(0, len(ruta) - 1)
      j = random.randint(0, len(ruta) - 1)
      ruta_tmp = ruta[:]
      ciudad_tmp = ruta_tmp[i]
      ruta_tmp[i] = ruta_tmp[j]
      ruta_tmp[j] = ciudad_tmp
      dist = evalua_ruta(ruta_tmp)
      delta = dist_actual - dist
      if (dist < dist_actual):
        ruta = ruta_tmp[:]
        break
      elif random.random() < math.exp(delta / T):
        ruta = ruta_tmp[:]
        break

    # Enfriamos T
    T = T - 0.05
  return ruta

if __name__ == "__main__":
  # Crear ruta inicial
  ruta = []
  for ciudad in coordenadas:
    ruta.append(ciudad)
  random.shuffle(ruta)

  ruta = simulated_annealing(ruta)
  print(ruta)
  print("Distancia total: " + str(evalua_ruta(ruta)))
