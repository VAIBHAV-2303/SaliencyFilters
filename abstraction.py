import numpy as np
import matplotlib.pyplot as plt
import cv2
import sys

# Loading image as RGB
I = cv2.imread(sys.argv[1])
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(I, cv2.COLOR_BGR2RGB))

# Parameters
m = 80
K = int(sys.argv[2])
N = I.shape[0]*I.shape[1]
S = ((N/K)**0.5)

I = cv2.cvtColor(I, cv2.COLOR_BGR2Lab)

# Creating the 5-tuple for clustering
LabXY = []
for i in range(I.shape[0]):
	for j in range(I.shape[1]):
		LabXY.append( np.concatenate((I[i, j], [(m/S)*i, (m/S)*j])).astype(np.float32))
LabXY = np.array(LabXY)

# Applying the kmeans clustering
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
flags = cv2.KMEANS_RANDOM_CENTERS
compactness, labels, centers = cv2.kmeans(LabXY, K, None, criteria, 10, flags)

# Output image construction
labels = labels.reshape((I.shape[0], I.shape[1]))
for i in range(I.shape[0]):
	for j in range(I.shape[1]):
		I[i, j] = centers[labels[i, j]][:3]

plt.subplot(1, 2, 2)
I = cv2.cvtColor(I, cv2.COLOR_Lab2RGB)
plt.imshow(I)
plt.show()