# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    return  [s, s, w, s, w, w, s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    #print "Start:", problem.getStartState()
    #print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    #print "Start's successors:", problem.getSuccessors(problem.getStartState())
    fringe = util.Stack()
    moves = []
    visited_node = []
    fringe.push((problem.getStartState(), []))
    while not fringe.isEmpty():
        current_node, moves = fringe.pop()
        if problem.isGoalState(current_node):
            return path
        #print direction[0:2]
        for next_node, next_move, steps in problem.getSuccessors(current_node):
            if not next_node in visited_node:
                fringe.push((next_node, moves + [next_move]))
                visited_node += [current_node]
                path = moves + [next_move]
            print steps
            
    return []
    util.raiseNotDefined()
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    fringe = util.Queue()
    fringe.push((problem.getStartState(), []))
    expanded_node = [problem.getStartState()]
    while not fringe.isEmpty():
        current_node, moves = fringe.pop()
        if problem.isGoalState(current_node):
            return moves
        #print direction[0:2]
        for next_node, next_move, steps in problem.getSuccessors(current_node):
            if not next_node in expanded_node:
                fringe.push((next_node, moves + [next_move]))
                expanded_node += [next_node]
        print len(expanded_node)
    return []
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    fringe = []
    fringe.append([0, problem.getStartState(),[]]) #steps, state, path to reach
    checked_node = []
    while fringe:
        fringe.sort()
        steps, current_node, moves = fringe.pop(0)
        if problem.isGoalState(current_node):
            return moves
        checked_node += [current_node]
        for next_node, next_move, next_step in problem.getSuccessors(current_node):
            if not next_node in checked_node:
                checker = False #check if next_node in fringe yet
                for i in range (len(fringe)):
                    if next_node == fringe[i][1]:
                        checker = True;
                        if steps + next_step < fringe[i][0]:
                            fringe[i][0] = steps + next_step
                            fringe[i][2] = moves + [next_move]
                if  not checker:
                    fringe.append([steps+next_step, next_node, moves + [next_move]])

    return []
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    open_node = [[0, 0, problem.getStartState(),[]]]
    close_node = []
    while open_node:
        open_node.sort()
        distance, g_distance, current_node, moves = open_node.pop(0)
        close_node.append(current_node)
        if problem.isGoalState(current_node):
            return moves
        for next_node, next_move, steps in problem.getSuccessors(current_node):            
            if not next_node in close_node:               
                #print next_node
                checker = False
                for i in range(len(open_node)):
                    if next_node == open_node[i][2]:
                        checker = True
                        if open_node[i][0] > (heuristic(next_node, problem) +g_distance + steps):
                            open_node[i][0] = (heuristic(next_node, problem) +g_distance + steps)
                            open_node[i][1] = g_distance + steps
                            open_node[i][3] = moves + [next_move]
                        break
                if not checker:
                    open_node.append([heuristic(next_node, problem)+ g_distance+ steps,g_distance+ steps, next_node,moves + [next_move]])
                    #print(open_node[-1])

    return []           



    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
