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

    How many folks in this dataset have a quantified salary? What about a known email address?

"""

import pickle

#fileLines = tuple(open('../final_project/poi_names.txt', 'r'))
personsOfInterest = 0
file = open('../final_project/final_project_dataset.pkl', 'rb')


enron_data = pickle.load(file)

#numItems = len(enron_data["SKILLING JEFFREY K"])

poi_lastnames = ["Lay", "Skilling", "Fastow"]
lookingFor = ["salary", "email_address"]

numberOfPersonsWithSalaryInfo = 0
numberOfPersonsWithEmailInfo = 0


for person in enron_data:
    for item in enron_data[person]:
        if (enron_data[person][item] != "NaN"):
            if item.find(lookingFor[0]) >= 0:
                numberOfPersonsWithSalaryInfo += 1
            if item.find(lookingFor[1]) >= 0:
                print("Found: " + item)
                numberOfPersonsWithEmailInfo += 1


print("Emails: " + str(numberOfPersonsWithEmailInfo))
print("Salary: " + str(numberOfPersonsWithSalaryInfo))
