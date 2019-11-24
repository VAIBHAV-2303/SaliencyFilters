import numpy as np
import matplotlib.pyplot as plt
import cv2
import pickle
import sys

def load(filename):
	"""Loads data from pickle files"""
	file = open(filename, 'rb')
	data = pickle.load(file)
	file.close()
	return data

def gaussWeight(pi,pj):
    """Calculates the gaussian weights between 2 segment locations"""
    sigma = 60
    prox = np.sum((pi-pj)**2)
    return np.exp(-prox/(2*(sigma**2)))

def uniqCenteres(centers):
	"""Computes the uniqueness of the centers of the image """
	uCenter = []
	for a in centers:
	    c = 0
	    z = 0
	    ci = a[:3]
	    pi = a[-2:]
	    for k in centers:
	        cj = k[:3]
	        pj = k[-2:]
	        z += gaussWeight(pi,pj)
	        c += np.sum((ci-cj)**2)*gaussWeight(pi,pj)
	    uCenter.append(c/z)
	print("Uniqueness completed")
	return np.asarray(uCenter)

def plotImage(centers,labels):
	"""Plots the image """
	h,w = labels.shape
	newImage = np.zeros((h,w))
	for i in range(h):
		for j in range(w):
			newImage[i, j] = centers[labels[i, j]]
	return newImage

def save(filename,centers):
	"""saves in form of pickle file"""
	with open(filename+'.pkl', 'wb') as f:
		pickle.dump(centers, f)

if __name__ == '__main__':
	centers = load('centers.pkl')
	labels = load('labels.pkl')
	unique = uniqCenteres(centers)
	unique = unique / np.max(unique)
	plt.imshow(plotImage(unique,labels),cmap='gray')
	plt.show()
	save('uniq',unique)
