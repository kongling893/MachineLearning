from itertools import combinations
from init import *
from operator import itemgetter
class exhaustive:
        def search(self,classifier,estimator,training_file):
                d=read_data(training_file)
                selected_features=[]
                for i in range(1,3):
                        comb=self.exhaustive_search(70,i)
                        optimal=0
                        tmp=[]
                        for j in comb:
                                data=read_col(j,d)
                                label=read_col_label(71,d)
                                tmp_corr=estimator.estimate(classifier,data,label)
                                tmp.append({'feature':j,'corr':tmp_corr})
                                if tmp_corr > optimal:
                                        optimal=tmp_corr
                        for k in tmp:
                                if k['corr']==optimal:
                                        selected_features.append(k)
                return selected_features
        def exhaustive_search(self,total,num):
                ind=range(1,total+1)
                comb=[]
                tmp=combinations(ind,num)
                for j in tmp:
                        comb.append(list(j))
                return comb
class SFS:
        def search(self,classifier,estimator,training_file):
                d=read_data(training_file)
                ind=range(1,71)
                feature=[]
                tmp=self.ADD_one_feature({},70,d,classifier,estimator)
                feature+=tmp
                for i in range(2,6):
                    tmp=[]
                    for j in range(len(feature)):
                        tmp+=self.ADD_one_feature(feature[j],70,d,classifier,estimator)
                    tt=[]
                    optimal=0
                    for j in tmp:
                        if len(j['o'])==i:
                            tt.append(j)
                            if j['o'][i-1]>optimal:
                                optimal=j['o'][i-1]
                    ttt=[]
                    for j in tt:
                        if j['o'][i-1]==optimal:
                            ttt.append(j)
                    feature=ttt
                return feature



        def ADD_one_feature(self,pre_feature,N,d,classifier,estimator):
                ind=range(1,N+1)
                pf=[]
                po=[]
                if len(pre_feature)!=0:
                    pf=pre_feature['f']
                    po=pre_feature['o']
                    for i in pf:
                        ind.remove(i)
                C=[]
                for i in ind:
                        f=pf+[i]
                        data=read_col(f,d)
                        label=read_col_label(71,d)
                        corr=estimator.estimate(classifier,data,label)
                        C.append({'feature':i,'corr':corr})
                s_C=sorted(C,key=itemgetter('corr'))
                optimal=s_C[len(s_C)-1]['corr']
                feature=[]
                for i in s_C:
                        if i['corr']==optimal:
                            feature.append({'f':pf+[i['feature']],'o':po+[optimal]})
                return feature
