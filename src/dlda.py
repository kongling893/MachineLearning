from math import log
class DLDA:
        def __init__(self):
                self.a=[]
                self.b=0
        def training(self,data,label):
                sep=self.sep_data(data,label)
                u0=self.mean(sep[0])
                u1=self.mean(sep[1])
                N0=len(sep[0])
                N1=len(sep[1])
                cov0=self.var(sep[0],u0,N0)
                cov1=self.var(sep[1],u1,N1)
                sigma_inv=self.pooled_sigma_inv(cov0,cov1,N0,N1)
                self.set_a_b(u0,u1,sigma_inv,N0,N1)

        def testing(self,data,label):
                ret=[-1]*len(label)
                for i in range(len(data)):
                        ax=0
                        for j in range(len(data[i])):
                                ax+=self.a[j]*data[i][j]
                        gn=ax+self.b
                        pre=(gn>=0)
                        if pre==label[i]:
                                ret[i]=1
                        else:
                                ret[i]=0
                return ret        

        def mean(self,data):
                N=len(data[0])
                m=[0]*N
                for i in data:
                        for j in range(N):
                                m[j]+=i[j]
                return [float(i)/float(N) for i in m]

        def sep_data(self,data,label):
                c0=[]
                c1=[]
                for (i,j) in zip(data,label):
                        if j==0:
                                c0.append(i);
                        elif j==1:
                                c1.append(i);
                return [c0,c1]                
        def var(self,data,mean,N):
                V=[0]*len(mean)
                for i in data:
                        for j in range(len(mean)):
                                V[j]+=(i[j]-mean[j])**2
                return [float(i)/float(N-1) for i in V]
        def pooled_sigma_inv(self,V0,V1,N0,N1):
                N=len(V0)
                return [float(N0+N1-2)/((N0-1)*V0[i]+(N1-1)*V1[i]) for i in range(N)]

        def set_a_b(self,u0,u1,sigma_inv,N0,N1):        
                self.a=[sigma_inv[i]*(u1[i]-u0[i]) for i in range(len(u0))]
                bb=[sigma_inv[i]*(u1[i]+u0[i]) for i in range(len(u0))]
                b=0
                for i in range(len(u0)):
                        b+=-1.0/2.0*(u1[i]-u0[i])*bb[i]        
                self.b=b+log(float(N1)/N0)
                
