import numpy as np
from sympy import Symbol, cos as c, sin as s

theta1 = Symbol('theta1')
d2 = Symbol('d2')
L2 = Symbol('L2')
theta3 = Symbol('theta3')

dh = np.array([[0, 0, 0, theta1], [np.pi/2, 0, d2, 0], [0, 0, L2, theta3]])
print("Table: ")
print(dh)
print("-----")

for i in range(3):
    Ti_i_1 = np.array([[c(dh[i][3]), -s(dh[i][3]), 0, dh[i][1]],
                 [s(dh[i][3])*c(dh[i][0]), c(dh[i][3])*c(dh[i][0]), -s(dh[i][0]), -s(dh[i][0])*dh[i][2]], 
                 [s(dh[i][3])*s(dh[i][0]), c(dh[i][3])*s(dh[i][0]), c(dh[i][0]), c(dh[i][0])*dh[i][2]],
                 [0, 0, 0, 1]])
    print(Ti_i_1)
    print("-----")