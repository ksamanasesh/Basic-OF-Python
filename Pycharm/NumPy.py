import numpy as np
import random

# name = np.array(["James","Gunn","Avengers"])
# print("String Array",name)
# print("String datatype",name.dtype)                                    # Getting data type
#
# array = np.array([1,2,3,4,5],ndmin=2)
# print(array)
#
# d2 = np.array([[1,2,3,4],[5,6,7,8]])                                   # 2D Array
# print("2D array",d2)
#
# dtyp = np.array(([25,152,4541,74]),dtype=float)                        # Changing Data Type
# print ("Changing data type",dtyp.dtype)
#
# person = np.dtype([("Height","i4"),("Weight","i1")])                   # Giving data limit
# p1 = np.array([(180,60)],dtype=person)
# print(p1)
#
# a1 = np.array([10,20,30])
# a2 = np.array([40,50,60])
# print("Addition of 2 array",a1+a2)                                     # Adding a 2 array
# print("Adding a number :",a1+20)                                       # Adding a numeber
# print("Subtraction :",np.subtract(a1,a2))
# print("Sum of array :",np.sum(d2))
#
# d3one = np.array([[30,50,10],[5,25,125],[6,3,2]])
# d3two = np.array([[40,20,60],[125,105,5],[2,5,6]])
# print("Adding 3D Array :",d3one+d3two)
#
#
# matrix = np.array(([10,20,30,40],[50,60,70,80])).reshape(4,2)          # Reshaping Array
# print("Reshape :",matrix)
#
# tuple = (1,2,3,4,5)
# print("Tuple :",tuple)
# tu = np.array(tuple)
# print("Tuple to array :",tu)                                           # conerting to tuple
#
# arrange = np.arange(1,11)
# print("Arrange array",arrange)                                         # arange
#
# arr = np.arange(2,62,2).reshape(10,3)
# print("Reshaping Arange :",arr)
#
# Root = 25
# print("Square Root :",np.sqrt(Root))                                   # Square Root
#
# sqr = np.array([4,25,64])
# print("Square of Array :",np.sqrt(sqr))
#
# tranform = np.array([[3,9,6],[5,1,4]])                                 # Transforming
# print("Tranforming :",tranform.T)
#
# zero = np.zeros((2,2))                                                 # Zeros
# print("Zeros :",zero)
#
# ones = np.ones((5,2))                                                  # Onces
# print("Onces :",ones)
#
# sharing = np.linspace(0,20,3)                                          # linespace get mid value of the range
# print("LineSpace :",sharing)

# rZeros = np.random.rand(5)                                             # random values less than 1
# print("Random Zero Values :",rZeros)

# randn =np.random.randn(5)                                              # Random values with negative values
# print("Random values with negative :",randn)

# randi = np.random.randint(1,6,2)                                       # Randoms Values within range
# print("Two random numbers from 1 to 6 ",randi)

# rows = np.arange(11)
# np.random.shuffle(rows)                                                # Shuffels the given values
# print("Shuffel the values :",rows)

bikeSpeed = [32,111,138,28,59,77,97]
standard_Deviation = np.std(bikeSpeed)
variance = np.var(bikeSpeed)
print("Varience for Bike Speed :",variance)                              # Variance of the Bike Speed  
print("Standard Deviation For Bike Speed :",standard_Deviation)          # Standard Deviation