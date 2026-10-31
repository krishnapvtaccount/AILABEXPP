
import heapq

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 6)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

heuristic = {
    'A': 7, 'B': 6, 'C': 4,
    'D': 2, 'E': 1, 'F': 2, 'G': 0
}

def astar(start, goal):
    open_list = [(heuristic[start], 0, start)]
    came_from = {}
    g_cost = {start: 0}

    while open_list:
        f, current_cost, current = heapq.heappop(open_list)

        if current_cost != g_cost[current]:
            continue

        if current == goal:
            path = [goal]
            while path[-1] in came_from:
                path.append(came_from[path[-1]])
            path.reverse()
            return path, g_cost[goal]

        for neighbour, cost in graph[current]:
            new_cost = g_cost[current] + cost

            if neighbour not in g_cost or new_cost < g_cost[neighbour]:
                g_cost[neighbour] = new_cost
                came_from[neighbour] = current
                priority = new_cost + heuristic[neighbour]
                heapq.heappush(
                    open_list, (priority, new_cost, neighbour)
                )

    return None, float('inf')


path, cost = astar('A', 'G')

print("Shortest path:", path)
print("Total cost:", cost)