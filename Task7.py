#iris contains data set of an iris flower
import numpy as np 
from sklearn import preprocessing 
from sklearn import datasets
iris_flower=datasets.load_iris()
print(iris_flower.data.shape)#returns rows and column

dim_shape=iris_flower.data.shape #returns dimension of petals
print(dim_shape)

name=iris_flower.feature_names #returns feature name
print(name)

dataset=iris_flower.data # returns only data info('sepal length (cm)','sepal width (cm)', 'petal length (cm)', 'petal width (cm)') 
print (dataset)

print(iris_flower.target_names)#returns target names

print(iris_flower.target) #target count nos

print(iris_flower.target.shape) #returns target count