from sklearn import svm
class SVM:
    def __init__(self):
        self.SVM=svm.SVC(kernel='linear')
    
    def training(self,X,Y):
        self.SVM=svm.SVC(kernel='linear')
        self.SVM.fit(X,Y)

    def testing(self,vectors,labels):
        pre=self.SVM.predict(vectors)
        return [pre[i]==labels[i] for i in range(0,len(labels))]		
