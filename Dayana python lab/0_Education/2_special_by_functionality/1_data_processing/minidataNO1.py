
#-----------------------(start area) Generated in DPL play ground ----------------------#
import numpy as np

#--------------------------------------------- numpy, array and shape functions
one_d = np.array([1,25,35,66], float) # 1_D numpy array
print(one_d)
print("-----------------------------------")
print("one_d.shape")
print(one_d.shape) # 1x4 matris
print("-----------------------------------")
two_d = np.array([[15,25,12,5,0],[55,58,85,6,5]], float) # 2_D numpy array
print(two_d)
print("-----------------------------------")
print("two_d.shape")
print(two_d.shape) # 2x5 matris
print("-----------------------------------")

#-------------------------------------------------------numpy reshape function
# Use of 'reshape' : transforms elements from 1-D to 2-D here
one_d_before_reshape = np.array(range(12), float)
print("one_d_before_reshape")
print(one_d_before_reshape)
print("-----------------------------------")
one_d_after_reshape = one_d_before_reshape.reshape(2,6)
print("one_d_after_reshape")
print(one_d_after_reshape)
print("-----------------------------------")

#--------------------------------------------- numpy fill function
#Fills whole array with single value, done inplace
one_d_after_fill = one_d.fill(6)
print("one_d_after_fill")
print(one_d_after_fill)
print("-----------------------------------")

#--------------------------------------------- numpy transpose function
two_d_after_transpose = two_d.transpose()
print("two_d_after_transpose")
print(two_d_after_transpose)
print("-----------------------------------")

#--------------------------------------------- numpy flatten function
#flatten the whole array
two_d_after_transpose = two_d.transpose()
print("two_d_after_transpose")
print(two_d_after_transpose)
print("-----------------------------------")

#-----------------------(end of area) Generated in DPL play ground ----------------------#

# ------- some other functions of numpy library
sample = np.array([[0,2],[3,-1],[3,5]], float)
print(sample.mean(axis=0))# Mean of elements column-wise
print(sample.mean(axis=1))# Mean of elements row-wise
print(sample.mean())
print(sample.min())
print(sample.max())
print(sample.std())

# now let see ------------- pandas -----------------------------------------------------#


import pandas as pd

# lets play a little with pandas and see it's functions
series_sample1 = pd.Series([-2,3,9,6])
series_sample1.abs()
print(series_sample1.values.take(2))