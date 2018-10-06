#!/usr/bin/python

import random
import numpy
import matplotlib.pyplot as plt
import pickle

from outlier_cleaner import outlierCleaner

### 
### Updated for Python 3
###
"""
   Generates answers till 8.12
    
"""

### load up some practice data with outliers in it
ages = pickle.load(open("practice_outliers_ages.pkl", "rb"), fix_imports=True)
net_worths = pickle.load(open("practice_outliers_net_worths.pkl", "rb"), fix_imports=True)

### Import basic libraries / modules for regression etc...
from sklearn import linear_model
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score



### ages and net_worths need to be reshaped into 2D numpy arrays
### second argument of reshape command is a tuple of integers: (n_rows, n_columns)
### by convention, n_rows is the number of data points
### and n_columns is the number of features
ages       = numpy.reshape( numpy.array(ages), (len(ages), 1))
net_worths = numpy.reshape( numpy.array(net_worths), (len(net_worths), 1))
from sklearn.model_selection import train_test_split
ages_train, ages_test, net_worths_train, net_worths_test = train_test_split(ages, net_worths, test_size=0.1, random_state=42)

### fill in a regression here!  Name the regression object reg so that
### the plotting code below works, and you can see what your regression looks like


reg = linear_model.LinearRegression()
reg.fit(ages_train, net_worths_train)


coef = reg.coef_
networth_pred = reg.predict(ages_test)

# The coefficients
print('Coefficient (Slope): \n', reg.coef_)
print('Intercept (Independent factor): \n', reg.intercept_)
# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(net_worths_test, networth_pred))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(net_worths_test, networth_pred))
print ("Regression score: " + str(reg.score(ages_test, net_worths_test)))


try:
    plt.plot(ages, reg.predict(ages), color="blue")
except NameError:
    pass
plt.scatter(ages, net_worths)
plt.show()


### identify and remove the most outlier-y points
""" NOTE: In outliers/outlier_removal_regression.py, in the section where outlier cleaning is performed (starts with the comment ### identify and remove the most outlier-y points), make sure that the input argument to reg.predict is ages_train and not ages so that you are cleaning based on just the training data. The arguments to the cleaner should also be based off of the *_train variables.
"""

cleaned_data = []
try:
    predictions = reg.predict(ages_train)
    cleaned_data = outlierCleaner( predictions, ages_train, net_worths_train )
except NameError:
    print ("your regression object doesn't exist, or isn't name reg")
    print ("can't make predictions to use in identifying outliers")



### only run this code if cleaned_data is returning data
if len(cleaned_data) > 0:
    ages, net_worths, errors = zip(*cleaned_data)
    ages       = numpy.reshape( numpy.array(ages), (len(ages), 1))
    net_worths = numpy.reshape( numpy.array(net_worths), (len(net_worths), 1))
    
    ### refit your cleaned data!
    try:
        reg.fit(ages, net_worths)
    
        print("\n After cleaning 10% of outliers: ")
        # The coefficients
        print('Coefficient (Slope): \n', reg.coef_)
        print('Intercept (Independent factor): \n', reg.intercept_)
        # The mean squared error
        print("Mean squared error: %.2f" % mean_squared_error(ages, reg.predict(ages)))
        # Explained variance score: 1 is perfect prediction
        print('Variance score: %.2f' % r2_score(ages, net_worths))
        print ("Regression score: " + str(reg.score(ages, net_worths)))
        plt.plot(ages, reg.predict(ages), color="blue")

    except NameError:
        print ("you don't seem to have regression imported/created,")
        print ("   or else your regression object isn't named reg")
        print ("   either way, only draw the scatter plot of the cleaned data")
    plt.scatter(ages, net_worths)
    plt.xlabel("ages")
    plt.ylabel("net worths")
    plt.show()





else:
    print ("outlierCleaner() is returning an empty list, no refitting to be done")
