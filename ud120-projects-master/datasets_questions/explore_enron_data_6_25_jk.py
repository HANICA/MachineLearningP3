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

    Of these three individuals (Lay, Skilling and Fastow), who took home the most money (largest value of total_payments feature)?

"""

import pickle

#fileLines = tuple(open('../final_project/poi_names.txt', 'r'))
personsOfInterest = 0
file = open('../final_project/final_project_dataset.pkl', 'rb')


enron_data = pickle.load(file)

#numItems = len(enron_data["SKILLING JEFFREY K"])

poi_lastnames = ["Lay", "Skilling", "Fastow"]
lookingFor = "total_payments"


for person in enron_data:
    for poi in poi_lastnames:
        if person.find(poi.upper()) >= 0:
            print("Found: " + person)
            #print(enron_data[person])
            print("Query result: " + str(enron_data[person][lookingFor]))

#print(str(enron_data[person]["total_stock_value"]))

#print(fileLines)
#print("Number of features: " + str(personsOfInterest))
