
#Define the function that will count the numbr of routes.
def countRoutes(n):
    #return one if n is less or equal to 1
    if n <= 1:
        return 1

    # Create an array to store the number of ways to reach each step
    ways = [0] * (n + 1)

    # There's one way to reach the first step (the top of the ladder)
    ways[0] = 1
    ways[1] = 1
    ways[2] = 2  # Two ways to reach the second step

    for i in range(3, n + 1):
        # The number of ways to reach step i is the sum of the ways to reach the
        # three previous steps (i-1, i-2, and i-3)
        ways[i] = ways[i - 1] + ways[i - 2] + ways[i - 3]

    return ways[n]

n = 8 # Number of steps in the ladder
#assign the function returned value to  a variable called routes.
routes = countRoutes(n)
print(f"The number of possible routes from the top to the ground with {n} steps is: {routes}")
