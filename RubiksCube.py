'''RubiksCube.py

Dustin Langner and Brian Yu
CSE 415, Winter 2019, Project
March 11th, 2019

'''
# <METADATA>
QUIET_VERSION = "0.2"
PROBLEM_NAME = "Rubik's Cube"
PROBLEM_VERSION = "0.1"
PROBLEM_AUTHORS = ['Brian Yu', 'Dustin Langner']
PROBLEM_CREATION_DATE = "03-MAR-2019"
PROBLEM_DESC = \
'''
This formulation of the Rubik's Cube game uses generic
Python 3 constructs and has been tested with Python 3.6.
It is designed to work according to the QUIET2 tools interface.

The goal of this game is to convert a given Rubik's Cube that has been randomly
shuffled a given number of times into a goal state. A Rubik's Cube is considered 
to be in a goal state if each side of the cube has a unique, single color to 
its tiles. For example, one side should consist of only white colored tiles, another
of only green tiles, and so on.  
'''

# </METADATA>

import random

# <COMMON_DATA>

NUM_RANDOM_GENERATION_MOVES = 20
GOAL_STATE = None

sides = ['a', 'aprime', 'b', 'bprime', 'c', 'cprime']


# </COMMON_DATA>
#state representation
# <COMMON_CODE>
class State:
    def __init__(self, d):
        self.d = d

    def __eq__(self, s2):
        # i'm calling the front face a, the top face b, the right face c, and the
        # opposites of those their primes
        for side in sides:
            if self.d[side] != s2.d[side]: return False
        return True

    def __str__(self):
        # Produces a textual description of a state.
        # Might not be needed in normal operation with GUIs.
        # [0 1]
        # [2 3]
        # in array form, [0, 1, 2, 3]
        txt = "["
        for side in sides:
            txt += str(self.d[side]) + " ,"
        return txt[:-2] + "]"

    def __hash__(self):
        return (self.__str__()).__hash__()

    def copy(self):
        # Performs an appropriately deep copy of a state,
        # for use by operators in creating new states.
        news = State({})
        for side in sides:
            news.d[side] = self.d[side][:]
        return news
    #move definitions
    def move(self, face):

        new_state = self.copy()  # start with a deep copy.

        curA = new_state.d['a']
        curAprime = new_state.d['aprime']
        curB = new_state.d['b']
        curBprime = new_state.d['bprime']
        curC = new_state.d['c']
        curCprime = new_state.d['cprime']

        if face == 'a':
            new_state.d['a'] = new_state.flip(curA)

            new_state.d['c'] = [curCprime[0], curC[1], curCprime[2], curC[3]]
            new_state.d['cprime'] = [curC[0], curCprime[1], curC[2], curCprime[3]]
            new_state.d['b'] = [curBprime[0], curB[1], curBprime[2], curB[3]]
            new_state.d['bprime'] = [curB[0], curBprime[1], curB[2], curBprime[3]]

        elif face == 'aprime':
            new_state.d['aprime'] = new_state.flip(curAprime)

            new_state.d['b'] = [curB[0], curBprime[1], curB[2], curBprime[3]]
            new_state.d['bprime'] = [curBprime[0], curB[1], curBprime[2], curB[3]]
            new_state.d['c'] = [curC[0], curCprime[1], curC[2], curCprime[3]]
            new_state.d['cprime'] = [curCprime[0], curC[1], curCprime[2], curC[3]]

        elif face == 'b':
            new_state.d['b'] = new_state.flip(curB)

            new_state.d['a'] = [curAprime[0], curAprime[1], curA[2], curA[3]]
            new_state.d['aprime'] = [curA[0], curA[1], curAprime[2], curAprime[3]]
            new_state.d['c'] = [curCprime[3], curCprime[2], curC[2], curC[3]]
            new_state.d['cprime'] = [curCprime[0], curCprime[1], curC[1], curC[0]]

        elif face == 'bprime':
            new_state.d['bprime'] = new_state.flip(curBprime)

            new_state.d['a'] = [curA[0], curA[1], curAprime[2], curAprime[3]]
            new_state.d['aprime'] = [curAprime[0], curAprime[1], curA[2], curA[3]]
            new_state.d['c'] = [curC[0], curC[1], curCprime[1], curCprime[0]]
            new_state.d['cprime'] = [curC[3], curC[2], curCprime[2], curCprime[3]]

        elif face == 'c':
            new_state.d['c'] = new_state.flip(curC)

            new_state.d['a'] = [curA[0], curAprime[2], curA[2], curAprime[0]]
            new_state.d['aprime'] = [curA[3], curAprime[1], curA[1], curAprime[3]]
            new_state.d['b'] = [curB[0], curB[1], curBprime[1], curBprime[0]]
            new_state.d['bprime'] = [curB[3], curB[2], curBprime[2], curBprime[3]]

        elif face == 'cprime':

            new_state.d['cprime'] = new_state.flip(curCprime)

            new_state.d['a'] = [curAprime[3], curA[1], curAprime[1], curA[3]]
            new_state.d['aprime'] = [curAprime[0], curA[2], curAprime[2], curA[0]]
            new_state.d['b'] = [curBprime[3], curBprime[2], curB[2], curB[3]]
            new_state.d['bprime'] = [curBprime[0], curBprime[1], curB[1], curB[0]]

        return new_state  # return new state

    # flips the current facing face
    def flip(self, face):
        new_face = []
        for i in range(4):
            new_face.append(face[3 - i])
        return new_face
    #acts num_moves times on the current state
    def randomize(self, num_moves):

        new_state = self.copy()

        for _ in range(num_moves):
            face_to_move = random.choice(sides)
            new_state = new_state.move(face_to_move)

        return new_state

