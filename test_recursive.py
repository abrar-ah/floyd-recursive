# Test Floyd Recursive function

# Import the recursive function
from src.floyd_recursive import (floyd_recursive_func)

# Define INF with a very large variable
INF = 99999

input_graph = [[0, 5, INF, 10],
               [INF, 0, 3, INF],
               [INF, INF, 0, 1],
               [INF, INF, INF, 0]
               ]

# Return and print the results
print(INF, "represents infinity\n")
print(*floyd_recursive_func(input_graph), sep="\n")
