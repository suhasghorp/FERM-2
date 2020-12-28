import numpy as np
import cvxpy as cp

print("Practicing the spreadsheet in the video")
returns = np.array([3.15,	1.75,	-6.39,	-2.86,	-6.75,	-0.54,	-6.75,	-5.26], dtype=float)/100.0
covar = np.array([[0.0010,	0.0013,	-0.0006,	-0.0007,	0.0001,	0.0001,	-0.0004,	-0.0004],
[0.0013,	0.0073,	-0.0013,-0.0006,	-0.0022,	-0.0010,	0.0014,	-0.0015],
[-0.0006,	-0.0013	,0.0599,	0.0276,	0.0635	,0.0230	,0.0330	,0.0480],
[-0.0007,	-0.0006	,0.0276	,0.0296	,0.0266	,0.0215	,0.0207,	0.0299],
[0.0001	,-0.0022,	0.0635,	0.0266,	0.1025,	0.0427,	0.0399,	0.0660],
[0.0001,	-0.0010,	0.0230,	0.0215,	0.0427,0.0321,	0.0199,	0.0322],
[-0.0004,	0.0014,	0.0330,	0.0207,	0.0399,0.0199,	0.0284,	0.0351],
[-0.0004,	-0.0015,	0.0480,	0.0299,	0.0660,	0.0322,	0.0351,0.0800]], dtype=float)

volatility = np.sqrt(np.diag(covar),dtype=float)

w = cp.Variable(8)
target_volatility = 0.8594
ret = returns.T @ w
risk = cp.quad_form(w, covar)
prob = cp.Problem(cp.Maximize(ret),[cp.sum(w) == 1, risk <= target_volatility])
#prob = cp.Problem(cp.Maximize(ret),[cp.sum(w) == 1, risk <= target_volatility, w >= 0]) # long only
prob.solve()
print("\nThe optimal return is {}".format(prob.value))
print("\nThe optimal weights is {}".format(w.value))

print("\nQuiz begins here")
'''
                            Mean-Variance Analysis and CAPM
Consider a market with d=3d=3 risky assets and 1 risk-free asset with the following parameters:
mu = [6,2,4] V = [[8,-2,4],[-2,2,-2],[4,-2,8]]X10e-3, rf = 1%
Note that the mean returns on the assets are in % but the variance is not
Note that the asset returns and variances are not representative of realistic market conditions. 
'''

print("\nQ1:Compute the mean return on the portfolio x= 1/3(1,1,1) consisting only of the risky assets.")
risky_returns = np.array([6.0,2.0,4.0])/100.0
risky_covar = np.array([[8.0, -2.0, 4.0],[-2.0,2.0,-2.0],[4.0,-2.0,8.0]])/1000.0
riskfree_rate = 0.01
volatility = np.sqrt(np.diag(covar),dtype=float)
risky_weights = np.array([1.0,1.0,1.0])/3.0
portfolio_return = np.dot(risky_returns.T, risky_weights)
print("\nanswer:{}".format(round(portfolio_return*100.0,2)))

print("\nQ2:Compute the volatility of the return on the portfolio x=1/3(1,1,1) consisting only of the risky assets "
      "(i.e. same portfolio as Question 1).")
portfolio_volatility = np.sqrt(np.dot(risky_weights.T, np.dot(risky_weights,risky_covar)))
print("\nanswer:{}".format(round(portfolio_volatility*100.0,2)))

print(
    "\nQ3:Compute the mean return on the minimum variance portfolio of just the risky assets.\n"
    "The minimum variance portfolio is defined as the portfolio of risky assets that has the least volatility \n"
    "among all possible portfolios of just the risky assets. This portfolio is the solution to the optimization \n"
    "problem")
w = cp.Variable(3)
prob = cp.Problem(cp.Minimize(cp.quad_form(w, risky_covar)),[cp.sum(w) == 1])
prob.solve()
print("\nanswer:{}".format(round(np.dot(risky_returns, w.value)*100.0,2)))

print("\nQ4:Compute the mean return on the Sharpe optimal portfolio for this market.")
mu_hat = risky_returns - riskfree_rate
positions = np.dot(mu_hat.T, np.linalg.inv(risky_covar))
sum_of_positions = np.sum(positions)
sharpe_opt_weights = positions/sum_of_positions
sharpe_opt_return = np.dot(risky_returns.T, sharpe_opt_weights)
print("\nanswer:{}".format(round(sharpe_opt_return*100,2)))

print("\nQ5:Compute the volatility of the Sharpe optimal portfolio for this market.")
sharpe_opt_volatility = np.sqrt(np.dot(sharpe_opt_weights,np.dot(risky_covar, sharpe_opt_weights)))
print("\nanswer:{}".format(round(sharpe_opt_volatility*100,2)))

print("\nQ6:Using the results in the previous question, compute the slope of the capital market line.")
slope = (sharpe_opt_return - riskfree_rate)/sharpe_opt_volatility
print("\nanswer:{}".format(round(slope,2)))

print(
    "\nQ7:Suppose the volatility of a an efficient investment opportunity is sigma=5%.\n"
    "What is the return on this opportunity?")
opp_volatility = 0.05
expected_return = riskfree_rate + ((sharpe_opt_return - riskfree_rate)/sharpe_opt_volatility) * opp_volatility
print("\nanswer:{}".format(round(expected_return * 100., 2)))








