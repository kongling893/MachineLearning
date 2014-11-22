from KNN import *
class LOO:
        def estimate(self,classifier,data_set,label):
                assert(len(data_set))
		assert(len(data_set)==len(label))
                N=len(data_set)
                testing=[data_set.pop(0)]
		t_label=[label.pop(0)]
                num=0
                for i in range(0,N):
                        classifier.training(data_set,label)
                        num+=sum(classifier.testing(testing,t_label))
                        data_set.append(testing[0])
			label.append(t_label[0])
                        testing=[data_set.pop(0)]
			t_label=[label.pop(0)]
                corr=float(num)/float(N)
                return corr
class Resub:
        def estimate(self,classifier,data_set,label):
                assert(len(data_set))
                classifier.training(data_set,label)
                N=len(data_set)
                num=sum(classifier.testing(data_set,label))
#                print  float(num)/float(N)
                return float(num)/float(N)

                        
                                
