#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
import numpy

sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### Updated for Python 3


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "rb"), fix_imports = True )

features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below
### scatterplot:


for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
"""
# ToDo: detect outlier:
# from eye-balling we can see that the salary is the problem...

# Let's sort first...
#data.sort(key=lambda i:i[0])
sorted_data = numpy.lexsort((data[:,0],data[:,1]))

filtered_data = data[sorted_data]
filtered_data = filtered_data[:-1]

#print(str(filtered_data))

# Then see the data:
for datapoint in data[sorted_data]:
    #print("salary: " + str(datapoint[0]) + ", bonus: " + str(datapoint[1]))
    print(datapoint)

"""

max_salary_1 = 0
max_salary_1_key = ''
for data_element in data_dict:
    # print data_element[0]['salary']
    if data_dict[data_element]['salary'] != 'NaN' and data_dict[data_element]['salary'] > max_salary_1:
        max_salary_1 = data_dict[data_element]['salary']
        max_salary_1_key = data_element

print(max_salary_1_key)
print(max_salary_1)
print(data_dict[max_salary_1_key])

data_dict.pop( max_salary_1_key, 0 )
data = featureFormat(data_dict, features)

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()


# Quiz 8.18 - Identifying Two More Outliers

for name in data_dict:
    # float() does not include NaN values
    bonus = float(data_dict[name]["bonus"])
    salary = float(data_dict[name]["salary"])
    if bonus >= 5000000 and salary >= 1000000:
        print (name, "bonus: ", data_dict[name]["bonus"], "salary: ", data_dict[name]["salary"])
