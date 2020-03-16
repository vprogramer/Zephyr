import pandas as pd
import numpy as np
import copy
import random


# Search for multiple lows and highs
def find_min(lst, quantity, flag=True):
    if(flag == True):
        for i in range(quantity):
            lst.remove(max(lst))
    else:
        for i in range(quantity):
            lst.remove(min(lst))

def average(lst):
    return sum(lst) / len(lst)

def income(lst_1, lst_2):
    summa = 0
    if len(lst_1) != len(lst_2):
        raise IndexError
    for i in range(len(lst_1)):
        summa += lst_1[i] * lst_2[i]
    return summa


file_three = pd.read_csv('file_3.csv')
print(file_three.head())

cost, demand = [], []
# The difference between the initial price and the current price, and the difference between the initial price and the
# current.
cost_er, income_er = [], []

for i in file_three['спрос']:
    demand.append(float(i.replace("%","")))
for i in file_three['цена']:
    cost.append(float(i.replace("$", "")))

start_cost = copy.deepcopy(cost)
start_demand = copy.deepcopy(demand)
start_average = average(cost)
start_income = income(cost, demand)
print(start_average, start_income)

# for j in range(1000000000):
#     rnd_mass = random.sample(range(8), random.randint(0, 8))
    # print(rnd_mass)

for i in range(9):
    # Algorithm from the condition.
    cost[i] = cost[i] * 1.01
    lose = demand[i] * 0.1
    demand[i] = demand[i] - lose
    demand[i+1] = demand[i+1] + lose
    # print(i, average(cost), income(cost, demand))
    cost_er.append(average(cost) - start_average)
    income_er.append(start_income - income(cost, demand))
    print(average(cost), income(cost, demand))
    cost = copy.deepcopy(start_cost)
    demand = copy.deepcopy(start_demand)
# print(cost)
# print(demand)

print(cost_er, income_er)
# find_min(cost_er, 1, False)
# find_min(income_er, 1, True)
# print(cost_er, income_er)

    # if(average(cost) > start_average and income(cost, demand) >= start_income):
    #     print(rnd_mass, average(cost), income(cost, demand))

    # cost = copy.deepcopy(start_cost)
    # demand = copy.deepcopy(start_demand)



print(cost)
print(demand)

#   39.4   5770.5
# 0 39.519 5748.1
# 1 39.498 5766.246
# 2 39.475 5743.549
# 3 39.449 5701.717
# 4 39.426 5764.17
# 5 39.411 5770.199
# 6 39.407 5769.541
# 7 39.405 5769.8625
# [120.0, 98.0, 75.0, 49.0, 26.0, 11.0, 7.0, 5.0, 2.0, 1.0]
# [20.0, 3.0, 14.0, 37.0, 5.0, 1.0, 7.0, 2.5, 0.5, 10.0]