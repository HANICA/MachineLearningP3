#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
    ../final_project/poi_names.txt
    
"""

import pickle

fileLines = tuple(open('../final_project/poi_names.txt', 'r'))
personsOfInterest = 0

for line in fileLines:
    if line.find("(y)") == 0 or line.find("(n)") == 0:
        personsOfInterest += 1

#print(fileLines)
print("Number of features: " + str(personsOfInterest))
