from math import sin, cos, acos, sqrt

conexiones = {
    'Malaga': { 'Salamanca', 'Madrid', 'Barcelona' },
    'Sevilla': { 'Santiago', 'Madrid' },
    'Granada': { 'Valencia' },
    'Valencia': { 'Barcelona' },
    'Madrid': { 'Salamanca', 'Sevilla', 'Malaga', 'Barcelona', 'Santander' },
    'Salamanca': { 'Malaga', 'Madrid' },
    'Santiago': { 'Sevilla', 'Santander', 'Barcelona' },
    'Santander': { 'Santiago', 'Madrid' },
    'Zaragoza': { 'Barcelona' },
    'Barcelona': { 'Zaragoza', 'Santiago', 'Madrid', 'Malaga', 'Valencia' },
  }

conexiones_terrestres = {
  'Malaga': { 'Granada': 125, 'Madrid': 513 },
  'Sevilla': { 'Madrid': 514 },
  'Granada': { 'Malaga': 125, 'Madrid': 423, 'Valencia': 491 },
  'Valencia': { 'Granada': 491, 'Madrid': 356, 'Zaragoza': 309, 'Barcelona': 346 },
  'Madrid': { 'Salamanca': 203, 'Sevilla': 514, 'Malaga': 513, 'Granada': 423, 'Barcelona': 603, 'Santander': 437, 'Santiago': 599 },
  'Salamanca': { 'Santiago': 390, 'Madrid': 203 },
  'Santiago': { 'Salamanca': 390, 'Madrid': 599 },
  'Santander': { 'Zaragoza': 394, 'Madrid': 437 },
  'Zaragoza': { 'Barcelona': 296, 'Valencia': 390, 'Madrid': 313 },
  'Barcelona': { 'Zaragoza': 296, 'Madrid': 603, 'Valencia': 346 }
}

coordenadas = {
  'Malaga': (36.43, -4.24),
  'Sevilla': (37.23, -5.59),
  'Granada': (37.11, -3.35),
  'Valencia': (39.28, -0.22),
  'Madrid': (40.24, -3.41),
  'Salamanca': (40.57, -5.40),
  'Santiago': (42.52, -8.33),
  'Santander': (43.28, -3.48),
  'Zaragoza': (41.39, -0.52),
  'Barcelona': (41.23, 2.11),
}

def distancia(coord1, coord2):
  lat1 = coord1[0]
  lon1 = coord1[0]
  lat2 = coord2[0]
  lon2 = coord2[0]
  return sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)

def geodist(lat1, lon1, lat2, lon2):
  grad_rad = 0.01745329
  rad_grad = 57.29577951
  longitud = lon1 - lon2
  val = (sin(lat1 * grad_rad) * sin(lat2 * grad_rad) + cos(lat1 * grad_rad) * cos(lat2 * grad_rad) * cos(longitud * grad_rad) )
  return (acos(val) * rad_grad * 111.32)

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

