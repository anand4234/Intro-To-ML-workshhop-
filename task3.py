##data binarization (greater than threshold would binarize to 1 and less would go to 0 )
import numpy as np 
from sklearn import preprocessing 
input_data=np.array([[2,-1.5,3,6],[2,-1.3,4,-5],[2.3,-2.9,-4.3,3]])
data_binarized=preprocessing.Binarizer(threshold=1.7)
tms_binarized=data_binarized.transform(input_data)
print("Binarized data = ",tms_binarized)