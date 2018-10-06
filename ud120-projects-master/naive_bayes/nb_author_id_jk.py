#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1

    Implementation example J.A. Korten, Sept 2018
    see: https://classroom.udacity.com/courses/ud120/lessons/2254358555/concepts/24307885370923
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess

#added:
import numpy




### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###
### J.A. Korten Sept 2018

from sklearn.naive_bayes import GaussianNB

clf = GaussianNB()
clf.fit(features_train, labels_train)

predict = clf.predict(features_test)

accuracy = clf.score(features_test, labels_test)


print(accuracy)

#########################################################


