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

# The influence of each on the change in average price and total profit.
for i in range(9):
    # Algorithm from the condition.
    cost[i] = cost[i] * 1.01
    lose = demand[i] * 0.1
    demand[i] = demand[i] - lose
    demand[i+1] = demand[i+1] + lose
    cost_er.append(average(cost) - start_average)
    income_er.append(start_income - income(cost, demand))
    print(i, round(average(cost),3), round(income(cost, demand),4))
    cost = copy.deepcopy(start_cost)
    demand = copy.deepcopy(start_demand)
print(cost)
print(demand)
print("Cost error", cost_er)
print("Income error", income_er)
# Find some min and max elements in array.
# find_min(cost_er, 4, False)
# find_min(income_er, 4, True)
# print(cost_er, income_er)

# The effect of each price increase on the change in average price and total profit.
for i in range(9):
    # Algorithm from the condition.
    cost[i] = cost[i] * 1.01
    lose = demand[i] * 0.1
    demand[i] = demand[i] - lose
    demand[i+1] = demand[i+1] + lose
    cost_er.append(average(cost) - start_average)
    income_er.append(start_income - income(cost, demand))
print(round(average(cost),3), round(income(cost, demand),4))
print("Price and profit after each change")
print(cost)
print(demand)
cost = copy.deepcopy(start_cost)
demand = copy.deepcopy(start_demand)

# Generates a random array and checks for changes in average price and profit.
for j in range(1000000):
    rnd_mass = random.sample(range(8), random.randint(0, 8))

    for i in rnd_mass:
        # Algorithm from the condition.
        cost[i] = cost[i] * 1.01
        lose = demand[i] * 0.1
        demand[i] = demand[i] - lose
        demand[i+1] = demand[i+1] + lose
        cost_er.append(average(cost) - start_average)
        income_er.append(start_income - income(cost, demand))
    if(average(cost) > start_average) and (income(cost, demand) >= start_income - 1):
        print(rnd_mass, average(cost), income(cost, demand))
        print(cost)
        print(demand)

    cost = copy.deepcopy(start_cost)
    demand = copy.deepcopy(start_demand)

# As a result, the best average price – profit ratio is [5], [6], [7], [5, 7]. At the same time, the profit is still less than the initial one.


