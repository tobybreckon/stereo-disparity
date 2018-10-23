#####################################################################

# equation of a plane in python hints (incomplete)

# originally aimed at 2017/18 L3 SSA students at DU for the road surface task
# not directly relevant to the 2018/19 assignment on object detection

import numpy as np
import sys
import random
import math

#####################################################################

if __name__ == "__main__":
    print("This file doesn't execute fully - see example code after this message")
    exit();
#####################################################################

# points = np.array(....) ... of 3D points
# ....

# how to - select 3 non-colinear points

cross_product_check = np.array([0,0,0]);
while cross_product_check[0] == 0 and cross_product_check[1] == 0 and cross_product_check[2] == 0:
    [P1,P2,P3] = points[random.sample(range(len(points)), 3)];
    # make sure they are non-collinear
    cross_product_check = np.cross(P1-P2, P2-P3);

# how to - calculate plane coefficients from these points
# N.B. this may fail on occasion if matrix is singular - put inside a try/catch to avoid this instance when it occurs

coefficients_abc = np.dot(np.linalg.inv(np.array([P1,P2,P3])), np.ones([3,1]))
coefficient_d = math.sqrt(coefficients_abc[0]*coefficients_abc[0]+coefficients_abc[1]*coefficients_abc[1]+coefficients_abc[2]*coefficients_abc[2])

# how to - measure distance of all points from plane given the plane coefficients calculated

dist = abs((np.dot(points, coefficients_abc) - 1)/coefficient_d)

# ....

#####################################################################
