# Viaje por carretera con busqueda de coste uniforme

from arbol import Nodo
from datos import conexiones_terrestres

def compara(item):
  return item.get_coste()

def buscar_solucion_UCS(conexiones, estado_inicial, solucion):
  solucionado = False
  nodos_visitados = []
  nodos_frontera = []
  nodo_inicial = Nodo(estado_inicial)
  nodos_frontera.append(nodo_inicial)
  nodo_inicial.set_coste(0)
  nodos_frontera.append(nodo_inicial)

  while (not solucionado) and len(nodos_frontera) != 0:
    # Ordernar la lista
    nodos_frontera = sorted(nodos_frontera, key = compara)
    nodo = nodos_frontera[0]
    
    # Extraer nodo y añadirlo a visitados
    nodos_visitados.append(nodos_frontera.pop(0))
    if nodo.get_datos() == solucion:
      solucionado = True
      return nodo
    else:
      # Expandir nodos hijo
      dato_nodo = nodo.get_datos()
      lista_hijos = []
      for h in conexiones[dato_nodo]:
        hijo = Nodo(h)
        coste = conexiones[dato_nodo][h]
        hijo.set_coste(nodo.get_coste() + coste)
        lista_hijos.append(hijo)
        if not hijo.en_lista(nodos_visitados):
          # Si esta en la lista lo sustituimos con el nuevo valor de coste si es menor
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