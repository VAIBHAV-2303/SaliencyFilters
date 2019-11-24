# Saliency Filters

## Description

This is a python-openCV implementation of this [research paper](./2012-06-01-cvpr.pdf) by Stanford University and Disney Research. The basic goal of this piece of code is to do saliency estimation. It has become a valuable tool in image processing. Yet, existing approaches exhibit considerable variation in methodology, and it is often difficult to attribute improvements in result quality to specific algorithm properties. In this algorithm, we reconsider some of the design choices of previous methods and implement a conceptually clear and intuitive algorithm for contrast-based saliency estimation.

## Working

The algorithm can be divided into 4 major steps.

* Abstraction - In this we try to remove unimportant details and maintain the overall structure of the image. We aim to cluster images with similar properties such as colour into perceptually homogenous regions. We follow the approach of SLIC but instead of clustering in RGBXY space, we cluster in CIELab space. This ensures, connectivity while retaining the locality, compactness and edge awareness of the superpiexels.

* Uniqueness Score - This first contrast measure implements the commonly employed assumption that image regions, which stand out from other regions in certain aspects, catch our attention and hence should be labeled more salient. We therefore evaluate how different each respective element is from all other elements constituting an image, essentially measuring the “rarity” of each element. 

* Distribution Score - Here we measure the spatial distribution of the color of each segment of the image. The hypothesis that more compact elements are more salient has been employed here. Moreover a gaussian distribution over the difference of colors has been assumed.

* Assignment - In a final step, we assign the actual saliency values to the input image to get a pixel-accurate saliency map. Thanks to this step, our method can assign proper saliency values even to fine pixel-level detail that was excluded, on purpose, during the abstraction phase, but for which we still want a saliency estimate that conforms to the global saliency analysis.

## How To

* First, make sure you have the required libraries as mentioned in requirements.txt
```console
pip3 install -r ./requirements.txt
```

* If you want to see the intermediate results use:
```console
python3 abstraction.py <path_to_img> <num_of_superpixels>  
python3 uniqueness.py
python3 distribution.py
python3 assignment.py <path_to_img>
```

* To directly run and save the results in a folder named 'results' in the same directory:
```console
bash script.sh <path_to_img> <num_of_superpixels>
```

## Built With

* [Python3](https://docs.python.org/3/)
* [Numpy](https://numpy.org/)
* [Matplotlib](https://matplotlib.org/)
* [OpenCV](https://pypi.org/project/opencv-python/)
* [Pickle](https://docs.python.org/3.5/library/pickle.html)

Version details can be found in requirements.txt

## Authors 

* Pulkit Gera(20171035)
* Vaibhav Garg(20171005)
* Saraansh Tandon(20171007)
