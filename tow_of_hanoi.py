def get_moves(state):
    moves = []
    for i in range (len(state)):
        if state[i]:
            for j in range (len(state)):
                if not state[j] or state[j][-1] > state[i][-1]:
                    new_state = [s[:] for s in state]
                    new_state[j].append(new_state[i].pop())
                    moves.append((i, j, new_state))
                    #print("\nmoves :",moves)
    return moves
    
def bfs(initial_state, goal):
    visited = set()
    queue = [(initial_state, [])]
    while queue:
        current_state, path = queue.pop(0)
        if current_state == goal:
            return path
        
        visited.add(tuple(map(tuple, current_state)))
        for move in get_moves(current_state):
            if tuple(map(tuple, move[2])) not in visited:
                queue.append((move[2], path + [move]))
    return None
    
def print_sol(moves):
    for i in moves:
        print("Move disc from rod {} to rod {}".format(i[0], i[1]))

n_disks = 3
n_pillars = 3

initial_state = [[n_disks -i for i in range (n_disks)], [], []]
goal = [[], [], [n_disks -i for i in range(n_disks)]]

print("The solution is:")
print_sol(bfs(initial_state, goal))