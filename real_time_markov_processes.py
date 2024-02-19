import numpy as np
import matplotlib.pyplot as plt

N = 1000
sigma = 5
r = 0.99 # Чтобы не было бесконечного прироста диспресии
en = np.sqrt((1 - r ** 2) * sigma ** 2)

fSignal = np.zeros(N)
fSignal[0] = np.random.normal(0, sigma)

for i in range(N):
    fSignal[i] = r * fSignal[i-1] + np.random.normal(0, en)

plt.plot(fSignal)
plt.grid(True)
plt.show()
