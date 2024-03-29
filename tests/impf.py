import MPImfp
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('sample.png', 0)
size = 1000
barrier = 0
freq_single = np.zeros(size, dtype=np.uint32)
freq_double = np.zeros(size, dtype=np.uint32)
dpix = 1.0
nsample = 1000000
seed = 12345
# single mode
MPImfp.measure(img, barrier, freq_single, dpix, nsample, seed, 0)
ave_single = np.sum(np.arange(size)*np.array(freq_single, dtype=np.float64)/np.sum(freq_single))
print('Average Single :', ave_single)
# double mode
MPImfp.measure(img, barrier, freq_double, dpix, nsample, seed, 1)
ave_double = np.sum(np.arange(size)*np.array(freq_double, dtype=np.float64)/np.sum(freq_double))
print('Average Double :', ave_double)
# plot
plt.plot(np.arange(size), freq_single)
plt.plot(np.arange(size), freq_double)
plt.xlabel('Pixel'), plt.ylabel('Frequency')
plt.show()
