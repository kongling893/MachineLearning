#!/usr/bin/env python
from feature_sel import *
from KNN import *
from err_est import *
from SVM import *
from dlda import *
F=SFS()
#F=exhaustive()
K=KNN(3)
L=LOO()
training_file='../Data/Training_Data.txt'
xx=F.search(K,L,training_file)

for i in xx:
    print i
