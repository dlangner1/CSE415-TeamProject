'''RubiksCube_Q_Learn.py

Brian Yu and Dustin Langner
CSE 415, Winter 2019, Project
March 11th, 2019

'''

import tkinter
import random
import time
import RubiksCube as cube
import RubiksCube_Q_Learn as agent

window = tkinter.Tk()
window.title("GUI")

cur = cube.CREATE_CLEAN_STATE()
agent.generate_weights()

a = cur.d['a']
b = cur.d['b']
c = cur.d['c']
aprime = cur.d['aprime']
bprime = cur.d['bprime']
cprime = cur.d['cprime']

#updates the cube in the GUI
def displayCube():
    colors = {0: "blue", 1: "red", 2: "yellow", 3: "green", 4: "orange", 5: "purple"}

    acounter = 0
    bcounter = 0
    ccounter = 0
    aprimecounter = 0
    bprimecounter = 0
    cprimecounter = 0
    global a, b, c, aprime, bprime, cprime
    for i in range(2):
        for j in range(2, 4):
            tkinter.Label(window, text=b[bcounter], fg="white", bg=colors[b[bcounter]], font="Verdana 40 bold").grid(
                row=i, column=j)
            bcounter += 1
    for i in range(2, 4):
        for j in range(2):
            tkinter.Label(window, text=a[acounter], fg="white", bg=colors[a[acounter]], font="Verdana 40 bold").grid(
                row=i, column=j)
            acounter += 1
    for i in range(2, 4):
        for j in range(2, 4):
            tkinter.Label(window, text=c[ccounter], fg="white", bg=colors[c[ccounter]], font="Verdana 40 bold").grid(
                row=i, column=j)
            ccounter += 1
    for i in range(2, 4):
        for j in range(4, 6):
            tkinter.Label(window, text=aprime[aprimecounter], fg="white", bg=colors[aprime[aprimecounter]],
                          font="Verdana 40 bold").grid(row=i, column=j)
            aprimecounter += 1
    for i in range(4, 6):
        for j in range(2, 4):
            tkinter.Label(window, text=bprime[bprimecounter], fg="white", bg=colors[bprime[bprimecounter]],
                          font="Verdana 40 bold").grid(row=i, column=j)
            bprimecounter += 1
    for i in range(6, 8):
        for j in range(2, 4):
            tkinter.Label(window, text=cprime[cprimecounter], fg="white", bg=colors[cprime[cprimecounter]],
                          font="Verdana 40 bold").grid(row=i, column=j)
            cprimecounter += 1


#flips A, applies Q learning, and performs the necessary GUI changes
def flipA():
    global a, b, c, aprime, bprime, cprime, cur

    agent.q_learn(cur, 'a')

    cur = cur.move('a')
    updateStates()
    displayCube()

#flips B, applies Q learning, and performs the necessary GUI changes
def flipB():
    global a, b, c, aprime, bprime, cprime, cur

    agent.q_learn(cur, 'b')

    cur = cur.move('b')
    updateStates()
    displayCube()

#flips C, applies Q learning, and performs the necessary GUI changes
def flipC():
    global a, b, c, aprime, bprime, cprime, cur

    agent.q_learn(cur, 'c')

    cur = cur.move('c')
    updateStates()
    displayCube()

#flips APrime, applies Q learning, and performs the necessary GUI changes
def flipAPrime():
    global a, b, c, aprime, bprime, cprime, cur

    agent.q_learn(cur, 'aprime')

    cur = cur.move('aprime')
    updateStates()
    displayCube()

#flips BPrime, applies Q learning, and performs the necessary GUI changes
def flipBPrime():
    global a, b, c, aprime, bprime, cprime, cur

    agent.q_learn(cur, 'bprime')

    cur = cur.move('bprime')
    updateStates()
    displayCube()

#flips CPrime, applies Q learning, and performs the necessary GUI changes
def flipCPrime():
    global a, b, c, aprime, bprime, cprime, cur

    agent.q_learn(cur, 'cprime')

    cur = cur.move('cprime')
    updateStates()
    displayCube()

#updates the global values of the current state
def updateStates():
    global a, b, c, aprime, bprime, cprime, cur
    a = cur.d['a']
    b = cur.d['b']
    c = cur.d['c']
    aprime = cur.d['aprime']
    bprime = cur.d['bprime']
    cprime = cur.d['cprime']

#randomly moves a clean cube into a shuffled cube
def shuffle_cube():
    global a, b, c, aprime, bprime, cprime, cur
    cur = cube.CREATE_INITIAL_STATE()
    updateStates()
    displayCube()

#applies Q-learning to a random move
def run_agent_1_time():
    run_agent(1)

#applies Q-learning to 10 random moves
def run_agent_10_times():
    run_agent(10)

#applies Q-learning to 20 random moves
def run_agent_20_times():
    run_agent(20)

#applies Q-learning to num_times random moves
def run_agent(num_times):
    actions = cube.sides

    for _ in range(num_times):
        random_move = random.choice(actions)

        if random_move == 'a':
            flipA()
        elif random_move == 'b':
            flipB()
        elif random_move == 'c':
            flipC()
        elif random_move == 'aprime':
            flipAPrime()
        elif random_move == 'bprime':
            flipBPrime()
        else:
            flipCPrime()

    tkinter.Label(window, text="Weights: " + str(agent.WEIGHTS), font="Verdana 10 bold").grid(
        row=24, column=14)

#finds the move with the largest immediate Q value
best_move_text = ''
def extract_policy():
    global cur, best_move_text
    best_action = agent.extract_policy(cur)
    best_move_text = "Your best move is " + best_action
    print(best_move_text)

    tkinter.Label(window, text=best_move_text, font="Verdana 10 bold").grid(
        row=24, column=10)

#resets the GUI and current state to the clean cube state
def reset_state():
    global a, b, c, aprime, bprime, cprime, cur
    cur = cube.CREATE_CLEAN_STATE()
    updateStates()
    displayCube()

#GUI interactive buttons
tkinter.Button(window, text="Flip A", command=flipA).grid(row=12, column=10)
tkinter.Button(window, text="Flip B", command=flipB).grid(row=14, column=10)
tkinter.Button(window, text="Flip C", command=flipC).grid(row=16, column=10)
tkinter.Button(window, text="Flip APrime", command=flipAPrime).grid(row=18, column=10)
tkinter.Button(window, text="Flip BPrime", command=flipBPrime).grid(row=20, column=10)
tkinter.Button(window, text="Flip CPrime", command=flipCPrime).grid(row=22, column=10)

tkinter.Button(window, text="Run Q-Learn Agent 1 time", command=run_agent_1_time).grid(row=12, column=14)
tkinter.Button(window, text="Run Q-Learn Agent 10 times", command=run_agent_10_times).grid(row=14, column=14)
tkinter.Button(window, text="Run Q-Learn Agent 20 times", command=run_agent_20_times).grid(row=16, column=14)
tkinter.Button(window, text="Show Best Move", command=extract_policy).grid(row=18, column=14)

tkinter.Button(window, text="Shuffle Cube", command=shuffle_cube).grid(row=20, column=14)
tkinter.Button(window, text="Reset", command=reset_state).grid(row=22, column=14)

displayCube()
window.mainloop()
