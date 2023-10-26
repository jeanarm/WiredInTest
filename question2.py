from itertools import permutations
import sys

# Define the cost traveling matrix
cost_traveling_matrix = {
    ('A', 'B'): 17,
    ('A', 'C'): 9,
    ('A', 'D'): 5,
    ('A', 'E'): 6,
    ('A', 'F'): 9,
    ('B', 'A'): 11,
    ('B', 'C'): 7,
    ('B', 'D'): 8,
    ('B', 'E'): 5,
    ('B', 'F'): 8,
    ('C', 'A'): 9,
    ('C', 'B'): 7,
    ('C', 'D'): 4,
    ('C', 'E'): 5,
    ('C', 'F'): 4,
    ('D', 'A'): 5,
    ('D', 'B'): 8,
    ('D', 'C'): 4,
    ('D', 'E'): 13,
    ('D', 'F'): 8,
    ('E', 'A'): 6,
    ('E', 'B'): 5,
    ('E', 'C'): 5,
    ('E', 'D'): 11,
    ('E', 'F'): 9,
    ('F', 'A'): 9,
    ('F', 'B'): 8,
    ('F', 'C'): 4,
    ('F', 'D'): 8,
    ('F', 'E'): 13,

}

# Define the list of cities
cities = ['A', 'B', 'C', 'D', 'E', 'F']

def calculate_total_cost(path):
    total_cost = 0
    for i in range(len(path) - 1):
        total_cost += cost_traveling_matrix.get((path[i], path[i + 1]), 0)
    return total_cost

min_cost = sys.maxsize
optimal_path = []

for path in permutations(cities):
    path = list(path)
    path.append(path[0])  # Return to the starting city to complete the tour
    total_cost = calculate_total_cost(path)
    if total_cost < min_cost:
        min_cost = total_cost
        optimal_path = path

#Print the order of visited friends
print("The order to visit Jack's friends is:", optimal_path)
#Print the Minimum amount to visit hsi friends.
print("The smallest amount Jack needs to spend  to visit his friends and go back home is:", min_cost)
