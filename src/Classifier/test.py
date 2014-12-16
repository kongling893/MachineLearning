 
x1={"val":[1,1,1],"label":"00"}
x2={"val":[1,1,0],"label":"11"}
x3={"val":[1,0,1],"label":"11"}
x4={"val":[0,1,1],"label":"00"}
x5={"val":[1,0,0],"label":"00"}
x6={"val":[0,0,1],"label":"00"}
x7={"val":[0,1,0],"label":"00"}
x8={"val":[0,0,0],"label":"00"}


import DecisionTree

x=[]
x.append(x1)
x.append(x2)
x.append(x3)
x.append(x4)
x.append(x5)
x.append(x6)
x.append(x7)
x.append(x8)


DTree = DecisionTree.DecisionTree().createTree(x)
print DTree
x9 = x1["val"]
label = DecisionTree.DecisionTree().classify(DTree,x)
print label
