import tkinter
window = tkinter.Tk()
window.title("GUI")

a = [0,0,0,0]
b = [1,1,1,1]
c = [2,2,2,2]
aprime = [3,3,3,3]
bprime = [4,4,4,4]
cprime = [5,5,5,5]
def displayCube():
    colors = {0:"blue", 1:"red", 2:"yellow", 3:"green", 4:"orange", 5:"purple"}
    acounter = 0;
    bcounter = 0;
    ccounter = 0;
    aprimecounter = 0;
    bprimecounter = 0;
    cprimecounter = 0;
    global a, b, c, aprime, bprime, cprime
    for i in range(2):
        for j in range(2, 4):
            tkinter.Label(window, text = b[bcounter], fg = "white", bg = colors[b[bcounter]]).grid(row = i, column = j)
            bcounter += 1
    for i in range(2, 4):
        for j in range(2):
            tkinter.Label(window, text = a[acounter], fg = "white", bg = colors[a[acounter]]).grid(row = i, column = j)
            acounter += 1
    for i in range(2, 4):
        for j in range(2, 4):
            tkinter.Label(window, text = c[ccounter], fg = "white", bg = colors[c[ccounter]]).grid(row = i, column = j)
            ccounter += 1
    for i in range(2, 4):
        for j in range(4, 6):
            tkinter.Label(window, text = aprime[aprimecounter], fg = "white", bg = colors[aprime[aprimecounter]]).grid(row = i, column = j)
            aprimecounter += 1
    for i in range(4, 6):
        for j in range(2, 4):
            tkinter.Label(window, text = bprime[bprimecounter], fg = "white", bg = colors[bprime[bprimecounter]]).grid(row = i, column = j)
            bprimecounter += 1
    for i in range(6, 8):
        for j in range(2, 4):
            tkinter.Label(window, text = cprime[cprimecounter], fg = "white", bg = colors[cprime[cprimecounter]]).grid(row = i, column = j)
            cprimecounter += 1
def flipA():
    global a
    a = [1, 1, 1, 1]
def flipB():
    global b
    b = [2,2,2,2]
def flipC():
    global c
    c = [3,3,3,3]
def flipAPrime():
    global aprime
    aprime = [4,4,4,4]
def flipBPrime():
    global bprime
    bprime = [5,5,5,5]
def flipCPrime():
    global cprime
    cprime = [0,0,0,0]


tkinter.Button(window, text = "Update", command = displayCube).grid(row = 10, column = 10)
tkinter.Button(window, text = "Flip A", command = flipA).grid(row = 12, column = 10)
tkinter.Button(window, text = "Flip B", command = flipB).grid(row = 14, column = 10)
tkinter.Button(window, text = "Flip C", command = flipC).grid(row = 16, column = 10)
tkinter.Button(window, text = "Flip APrime", command = flipAPrime).grid(row = 18, column = 10)
tkinter.Button(window, text = "Flip BPrime", command = flipBPrime).grid(row = 20, column = 10)
tkinter.Button(window, text = "Flip CPrime", command = flipCPrime).grid(row = 22, column = 10)
window.mainloop()
