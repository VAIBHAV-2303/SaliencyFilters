import numpy as np
import pickle
import cv2
import matplotlib.pyplot as plt

def wt(ci, cj, pi, pj):
	c = np.sum((ci-cj)**2)
	p = np.sum((pi-pj)**2)
	return np.exp(-0.5*(alpha*c + beta*p))

# Parameters
k = 6
alpha = 1/30
beta = 1/30

# Loading labels, centers, uniqueness values, and distribution



# Normalizing uniqueness and distribution
S = U*np.exp(-k*D)

# Creating the final output
I = cv2.imread(sys.argv[1])
I = cv2.cvtColor(I, cv2.COLOR_BGR2Lab)
final = np.zeros((h, w))
for i in range(h):
	for j in range(w):
		z = 0
		ci = I[i, j]
		pi = np.array([i, j])
		for c in range(S.shape[0]):
			cj = centers[c][:3]
			pj = centers[c][-2:]
			final[i, j] += S[c]*wt(ci, cj, pi, pj)
			z += wt(ci, cj, pi, pj)

		final = final/z

plt.imshow(final, cmap='gray')
plt.show()