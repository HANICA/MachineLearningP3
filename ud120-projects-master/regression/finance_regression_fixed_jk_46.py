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
   
    Quiz 7.46 asks us to:
    
    This is a sneak peek of the next lesson, on outlier identification and removal. Go back to a setup where you are using the salary to predict the bonus, and rerun the code to remind yourself of what the data look like. You might notice a few data points that fall outside the main trend, someone who gets a high salary (over a million dollars!) but a relatively small bonus. This is an example of an outlier, and we’ll spend lots of time on them in the next lesson.
    
    A point like this can have a big effect on a regression: if it falls in the training set, it can have a significant effect on the slope/intercept if it falls in the test set, it can make the score much lower than it would otherwise be As things stand right now, this point falls into the test set (and probably hurting the score on our test data as a result). Let’s add a little hack to see what happens if it falls in the training set instead. Add these two lines near the bottom of finance_regression.py, right before plt.xlabel(features_list[1]):
    
    reg.fit(feature_test, target_test)
    plt.plot(feature_train, reg.predict(feature_train), color="b")
    
    Now we’ll be drawing two regression lines, one fit on the test data (with outlier) and one fit on the training data (no outlier). Look at the plot now--big difference, huh? That single outlier is driving most of the difference. What’s the slope of the new regression line?
    
    (That’s a big difference, and it’s mostly driven by the outliers. The next lesson will dig into outliers in more detail so you have tools to detect and deal with them.)
    
"""


import sys
import pickle
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
dictionary = pickle.load( open("../final_project/final_project_dataset_modified.pkl", "rb"), fix_imports=True )

### list the features you want to look at--first item in the
### list will be the "target" feature
features_list = ["bonus", "salary"]

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
print ("Regression score of salary: " + str(reg.score(feature_test, target_test)))


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

reg.fit(feature_test, target_test)
print('Coefficient (Slope) of green line: \n', reg.coef_)

plt.plot(feature_train, reg.predict(feature_train), color="g")
plt.xlabel(features_list[1])
plt.ylabel(features_list[0])
plt.legend()
plt.show()
