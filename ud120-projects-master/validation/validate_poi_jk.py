#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
    
    JK: Updated for P3
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "rb") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

sort_keys = '../tools/python2_lesson13_keys.pkl'

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

### it's all yours from here forward!

## Step 1. Create a decision tree classifier (just use the default parameters),

from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

clf = DecisionTreeClassifier(random_state=0)
iris = load_iris()
cross_val_score(clf, iris.data, iris.target, cv=10)

clf.fit(features, labels)

## Step 2. Train it on all the data (you will fix this in the next part!),

accuracy = clf.score(features, labels)

## Step 3. Print out the accuracy. (Note: THIS IS AN OVERFIT TREE, DO NOT TRUST THIS NUMBER!)
## Nonetheless, what’s the accuracy?
print("Accuracy before splitting with random: " + str(accuracy)) # should be 0.9894736842105263


# 14.18:

data = featureFormat(data_dict, features_list,sort_keys = sort_keys)

labels, features = targetFeatureSplit(data)
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)

clf = DecisionTreeClassifier(random_state=0)
iris = load_iris()
cross_val_score(clf, iris.data, iris.target, cv=10)

clf.fit(features_train, labels_train)

pred = clf.predict(features_test)

accuracy = clf.score(features_test, labels_test) # 0.7241379310344828
print("Accuracy after splitting with random: " + str(accuracy))
