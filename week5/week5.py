import numpy as np

default_probs = np.array([0.2,0.2,0.06,0.3,0.4,0.65,0.3,0.23,0.02,0.12,0.134,0.21,0.08,0.1,0.1,0.02,0.3,0.015,0.2,0.03])
N = len(default_probs)
p = np.zeros((N+1))
p[0] = 1-default_probs[0]
p[1] = default_probs[0]
for i in range(2,N+1):
    for j in range(i,0,-1):
        p[j] = p[j-1]*default_probs[i-1] + p[j]*(1-default_probs[i-1])
    p[0] = p[0]*(1-default_probs[i-1])

print("\nQ1:What is p^N(3)?")
print("\nAnswer:{}".format(round(p[3],3)))

print("\nQ2:What is the expected number of losses in the portfolio?")
expected_loss = np.sum(default_probs)
print("\nAnswer:{}".format(round(expected_loss,2)))

print("\nQ3:Compute the variance of the number of losses in the portfolio. ")
variance = np.sum([p[i]*(i-expected_loss)**2 for i in range(len(p))])
print("\nAnswer:{}".format(round(variance,2)))

print("\nQ4:What is the expected tranche loss in the tranche with lower and upper attachment points of 0 and 2, respectively? ")
loss = 1*p[1] + 2*(1-p[0]-p[1])
print("\nAnswer:{}".format(round(loss,2)))

print("\nQ5:What is the expected tranche loss in the tranche with lower and upper attachment points of 2 and 4, respectively?")
loss = 1*p[3] + 2*np.sum([p[i] for i in range(4,21)])
print("\nAnswer:{}".format(round(loss,2)))

print("\nQ6:What is the expected tranche loss in the tranche with lower and upper attachment points of 4 and 20, respectively?")
loss = np.sum([(i-4)*p[i] for i in range(5,20)])
print("\nAnswer:{}".format(round(loss,2)))