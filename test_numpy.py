# import numpy as np

# print(np.__version__)
# arr=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
             
# print(arr.shape)
# print(arr.size)
# print(arr.ndim)
# print(arr.dtype)
# import numpy as np
# a=np.zeros((2,3))
# print(a)
# b=np.ones((2,2))
# print(b)

# c=np.arange(0,10,2)
# print(c)
# d=np.linspace(0,1,5)
# print(d)
# e=np.eye(3)
# print(e)
# f=np.random.random((2,3))
# g=np.random.randint(1,10,(2,3))
# print(f)
# print(g)
import numpy as np
# arr=np.array([10,20,30,40])
# print(arr[2])
# a=np.array([[1,2,3],[4,5,6]])
# print(a[1,2])
# a=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(a[0,:])
# print(a[:,1])
# print(a[:,2])

# arr=np.array([10,20,30,40,50])
# print(arr[arr>25])

# a=np.array([1,2])
# b=np.array([[1,2,3],[4,5,6]])
# print(a+b)
# print(a-b)
# print(a*b)i
# print(a/b)
# print(np.mean(a))
# print(np.median(a))
# print(np.sum(a))

# print(np.std(a))
# print(np.var(a))
# print(np.max(a))
# print(np.min(a))
# print(np.argmin(a))
# print(np.argmax(a))

# arr=np.arange(6)
# new_arr=arr.reshape(3,2)
# print(new_arr)

# rint(np.concatenate((a,b)))
# print(np.split(b[2]))print(a.flatten())
# print(a.ravel())
# print(a.transpose())

# b=np.array([3,4,5,6])
# p

# a=np.array([[1,2],[7,8]])
# b=np.array([[5,6],[7,8]])
# result=np.matmul(a,b)
# print(result)
# v1=np.array([1,2])
# v2=np.array([4,5])
# print(np.dot(v1,v2))
# print(np.linalg.inv(a))

# # print(np.linalg.det(v1,v2))
# np.random.rand(3)

# data=[10,20,30,40,50]
# np.random.choice(data,3)
# np.random.normal(loc=0,scale=1,size=5)
# print(np.random.default_rng(5))
# np.random.seed(10)
# print(np.random.rand(3))
# rng1=np.random.default_rng(seed=5)
# print(rng1.random())

import pandas as pd
# print(s)
# df=pd.DataFrame({'a':[10,20,30],'b':[5,6,7]})
# print(df)
# data={'name':['asha','ravi','john'],'age':[22,23,24]}
# df=pd.DataFrame(data)
# print(df)
# s=pd.Series([10,20,30])

# s=pd.Series([10,20,30],index=['a','b','c'])
# print(s)
df=pd.read_csv(r"C:\Users\THINKPAD P15s\Downloads\archive\players_17.csv")
print(df.head())

json_data=pd.read_json("colors.json")
print(json_data)
print(json_data.head(10))
print(json_data.tail(10))
print(json_data.info())
