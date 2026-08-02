#Write code that:

#1. Creates two large NumPy arrays (say, 1 million elements each) of random numbers
#2. Computes their element-wise product two ways: once with a plain Python for loop, once with vectorized NumPy (*)
#3. Times both using time.time() or timeit
#4. Prints the time taken for each and the speedup factor

import numpy as np
import time
import random

#1. creating 2 numpy arrays of 1 million random numbers
arr1=np.random.rand(1000000)
arr2=np.random.rand(1000000)

#2. computing element-wise product using a plain python for loop, once with vectorized numpy (*)
#using the plain loop for python
start_time=time.time()
result_loop=[]
for i in range(len(arr1)):
    result_loop.append(arr1[i]*arr2[i])
end_time=time.time()
time_loop=end_time-start_time
print("time taken for the plain python for loop is:", time_loop)

#using vectorized numpy
start_time=time.time()
result_numpy=arr1*arr2
end_time=time.time()
time_numpy=end_time-start_time
print("time taken for the vectorized numpy is:", time_numpy)
#speedup factor
speedup_factor=time_loop/time_numpy
print("speedup factor is:", speedup_factor)
