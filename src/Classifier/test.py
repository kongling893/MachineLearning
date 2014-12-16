 
x1={"val":[1,1,1],"label":"0"}
x2={"val":[1,1,0],"label":"0"}
x3={"val":[1,0,1],"label":"1"}
x4={"val":[0,1,1],"label":"0"}
x5={"val":[1,0,0],"label":"1"}
x6={"val":[0,0,1],"label":"1"}
x7={"val":[0,1,0],"label":"1"}
x8={"val":[0,0,0],"label":"1"}


import DecisionTree

x=[]
x.append(x1)
x.append(x2)
x.append(x3)
x.append(x4)
x.append(x5)
x.append(x6)
x.append(x7)
#x.append(x8)


DTree = DecisionTree.DecisionTree().createTree(x)
print DTree

x9 = x8["val"]
label = DecisionTree.DecisionTree().classify(DTree,x9)
print label
'''
E = DecisionTree.DecisionTree().entropy(x)
print E


sub = DecisionTree.DecisionTree().optimalSplitingFeature(x)
print sub

sub = DecisionTree.DecisionTree().majority([1,1,1,1,0,0,0,0,3])
print sub
'''

