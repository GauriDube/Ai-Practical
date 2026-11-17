# Practical 11: DFS for Water Jug Problem

def dfs(a, b, visited):
    if (a, b) in visited:
        return False

    visited.add((a, b)) 
    print("Current State:", a, b)

    if a == 0 and b == 1:
        print("Goal Reached:", a, b)
        return True

    states = [
        (0, b), (a, 0), (2, b), (a, 5),
        (a-min(a, 5-b), b+min(a, 5-b)),
        (a+min(b, 2-a), b-min(b, 2-a))
    ]

    for x, y in states:
        if dfs(x, y, visited):
            return True

    return False

dfs(0, 0, set())
