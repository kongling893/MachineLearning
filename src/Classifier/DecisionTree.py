'''
Data struct:
        datavec = {"val":val,"label":label} where datavec is just one data point with val means value and label.
        
        dataset is a set of data.
        
        For example: 
                datavec1 = {"val":[1,1,1,1],"label":1}
                datavec2 = {"val":[0,0,0,1],"label":0}
                
                dataset = [datavec1,datavec2]


How to use:
        >import DecisionTree
        >DTree = DecisionTree.createTree(dataset)
        >label = DecisionTree.classify(DTree,testDataVec)
        >

author: Wei Qiao
Email: qiaowei@tamu.edu
'''
from math import log
from copy import deepcopy
import operator


class DecisionTree:
        
        def __init__(self):
                pass

        def createTree(self,dataset):
                labelsList = [datavec["label"] for datavec in dataset]
                majority = self._majority(labelsList)
                if labelsList.count([labelsList[0]]) == len(labelsList):
                        return labelsList[0]
                if len(dataset[0]["val"]) == 1:
                        return majority
                bestFeature = self._optimalSplitingFeature(dataset)
                if bestFeature ==-1: return majority
                DTree = {bestFeature:{}}
                featureValues = [datavec["val"][bestFeature] for datavec in dataset] 
                uniqueValues = set(featureValues)
                for value in uniqueValues:
                        subdataset = self._splitDataset(dataset,bestFeature,value)
                        DTree[bestFeature][value] = self.createTree(subdataset)
                return DTree

        def classify(self,DTree,data):
                if type(DTree).__name__!="dict": return DTree
                firstLevel = DTree.keys()[0]
                secondLevel = DTree[firstLevel]
                for key in secondLevel.keys():
                        if type(secondLevel[key]).__name__ !='dict':
                                classifiedLabel = secondLevel[key]
                        else: classifiedLabel = self.classify(secondLevel[key],data) 
                return classifiedLabel

        def _entropy(self,dataset):
                #Calculates the entropy of the given dataset
                n = len(dataset)
                labelSet = {}    #Record all the labels and their corresponding counts
                for datavec in dataset:
                        label = datavec["label"]
                        if label not in labelSet.keys():
                                labelSet[label] = 1
                        else:
                                labelSet[label] +=1
                Entropy = 0
                for key in labelSet:
                        prob = float(labelSet[key])/n
                        Entropy -= prob*log(prob,2)
                return Entropy

        def _splitDataset(self,dataset,index,value):
                #Splits the dataset based on given Feature index and Value
                remainedData = []
                for datavec in dataset:
                        if datavec["val"][index] == value:
                                reducedFeatvec = deepcopy(datavec["val"][:index])
                                reducedFeatvec.extend(datavec["val"][index+1:])
                                newdatavec = {"val":reducedFeatvec,"label":datavec["label"]}
                                remainedData.append(newdatavec)
                return remainedData

        def _optimalSplitingFeature(self,dataset):
                #Finds the optimal feature index to split the dataset
                N = len(dataset[0]["val"]) - 1
                oldEntropy = self._entropy(dataset)
                bestFeature = -1
                bestInforGain = 0.0
                for i in range(N):
                        featlists = [datavec["val"][i] for datavec in dataset]
                        uniquevalues = set(featlists)
                        newEntropy = 0.0
                        for value in uniquevalues:
                                splittedDataset = self._splitDataset(dataset,i,value)
                                prob = len(splittedDataset)/float(len(dataset))
                                newEntropy += prob*self._entropy(splittedDataset)
                        inforGain = oldEntropy - newEntropy
                        if inforGain > bestInforGain:
                                bestInforGain = inforGain
                                bestFeature = i
                return bestFeature

        def _majority(self,labels):
                labelCount = {}
                for label in labels:
                        if label not in labelCount.keys():
                                labelCount[label] = 0
                        labelCount[label] += 1
                sortedLabels = sorted(labelCount.iteritems(),key = operator.itemgetter(1), reverse = True)
                return sortedLabels[0][0]
                                                                
                
        


 
