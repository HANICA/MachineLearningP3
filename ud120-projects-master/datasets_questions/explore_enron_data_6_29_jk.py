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

    How many people in the E+F dataset (as it currently exists) have "NaN" for their total payments?
    What percentage of people in the dataset as a whole is this?

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
totalPersons = 0

for person in enron_data:
    totalPersons += 1
    for item in enron_data[person]:
        if (enron_data[person][item] == "NaN"):
            if item.find(lookingFor) >= 0:
                numberOfPersonsWithoutTotalPayments += 1


print("Total Payments NaN : " + str(numberOfPersonsWithoutTotalPayments))
print("Total amount of persons: " + str(totalPersons))
print("Percentage: " + str((100 / totalPersons) * numberOfPersonsWithoutTotalPayments))
