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

    If you added in, say, 10 more data points which were all POI’s, and put "NaN"
    for the total payments for those folks, the numbers you just calculated would change.
    
    What is the new number of people of the dataset?
    What is the new number of folks with "NaN" for total payments?

"""

import pickle

# ../tools/feature_format.py

#fileLines = tuple(open('../final_project/poi_names.txt', 'r'))
personsOfInterest = 0
file = open('../final_project/final_project_dataset.pkl', 'rb')


enron_data = pickle.load(file)

#numItems = len(enron_data["SKILLING JEFFREY K"])

lookingFor = "total_payments"

numberOfPersonsWithoutTotalPayments = 0
numberOfPersonsOIWithoutTotalPayments = 0
totalPersonsOfInterest = 0
totalPersons = 0


for person in enron_data:
    print(enron_data[person])
    totalPersons += 1
    if (enron_data[person]["poi"] == True):
        totalPersonsOfInterest += 1
        if (enron_data[person]["total_payments"] == "NaN"):
            numberOfPersonsOIWithoutTotalPayments += 1

    if (enron_data[person]["total_payments"] == "NaN"):
        numberOfPersonsWithoutTotalPayments += 1

print("Before adding...")

print("POI's: " + str(totalPersonsOfInterest))
print("POI w/o Total Payments: " + str(numberOfPersonsOIWithoutTotalPayments))
print("Persons w/o Total Payments: " + str(numberOfPersonsWithoutTotalPayments))
print("Percentage: " + str((100 / totalPersonsOfInterest) * numberOfPersonsOIWithoutTotalPayments))
print()

numberOfPersonsOIWithoutTotalPayments += 10
totalPersonsOfInterest += 10
numberOfPersonsWithoutTotalPayments += 10
totalPersons += 10

print("After adding...")
print("Total persons: " + str(totalPersons))
print("POI's: " + str(totalPersonsOfInterest))
print("POI w/o Total Payments: " + str(numberOfPersonsOIWithoutTotalPayments))
print("Persons w/o Total Payments: " + str(numberOfPersonsWithoutTotalPayments))
print("Percentage: " + str((100 / totalPersonsOfInterest) * numberOfPersonsOIWithoutTotalPayments))
