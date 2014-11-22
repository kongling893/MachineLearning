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


EX_LOO_KNN=Ex.search(Knn,Loo,training_file)
#print EX_LOO_KNN
for i in EX_LOO_KNN:
    f=i['feature']
    e=i['corr']
    s=final_test(testing,testing_l,training,training_l,f,Knn)
    s='EX\tLOO\tKNN\t'+s+'\t'+str(e)+'\t'+str(len(f))
    print s
EX_RESUB_KNN=Ex.search(Knn,resub,training_file)
#print EX_RESUB_KNN
for i in EX_RESUB_KNN:
    f=i['feature']
    e=i['corr']
    s=final_test(testing,testing_l,training,training_l,f,Knn)
    s='EX\tRESUB\tKNN\t'+s+'\t'+str(e)+'\t'+str(len(f))
    print s

EX_LOO_SVM=Ex.search(Svm,Loo,training_file)
#print EX_LOO_SVM
for i in EX_LOO_SVM:
    f=i['feature']
    e=i['corr']
    s=final_test(testing,testing_l,training,training_l,f,Svm)
    s='EX\tLOO\tSVM\t'+s+'\t'+str(e)+'\t'+str(len(f))
    print s

EX_RESUB_SVM=Ex.search(Svm,resub,training_file)
#print EX_RESUB_SVM
for i in EX_RESUB_SVM:
    f=i['feature']
    e=i['corr']
    s=final_test(testing,testing_l,training,training_l,f,Svm)
    s='EX\tRESUB\tSVM\t'+s+'\t'+str(e)+'\t'+str(len(f))
    print s

EX_LOO_DLDA=Ex.search(Dlda,Loo,training_file)
#print EX_LOO_DLDA
for i in EX_LOO_DLDA:
    f=i['feature']
    e=i['corr']
    s=final_test(testing,testing_l,training,training_l,f,Dlda)
    s='EX\tLOO\tDLDA\t'+s+'\t'+str(e)+'\t'+str(len(f))
    print s

EX_RESUB_DLDA=Ex.search(Dlda,resub,training_file)
#print EX_RESUB_DLDA
for i in EX_RESUB_DLDA:
    f=i['feature']
    e=i['corr']
    s=final_test(testing,testing_l,training,training_l,f,Dlda)
    s='EX\tRESUB\tDLDA\t'+s+'\t'+str(e)+'\t'+str(len(f))
    print s
