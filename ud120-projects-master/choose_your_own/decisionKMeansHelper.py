#!/usr/bin/python

"""
    Helper methods for decision K Means
    
    J.A. Korten, Sept 2018
    
    Helper Class
    Intent is to make these also for other algorithms
    including e.g. k-means and k nearest neighbors
    
    http://scikit-learn.org/stable/modules/neighbors.html

"""
from time import time

#JK: import specific libraries for particular algorithm
from sklearn.cluster import KMeans


def classify(features_train, labels_train, n_clusters):
    
    ### your code goes here--should return a trained decision tree classifer
    print("Classify (Fit)...")
    clf = KMeans(n_clusters = n_clusters)
    t0 = time()
    clf.fit(features_train, labels_train)
    timing_str = "Fit:   " + str(round(time()-t0, 3)) + "s"
    print(timing_str)
    return clf

def predict(clf, features_test):
    t0 = time()
    print("Predict...")
    prediction = clf.predict(features_test)
    
    timing_str = "Predict:   " + str(round(time()-t0, 3)) + "s"
    print(timing_str)
    
    return prediction
