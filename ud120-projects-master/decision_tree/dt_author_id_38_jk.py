#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1

    J.A. Korten, Sept 2018

    4.38: Decision Trees Excercise
    

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

def classify(features_train, labels_train, min_samples_split):

    ### your code goes here--should return a trained decision tree classifer
    print("Classify (Fit)...")
    clf = tree.DecisionTreeClassifier(min_samples_split = min_samples_split)
    t0 = time()
    clf.fit(features_train, labels_train)
    timing_str = "Fit:   " + str(round(time()-t0, 3)) + "s"
    print(timing_str)
    return clf

def predict(clf, features_train, labels_train):
    t0 = time()
    print("Predict...")
    prediction = clf.predict(features_test)

    timing_str = "Predict:   " + str(round(time()-t0, 3)) + "s"
    print(timing_str)

    return prediction


#########################################################
### your code goes here ###


print("Amount of features: " + str(len(features_train[0])))

#clf0 = classify(features_train, labels_train, 2)
#prediction0 = predict(clf0, features_train, labels_train)
#acc_min_samples_split_2 = accuracy_score(prediction0, labels_test)
#print("Accuracy prediction 1 (2): " + str(acc_min_samples_split_2))

#clf1 = classify(features_train, labels_train, 50)
#prediction1 = predict(clf1, features_train, labels_train)
#acc_min_samples_split_50 = accuracy_score(prediction1, labels_test)
#print("Accuracy prediction 2 (50): " + str(acc_min_samples_split_50))

#clf2 = classify(features_train, labels_train, 40)
#prediction2 = predict(clf2, features_train, labels_train)
#acc_min_samples_split_40 = accuracy_score(prediction2, labels_test)
#print("Accuracy prediction 3 (40): " + str(acc_min_samples_split_40))

#########################################################


