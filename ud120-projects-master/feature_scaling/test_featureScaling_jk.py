#!/usr/bin/python

"""
    Test file for feature scaling
    Lesson 10 assignment 10
    
    Should be Python 3 proof...
    
    J.A. Korten Okt 2018
    
    """




import pickle
import numpy
import matplotlib.pyplot as plt
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn.cluster import KMeans
import numpy as np

from rescaler_jk import featureScaling


data = [115, 140, 175]
print (featureScaling(data))

