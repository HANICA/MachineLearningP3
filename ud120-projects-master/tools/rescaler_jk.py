#!/usr/bin/python

import numpy
import sys

def featureScaling(arr):
    minF = 0
    maxF = 0
    feature = 0
    if len(arr) == 3:
        minF = min(arr)
        maxF = max(arr)
        for item in arr:
            if (item != minF) and (item != maxF):
                feature = item
        rescaledFeature = (feature - minF) / (maxF - minF)
        return (feature - minF) / (maxF - minF)
    else:
        return 0.0
