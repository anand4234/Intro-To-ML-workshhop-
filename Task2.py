#data normalization of an array
import numpy as np 
from sklearn import preprocessing 
input_data=np.array([[2,-1.5,3,6],[2,-1.3,4,-5],[2.3,-2.9,-4.3,3]])
data_normalized_1=preprocessing.normalize(input_data,norm='l1')
print("L1 normalized=",data_normalized_1)

data_normalized_2=preprocessing.normalize(input_data,norm="l2")
print("L2 normalized data ",data_normalized_2)

