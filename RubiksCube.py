'''RubiksCube.py
'''
#<METADATA>
QUIET_VERSION = "0.2"
PROBLEM_NAME = "Rubik's Cube"
PROBLEM_VERSION = "0.1"
PROBLEM_AUTHORS = ['Brian Yu', 'Dustin Langner']
PROBLEM_CREATION_DATE = "03-MAR-2019"
# TODO: replace this problem description
PROBLEM_DESC=\
'''This formulation of the Towers of Hanoi problem uses generic
Python 3 constructs and has been tested with Python 3.6.
It is designed to work according to the QUIET2 tools interface.

This formulation is slightly different from others of this puzzle,
with some reordering of operators for better compatibility with
the Reinforcement Learning software.
The goal test is also different, but should function fine
with other tools.
'''


# TODO: everything below is a copy of Towers of Hanoi.
#  We need to create a feature based representation of Rubik's Cube

#</METADATA>

#<COMMON_DATA>

#following part is unnecesssary for rubik's cube
try:
  import sys
  arg2 = sys.argv[2]
  N_disks = int(arg2)
  #print("Number of disks is "+arg2)
except:
  pass
  #print("Using default number of disks: "+str(N_disks))
  #print(" (To use a specific number, enter it on the command line, e.g.,")
  #print("python3 ../Int_Solv_Client.py TowersOfHanoi 3")
#</COMMON_DATA>

#<COMMON_CODE>
class State:
  def __init__(self, d):
    self.d = d

  def __eq__(self,s2):
    #i'm calling the front face a, the top face b, the right face c, and the
    #opposites of those their primes
    for side in ['a','aprime','b', 'bprime', 'c', 'cprime']:
      if self.d[side] != s2.d[side]: return False
    return True

  def __str__(self):
    # Produces a textual description of a state.
    # Might not be needed in normal operation with GUIs.
    # [0 1]
    # [2 3]
    # in array form, [0, 1, 2, 3]
    txt = "["
    for side in ['a','aprime','b', 'bprime', 'c', 'cprime']:
      txt += str(self.d[side]) + " ,"
    return txt[:-2]+"]"

  def __hash__(self):
    return (self.__str__()).__hash__()

  def copy(self):
    # Performs an appropriately deep copy of a state,
    # for use by operators in creating new states.
    news = State({})
    for side in ['a','aprime','b', 'bprime', 'c', 'cprime']:
      news.d[side]=self.d[side][:]
    return news

  def move(self,face):
   
      
    new_state = self.copy() # start with a deep copy.
    curA=new_state.d['a']
    curAprime=new_state.d['aprime']
    curB=new_state.d['b']
    curBprime=new_state.d['bprime']
    curC=new_state.d['c']
    curCprime=new_state.d['cprime'] 
    #TODO
    if face=='a':
      new_state.d['a'] = flip(curA)
      new_state.d['b'] = [curBprime[0], curB[1], curBprime[2], curB[3]]
      new_state.d['c'] = [curCprime[0], curC[1], curCprime[2], curC[3]]
      new_state.d['aprime'] = curAprime
      new_state.d['bprime'] = [curB[0], curBprime[1], curB[2], curBprime[3]]
      new_state.d['cprime'] = [curC[0], curCprime[1], curC[2], curCprime[3]]
    elif face=='aprime':
      new_state.d['a'] = curA
      new_state.d['b'] = [curB[0], curBprime[1], curB[2], curBprime[3]]
      new_state.d['c'] = [curC[0], curCprime[1], curC[2], curCprime[3]]
      new_state.d['aprime'] = flip(curAprime)
      new_state.d['bprime'] = [curBprime[0], curB[1], curBprime[2], curB[3]]
      new_state.d['cprime'] = [curCprime[0], curC[1], curCprime[2], curC[3]]
    elif face=='b':
      new_state.d['a'] = [curAprime[0], curAprime[1], curA[2], curA[3]]
      new_state.d['b'] = flip(curB)
      new_state.d['c'] = [curCprime[3], curCprime[2], curC[2], curC[3]]
      new_state.d['aprime'] = [curA[0], curA[1], curAprime[2], curAprime[3]]
      new_state.d['bprime'] = curBprime
      new_state.d['cprime'] = [curCprime[0], curCprime[1], curC[1], curC[0]]
    elif face=='bprime':
      
    elif face=='c':
     
    elif face=='cprime':
      
    
      
    
    news.d[From]=pf[:-1] # remove it from its old peg.
    news.d[To]=pt[:]+[df] # Put disk onto destination peg.
    return new_state # return new state
#unsure
  def flip(face):
    newface = []
    for i in range(4):
      newface.append(face[3-i])
    return newface

def make_goal_state():
  global GOAL_STATE
  GOAL_STATE = State({'a':[0, 0, 0, 0],'b':[1, 1, 1, 1],'c':[2, 2, 2, 2], 'aprime':[3, 3, 3, 3], 'bprime':[4, 4, 4, 4], 'cprime':[5, 5, 5, 5]})
  #print("GOAL_STATE="+str(GOAL_STATE))

make_goal_state()

def goal_test(s):
  '''Made stricter for use in Reinforcement Learning app.
  If the third peg has all N_disk disks on it, then s is a goal state.'''
  #return len(s.d['peg3'])==N_disks
  global GOAL_STATE
  return s==GOAL_STATE

def goal_message(s):
  return "Cube is Solved!"

class Operator:
  def __init__(self, name, precond, state_transf):
    self.name = name
    self.precond = precond
    self.state_transf = state_transf

  def is_applicable(self, s):
    return self.precond(s)

  def apply(self, s):
    return self.state_transf(s)

#</COMMON_CODE>

#<INITIAL_STATE>
#  INITIAL_DICT = {'peg1': list(range(N_disks,0,-1)), 'peg2':[], 'peg3':[] }
#  CREATE_INITIAL_STATE = lambda: State(INITIAL_DICT)
#DUMMY_STATE =  {'peg1':[], 'peg2':[], 'peg3':[] }
def CREATE_CLEAN_STATE():
  return State({'a':[0,0,0,0], 'b':[1,1,1,1], 'c':[2,2,2,2], 'aprime':[3,3,3,3], 'bprime':[4,4,4,4], 'cprime':[5,5,5,5]})
def CREATE_INITIAL_STATE():
  #TODO


  
#</INITIAL_STATE>

#<OPERATORS>
OPERATORS = [Operator("Move disk from "+p+" to "+q,
                      lambda s,p1=p,q1=q: s.can_move(p1,q1),
                      # The default value construct is needed
                      # here to capture the values of p&q separately
                      # in each iteration of the list comp. iteration.
                      lambda s,p1=p,q1=q: s.move(p1,q1) )
             for (p,q) in peg_combinations]
#</OPERATORS>

#<GOAL_TEST> (optional)
GOAL_TEST = lambda s: goal_test(s)
#</GOAL_TEST>

#<GOAL_MESSAGE_FUNCTION> (optional)
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
#</GOAL_MESSAGE_FUNCTION>

