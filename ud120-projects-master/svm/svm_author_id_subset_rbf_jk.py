#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1

    J.A. Korten Sept 2018
    See: http://scikit-learn.org/stable/modules/svm.html
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

from sklearn import svm

clf = svm.SVC(kernel='rbf')
print("Fit (training)...")

t0 = time()

# Making it a lot faster but using less features / labels:
features_train = features_train[:int(len(features_train)/100)] 
labels_train = labels_train[:int(len(labels_train)/100)] 

clf.fit(features_train, labels_train)
timing_str = "training time:   " + str(round(time()-t0, 3)) + "s"
print(timing_str)

t1 = time()
print("Predict...")
predict = clf.predict(features_test)
timing_str = "prediction time: " + str(round(time()-t1, 3)) + "s"
print(timing_str)

print("Accuracy...")
accuracy = clf.score(features_test, labels_test)

print("accuracy: " + str(round(accuracy, 4)))

#########################################################


