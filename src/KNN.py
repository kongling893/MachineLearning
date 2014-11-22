from operator import itemgetter
class KNN:
        def __init__(self,K):
                self.K=K
                self.data=[]
		self.label=[]

        def training(self,t_data,t_label):
                self.data=t_data
		self.label=t_label

	def testing(self,vectors,labels):
		ret=[-1]*len(labels)
		for i in range(0,len(vectors)):
			pre=self.testing_one(vectors[i])
			if(pre==labels[i]):
				ret[i]=1
			else:
				ret[i]=0
		return ret	
        def testing_one(self,test_v):
                distance=[]
                for i in range(0,len(self.data)):
                        vector=self.data[i]
			label=self.label[i]
                        distance.append({'dist':L2_norm(vector,test_v),'label':label})
		sort=sorted(distance,key=itemgetter('dist'))
                tmp=0.0
                for i in range(0,self.K):
                        tmp=tmp+sort[i]['label']
                tmp=tmp/self.K
                if(tmp>=0.5):
                        return 1
                else:
                        return 0

def L2_norm(X,Y):
        return sum((i-j)**2 for (i,j) in zip(X,Y))
                
