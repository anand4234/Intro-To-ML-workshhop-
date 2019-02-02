#label encodin (giving a label to each input data)
import numpy as np 
from sklearn import preprocessing 
input_class=["Apple", "Mango", "Banana", "Litchi", "Guava"]
label_encoder=preprocessing.LabelEncoder()
label_encoder.fit(input_class)
for i,item in enumerate (label_encoder.classes_):
    print (item,'-->',i)