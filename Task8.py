#SVM(SUPPORT VECTOR MACHINE) Algorithm intro using iris datasets
import numpy as np 
from sklearn import preprocessing 
from sklearn import datasets
import matplotlib.pyplot as plt

iris_flower=datasets.load_iris()
datasets=iris_flower.data
print(iris_flower["DESCR"])    #returns description 

X=iris_flower.data[:, :2]
y=iris_flower.target

plt.scatter(X[:,0],X[:,1],c=y,cmap=plt.cm.coolwarm) #SEPAL DESCRIPTION
plt.xlabel("SEPAL  Length")
plt.ylabel("SEPAL Width")
plt.title("SEPAL Width and Length")
plt.show()

X=iris_flower.data[:, 2:]
y=iris_flower.target
plt.scatter(X[:,0],X[:,1],c=y,cmap=plt.cm.coolwarm)     #PETAL DESCRIPTION
plt.xlabel("PETAL Length")
plt.ylabel("PETAL Width")
plt.title("PETAL Width and Length")
plt.show()