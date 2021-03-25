import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import rsg
import f

n = 12
W = 2400
N = 1024
time = range(N)
signal = rsg.getRandomSignal(n, W, N)

s = f.f(signal)

fig, (ax1, ax2) = plt.subplots(2, 1)
fig.suptitle('Lab 2.1')

ax1.plot(signal, linewidth=0.8)
ax1.set_title('Generated signal')
ax1.set(xlabel='time', ylabel='generated signal')

ax2.plot(s, color='r', linewidth=0.8)
ax2.set_title('Discrete Fourier transform')
ax2.set(xlabel='p', ylabel='F(p)')
plt.show()
