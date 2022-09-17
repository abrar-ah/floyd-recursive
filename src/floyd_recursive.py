# Recursive function of Floyd Algorithm

# Main recursive function
def floyd_recursive_func(dist):
    # Find the number of vertices
    vertices = len(dist)

    # Cache used for caching the outputs of function
    cache = {}
    # Function to find the shortest path

    def floyd_rec(i, j, k):

        # Checks if the output already exists in cache
        if (i, j, k) in cache:
            return cache[i, j, k]

        # if it's the first vertex
        if k == -1:
            return dist[i][j]

        length = min(floyd_rec(i, j, k - 1),
                     floyd_rec(i, k, k - 1) + floyd_rec(k, j, k - 1))

        # Add the result to cache
        cache[i, j, k] = length
        return length
    # Find the shortest path and update graph
    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                dist[i][j] = floyd_rec(i, j, k)

            # Return the shortest path graph
    return dist
