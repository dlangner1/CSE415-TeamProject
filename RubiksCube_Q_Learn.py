'''RubiksCube_Q_Learn.py

Brian Yu and Dustin Langner
CSE 415, Winter 2019, Project
March 11th, 2019

Implement Q-Learning in this file by completing the implementations
of the functions whose stubs are present.
Add or change code wherever you see #*** ADD OR CHANGE CODE HERE ***

'''

from RubiksCube import *

STATES = None;
ACTIONS = None;
UQV_callback = None;
is_valid_goal_state = None;
Terminal_state = None
USE_EXPLORATION_FUNCTION = None
INITIAL_STATE = None

ALPHA = 0.5
CUSTOM_ALPHA = False
EPSILON = 0.5
CUSTOM_EPSILON = False
GAMMA = 0.9

ALL_STATES = []
WEIGHTS = {}
Q_VALUES = {}

def generate_all_states():
    global ALL_STATES
    moves = ['a', 'b', 'c', 'aprime', 'bprime', 'cprime']
    initial_state = CREATE_CLEAN_STATE()
    OPEN = [initial_state]
    while OPEN != []:
        S = OPEN.pop(0)
        ALL_STATES.append(S)
        L = []
        for i in range(6):
            new_state = S.move(moves[i])
            L.append(new_state)
        for s2 in ALL_STATES:
            for i in range(len(L)):
                if s2 == L[i]:
                    del L[i]
                    break
        OPEN = OPEN + L


def generate_weights():
    global ALL_STATES, WEIGHTS

    for state in ALL_STATES:
        feature_state = get_feature_states(state)

        if goal_test(state):
            WEIGHTS[feature_state] = 1000
        else:
            WEIGHTS[feature_state] = 0


def get_feature_states(state):
    f1 = game_solved(state)
    f2 = face_c_solved(state)
    f3 = top_layer_solved(state)
    f4 = face_c_almost_solved(state)
    return (f1, f2, f3, f4)


def extract_policy(state):
    global Q_VALUES

    best_action = sides[1]
    max_q = 0
    state_feature = get_feature_states(state)

    for action in sides:
        q_val = Q_VALUES[(state_feature, action)]

        if q_val > max_q:
            best_action = action
            max_q = q_val

    return best_action


def q_learn(iter_times):
    global Q_VALUES, ALL_STATES, WEIGHTS

    generate_all_states()
    generate_weights()

    for _ in range(iter_times):
        for state in ALL_STATES:
            # for the given state, we generate a list of features (1, 0 ,1 ,0 etc)
            state_feature = get_feature_states(state)

            max_weight = 0

            for action in sides:
                if not (state_feature, action) in Q_VALUES:
                    Q_VALUES[(state_feature, action)] = 0.0

                new_state = state.move(action)
                new_state_feature = get_feature_states(new_state)

                prev_weight = WEIGHTS[new_state_feature]

                max_weight = max(max_weight, prev_weight)

                Q_VALUES[(state_feature, action)] = Q_VALUES[(state_feature, action)] * (1 - ALPHA) + \
                                                    ALPHA * WEIGHTS[new_state_feature]

            WEIGHTS[state_feature] = (1 - ALPHA) * WEIGHTS[state_feature] + ALPHA * max_weight

    print("Weights: " + str(WEIGHTS))
    print("Q-Vals: " + str(Q_VALUES))


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

















