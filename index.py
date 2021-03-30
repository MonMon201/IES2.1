import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import rsg
import f
import additionalTask as at

n = 12
W = 2400
N = 1024
time = range(N)
signal = rsg.getRandomSignal(n, W, N)

s = f.f(signal)

myF_N, myF_T, myF_avg = at.getAvgTime(50, n, W)
npF_N, npF_T, npF_avg = at.getAvgTime(50, n, W, False)

fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
fig.suptitle('Lab 2.1')

ax1.plot(signal, linewidth=0.8)
ax1.set_title('Generated signal')
ax1.set(xlabel='time', ylabel='generated signal')

ax2.plot(s, color='r', linewidth=0.8)
ax2.set_title('Discrete Fourier transform')
ax2.set(xlabel='p', ylabel='F(p)')

ax3.plot(myF_N, myF_T, color='g', label='my function')
ax3.plot(npF_N, npF_T, color='b', label='numpy function')
ax3.set_title('Time comparsion')
ax3.set(xlabel='signal size', ylabel='time')
ax3.legend()
plt.show()