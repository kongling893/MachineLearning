class DLDA:
        def __init__(self)
                self.mean0=0
                self.mean1=0
                self.cov0 =[]
                self.cov1 =[]
                self.N0 = 0
                self.N1 = 0
        def DLDA_training(slef,training_data,N):
                self.mean0= [0]*N#N is the number of features we use
                self.mean1 =[0]*N
                self.N1 = 0
                N_sample = 0 #the number of samples
                for data in training_data:
                        N_sample = N_sample+1
                        self.N1 = N1+data[0,-1]
                        if data[0,-1] == 0:
                                for i in range(0,N):
                                        self.mean0[i] = self.mean0[i]+data[0,i+1]
                        else: 
                                for i in range(0,N):
                                        self.mean1[i] = self.mean1[i]+data[0,i+1]
                for i in range(0,len(self.mean0)):
                        self.mean0[i] = self.mean0[i]/float(N_sample-self.N1)
                for i in range(0,len(self.mean1)):
                        self.mean1[i] = self.mean1[i]/float(self.N1)
                self.cov0 = [0]*N
                self.cov1 = [0]*N
                for i in range(N):
                        for data in training_data:
                                if data[0,-1] == 0:
                                        self.cov0[i] = (data[0,i+1]-self.mean0[i])*(data[0,i+1]-self.mean0[i])
                                else:
                                        
                                        self.cov1[i] = (data[0,i+1]-self.mean1[i])*(data[0,i+1]-self.mean1[i])
                for i in range(0,len(self.cov0)):
                        self.cov0[i] = self.cov0[i]/float(N_sample-self.N1)
                for i in range(0,len(self.cov1)):
                        self.cov1[i] = self.cov1[i]/float(self.N1)
                self.N0=N_sample-self.N1
                return 1   
        def DLDA_testing(self,testing_data):
                sigma= [0]*len(self.mean0)
                for i in range(0,len(self.mean0)):
                        sigma[i]=((self.N0-1)*self.cov0[i]+(self.N1-1)*self.cov1[i])/(self.N0+self.N1-2)
                a = [0]*len(self.mean0)
                for i in range(0,len(a)):
                        a[i] = 1/sigma[i]*(self.mean1[i]-self.mean0[i])
                b=0
                for i in range(0,len(a)):
                        b1 = 1/sigma[i]*(self.mean1[i]+self.mean0[i])
                        b2 = (self.mean1[i]-self.mean0[i])
                        b=b-b1*b2/2
                label = [0]*len(testing_data)
                mistakes = [0]*len(testing_data)
                for i in range(0,len(testing_data)):
                        p=0
                        for j in range(0,len(a)):
                                p=testing_data[i,j+1]*a[j]
                        p=p+b
                        if p>0:
                                label[i] = 1
                        else:
                                label[i] = 0
                        if label[i]==testing_data[i,-1]:
                                mistakes[i]=1
                return mistakes 
