import heapq


# shaurya kethireddy

def print_succ(state):
    possible = succ(state)
    for x in possible:
        print(str(x) + " h=" + str(distance(x)))


def helper(state, x, y):
    swap = state[:]
    temp = swap[x]
    swap[x] = swap[y]
    swap[y] = temp
    return swap


def succ(state):
    switch = {
        '0': [1, 3],
        '1': [0, 2, 4],
        '2': [1, 5],
        '3': [0, 4, 6],
        '4': [1, 3, 5, 7],
        '5': [2, 4, 8],
        '6': [3, 7],
        '7': [4, 6, 8],
        '8': [5, 7],
    }
    empty = state.index(0)
    successors = []
    for x in switch[str(empty)]:
        successors.append(helper(state, empty, x))

    return successors


def distance(state):
    count = 0
    holder = state[:]
    for x in holder:
        if x == 0:
            continue
        count += abs(int(holder.index(x) / 3) - (int(x - 1) / 3)) + abs((holder.index(x) % 3) - ((x - 1) % 3))
    return count


def solve(state):
    closed = []
    opened = []
    visited = []
    h = distance(state)
    start = (h, state, (0, h, -1))
    heapq.heappush(opened, start)
    parent = 0  # parent index
    while 1 == 1:
        if len(opened) == 0:
            print("exited with failure because open is empty")
            break
        n = heapq.heappop(opened)
        closed.append(n)

        g = n[2][0] + 1

        if n[1] == [1, 2, 3, 4, 5, 6, 7, 8, 0]:  # end case
            break

        next = succ(n[1])
        for x in next:
            h = distance(x)
            n_dash = (g + h, x, (g, h, parent))
            if x in visited:
                continue

            heapq.heappush(opened, n_dash)

        visited.extend(next)
        parent += 1

    node = closed[-1]
    traceback = []
    while node[2][2] > 0:
        node = closed[node[2][2]]
        traceback.append(node)

    traceback.append(start)
    traceback.reverse()
    traceback.append(n)

    for i in range(len(traceback)):  # trace print
        print(str(traceback[i][1]) + " h=" + str(traceback[i][2][1]) + " moves: " + str(traceback[i][2][0]))

# solve([8, 7, 6, 5, 4, 3, 2, 1, 0])
# print()
# solve([4,3,8,5,1,6,7,2,0])
# print_succ([1,2,3,4,5,0,6,7,8])
# print_succ([8, 7, 6, 5, 4, 3, 2, 1, 0])
# solve([1, 2, 3, 4, 5, 6, 7, 0, 8])
# solve([1,2,3,4,5,8,0,7,6])
# print_succ([1,2,3,4,5,0,6,7,8])
# solve([6, 4, 7, 8, 5, 0, 3, 2, 1])
# solve([8, 7, 6, 5, 4, 3, 2, 1, 0])
solve([4,3,8,5,1,6,7,2,0])
