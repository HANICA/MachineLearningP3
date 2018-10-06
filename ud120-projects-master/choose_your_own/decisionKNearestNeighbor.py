#!/usr/bin/python

"""
    Helper methods for decision K Nearest Neighbor
    
    J.A. Korten, Sept 2018
    
    Helper Class
    Intent is to make these also for other algorithms
    including e.g. k-means and k nearest neighbors
    
    http://scikit-learn.org/stable/modules/neighbors.html

"""
from time import time


#JK: import specific libraries for particular algorithm
from sklearn.neighbors import KNeighborsClassifier
from sklearn import neighbors, datasets


def classify(features_train, labels_train, n_neighbors):
    
    ### your code goes here--should return a trained decision tree classifer
    print("Classify (Fit)...")
    clf = KNeighborsClassifier(n_neighbors = n_neighbors)
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
