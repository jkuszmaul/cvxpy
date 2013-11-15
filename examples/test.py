from cvxpy import *

import cvxopt
import numpy


# Problem data.
m = 30
n = 20
A = cvxopt.normal(m,n)
b = cvxopt.normal(m)

import cProfile
# Construct the problem.
x = Variable(n)

objective = Minimize(sum(square(A*x - b)))
constraints = [0 <= x, x <= 1]
p = Problem(objective, constraints)


# The optimal objective is returned by p.solve().
cProfile.run("""
result = p.solve()
""")
# The optimal value for x is stored in x.value.
print x.value
# The optimal Lagrange multiplier for a constraint
# is stored in constraint.dual_value.
print constraints[0].dual_value