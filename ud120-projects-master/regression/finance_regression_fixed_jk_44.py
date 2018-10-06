#!/usr/bin/python

"""
    Starter code for the regression mini-project.
    
    Loads up/formats a modified version of the dataset
    (why modified?  we've removed some trouble points
    that you'll find yourself in the outliers mini-project).
    Draws a little scatterplot of the training/testing data
    You fill in the regression code where indicated:
    
    Lessen 7.17 - further
    http://scikit-learn.org/stable/auto_examples/linear_model/plot_ols.html

    Some fixes for Python 3 were added...
    Challenge of item 7.44 is to:
    
    There are lots of finance features available, some of which might be more powerful than others in terms of predicting a person’s bonus. For example, suppose you thought about the data a bit and guess that the "long_term_incentive" feature, which is supposed to reward employees for contributing to the long-term health of the company, might be more closely related to a person’s bonus than their salary is.
    
    A way to confirm that you’re right in this hypothesis is to regress the bonus against the long term incentive, and see if the regression score is significantly higher than regressing the bonus against the salary. Perform the regression of bonus against long term incentive -
    
    what’s the score on the test data?
    
"""


import sys
import pickle
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
dictionary = pickle.load( open("../final_project/final_project_dataset_modified.pkl", "rb"), fix_imports=True )

### list the features you want to look at--first item in the
### list will be the "target" feature
features_list = ["bonus", "long_term_incentive"]

data = featureFormat( dictionary, features_list, remove_any_zeroes=True, sort_keys = '../tools/python2_lesson06_keys.pkl')
target, features = targetFeatureSplit( data )

### training-testing split needed in regression, just like classification
from sklearn import linear_model
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


feature_train, feature_test, target_train, target_test = train_test_split(features, target, test_size=0.5, random_state=42)

train_color = "b"
test_color = "r"

### Your regression goes here!
### Please name it reg, so that the plotting code below picks it up and
### plots it correctly. Don't forget to change the test_color above from "b" to
### "r" to differentiate training points from test points.


reg = linear_model.LinearRegression()
reg.fit(feature_train, target_train)

print ("Regression score of training data: " + str(reg.score(feature_train, target_train)))

coef = reg.coef_
feature_pred = reg.predict(feature_test)

# The coefficients
print('Coefficient (Slope): \n', reg.coef_)
print('Intercept (Independent factor): \n', reg.intercept_)
# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(feature_test, feature_pred))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(feature_test, feature_pred))
print ("Regression score of long_term_incentive: " + str(reg.score(feature_test, target_test)))


### draw the scatterplot, with color-coded training and testing points
import matplotlib.pyplot as plt
for feature, target in zip(feature_test, target_test):
    plt.scatter( feature, target, color=test_color )
for feature, target in zip(feature_train, target_train):
    plt.scatter( feature, target, color=train_color )

### labels for the legend
plt.scatter(feature_test[0], target_test[0], color=test_color, label="test")
plt.scatter(feature_test[0], target_test[0], color=train_color, label="train")




### draw the regression line, once it's coded
try:
    plt.plot( feature_test, reg.predict(feature_test) )
except NameError:
    pass
plt.xlabel(features_list[1])
plt.ylabel(features_list[0])
plt.legend()
plt.show()
