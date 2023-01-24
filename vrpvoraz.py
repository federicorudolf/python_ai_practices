# VRP
from operator import itemgetter
from datos import distancia, coordenadas

def en_ruta(rutas, c):
  ruta = None
  for r in rutas:
    if c in r:
      ruta = r
  return ruta

def peso_ruta(ruta):
  total = 0
  for c in ruta:
    total = total + pedidos[c]
  return total

def vrp_voraz():
  # Calcular los ahorros
  s = {}
  for c1 in coordenadas:
    for c2 in coordenadas:
      if c1 != c2:
        if not(c2, c1) in s:
          d_c1_c2 = distancia(coordenadas[c1], coordenadas[c2])
          d_c1_almacen = distancia(coordenadas[c1], almacen)
          d_c2_almacen = distancia(coordenadas[c2], almacen)
          s[c1, c2] = d_c1_almacen + d_c2_almacen - d_c1_c2
  
  # Ordenar ahorros
  s = sorted(s.items(), key=itemgetter(1), reverse=True)

  # Construir rutas
  rutas = []
  for k, v in s:
    rc1 = en_ruta(rutas, k[0])
    rc2 = en_ruta(rutas, k[1])
    if rc1 == None and rc2 == None:
      # No estan en ninguna ruta. La creamos
      if peso_ruta([k[0], k[1]]) <= max_carga:
        rutas.append([k[0], k[1]])
    elif rc1 != None and rc2 == None:
      # Ciudad 1 esta en una ruta. Agregamos la 2
      if rc1[0] == k[0]:
        if peso_ruta(rc1) + peso_ruta([k[1]]) <= max_carga:
          rutas[rutas.index(rc1)].insert(0, k[1])
      elif rc1[len(rc1) - 1]==k[0]:
        if peso_ruta(rc1) + peso_ruta([k[1]]) <= max_carga:
          rutas[rutas.index(rc1)].append(k[1])
    elif rc1 == None and rc2 != None:
      # Ciudad 2 esta en una ruta. Agregamos la 1
      if rc2[0] == k[1]:
        if peso_ruta(rc2) + peso_ruta([k[0]]) <= max_carga:
          rutas[rutas.index(rc2)].insert(0, k[0])
      elif rc2[len(rc2) - 1] == k[1]:
        if peso_ruta(rc2) + peso_ruta([k[0]]) <= max_carga:
          rutas[rutas.index(rc2)].append(k[0])
    elif rc1 != None and rc2 != None and rc1 != rc2:
      # Ciudad 1 y 2 ya en una ruta. Tratamos de unirlas
      if rc1[0] == k[0] and rc2[len(rc2) - 1] == k[1]:
        if peso_ruta(rc1) + peso_ruta(rc2) <= max_carga:
          rutas[rutas.index(rc2)].extend(rc1)
          rutas.remove(rc1)
      elif rc1[len(rc1) - 1] == k[0] and rc2[0] == k[1]:
        if peso_ruta(rc1) + peso_ruta(rc2) <= max_carga:
          rutas[rutas.index(rc1)].extend(rc2)
          rutas.remove(rc2)
  return rutas

if __name__ == "__main__":
  pedidos = {
    'Malaga': 10,
  'Sevilla': 13,
  'Granada': 7,
  'Valencia': 11,
  'Madrid': 15,
  'Salamanca': 8,
  'Santiago': 6,
  'Santander': 7,
  'Zaragoza': 8,
  'Barcelona': 14,
  }
  almacen = (40.23, -3.40)
  max_carga = 40

  rutas = vrp_voraz()
  for ruta in rutas:
    print(ruta)

