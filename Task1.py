import numpy as np 
from sklearn import preprocessing 
input_data=np.array([[2,-1.5,3,6],[2,-1.3,4,-5],[2.3,-2.9,-4.3,3]])
print(input_data)
print("mean",input_data.mean(axis=0))
print("sd=",input_data.std(axis=0))
data_scaler=preprocessing.MinMaxScaler(feature_range=(0,1))
data_scaled=data_scaler.fit_transform(input_data) 
print("data scaled \n",data_scaled) 
print("standardized mean",data_standardized.mean(axis=0))  #standard mean
print("standardized stdev",data_standardized.std(axis=0))  #standard deviation 

