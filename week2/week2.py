import numpy as np
import cvxpy as cp

print("\nQ1:Compute an estimated efficient portfolio with 5% volatility. What is the estimated return on this portfolio?")
returns = np.array([-0.5186,	4.7057,	-0.6986])
cov_matrix = np.array([[0.0056,	-0.0020,	0.0037],
[-0.0020,	0.0022,	-0.0022],
[0.0037,	-0.0022,	0.0074]])
riskfree_rate = 1.0
volatility = np.sqrt(np.diag(cov_matrix),dtype=float)

w = cp.Variable(4)
target_volatility = 0.05
ret = returns.T @ w[0:3] + w[3] * riskfree_rate
risk = cp.quad_form(w[0:3], cov_matrix)
prob = cp.Problem(cp.Maximize(ret),[cp.sum(w) == 1, (risk - target_volatility**2) <= 1e-8])
prob.solve()
ret = returns.T @ w.value[0:3] + w.value[3] * riskfree_rate
print("\nanswer:{}".format(round(ret,2)))

print("\nQ2:Compute the true expected return (realized return) of the portfolio that you computed in Problem 1.")
mean_return = np.array([6.0,2.0,4.0]) # from "Data" worksheet
expected_return = mean_return.T @ w.value[0:3] + w.value[3] * 1.0
print("\nanswer:{}".format(round(expected_return,2)))

print("\nQ3:Use this data to estimate the Value-at-Risk at the 90% probability level.")
equally_weighted_loss = np.sort(np.array([-1.1168,-1.3565,1.3754,-1.0396,0.5662,-0.0050,-1.9092,1.1039,-0.2332,-0.6678,-1.3045,
                                0.8229,0.9616,-0.9685,1.0631,-2.8888,0.6022,1.1204,-0.9511,0.0810,-0.8619,0.0685,-0.2053,
                                 0.9565,0.1795,-2.4565,-0.0656,-0.1942,0.3471,-0.2564,1.2923,-0.3045,0.4619,-1.8819,-1.1397,1.9877,
                                 -0.0960,1.0440,-0.2722,-0.0218,0.8140,1.9191,2.1450,-0.3924,0.8846,-2.0569,-0.8699,-0.4551,-0.5114,
                                 -0.0412,0.2515,-0.6077,1.8807,-0.2756,-1.2639,-1.4916,-0.9395,2.3707,-0.2759,-0.7360])*-1.0)
var90 = -np.quantile(equally_weighted_loss,0.1, interpolation='higher')
print("\nanswer:{}".format(round(var90,2)))

print("\nQ4:Use this data to estimate the Conditional Value-at-Risk at the 90% probability level.")
ES = -1/ (60 * (1 - 0.9)) * np.sum(equally_weighted_loss[equally_weighted_loss <= -var90])
print("\nanswer:{}".format(round(ES,2)))

import math
print("\nQ5:Consider a portfolio manager who has been successful in 12 years out of 15. Compute the probability of the "
"manager having a track record as good as or better than this if he had no skill. You may assume that success or "
"failure in any year is independent of success or failure in any other year.")
def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

n = 15
p = .5
probNoSkill = 0.
for r in range(12, n+1):
    probNoSkill += nCr(n,r)*(p**r)*((1-p)**(n-r))

print("\nanswer:{}".format(round(probNoSkill,4)))

#another way to do this
#1-scipy.stats.binom.cdf(11,15,0.5)

print("\nQ6:Suppose now that there are M=100 fund managers, each of whom have 15-year track records. "
"Suppose that the best manager outperformed in 14 of the 15 years. "
"Compute the probability that the best of the managers had a track record as good as or better than this "
"if all of them had no skill. You may assume that success or failure in any year is independent of success or failure "
"in any other year and that the managers' performances are independent of each other.")

n = 15
p = .5
probNoSkill = 0.
for r in range(14, n + 1):
    probNoSkill += nCr(n, r) * (p ** r) * ((1 - p) ** (n - r))

M = 100
bestManagerNoSkill = 1. - (1. - probNoSkill) ** M
print("\nanswer:{}".format(round(bestManagerNoSkill, 4)))

#another way to do this
#1-(scipy.stats.binom.cdf(13,15,0.5))**100

print("\nQ7 - what ever")
# 2 goats, 2 cars

# door 1, chosen
# door 2
# door 3
# door 4, goat

# door 1 can be either car or goat
# 2/4 = 0.5
# door 2 and 3 can either be car, car or car, goat
print("\nanswer:{}".format(0.5 * 0.5 + 1.0 * 0.5))
