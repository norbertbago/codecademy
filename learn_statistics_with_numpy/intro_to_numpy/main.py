import numpy as np

data1 = np.genfromtxt('numbers.csv', delimiter=',')
data2 = np.array([1,2,3,4,5,6])
data3 = np.array([6,5,4,3,2,1])
data4 = np.array([data2, data3])

#operation with array
data2_plus_3 = data2 + 3
data2_expo_2 = data2 ** 2
data2_sqrt_2 = np.sqrt(data2)
data2_data3  = data2 + data3

#slice 2d array
select_2d_1 = data2[2]
select_2d_2 = data2[2:]
select_2d_3 = data2[::-1]
select_2d_4 = data2[-1:-(len(data2)+1):-1]
select_2d_5 = data2[::-3])

#slice 2d array
select_3d_1 = data1[0]
select_3d_2 = data1[0,0]
select_3d_3 = data1[:,0]
select_3d_4 = data1[:,0:2]

#Logic operatin
data1_great_2       = data1 > 2
data1_less_2        = data1[data1 < 2]
data1_great_less1   = data1[(data1 > 1) & (data1 < 2)]
data1_great_less2   = data1[(data1 < 1 ) | (data1 == 2)]
