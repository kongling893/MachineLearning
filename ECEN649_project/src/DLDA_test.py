from DLDA import *
from init import *
from numpy import matrix
training_file="../Data/Training_Data.txt"
training=matrix(init(training_file))
testing_file="../Data/Testing_Data.txt"
testing=matrix(init(testing_file))
total_gene=70
ex_range=3
ex_search=exhaustive_search(total_gene,ex_range)
minerror=1.0
for i in ex_search:
        parameters = DLDA_training(training[:,i],len(i)-2)
	mean0=parameters[0]
	mean1=parameters[1]
	cov0 = parameters[2]
	cov1=parameters[3]
	N0=parameters[4]
	N1=parameters[5]
	label = DLDA_testing(testing[:,i], mean0,mean1,cov0,cov1,N0,N1)
        error =0.0
        for j in range(0,len(testing)):
                if testing[j,-1]!=label[j]:
                        error =error+1
        error=float(error/len(testing))
        if error<minerror:
                minerror = error
                feture_selected = i 
print error
print feture_selected    
