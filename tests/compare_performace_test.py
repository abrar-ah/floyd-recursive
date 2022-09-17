# Compare the perfomrace betwween imperative and recursive function

# Import built-in packages
import sys
import time


# Use current path when importing packages
sys.path.append('.')

#
#
# Import src from src folder
from src.floyd_recursive import floyd_recursive_func
from src.floyd_imperative import floyd_imperative_func


def performance_comparison():

    INF = 99999
    graph = [[0, 5, INF, 10],
             [INF, 0, 3, INF],
             [INF, INF, 0, 1],
             [INF, INF, INF, 0]
             ]

    started_at = time.time()
    for _ in range(2 ** 12):
        floyd_recursive_func(graph)
    runtime_recursive_time = time.time() - started_at

    started_at = time.time()
    for _ in range(2 ** 12):
        floyd_imperative_func(graph)
    runtime_imperative_time = time.time() - started_at

    return runtime_recursive_time, runtime_imperative_time


if __name__ == '__main__':
    runtime_recursive, runtime_imperative = performance_comparison()

    # Print the comparison between both versions in seconds
    print('Recursive: ', round(runtime_recursive, 2), 'seconds')
    print('Imperative: ', round(runtime_imperative, 2), 'seconds')
