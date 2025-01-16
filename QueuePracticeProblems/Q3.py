# 3) Gas Station

# There are n gas stations along a circular tour, where the amount of gas at the ith gas station is gas[i]. You have a car with a gas tank of unlimited capacity and it costs cost[i] of gas to travel from the ith station to its next station. You begin the journey with an empty tank at one of the gas station. Given two integer arrays gas[] and cost[], the task is to return the starting gas station’s index if you want to travel around the circular tour once in the clockwise direction, otherwise return -1.

# Note: If a solution exists, it is guaranteed to be unique.

# Examples:

# Input: gas[] = [4, 5, 7, 4], cost[] = [6, 6, 3, 5]
# Output: 2

# Explanation: Start at gas station at index 2 and fill up with 7 units of gas. Your tank = 0 + 7 = 7
# Travel to station 3. Available gas = (7 – 3 + 4) = 8.
# Travel to station 0. Available gas = (8 – 5 + 4) = 7.
# Travel to station 1. Available gas = (7 – 6 + 5) = 6.
# Return to station 2. Available gas = (6 – 6) = 0.
# Therefore, return 2 as the starting index.

# Input: gas[] = [1, 2 ,3 ,4, 5], cost[] = [3, 4, 5, 1, 2]
# Output: 3

# Explanation: Start at gas station 3 (index 3) and fill up with 4 units of gas. Your tank = 0 + 4 = 4
# Travel to station 4. Available gas = 4 – 1 + 5 = 8
# Travel to station 0. Available gas = 8 – 2 + 1 = 7
# Travel to station 1. Available gas= 7 – 3 + 2 = 6
# Travel to station 2. Available gas = 6 – 4 + 3 = 5
# Travel to station 3. The cost is 5. The gas is just enough to travel back to station 3.
# Therefore, return 3 as the starting index.

# Input: arr[] = [3, 9], cost[] = [7, 6]
# Output: -1

# Explanation: There is no gas station to start with such that you can complete the tour.

# -----------------------------------------------------------------------------------------------------------------------------------------

def gas_station(gas, cost):
    total_tank = 0
    current_tank = 0
    start_index = 0  

    for i in range(len(gas)):
        total_tank += gas[i] - cost[i]
        current_tank += gas[i] - cost[i]


        if(current_tank < 0):
            current_tank = 0
            start_index = i + 1

    if total_tank >= 0:
        return start_index 
    else:
        return -1

gas = [4, 5, 7, 4]
cost = [6, 6, 3, 5]

if (gas_station(gas, cost) == -1):
    print("Not Possible to complete journey")
else:
    print("Stating index will be:", gas_station(gas, cost))