#defines a goal state
def make_goal_state():
    global GOAL_STATE
    GOAL_STATE = State(
        {'a': [0, 0, 0, 0],
         'b': [1, 1, 1, 1],
         'c': [2, 2, 2, 2],
         'aprime': [3, 3, 3, 3],
         'bprime': [4, 4, 4, 4],
         'cprime': [5, 5, 5, 5]})


make_goal_state()

#tests a state for the goal
#goal states don't have to be the initial, all the sides just have to be
#in the goal set
def goal_test(s):

    global GOAL_STATE, sides
    match = 0
    for side_cur in sides:
        for side_goal in sides:
            if s.d[side_goal] == GOAL_STATE.d[side_cur]:
                match += 1
    return match == 6

#returns goal message
def goal_message(s):
    return "Cube is Solved!"


class Operator:
    def __init__(self, name, state_transf):
        self.name = name
        self.state_transf = state_transf

    def apply(self, s):
        return self.state_transf(s)


# </COMMON_CODE>

# <INITIAL_STATE>
#clean cube
def CREATE_CLEAN_STATE():
    return State({'a': [0, 0, 0, 0],
                  'b': [1, 1, 1, 1],
                  'c': [2, 2, 2, 2],
                  'aprime': [3, 3, 3, 3],
                  'bprime': [4, 4, 4, 4],
                  'cprime': [5, 5, 5, 5]})

#randomly shuffled initial cube
def CREATE_INITIAL_STATE():
    return CREATE_CLEAN_STATE().randomize(NUM_RANDOM_GENERATION_MOVES)

# </INITIAL_STATE>

# <OPERATORS>

OPERATORS = [Operator("Move side " + p, lambda s, p1=p: s.move(p1)) for p in sides]
# </OPERATORS>

# <GOAL_TEST> (optional)
GOAL_TEST = lambda s: goal_test(s)
# </GOAL_TEST>

# <GOAL_MESSAGE_FUNCTION> (optional)
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
# </GOAL_MESSAGE_FUNCTION>
