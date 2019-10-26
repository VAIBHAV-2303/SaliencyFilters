# DIP_Project

Saliency Filters: Contrast Based Filtering for Salient Region Detection

# Team Members

* Pulkit Gera
* Vaibhav Garg
* Saraansh Tandon

# Usage
Currently we have implemented the first part of the process namely Abstraction of the important regions.  
To run `python abstraction.py <path_to_img> <num_of_superpixels>  

# Working
+ Abstraction - In this we try to remove unimportant details and maintain the overall structure of the image. We aim to cluster images with similar properties such as colour into perceptually homogenous regions. We follow the approach of SLIC but instead of clustering in RGBXY space, we cluster in CIELab space based on geodesic distance. This ensures, connectivity while retaining the locality, compactness and edge awareness of the superpiexels.



