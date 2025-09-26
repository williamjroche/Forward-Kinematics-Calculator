import numpy as np
from sympy import Symbol, cos as c, sin as s, pi

theta1 = Symbol('theta1')
theta2 = Symbol('theta2')
theta3 = Symbol('theta3')
theta4 = Symbol('theta4')
theta5 = Symbol('theta5')
theta6 = Symbol('theta6')
a2 = Symbol('a2')
a3 = Symbol('a3')
d3 = Symbol('d3')
d4 = Symbol('d4')
L2 = Symbol('L2')

#dh table for the Puma 560 robot
dh = np.array([[0, 0, 0, theta1], [-pi/2, 0, 0, theta2], [0, a2, d3, theta3], [-pi/2, a3, d4, theta4], [pi/2, 0, 0, theta5], [-pi/2, 0, 0, theta6]])

#function for transform matrix
def transform_matrix(alpha, a, d, theta):
    T = np.array([[c(theta), -s(theta), 0, a],
                 [s(theta)*c(alpha), c(theta)*c(alpha), -s(alpha), -s(alpha)*d], 
                 [s(theta)*s(alpha), c(theta)*s(alpha), c(alpha), c(alpha)*d],
                 [0, 0, 0, 1]])
    print(T)

#for loop to loop through each transformation matrix
for i in range(6):
    transform_matrix(dh[i][0], dh[i][1], dh[i][2], dh[i][3])
    print("-----")