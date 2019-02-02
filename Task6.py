#decoding labels from encoded values
import numpy as np 
from sklearn import preprocessing 
input_class=["Apple", "Mango", "Banana", "Litchi", "Guava"]
label_encoder=preprocessing.LabelEncoder()
label_encoder.fit(input_class)
encoded_labels=label_encoder.transform(input_class)
decoded_labels=label_encoder.inverse_transform(encoded_labels)
print("Encoded Labels = ",encoded_labels)
print("Decoded Labels =",list(decoded_labels))