# Viaje por carretera con busqueda A*

from arbol import Nodo
from datos import geodist, conexiones_terrestres, coordenadas

def compara(x):
  # g(n) + h(n) para ciudad x
  lat1 = coordenadas[x.get_datos()][0]
  lon1 = coordenadas[x.get_datos()][1]
  lat2 = coordenadas[solucion][0]
  lon2 = coordenadas[solucion][1]
  d = int(geodist(lat1, lon1, lat2, lon2))
  return x.get_coste() + d


def buscar_solucion_UCS(conexiones, estado_inicial, solucion):
  solucionado = False
  nodos_visitados = []
  nodos_frontera = []
  nodo_inicial = Nodo(estado_inicial)
  nodo_inicial.set_coste(0)
  nodos_frontera.append(nodo_inicial)
  while not solucionado and len(nodos_frontera) != 0:
    # Ordenar nodos frontera
    nodos_frontera = sorted(nodos_frontera, key=compara)
    nodo = nodos_frontera[0]
    # Extraer el nodo y anadirlo a visitados
    nodos_visitados.append(nodos_frontera.pop(0))
    if nodo.get_datos() == solucion:
      solucionado = True
      return nodo
    else:
      # Expandir nodos hijo (conexiones)
      dato_nodo = nodo.get_datos()
      lista_hijos = []
      for un_hijo in conexiones[dato_nodo]:
        hijo = Nodo(un_hijo)
        # Cálculo de g(n)
        coste = conexiones[dato_nodo][un_hijo]
        hijo.set_coste(nodo.get_coste() + coste)
        lista_hijos.append(hijo)
        if not hijo.en_lista(nodos_visitados):
          # Si esta en la lista lo sustituimos con el nuevo valor de coste, si este ultimo es menor
          if hijo.en_lista(nodos_frontera):
            for n in nodos_frontera:
              if n.igual(hijo) and n.get_coste() > hijo.get_coste():
                nodos_frontera.remove(n)
                nodos_frontera.append(hijo)
          else:
            nodos_frontera.append(hijo)
      nodo.set_hijos(lista_hijos)

if __name__ == "__main__":
  estado_inicial = 'Malaga'
  solucion = 'Santiago'
  nodo_solucion = buscar_solucion_UCS(conexiones_terrestres, estado_inicial, solucion)
  # Mostrar resultado
  resultado = []
  nodo = nodo_solucion
  while nodo.get_padre() != None:
    resultado.append(nodo.get_datos())
    nodo = nodo.get_padre()
  resultado.append(estado_inicial)
  resultado.reverse()
  print(resultado)
  print('Coste: ' + str(nodo_solucion.get_coste()))
