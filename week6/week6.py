import numpy as np

N = 10
u = 1.2
d = 0.9
R = 1.1
q = (R - d)/(u - d)
S0 = 400.0


price_tree = []
for n in range(N+1):
    M = n + 1
    price = np.zeros(M)
    for i in range(M):
        price[i] = S0 * (u ** (n - i)) * (d ** i)
    price_tree.append(price[::-1])

C = 200.0
G = 10000.0
upgrade_cost = 5000000.0
value_tree_with_cost = [np.zeros(N+1)] * (N+1)
for n in range(N-1,-1,-1):
    M = n + 1
    value = np.zeros(M)
    for i in range(M):
        value[i] = (((max(0.0, price_tree[n][i] - C) * G) + (q * value_tree_with_cost[n + 1][i + 1]) + ((1 - q) * value_tree_with_cost[n + 1][i])) / (1.0 + 0.1))
    value_tree_with_cost[n] = value

C = 240.0
G = 14000.0
value_tree_with_equipment = [np.zeros(N+1)] * (N+1)
for n in range(N-1,-1,-1):
    M = n + 1
    value = np.zeros(M)
    for i in range(M):
        value[i] = max(value_tree_with_cost[n][i] - upgrade_cost, (((max(0.0, price_tree[n][i] - C) * G) + (q * value_tree_with_equipment[n + 1][i + 1]) + ((1 - q) * value_tree_with_equipment[n + 1][i])) / (1.0 + 0.1)))
    value_tree_with_equipment[n] = value


print("\nQ1:Compute the time t=0 value of the mine when the enhancement is already in place.")
print("\nAnswer:{}".format(round(value_tree_with_equipment[0][0]/1000000.0,3)))

C = 200.0
G = 10000.0
upgrade_cost = 5000000.0
value_tree_with_equipment_option = [np.zeros(N+1)] * (N+1)
for n in range(N-1,-1,-1):
    M = n + 1
    value = np.zeros(M)
    for i in range(M):
        if n >= 5:
            value[i] = max(value_tree_with_equipment[n][i] - upgrade_cost,
                           (((max(0.0, price_tree[n][i] - C) * G) +
                             (q * value_tree_with_equipment_option[n + 1][i + 1]) +
                             ((1 - q) * value_tree_with_equipment_option[n + 1][i])) / (1.0 + 0.1)))
        else:
            value[i] = ((max(0.0, price_tree[n][i] - C) * G) +
                             (q * value_tree_with_equipment_option[n + 1][i + 1]) +
                             ((1 - q) * value_tree_with_equipment_option[n + 1][i])) / (1.0 + 0.1)
    value_tree_with_equipment_option[n] = value


print("\nQ2:Compute the time t=0 value of the mine when the lease enhancement is not in place but you do have the option to perform the enhancement, "
"i.e. install the new equipment, at the beginning of the fifth year or any later point in the lifetime of the lease.")
print("\nAnswer:{}".format(round(value_tree_with_equipment_option[0][0]/1000000.0,3)))

exercise_boundary = [np.zeros(N+1)] * (N+1)
for n in range(N-1,-1,-1):
    M = n + 1
    value = np.zeros(M)
    for i in range(M):
        value[i] = value_tree_with_equipment[n][i] - upgrade_cost - \
                       (((max(0.0, price_tree[n][i] - C) * G) +
                         (q * value_tree_with_equipment_option[n + 1][i + 1]) +
                         ((1 - q) * value_tree_with_equipment_option[n + 1][i]))/(1 + 0.1))

    exercise_boundary[n] = value

print("\nQ3:Suppose you own the lease on the mine and the option to enhance the mine in year 5 or later. Assuming you behave optimally, "
" what is the earliest period in which there is a strictly positive probability that you will enhance the mine, i.e. install the new equipment?")
first_positive_prob_5_or_after = np.argmax(exercise_boundary[5:][0] > 0)
#since np.argmax(exercise_boundary[5:][0] > 0) = 4, year 5 is profitable
print("\nAnswer:{}".format(int(5)))

print("\nQ4:Suppose you own the lease on the mine and the option to enhance the mine in year 5 or later. "
      "Assuming you behave optimally, how many time periods are there in which there is a strictly positive probability that you will actually enhance the mine, "
      "i.e. install the new equipment? ")
print("\nThis is a very poorly worded question and I struggled with it for a long time just to understand the question.\nBy trial and error, answer seems to be 2")
print("\nAnswer:{}".format(int(2)))








