import numpy as np


def calculate(list):
  #Checking whether list contains 9 elements or not
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")

  #Creating a numpy 3x3 matrix from python list
  A = np.array(list)
  A = A.reshape(3, 3)

  #Calculating means of rows, columns and overall matrix
  mean1 = A.mean(axis=0)
  mean2 = A.mean(axis=1)
  mean3 = A.mean()
  #Creating a list of all means
  mean = [mean1.tolist(), mean2.tolist(), mean3]

  #Calculating variances of rows, columns and overall matrix
  var1 = A.var(axis=0)
  var2 = A.var(axis=1)
  var3 = A.var()
  #Creating a list of all variances
  var = [var1.tolist(), var2.tolist(), var3]

  #Calculating std deviations of rows, columns and overall matrix
  std1 = A.std(axis=0)
  std2 = A.std(axis=1)
  std3 = A.std()
  #Creating a list of all std deviations
  std = [std1.tolist(), std2.tolist(), std3]

  #Calculating max of rows, columns and overall matrix
  max1 = A.max(axis=0)
  max2 = A.max(axis=1)
  max3 = A.max()
  #Creating a list of all max values
  max = [max1.tolist(), max2.tolist(), max3]

  #Calculating min of rows, columns and overall matrix
  min1 = A.min(axis=0)
  min2 = A.min(axis=1)
  min3 = A.min()
  #Creating a list of all min values
  min = [min1.tolist(), min2.tolist(), min3]

  #Calculating sums of rows, columns and overall matrix
  sum1 = A.sum(axis=0)
  sum2 = A.sum(axis=1)
  sum3 = A.sum()
  #Creating a list of all sums
  sum = [sum1.tolist(), sum2.tolist(), sum3]

  #Creating and returning the required dictionary
  calculations = {
    'mean': mean,
    'variance': var,
    'standard deviation': std,
    'max': max,
    'min': min,
    'sum': sum
  }

  return calculations
