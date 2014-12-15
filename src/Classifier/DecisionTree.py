'''
Data struct:
        datavec = {"val":val,"label":label} where datavec is just one data point with val means value and label.

        dataset is a set of data.
'''
from math import log


class DecisionTree():
        
        def __init__(self):
                pass

        def training(self,data,labels):
                #Create a decision tree
                pass
        def _entropy(self,dataset):
                #Calculates the entropy of the given dataset
                n = len(dataset)
                labelSet = {}    #Record all the labels and their corresponding counts
                for datavec in dataset:
                        label = datavec["label"]
                        if label is not in labelSet.keys():
                                labelSet[label] = 1
                        else:
                                labelSet[label] +=1
                Entropy = 0
                for key in labelSet:
                        prob = float(labelSet[key])/n
                        Entropy -= prob*log(prob,2)
                return Entropy

        def _splitDataset(set):
                
        def _gain(self):
                pass



 
