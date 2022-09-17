# Imperative function of Floyd Algorithm

def floyd_imperative_func(graph):
    vertices = len(graph)
    assert all(len(row) == vertices for row in graph)
    distance = [row[:] for row in graph]

    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                distance[i][j] = min(distance[i][j],
                                     distance[i][k] + distance[k][j])

                # Returns the shortest path graph

    return distance
