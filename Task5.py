#label encodin (giving a label to each input data)
import numpy as np 
from sklearn import preprocessing 
input_class=["Apple", "Mango", "Banana", "Litchi", "Guava"]
label_encoder=preprocessing.LabelEncoder()
label_encoder.fit(input_class)
encoded_labels=label_encoder.transform(input_class)
print("Labels= ",input_class)
print("Encoded labels= ", list(encoded_labels))