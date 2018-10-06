#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1

    J.A. Korten, Sept 2018
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.metrics import accuracy_score
from sklearn import tree

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()



#########################################################
### your code goes here ###

t0 = time()
#clf = classify(features_train, labels_train)

# without min_samples_split = 40
clf = tree.DecisionTreeClassifier()
print("Fitting...")

clf.fit(features_train, labels_train)

timing_str = "training time:   " + str(round(time()-t0, 3)) + "s"
print(timing_str)

t1 = time()

print("Prediction...")

prediction = clf.predict(features_test)

timing_str = "training time:   " + str(round(time()-t1, 3)) + "s"
print(timing_str)

print("Length predictions: " + str(len(prediction)) + " length labels: " + str(len(labels_test)))

acc = accuracy_score(prediction, labels_test)
print("Accuracy: " + str(acc))

#########################################################

def classify(features_train, labels_train):
    
    ### your code goes here--should return a trained decision tree classifer
    
    clf = tree.DecisionTreeClassifier()
    clf.fit(features_train, labels_train)
    
    return clf

