#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

from sklearn.metrics import accuracy_score

#JK: import specific libraries for particular algorithm
from sklearn import tree

features_train, labels_train, features_test, labels_test = makeTerrainData()

#JK: import helper methods for particular algorithm
from decisionTreesHelper import classify
from decisionTreesHelper import predict
algorithmName = "Decision Tree"

print("Simulation for [" + algorithmName + "] started...")
print("Note: Close initial data screen to allow further processing...")

### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary


clf = classify(features_train, labels_train, 2)
predict = predict(clf, features_test)
acc_score = accuracy_score(predict, labels_test)

print("Number of features: " + str(len(features_train)))
print("Number of labels: " + str(len(labels_train)))
print("Accuracy prediction: " + str(acc_score))


try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
