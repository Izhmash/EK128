import numpy as np
from matplotlib import pyplot as plt

# x = np.linspace(0, 3, 20)
# y = np.linspace(0, 9, 20)

# plt.plot(x, y)

image = np.diag(np.arange(40))
plt.imshow(image, cmap=plt.cm.hot)
plt.colorbar()
plt.show()
