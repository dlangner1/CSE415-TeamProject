'''RubiksCube_Q_Learn.py

Brian Yu and Dustin Langner
CSE 415, Winter 2019, Project
March 11th, 2019

Implement Q-Learning in this file by completing the implementations
of the functions whose stubs are present.
Add or change code wherever you see #*** ADD OR CHANGE CODE HERE ***

'''

from RubiksCube import *

ALPHA = 0.5
CUSTOM_ALPHA = False
EPSILON = 0.5
CUSTOM_EPSILON = False
GAMMA = 0.9

WEIGHTS = None

def generate_weights():
    global WEIGHTS
    # game solved, face_c_solved, top_layer, face_c_almost
    WEIGHTS = [100, 25, 25, 10]


def get_feature_states(state):
    f1 = game_solved(state)
    f2 = face_c_solved(state)
    f3 = top_layer_solved(state)
    f4 = face_c_almost_solved(state)
    return (f1, f2, f3, f4)


def extract_policy(state):
    actions = sides

    best_action = sides[0]
    max_q = 0

    for action in actions:
        curr_q_val = get_q_value(state, action)

        if curr_q_val > max_q:
            max_q = curr_q_val
            best_action = action

    return best_action


# state = sprime
def value(state):
    actions = sides
    max_val = -1000

    for action in actions:
        new_state = state.move(action)
        val = 100 if goal_test(new_state) else 0
        max_val = max(max_val, val)

    return max_val


def reward(state, action):
    new_state = state.move(action)

    if not goal_test(new_state):
        return -1
    else:
        return 100


def get_q_value(state, action):
    global WEIGHTS

    new_state = state.move(action)
    new_features = get_feature_states(new_state)

    q_sum = 0
    for i in range(len(WEIGHTS)):
        q_sum += WEIGHTS[i] * new_features[i]

    return q_sum


def q_learn(state, action):
    global GAMMA, ALPHA, WEIGHTS
    new_state = state.move(action)
    new_features = get_feature_states(state)

    correction = (reward(state, action) + GAMMA * value(new_state)) - get_q_value(state, action)

    for i in range(len(WEIGHTS)):
        WEIGHTS[i] = WEIGHTS[i] + (ALPHA * correction * new_features[i])


def game_solved(state):
    if goal_test(state):
        return 1
    else:
        return 0


def face_c_solved(state):
    face_c = state.d['c']
    if face_c[0] == face_c[1] == face_c[2] == face_c[3]:
        return 1
    else:
        return 0


def top_layer_solved(state):

    face_a = state.d['a']
    face_b = state.d['b']
    face_c = state.d['c']
    face_aprime = state.d['aprime']
    face_bprime = state.d['bprime']
    face_equals = face_c[0] == face_c[1] == face_c[2] == face_c[3]
    a_equals = face_a[1] == face_a[3]
    aprime_equals = face_aprime[0] == face_aprime[2]
    b_equals = face_b[2] == face_b[3]
    bprime_equals = face_bprime[0] == face_bprime[1]
    if face_equals and a_equals and aprime_equals and b_equals and bprime_equals:
        return 1
    else:
        return 0


def face_c_almost_solved(state):
    face_c = state.d['c']
    comb1 = face_c[0] == face_c[1] != face_c[2] == face_c[3]
    comb2 = face_c[0] == face_c[2] != face_c[1] == face_c[3]
    if comb1 or comb2:
        return 1
    else:
        return 0
