import math
import time


class State:
    def _init_(self, state, cost):
        self.state = state
        self.cost = cost

    def set_cost(self, cost):
        self.cost = cost



def get_neighbours(state):
    i = 0
    k = 0
    neighbours = []

    for item in state:
        j = 0
        for element in item:
            if element == 0:
                k = 1
                break

            j = j + 1
        if k == 1:
            break
        i = i + 1

    neighbour = list(state)
    n = 0

    for item in neighbour:
        neighbour[n] = list(item)
        n = n + 1

    if i < 2:
        neighbour[i][j] = state[i + 1][j]
        neighbour[i + 1][j] = 0

        n = 0
        for item in neighbour:
            neighbour[n] = tuple(item)
            n = n + 1
        neighbour = tuple(neighbour)

        neighbours.append(neighbour)

    neighbour = list(state)
    n = 0
    for item in neighbour:
        neighbour[n] = list(item)
        n = n + 1

    if j < 2:
        neighbour[i][j] = state[i][j + 1]
        neighbour[i][j + 1] = 0
        n = 0
        for item in neighbour:
            neighbour[n] = tuple(item)
            n = n + 1
        neighbour = tuple(neighbour)
        neighbours.append(neighbour)

    neighbour = list(state)
    n = 0
    for item in neighbour:
        neighbour[n] = list(item)
        n = n + 1

    if i > 0:
        neighbour[i][j] = state[i - 1][j]
        neighbour[i - 1][j] = 0
        n = 0
        for item in neighbour:
            neighbour[n] = tuple(item)
            n = n + 1
        neighbour = tuple(neighbour)
        neighbours.append(neighbour)

    neighbour = list(state)
    n = 0
    for item in neighbour:
        neighbour[n] = list(item)
        n = n + 1

    if j > 0:
        neighbour[i][j] = state[i][j - 1]
        neighbour[i][j - 1] = 0
        n = 0
        for item in neighbour:
            neighbour[n] = tuple(item)
            n = n + 1
        neighbour = tuple(neighbour)
        neighbours.append(neighbour)

    return neighbours


def goal_test(state):
    goal = ((0, 1, 2), (3, 4, 5), (6, 7, 8))
    result = 1
    if state != goal:
        result = 0
    return result



def solution(state, parent_map):
    sol = []
    cost_to_goal = 0
    while parent_map[state]:
        sol.append(state)
        state = parent_map[state]
        cost_to_goal += 1

    sol.reverse()
    sol.append(cost_to_goal)
    return sol



def get_cost(state, parent_map, l):
    h1 = 0
    h2 = 0
    for row in state:
        for element in row:
            h1 += abs(state.index(row) - int(element / 3)) + abs(row.index(element) - element % 3)
    for row in state:
        for element in row:
            h2 += math.sqrt((state.index(row) - int(element / 3)) * 2 + (row.index(element) - element % 3) * 2)

    g = 0
    while parent_map[state]:
        g = g + 1
        state = parent_map[state]
    if l == '1':
        return g + h1

    elif l == '2':
        return g + h2


def getInvCount(arr):
    l = []

    for item in arr:
        for element in item:
            l.append(element)

    inv_count = 0

    for i in range(0, 9):
        if l[i] == 0:
            continue
        for j in range(i + 1, 9):
            if l[j] == 0:
                continue
            if l[i] > l[j]:
                inv_count += 1

    return inv_count


def isSolvable(puzzle):
    invCount = getInvCount(puzzle)

    return (invCount % 2 == 0)

def BFS(init_state):
    frontier = [init_state]
    explored = []
    exploredNodes = 0

    parent_map = {init_state: 0}

    while frontier:
        current_state = frontier.pop(0)
        explored.append(current_state)
        exploredNodes += 1

        if goal_test(current_state):
            print("Explored nodes: ", exploredNodes - 1)
            sol = solution(current_state, parent_map)
            return sol

        for neighbour in get_neighbours(current_state):
            isFrontier = 0
            isExplored = 0

            for item in frontier:
                if neighbour == item:
                    isFrontier = 1
                    break

            for item in explored:
                if neighbour == item:
                    isExplored = 1
                    break

            if isFrontier == 0 and isExplored == 0:
                frontier.append(neighbour)
                parent_map[neighbour] = current_state


