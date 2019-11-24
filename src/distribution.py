import numpy as np
import matplotlib.pyplot as plt
import cv2
import pickle

# helper functions
def load(filename):
    """Loads data from pickle files"""
    file = open(filename, 'rb')
    data = pickle.load(file)
    file.close()
    return data

def save(filename, objects):
    """saves in form of pickle file"""
    with open(filename+'.pkl', 'wb') as f:
        pickle.dump(objects, f)

def gaussWeight(ci,cj):
    """Calculates the gaussian weights between 2 segment colors"""
    sigma = 20
    prox = np.sum((ci-cj)**2)
    return np.exp(-prox/(2*(sigma**2)))

def plotImage(colors,labels):
    """Plots the image """
    h,w = labels.shape
    newImage = np.zeros((h,w))
    for i in range(h):
        for j in range(w):
            newImage[i, j] = colors[labels[i, j]]
    return newImage


# loading
centers = load("centers.pkl")
labels = load("labels.pkl")

# calculating distribution
distribution = []
for centi in centers:
    ui = 0
    for centj in centers:
    	ui += gaussWeight(centj[:3], centi[:3])*centj[3:]
    
    Zi = 0
    summation = 0

    for centj in centers:
        w = gaussWeight(centi[:3], centj[:3])
        Zi += w
        summation += w * np.sum((centj[3:] - ui)**2)
    distribution.append(summation / Zi)
distribution = np.array(distribution)
distribution = distribution / np.max(distribution)
print("Distribution completed")

#display image
plt.imshow(plotImage(distribution, labels), cmap='gray')
plt.show()
plt.savefig('results/distribution')
# save data
save('distribution', distribution)