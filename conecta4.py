import sys
import copy

MAX = 1
MIN = -1
MAX_PROFUNDIDAD = 4

def negamax(tablero, jugador, profundidad, alfa, beta):
  max_puntuacion = -sys.maxsize - 1
  alfa_local = alfa
  for jugada in range(7):
    # Columna llena
    if tablero[0][jugada] == 0:
      tableroaux = copy.deepcopy(tablero)
      inserta_ficha(tableroaux, jugada, jugador)
      if game_over(tableroaux) or profundidad == 0:
        return [evalua_jugada(tableroaux, jugador), jugada]
      else:
        puntuacion = -negamax(tableroaux, jugador * (-1), profundidad - 1, -beta, -alfa_local)[0]
        if puntuacion > max_puntuacion:
          max_puntuacion = puntuacion
          jugada_max = jugada

          # Poda alfa beta
          if max_puntuacion >= beta:
            break
          if max_puntuacion > alfa_local:
            alfa_local = max_puntuacion
  return [max_puntuacion, jugada_max]

def evalua_jugada(tablero, jugador):
  n2 = comprueba_linea(tablero, 2, jugador)[1]
  n3 = comprueba_linea(tablero, 3, jugador)[1]
  n4 = comprueba_linea(tablero, 4, jugador)[1]
  valor_jugada = 4 * n2 + 9 * n3 + 1000 * n4
  return valor_jugada

def game_over(tablero):
  # Tablas?
  no_tablas = False
  for i in range(7):
    for j in range(7):
      if tablero[i][j] == 0:
        no_tablas = True
  
  # Ganador?
  if ganador(tablero)[0] == 0 and no_tablas:
    return False
  else:
    return True

def comprueba_linea(tablero, n, jugador):
  #Comprueba si hay linea de n fichas
  ganador = 0
  num_lineas = 0
  lineas_posibles = 8 - n

  # Buscar linea horizontal
  for i in range(7):
    for j in range(lineas_posibles):
      cuaterna = tablero[i][j:j + n]
      if cuaterna == [tablero[i][j]] * n and tablero[i][j] != 0:
        ganador = tablero[i][j]
        if ganador == jugador:
          num_lineas = num_lineas + 1

  # Buscar linea vertical
  for i in range(7):
    for j in range(lineas_posibles):
      cuaterna = []
      for k in range(n):
        cuaterna.append(tablero[j + k][i])
      if cuaterna == [tablero[j][i]] * n and tablero[j][i] != 0:
        ganador = tablero[j][i]
        if ganador == jugador:
          num_lineas = num_lineas + 1
  
  #Buscar linea diagonal
  for i in range(4):
    for j in range(lineas_posibles - i):
      cuaterna1 = []
      cuaterna2 = []
      cuaterna3 = []
      cuaterna4 = []

      for k in range(n):
        cuaterna1.append(tablero[i + j + k][j + k])
        cuaterna2.append(tablero[j + k][i + j + k])
        cuaterna3.append(tablero[i + j + k][6 - (j + k)])
        cuaterna4.append(tablero[j + k][6 - (i + j + k)])

      if cuaterna1 == [cuaterna1[0]] * n and tablero[i + j][j] != 0:
        ganador = tablero[i + j][j]
        if ganador == jugador:
          num_lineas = num_lineas + 1
        
      elif cuaterna2 == [cuaterna2[0]] * n and tablero[j][i + j] != 0:
        ganador = tablero[j][i + j]
        if ganador == jugador:
          num_lineas = num_lineas + 1
      
      elif cuaterna3 == [cuaterna3[0]] * n and tablero[i + j][6 - j] != 0:
        ganador = tablero[i + j][6 - j]
        if ganador == jugador:
          num_lineas = num_lineas + 1
      
      elif cuaterna4 == [cuaterna4[0]] * n and tablero[j][6 - (i + j)] != 0:
        ganador = tablero[j][6 - (i + j)]
        if ganador == jugador:
          num_lineas = num_lineas + 1
      
  return (ganador, num_lineas)

def ganador(tablero):
  return comprueba_linea(tablero, 4, 0)

def ver_tablero(tablero):
  tab_aux = copy.deepcopy(tablero)
  for i in range(7):
    for j in range(7):
      if tablero[i][j] == MAX:
        tab_aux[i][j] = 'X'
      elif tablero[i][j] == MIN:
        tab_aux[i][j] = 'O'
      else:
        tab_aux[i][j] = '.'
  print('\n'.join(['\t'.join([tab_aux[i][j] for j in range(7)]) for i in range(7)]))
  print('----------------------------------------------------')
  print('\t'.join([ str(j + 1) for j in range(7)]))

def inserta_ficha(tablero, columna, jugador):
  # Encontrar la primera casilla libre en la col
  ok = False
  for i in range(6, -1, -1):
    if (tablero[i][columna] == 0):
      tablero[i][columna] = jugador
      ok = True
      break
  return ok

def juega_humano(tablero):
  ok = False
  while not ok:
    col = input('Columna (0 = salir) ?')
    if str(col) in '1234567' and len(str(col)) == 1:
      if col == 0:
        sys.exit()
      ok = inserta_ficha(tablero, int(col) - 1, MIN)
    if ok == False:
      print('Movimiento ilegal')
  return tablero

def juega_ordenador(tablero):
  tablero_temp = copy.deepcopy(tablero)
  punt, jugada = negamax(tablero_temp, MAX, MAX_PROFUNDIDAD, -sys.maxsize - 1, sys.maxsize)
  inserta_ficha(tablero, jugada, MAX)

  return tablero

if __name__ == "__main__":
  # Tablero de 7 x 7
  tablero = [[0 for j in range(7)] for i in range(7)]

  ok = False
  profundidades = [3, 4, 6]
  while not ok:
    dificultad = input ('Dificultad ( 1 = facil; 2 = medio; 3 = dificil):')
    if str(dificultad) in '123' and len(str(dificultad)) == 1:
      MAX_PROFUNDIDAD = profundidades[int(dificultad) - 1]
      ok = True
  
  while(True):
    ver_tablero(tablero)
    tablero = juega_humano(tablero)
    if(game_over(tablero)):
      break
    
    tablero = juega_ordenador(tablero)
    if game_over(tablero):
      break

  ver_tablero(tablero)

  g = ganador(tablero)[0]
  if g == 0:
    gana = 'Tablas'
  elif g == MIN:
    gana = 'Jugador'
  else:
    gana = 'Ordenador'

  print('Ganador:', gana)