# def setup(states, actions, q_vals_dict, update_q_value_callback, \
#           goal_test, terminal, use_exp_fn=False):
#     '''This method is called by the GUI the first time a Q_Learning
#     menu item is selected. It may be called again after the user has
#     restarted from the File menu.
#     Q_VALUES starts out with all Q-values at 0.0 and a separate key
#     for each (s, a) pair.'''
#     global STATES, ACTIONS, UQV_callback, Q_VALUES, is_valid_goal_state
#     global USE_EXPLORATION_FUNCTION, Terminal_state
#     STATES = states
#     ACTIONS = actions
#     Q_VALUES = q_vals_dict
#     UQV_callback = update_q_value_callback
#     is_valid_goal_state = goal_test
#     Terminal_state = terminal
#     USE_EXPLORATION_FUNCTION = use_exp_fn
#     if USE_EXPLORATION_FUNCTION:
#         # *** ADD OR CHANGE CODE HERE ***
#         # Change this if you implement an exploration function:
#         print("You have not implemented an exploration function")
#
#
# PREVIOUS_STATE = None
# LAST_ACTION = None
#
#
# def set_starting_state(s):
#     '''This is called by the GUI when a new episode starts.
#     Do not change this function.'''
#     global INITIAL_STATE, PREVIOUS_STATE
#     print("In Q_Learn, setting the starting state to " + str(s))
#     INITIAL_STATE = s
#     PREVIOUS_STATE = s
#
#
#
#
#
# def set_learning_parameters(alpha, epsilon, gamma):
#     ''' Called by the system. Do not change this function.'''
#     global ALPHA, EPSILON, CUSTOM_ALPHA, CUSTOM_EPSILON, GAMMA
#     ALPHA = alpha
#     EPSILON = epsilon
#     GAMMA = gamma
#     if alpha < 0:
#         CUSTOM_ALPHA = True
#     else:
#         CUSTOM_ALPHA = False
#     if epsilon < 0:
#         CUSTOM_EPSILON = True
#     else:
#         CUSTOM_EPSILON = False
#
#
# def update_Q_value(previous_state, previous_action, new_value):
#     '''Whenever your code changes a value in Q_VALUES, it should
#     also call this method, so the changes can be reflected in the
#     display.
#     Do not change this function.'''
#     UQV_callback(previous_state, previous_action, new_value)
#
#
# def handle_transition(action, new_state, r):
#     '''When the user drives the agent, the system will call this function,
#     so that you can handle the learning that should take place on this
#     transition.'''
#     global PREVIOUS_STATE
#
#     # *** ADD OR CHANGE CODE HERE ***
#
#
#     # You should call update_Q_value before returning.  E.g.,
#     update_Q_value(PREVIOUS_STATE, action, -99)
#
#     print("Transition to state: " + str(new_state) + \
#           "\n with reward " + str(r) + " is currently not handled by your program.")
#     PREVIOUS_STATE = new_state
#     return  # Nothing needs to be returned.
#
#
# def choose_next_action(s, r, terminated=False):
#     '''When the GUI or engine calls this, the agent is now in state s,
#     and it receives reward r.
#     If terminated==True, it's the end of the episode, and this method
#      can just return None after you have handled the transition.
#
#     Use this information to update the q-value for the previous state
#     and action pair.
#
#     Then the agent needs to choose its action and return that.
#
#     '''
#     global INITIAL_STATE, PREVIOUS_STATE, LAST_ACTION
#     # Unless s is the initial state, compute a new q-value for the
#     # previous state and action.
#     if not (s == INITIAL_STATE):
#         # Compute your update here.
#         # if CUSTOM_ALPHA is True, manage the alpha values over time.
#         # Otherwise go with the fixed value.
#         new_qval = -99  # A bogus value for now.
#         # *** ADD OR CHANGE CODE HERE ***
#
#         # Save it in the dictionary of Q_VALUES:
#         Q_VALUES[(PREVIOUS_STATE, LAST_ACTION)] = new_qval
#
#         # Then let the Engine and GUI know about the new Q-value.
#         update_Q_value(PREVIOUS_STATE, LAST_ACTION, new_qval)
#
#     # Now select an action according to your Q-Learning criteria, such
#     # as expected discounted future reward vs exploration.
#
#     if USE_EXPLORATION_FUNCTION:
#         # Change this if you implement an exploration function:
#         # *** ADD OR CHANGE CODE HERE ***
#         print("You have not implemented an exploration function")
#
#     # If EPSILON > 0, or CUSTOM_EPSILON is True,
#     # then use epsilon-greedy learning here.
#     # In order to access q-values, simply get them from the dictionary, e.g.,
#     # some_qval = Q_VALUES[(some_state, some_action)]
#
#     # *** ADD OR CHANGE CODE HERE ***
#     some_action = ACTIONS[0]  # a placeholder, so some action is returned.
#     LAST_ACTION = some_action  # remember this for next time
#     PREVIOUS_STATE = s  # "       "    "   "    "
#     return some_action
#
#
# Policy = {}
#
#
# def extract_policy(S, A):
#     '''Return a dictionary mapping states to actions. Obtain the policy
#     using the q-values most recently computed.
#     Ties between actions having the same (s, a) value can be broken arbitrarily.
#     Reminder: goal states should map to the Exit action, and no other states
#     should map to the Exit action.
#     '''
#     global Policy, Q_VALUES
#
#     for state in S:
#         max_q_value = 0.0
#         for action in A:
#             q_value = Q_VALUES[(state, action)]
#             if max(max_q_value, q_value) == q_value:
#                 Policy[state] = action
#                 max_q_value = q_value
#
#     return Policy
#
#
# def create_initial_q_vals_dict(states, actions):
#     global Q_VALUES
#
#     for state in states:
#         for action in actions:
#             Q_VALUES[(state, action)] = 0.0
#
#
#


# FEATURES

# Action here is a given face to rotate

