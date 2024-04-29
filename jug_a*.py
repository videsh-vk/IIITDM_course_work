from collections import deque

def cost(state, goal_state):
    return abs(state[0] - goal_state[0]) + abs(state[1] - goal_state[1])

def pour(state, jug1, jug2):
    new_state = list(state)
    amount_to_pour = min(state[jug1], max_capacities[jug2] - state[jug2])
    new_state[jug1] -= amount_to_pour
    new_state[jug2] += amount_to_pour
    return tuple(new_state)


def generate_neighbors(state):
    successors = []
    for jug1, jug2 in [(0, 1), (1, 0)]:
        new_state = pour(state, jug1, jug2)
        if new_state != state:
            successors.append(new_state)
    for jug in [0, 1]:
        new_state = list(state)
        new_state[jug] = max_capacities[jug]
        successors.append(tuple(new_state))
    for jug in [0, 1]:
        new_state = list(state)
        new_state[jug] = 0
        successors.append(tuple(new_state))
    return successors


def astar(initial_state, goal_state, max_capacities):
    open_list = [(cost(initial_state, goal_state), initial_state)]
    closed_list = set()
    parent = {initial_state: None}
    while open_list:
        _, current_state = open_list.pop(0)
        if current_state == goal_state:
            path = deque()
            state = current_state
            while state is not None:
                path.appendleft(state)
                state = parent[state]
            return list(path)
        closed_list.add(current_state)
        for successors_state in generate_neighbors(current_state):
            if successors_state not in closed_list:
                successors_cost = cost(successors_state, goal_state)
                open_list.append((successors_cost, successors_state))
                open_list.sort()
                parent[successors_state] = current_state

    return None

initial_state = (0, 0)
goal_state = (2, 0)  # Example: Want to measure 2 liters of water in Jug A
max_capacities = (3, 5)  # Capacities of Jug A and Jug B respectively

result = astar(initial_state, goal_state, max_capacities)
if result == "No path to goal":
    print(result)
else:
    print("Path found:", result)  # Print path to goal if found
