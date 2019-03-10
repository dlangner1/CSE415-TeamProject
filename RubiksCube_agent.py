'''RubiksCube_agent.py

Brian Yu and Dustin Langner
CSE 415, Winter 2019, Project
March 11th, 2019

Value Iteration for Markov Decision Processes.
'''

Vkplus1 = {}
Q_Values_Dict = {}


def one_step_of_VI(S, A, T, R, gamma, Vk):
    '''S is list of all the states defined for this MDP.
    A is a list of all the possible actions.
    T is a function representing the MDP's transition model.
    R is a function representing the MDP's reward function.
    gamma is the discount factor.
    The current value of each state s is accessible as Vk[s].
    '''

    '''Your code should fill the dictionaries Vkplus1 and Q_Values_dict
    with a new value for each state, and each q-state, and assign them
    to the state's and q-state's entries in the dictionaries, as in
        Vkplus1[s] = new_value
        Q_Values_Dict[(s, a)] = new_q_value

    Also determine delta_max, which we define to be the maximum
    amount that the absolute value of any state's value is changed
    during this iteration.
    '''

    global Q_Values_Dict, Vkplus1

    delta_max = 0

    for state in S:
        new_value = 0
        for action in A:
            new_q_value = sum([T(state, action, sp) * (R(state, action, sp) + gamma * Vk[sp]) for sp in S])
            Q_Values_Dict[(state, action)] = new_q_value
            new_value = max(new_value, new_q_value)

        Vkplus1[state] = new_value
        delta_max = max(delta_max, abs(Vk[state] - new_value))

    return (Vkplus1, delta_max)


def return_Q_values(S, A):
    '''Return the dictionary whose keys are (state, action) tuples,
    and whose values are floats representing the Q values from the
    most recent call to one_step_of_VI. This is the normal case, and
    the values of S and A passed in here can be ignored.
    However, if no such call has been made yet, use S and A to
    create the answer dictionary, and use 0.0 for all the values.
    '''
    global Q_Values_Dict

    if not Q_Values_Dict:
        for state in S:
            for action in A:
                Q_Values_Dict[(state, action)] = 0.0

    return Q_Values_Dict


Policy = {}

def extract_policy(S, A):
    '''Return a dictionary mapping states to actions. Obtain the policy
    using the q-values most recently computed.  If none have yet been
    computed, call return_Q_values to initialize q-values, and then
    extract a policy.  Ties between actions having the same (s, a) value
    can be broken arbitrarily.
    '''
    global Policy, Q_Values_Dict

    # return, if I am at this state, what is the best action for me to take

    if len(Q_Values_Dict) == 0:
        # if one_step_of_VI hasn't been called yet,
        # populate Q_Values_Dict
        return_Q_values(S, A)

    for state in S:
        max_q_value = 0.0
        for action in A:
            q_value = Q_Values_Dict[(state, action)]
            if max(max_q_value, q_value) == q_value:
                Policy[state] = action
                max_q_value = q_value

    return Policy


def apply_policy(s):
    '''Return the action that your current best policy implies for state s.'''
    global Policy
    return Policy[s]
