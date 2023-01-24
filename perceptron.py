# Simple perceptron implementation for an OR operation

def output(k, weights, t):
    z = -t
    for i in range(len(k)):
      z = z + (k[i] * weights[i])
    if z >= 0:
      return 1
    else:
      return 0
    
def train_perceptron(data_entry, weights, t, l):
  errors = True
  while errors:
    errors = False
    # Train perceptron

    for k, v in iter(data_entry.items()):
      z = output(k, weights, t)
      if z != v:
        errors = True
        # Error
        e = (v - z)
        # Calculate adjustments
        delta_t = - (l * e)
        t = t + delta_t
        for i in range(len(k)):
          delta_w = l * e * k[i]
          weights[i] = weights[i] + delta_w
  return weights, t

def clasify(entry, weights, t):
  return output(entry, weights, t)

if __name__ == "__main__":
  data_entry = { (0, 0): 0, (0, 1): 0, (1, 0): 0, (1, 1): 0 }
  weights = [0.2, -0.5]
  t = 0.4
  l = 0.2
  weights, t = train_perceptron(data_entry, weights, t, l)
  print (clasify((0, 1), weights, t))

