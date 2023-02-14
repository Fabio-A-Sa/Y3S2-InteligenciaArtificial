class BucketState:

    c1 = 4   # capacity for bucket 1
    c2 = 3   # capacity for bucket 2
    
    def __init__(self, b1, b2):
        self.b1 = b1
        self.b2 = b2

    '''needed for the visited list'''
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        """Overrides the default implementation (unnecessary in Python 3)"""
        return not self.__eq__(other)
    
    def __hash__(self):
        return hash((self.b1, self.b2)) 
    ''' - '''

    def __str__(self):
        return "(" + str(self.b1) + ", " + str(self.b2) + ")"

# emptying the first bucket
def empty1(state):
    if state.b1 > 0:
        return BucketState(0, state.b2)
    return None

# emptying the second bucket
def empty2(state):
    if state.b2 > 0:
        return BucketState(state.b1, 0)
    return None

# fill first bucket
def fill1(state):
    if state.b1 < 4:
        return BucketState(4, state.b2)
    return None

# fill second bucket
def fill2(state):
    if state.b2 < 3:
        return BucketState(state.b1, 3)

# pour bucket 1 to bucket 2 and fill bucket 2
def pour12_fill2(state):
    if state.b2 < 3 and state.b1 > 0 and state.b1 + state.b2 >= 3:
        return BucketState(state.b1 - (3 - state.b2), 3)
    return None

# pour bucket 1 to bucket 2 and empty bucket 1
def pour12_empty1(state):
    if state.b1 > 0 and state.b2 < 3 and state.b1 + state.b2 < 3:
        return BucketState(0, state.b1 + state.b2)
    return None

# pour bucket 2 to bucket 1 and fill bucket 1
def pour21_fill1(state):
    if state.b1 < 4 and state.b2 > 0 and state.b1 + state.b2 >= 4:
        return BucketState(4, state.b2 - (4 - state.b2))
    return None

# pour bucket 2 to bucket 1 and empty bucket 2
def pour21_empty2(state):
    if state.b2 > 0 and state.b1 < 4 and state.b1 + state.b2 < 4:
        return BucketState(state.b1 + state.b2, 0)
    return None

def child_bucket_states(state):
    new_states = []
    if(empty1(state)):
        new_states.append(empty1(state))
    if(empty2(state)):
        new_states.append(empty2(state))
    if(fill1(state)):
        new_states.append(fill1(state))
    if(fill2(state)):
        new_states.append(fill2(state))
    if(pour12_fill2(state)):
        new_states.append(pour12_fill2(state))
    if(pour12_empty1(state)):
        new_states.append(pour12_empty1(state))
    if(pour21_fill1(state)):
        new_states.append(pour21_fill1(state))
    if(pour21_empty2(state)):
        new_states.append(pour21_empty2(state))
    return new_states

def bfs(unvisited, visited):

    current_state = unvisited[0]
    unvisited = unvisited[1:]
    visited.append(current_state)

    if current_state.b1 == 2:
        return visited

    else:
        next_states = child_bucket_states(current_state)
        for state in next_states:
            if state not in unvisited and state not in visited:
                unvisited.append(state)
        return bfs(unvisited, visited)

def dfs(state, depth, limit, accumulator):

    if depth == limit:
        return None

    else:

        if state not in accumulator: accumulator.append(state)
        if state.b1 == 2:
            return accumulator

        else:
            next_states = child_bucket_states(state)
            for new_state in next_states:
                solution = dfs(new_state, depth+1, limit, accumulator)
                if solution: return solution

def ids(state):

    limit = 0
    while True:
        attemp = dfs(state, 0, limit, [])
        if attemp:
            print("With limit = ", limit)
            return attemp
        else:
            limit += 1

initial_state = BucketState(0, 0)

print("BFS", end="\n")
result_bfs = bfs([initial_state], [])
for state in result_bfs:
    print(state)

print("DFS", end="\n")
result_dfs = dfs(initial_state, 0, 10, [])
for state in result_dfs:
    print(state)

print("IDS", end="\n")
result_ids = ids(initial_state)
for state in result_ids:
    print(state)