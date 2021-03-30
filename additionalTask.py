import time
import rsg
import f
import numpy.fft as fft

def getAvgTime(delta, n, W, myFn = True):
  fn = f.f if (myFn) else fft.fft
  t = []
  N = []
  for i in range(delta):
    amount = int(10 * (i + 1))
    N.append(amount)
    x = rsg.getRandomSignal(n, W, amount)
    start = time.perf_counter()
    fn(x)
    stop = time.perf_counter()
    t.append(stop - start)
  average = sum(t)/delta
  return N, t, average
