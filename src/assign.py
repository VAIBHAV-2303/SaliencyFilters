import numpy as np
import pickle
import cv2
import matplotlib.pyplot as plt
import sys

# Parameters
k = 6
alpha = 1/30
beta = 1/30

# Loading centers, uniqueness values, and distribution
with open('centers.pkl', 'rb') as f:
	centers = pickle.load(f)

with open('uniq.pkl', 'rb') as f:
	U = pickle.load(f)

with open('distribution.pkl', 'rb') as f:
	D = pickle.load(f)

# Normalizing uniqueness and distribution
S = U*np.exp(k*D)

# Creating the final output
I = cv2.imread(sys.argv[1])
I = cv2.cvtColor(I, cv2.COLOR_BGR2Lab)
h, w = I.shape[:2]
final = np.zeros((h, w))
for i in range(h):
	for j in range(w):

		ci = I[i, j]
		pi = np.array([i, j])

		c = np.sum((centers[:, :3]-ci)**2, axis=1)
		p = np.sum((pi-centers[:, -2:])**2, axis=1)
		W = np.exp(-0.5*(alpha*c  + beta*p))
		final[i, j] = S.dot(W)/np.sum(W)

# Contrast adjustment
final = (255*(final - np.min(final))/(np.max(final - np.min(final)))).astype(np.uint8)
final[final>15] = 255

plt.imshow(final, cmap='gray')
plt.show()