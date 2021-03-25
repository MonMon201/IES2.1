import math

def fCoef(pk, N):
  arg = 2 * math.pi * pk / N
  return complex(math.cos(arg), -math.sin(arg))

def f(signal):
  N = len(signal)
  spectre = list()
  for p in range(N):
    sum = 0
    for k in range(N):
      x = signal[k]
      w = fCoef(p*k, N)
      sum += w * x
    res = abs(sum)
    spectre.append(res)
  return spectre