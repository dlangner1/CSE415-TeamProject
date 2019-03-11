'''RubiksCube_Q_Learn.py

Brian Yu and Dustin Langner
CSE 415, Winter 2019, Project
March 11th, 2019

'''

import tkinter
import RubiksCube as cube

window = tkinter.Tk()
window.title("GUI")

cur = cube.CREATE_CLEAN_STATE()

a = cur.d['a']
b = cur.d['b']
c = cur.d['c']
aprime = cur.d['aprime']
bprime = cur.d['bprime']
cprime = cur.d['cprime']


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


def updateStates():
    global a, b, c, aprime, bprime, cprime, cur
    a = cur.d['a'];
    b = cur.d['b'];
    c = cur.d['c'];
    aprime = cur.d['aprime'];
    bprime = cur.d['bprime'];
    cprime = cur.d['cprime'];


def flipA():
    global a, b, c, aprime, bprime, cprime, cur
    cur = cur.move('a')
    updateStates()
    displayCube()


def flipB():
    global a, b, c, aprime, bprime, cprime, cur
    cur = cur.move('b')
    updateStates()
    displayCube()


def flipC():
    global a, b, c, aprime, bprime, cprime, cur
    cur = cur.move('c')
    updateStates()
    displayCube()


def flipAPrime():
    global a, b, c, aprime, bprime, cprime, cur
    cur = cur.move('aprime')
    updateStates()
    displayCube()


def flipBPrime():
    global a, b, c, aprime, bprime, cprime, cur
    cur = cur.move('bprime')
    updateStates()
    displayCube()


def flipCPrime():
    global a, b, c, aprime, bprime, cprime, cur
    cur = cur.move('cprime')
    updateStates()
    displayCube()


def shuffle_cube():
    global a, b, c, aprime, bprime, cprime, cur
    cur = cube.CREATE_INITIAL_STATE()
    updateStates()
    displayCube()


def reset_state():
    global a, b, c, aprime, bprime, cprime, cur
    cur = cube.CREATE_CLEAN_STATE()
    updateStates()
    displayCube()


tkinter.Button(window, text="Flip A", command=flipA).grid(row=12, column=10)
tkinter.Button(window, text="Flip B", command=flipB).grid(row=14, column=10)
tkinter.Button(window, text="Flip C", command=flipC).grid(row=16, column=10)
tkinter.Button(window, text="Flip APrime", command=flipAPrime).grid(row=18, column=10)
tkinter.Button(window, text="Flip BPrime", command=flipBPrime).grid(row=20, column=10)
tkinter.Button(window, text="Flip CPrime", command=flipCPrime).grid(row=22, column=10)

tkinter.Button(window, text="Shuffle Cube", command=shuffle_cube).grid(row=12, column=14)
tkinter.Button(window, text="Reset", command=reset_state).grid(row=14, column=14)

displayCube()
window.mainloop()