def DFS(init_state):
    frontier = [init_state]
    stack = []
    exploredNodes = 0

    parent_map = {init_state: 0}

    while frontier:
        current_state = frontier.pop()
        stack.append(current_state)
        exploredNodes += 1
        if goal_test(current_state):
            print("Explored nodes: ", exploredNodes - 1)
            sol = solution(current_state, parent_map)
            return sol

        for neighbour in get_neighbours(current_state):
            isFrontier = 0
            isExplored = 0

            for item in frontier:
                if neighbour == item:
                    isFrontier = 1
                    break

            for item in stack:
                if neighbour == item:
                    isExplored = 1
                    break

            if isFrontier == 0 and isExplored == 0:
                frontier.append(neighbour)
                parent_map[neighbour] = current_state



def A_star(init_state, n):
    explored = []

    state = State(init_state, 0)  #function takes the initial state and the current coast
    frontier = [state] # fadia lessa ma3amalsh exploration
    parent_map = {init_state: 0}
    exploredNodes = 0

    while frontier:
        frontier.sort(key=lambda x: x.cost)
        current_state = frontier.pop(0)
        explored.append(current_state.state)
        exploredNodes += 1

        if goal_test(current_state.state):
            print("Explored nodes: ", exploredNodes - 1)
            sol = solution(current_state.state, parent_map)
            return sol

        for neighbour in get_neighbours(current_state.state):
            isFrontier = 0
            isExplored = 0
            for item in frontier:
                if neighbour == item.state:
                    isFrontier = 1
                    break
            for item in explored:
                if neighbour == item:
                    isExplored = 1
                    break

            if isFrontier == 0 and isExplored == 0:
                parent_map[neighbour] = current_state.state
                neighbour_state = State(neighbour, get_cost(neighbour, parent_map, n))
                frontier.append(neighbour_state)

            elif isFrontier:
                neighbour_state = State(neighbour, get_cost(neighbour, parent_map, n))
                for item in frontier:
                    if item.state == neighbour:
                        if item.cost > neighbour_state.cost:
                            item.set_cost(neighbour_state.cost)


def choose_algo(z):
    sol = []
    if z == '1':
        start_time = time.time()
        sol = BFS(puzzle)
        print("--- %s seconds ---" % (time.time() - start_time))
    elif z == '2':
        start_time = time.time()
        sol = DFS(puzzle)
        print("--- %s seconds ---" % (time.time() - start_time))
    elif z == '3':
        m = input("CHOOSE THE Heuristics \n1-Manhattan Distance\n2-Euclidean Distance\n")
        start_time = time.time()
        sol = A_star(puzzle, m)
        print("--- %s seconds ---" % (time.time() - start_time))
    return sol


values0 = map(int, input("Enter first row: ").split(","))
values1 = map(int, input("Enter second row: ").split(","))
values2 = map(int, input("Enter third row: ").split(","))

l0 = values0
l1 = values1
l2 = values2

t0 = tuple(l0)
t1 = tuple(l1)
t2 = tuple(l2)
puzzle = (t0, t1, t2)

if isSolvable(puzzle):
    print("Solvable")
    z1 = input("CHOOSE THE SEARCH Algorithms \n1-BFS\n2-DFS\n3-A*\n")
    sol1 = choose_algo(z1)
    n = len(sol1)
    for item in sol1:
        if item == sol1[n - 1]:
            print(f'Cost of Path = Depth =  {item}')
            break
        print(item[0])
        print(item[1])
        print(item[2])
        print('')
else:
    print("Not Solvable")
