from init import *

def final_test(testing_data,testing_label,training_data,training_label,feature,classifier):
    t_d=read_col(feature,testing_data)
    d=read_col(feature,training_data)
    classifier.training(d,training_label)
    r=classifier.testing(t_d,testing_label)
    corr=float(sum(r))/float(len(testing_label))
    s=''
    for i in feature:
        s=s+str(i)+','
    x=sorted(feature)
    ss=''
    for i in x:
        ss=ss+str(i)+','
    return s+"\t"+ss+'\t'+str(corr)
