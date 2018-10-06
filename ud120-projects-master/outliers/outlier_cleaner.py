#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        
        In outliers/outlier_cleaner.py, you will find the skeleton for a function called outlierCleaner()
        that you will fill in with a cleaning algorithm.
        
        It takes three arguments: predictions is a list of predicted targets that come from your regression,
        ages is the list of ages in the training set,
        and net_worths is the actual value of the net worths in the training set.
        
        There should be 90 elements in each of these lists (because the training set has 90 points in it).
        Your job is to return a list called cleaned_data that has only 81 elements in it,
        which are the 81 training points where the predictions and the actual values (net_worths)
        have the smallest errors (90 * 0.9 = 81).
        
        The format of cleaned_data should be a list of tuples, where each tuple has the form (age, net_worth, error).
        
        In short:
        
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
        
        
    """
    
    percentageToReturn = 90 # 90 procent
    cutOffPoint = round(len(predictions) * (percentageToReturn / 100))
    showDebugData = False

    data_to_clean = []
    
    # just to be sure:
    lengthesMatch = (len(predictions) == len(ages) == len(net_worths))
    if (lengthesMatch == False):
        return []
    
    index = 0
    for item in predictions:
        error = predictions[index] - net_worths[index] # do not forget this!!!
        data_to_clean.append([ages[index], net_worths[index], error])
        index += 1
    
    data_to_clean.sort(key=lambda i: i[2])

    # To see what is going on:
    if showDebugData:
        for item in cleaned_data:
            print("age: " + str(item[0]) + ", net_worths: " + str(item[1]) + ", error: " + str(item[2]))


    # the smaller the error the better so we need the first 90% of the list only...
    # return till cutOffPoint (list needs to be sorted of course...
    
    cleaned_data = data_to_clean[:cutOffPoint]
    
    return cleaned_data

