# Clasificador spam con naive bayes

def lista_palabras(texto):
  palabras = []
  palabras_tmp = texto.lower().split()
  for p in palabras_tmp:
    if p not in palabras and len(p) > 2:
      palabras.append(p)
  return palabras

def entrenar(textos):
  c_palabras = {}
  c_categorias = {}
  c_textos = 0
  c_tot_palabras = 0
  
  # Añadir al diccionario las categorias
  for t in textos:
    c_textos = c_textos + 1
    if t[1] not in c_categorias:
      c_categorias[t[1]] = 1
    else:
      c_categorias[t[1]] = c_categorias[t[1]] + 1

  # Añadir palabras al diccionario
  for t in textos:
    palabras = lista_palabras(t[0])
    for p in palabras:
      if p not in c_palabras:
        c_tot_palabras = c_tot_palabras + 1
        c_palabras[p] = {}
        for c in c_categorias:
          c_palabras[p][c] = 0
      c_palabras[p][t[1]] = c_palabras[p][t[1]] + 1
  return (c_palabras, c_categorias, c_textos, c_tot_palabras)

def clasificar(texto, c_palabras, c_categorias, c_textos, c_tot_palabras):
  categoria = ""
  prob_categoria = 0
  for c in c_categorias:
    # Probabilidad de la categoria
    prob_c = float(c_categorias[c])/float(c_textos)
    palabras = lista_palabras(texto)
    prob_total_c = prob_c
    for p in palabras:
      # Probabilidad de la palabra
      if p in c_palabras:
        prob_p = float(c_palabras[p][c]) / float(c_tot_palabras)
        # Probabilidad P(categoria|palabra)
        prob_cond = prob_p  / prob_c
        # Probabilidad P(palabra|categoria)
        prob = (prob_cond * prob_p) / prob_c
        prob_total_c = prob_total_c * prob
    if prob_categoria < prob_total_c:
      categoria = c
      prob_categoria = prob_total_c
  return (categoria, prob_categoria)

if __name__ == '__main__':
  textos = [
    ["Viagra a buen precio", "spam"],
    ["Quedamos mañana lunes para ir al cine", "nospam"],
    ["Replicas de relojes y viagra a precios de risa", "spam"],
    ["Disponga de sus productos farmaceuticos en 24 horas", "spam"],
    ["La inteligencia artificial es una disciplina muy interesante", "nospam"]
  ]

  p, c, t, tp = entrenar(textos)
  clase = clasificar("Viagra a buen precio en 24 horas", p, c, t, tp)
  print("Texto clasificado como:" + str(clase))