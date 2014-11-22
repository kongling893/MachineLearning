#!/usr/bin/env python
from feature_sel import *
from KNN import *
from err_est import *
from SVM import *
from dlda import *
from testing import *
Sfs=SFS()
Ex=exhaustive()
Knn=KNN(3)
Svm=SVM()
Dlda=DLDA()
Loo=LOO()
resub=Resub()
training_file='../Data/Training_Data.txt'
testing_file='../Data/Testing_Data.txt'

testing=read_data(testing_file)
training=read_data(training_file)
testing_l=read_col_label(71,testing)
training_l=read_col_label(71,training)


SFS_LOO_SVM=Sfs.search(Svm,Loo,training_file)
#print SFS_LOO_SVM
for i in SFS_LOO_SVM:
    feature=i['f']
    est_err=i['o']
    for j in range(1,len(est_err)+1):
        f=feature[0:j]
        e=est_err[j-1]
        s=final_test(testing,testing_l,training,training_l,f,Svm)
        s='SFS\tLOO\tSVM\t'+s+'\t'+str(e)+'\t'+str(len(f))
        print s
SFS_RESUB_SVM=Sfs.search(Svm,resub,training_file)
#print SFS_RESUB_SVM
for i in SFS_RESUB_SVM:
    feature=i['f']
    est_err=i['o']
    for j in range(1,len(est_err)+1):
        f=feature[0:j]
        e=est_err[j-1]
        s=final_test(testing,testing_l,training,training_l,f,Svm)
        s='SFS\tRESUB\tSVM\t'+s+'\t'+str(e)+'\t'+str(len(f))
        print s
SFS_LOO_KNN=Sfs.search(Knn,Loo,training_file)
#print SFS_LOO_KNN
for i in SFS_LOO_KNN:
    feature=i['f']
    est_err=i['o']
    for j in range(1,len(est_err)+1):
        f=feature[0:j]
        e=est_err[j-1]
        s=final_test(testing,testing_l,training,training_l,f,Knn)
        s='SFS\tLOO\tKNN\t'+s+'\t'+str(e)+'\t'+str(len(f))
        print s
SFS_RESUB_KNN=Sfs.search(Knn,resub,training_file)
#print SFS_RESUB_KNN
for i in SFS_RESUB_KNN:
    feature=i['f']
    est_err=i['o']
    for j in range(1,len(est_err)+1):
        f=feature[0:j]
        e=est_err[j-1]
        s=final_test(testing,testing_l,training,training_l,f,Knn)
        s='SFS\tRESUB\tKNN\t'+s+'\t'+str(e)+'\t'+str(len(f))
        print s
SFS_LOO_DLDA=Sfs.search(Dlda,Loo,training_file)
#print SFS_LOO_DLDA
for i in SFS_LOO_DLDA:
    feature=i['f']
    est_err=i['o']
    for j in range(1,len(est_err)+1):
        f=feature[0:j]
        e=est_err[j-1]
        s=final_test(testing,testing_l,training,training_l,f,Dlda)
        s='SFS\tLOO\tDLDA\t'+s+'\t'+str(e)+'\t'+str(len(f))
        print s
SFS_RESUB_DLDA=Sfs.search(Dlda,resub,training_file)
#print SFS_RESUB_DLDA
for i in SFS_RESUB_DLDA:
    feature=i['f']
    est_err=i['o']
    for j in range(1,len(est_err)+1):
        f=feature[0:j]
        e=est_err[j-1]
        s=final_test(testing,testing_l,training,training_l,f,Dlda)
        s='SFS\tRESUB\tDLDA\t'+s+'\t'+str(e)+'\t'+str(len(f))
        print s
