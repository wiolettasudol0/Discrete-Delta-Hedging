import numpy as np

def NormalSample(m):
    Z = np.zeros(m)
    for i in range(m):
        Z[i] = np.random.normal()
    return Z
import numpy as np
