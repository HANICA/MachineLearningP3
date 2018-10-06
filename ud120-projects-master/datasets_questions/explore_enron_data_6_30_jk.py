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

    How many POIs in the E+F dataset have "NaN" for their total payments?
    What percentage of POI’s as a whole is this?

"""

import pickle

# ../tools/feature_format.py

#fileLines = tuple(open('../final_project/poi_names.txt', 'r'))
personsOfInterest = 0
file = open('../final_project/final_project_dataset.pkl', 'rb')


enron_data = pickle.load(file)

#numItems = len(enron_data["SKILLING JEFFREY K"])

lookingFor = "total_payments"

numberOfPersonsOIWithoutTotalPayments = 0
totalPersonsOfInterest = 0

for person in enron_data:
    print(enron_data[person])
    
    if (enron_data[person]["poi"] == True):
        totalPersonsOfInterest += 1
        if (enron_data[person]["total_payments"] == "NaN"):
            numberOfPersonsOIWithoutTotalPayments += 1

print("POI's: " + str(totalPersonsOfInterest))
print("POI w/o Total Payments: " + str(numberOfPersonsOIWithoutTotalPayments))
print("Percentage: " + str((100 / totalPersonsOfInterest) * numberOfPersonsOIWithoutTotalPayments))
