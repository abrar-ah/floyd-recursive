# 2 different tests samples with the sample inputs and expected outputs

# Define INF with a very large variable
INF = 99999

# Test 1: Example dataset
example1_input = [[0, 5, INF, 10],
                  [INF, 0, 3, INF],
                  [INF, INF, 0, 1],
                  [INF, INF, INF, 0]]

example1_result = [[0, 5, 8, 9],
                   [INF, 0, 3, 4],
                   [INF, INF, 0, 1],
                   [INF, INF, INF, 0]]

# Test 2: Example larger dataset
example2_input = [[0, 3, 8, INF, -4],
                  [INF, 0, INF, 1, 7],
                  [INF, 4, 0, INF, INF],
                  [2, INF, -5, 0, INF],
                  [INF, INF, INF, 6, 0]]

example2_result = [[0, 1, -3, 2, -4],
                   [3, 0, -4, 1, -1],
                   [7, 4, 0, 5, 3],
                   [2, -1, -5, 0, -2],
                   [8, 5, 1, 6, 0]]
