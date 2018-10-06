#!/usr/bin/python

"""
    Helper methods for decision Adaboost
    
    J.A. Korten, Sept 2018
    
    Helper Class
    Intent is to make these also for other algorithms
    including e.g. k-means and k nearest neighbors
    
    http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html
    http://scikit-learn.org/stable/modules/ensemble.html#adaboost

"""
from time import time

#JK: import specific libraries for particular algorithm
from sklearn.ensemble import AdaBoostClassifier

def classify(features_train, labels_train, n_estimators):
    
    ### your code goes here--should return a trained decision tree classifer
    print("Classify (Fit)...")
    clf = AdaBoostClassifier(n_estimators = n_estimators)
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
