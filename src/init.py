from itertools import combinations
from numpy import matrix
def read_data(file_name):
        f=open(file_name)
        data=[]
        h=f.readline()
        for line in f:
                tmp=line[0:len(line)-1].split("\t")
                floats=[float(x) for x in tmp]
                data.append(floats)
        return matrix(data)
def read_col(col_list,matrix):
        return matrix[:,col_list].tolist()
 
def read_col_label(col,matrix):
        return matrix[:,col].transpose().tolist()[0]
