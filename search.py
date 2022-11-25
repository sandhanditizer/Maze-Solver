"""
Zachariah Kline
6 May 2022
Templated functions and classed to solve any search problem
"""

import math
from priorityQ import PriorityQueue
from collections import deque


class Problem:
    def __init__(self, initial, is_goal, result, actions, action_cost) -> None:
        self.initial = initial
        self.is_goal = is_goal
        self.result = result
        self.actions = actions
        self.action_cost = action_cost

#-----------------------------------------------------------------------------

class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0) -> None:
        self.state = state
        self.path_cost = path_cost
        self.parent = parent
        self.action = action
        
    def __repr__(self):
        return f"Node({self.state})\n"
    
    def __len__(self):
        if self.parent is None:
            return 0
        else:
            return len(self.parent) + 1
        
    def __lt__(self, other):
        return self.path_cost < other.path_cost

#-----------------------------------------------------------------------------

def expand(problem, node):
    state = node.state
    for action in problem.actions(state):
        new_state = problem.result(state, action)
        cost = node.path_cost + problem.action_cost(state, action, new_state)
        yield Node(state=new_state, parent=node, action=action, path_cost=cost)
        
def extract_path(node):
    if node.parent is None:
        return [node.state]
    else:
        return extract_path(node.parent) + [node.state]
    
def extract_actions(node):
    if node.parent is None:
        return [node.action]
    else:
        return extract_actions(node.parent) + [node.action]

#-----------------------------------------------------------------------------
#Search Algorithms

failure = Node('Failure', path_cost=math.inf)
cutoff = Node('Reached Cutoff', path_cost=math.inf)

def best_first_search(problem, f):
    node = Node(problem.initial)
    frontier = PriorityQueue([node], priority=f)
    reached = {problem.initial: node}
    while not frontier.empty():
        node = frontier.pop()
        if problem.is_goal(node.state):
            return node
        
        for child in expand(problem, node):
            state = child.state
            if state not in reached or child.path_cost < reached[state].path_cost:
                reached[state] = child
                frontier.add(child)
        
    return failure
    
def breadth_first_search(problem):
    node = Node(problem.initial)
    if problem.is_goal(node.state):
        return node

    frontier = deque([node])
    reached = {problem.initial}
    while frontier:
        node = frontier.pop()
        for child in expand(problem, node):
            c_state = child.state
            if problem.is_goal(c_state):
                return child

            if c_state not in reached:
                reached.add(c_state)
                frontier.appendleft(child)
    
    return failure