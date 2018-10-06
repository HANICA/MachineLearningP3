#!/usr/bin/python

"""
    This is the code to accompany the Lesson 3 (decision tree) mini-project.
    
    Use a Decision Tree to identify emails from the Enron corpus by author:
    Sara has label 0
    Chris has label 1
    
    J.A. Korten, Sept 2018
    
    Helper Class
    Intent is to make these also for other algorithms
    including e.g. k-means and k nearest neighbors

"""
from time import time


#JK: import specific libraries for particular algorithm
from sklearn import tree


def classify(features_train, labels_train, min_samples_split):
    
    ### your code goes here--should return a trained decision tree classifer
    print("Classify (Fit)...")
    clf = tree.DecisionTreeClassifier(min_samples_split = min_samples_split)
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
