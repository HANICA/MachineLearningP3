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
print ("Number of POIs: " + str(int( sum(pred) )))
print ("Total people in Test Set: " + str(len(features_test)))

print("Labels Test: "+ str(labels_test))

# 15.30: If your identifier predicted 0. (not POI) for everyone in the test set, what would its accuracy be?
#labels_test = []
#for i in range(int(sum(pred))):
#    labels_test.append(0.0)
# Accuracy is now 0.862

#15.32:
# combines two lists pred,labels_test
of_true_positives = [(x,y) for x, y in zip(pred,labels_test) if x == y and x == 1.0]
print(of_true_positives)
print ("True positives on the Overfitted model: "+str(len(of_true_positives)))

from sklearn.metrics import recall_score
from sklearn.metrics import precision_score

precision = precision_score(labels_test, pred)
recall = recall_score(labels_test, pred)


accuracy = clf.score(features_test, labels_test) # 0.7241379310344828
print("Accuracy after splitting with random: " + str(accuracy))


#15.33
print ("Precision score: " + str(precision))
print ("Recall score: " + str(recall))

#15.34
predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

true_positives = [(x,y) for x, y in zip(predictions, true_labels) if x == y and x == 1.0]
print ("True positives (Q15.34): "+str(len(true_positives)))




predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

#15.35
true_negatives = [(x,y) for x, y in zip(predictions, true_labels) if x == y and x == 0.0]
print ("True negatives (Q15.35): "+str(len(true_negatives)))

#15.36
false_positives = [(x,y) for x, y in zip(predictions, true_labels) if x != y and y == 0.0]
print ("False positives (Q15.36): "+str(len(false_positives)))

#15.37
false_negatives = [(x,y) for x, y in zip(predictions, true_labels) if x != y and y == 1.0]
print ("False negatives (Q15.37): "+str(len(false_negatives)))

#15.38
precision_value = len(true_positives) / (len(true_positives) + len(false_positives))
print ("Precision (Q15.38): " + str(precision_value))

#15.39 Recall (True Positive / (True Positive + False Negative))
recall_value = len(true_positives) / (len(true_positives) + len(false_negatives))
print ("Recall (Q15.39): " + str(recall_value))
