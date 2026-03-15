import tkinter as tk
import numpy as np
import random

STEP_DELAY = 120
LEARNING_RATE = 0.4
mode = "graph"

history = []

def init_brain(n):
    global N, neurons, weights, pos, history
    N = n
    neurons = np.random.normal(0,0.3,N)
    weights = np.random.normal(0,0.3,(N,N))
    pos = [(random.randint(50,750),random.randint(50,450)) for _ in range(N)]
    history = []

def log(msg):
    logbox.insert(tk.END,msg+"\n")
    logbox.see(tk.END)

reward_signal = 0
pain_signal = 0

def reward():
    global reward_signal
    reward_signal = 1
    log("reward")

def pain():
    global pain_signal
    pain_signal = 1
    log("pain")

def learn():
    global weights,reward_signal,pain_signal
    activity = neurons.reshape(N,1)
    hebb = activity @ activity.T
    if reward_signal:
        weights += LEARNING_RATE * hebb
        reward_signal = 0
        log("learning positive")
    if pain_signal:
        weights -= LEARNING_RATE * hebb
        pain_signal = 0
        log("learning negative")
    weights[:] = np.clip(weights,-3,3)

def brain_step():
    global neurons, history
    noise = np.random.normal(0,0.2,N)
    syn = weights.dot(neurons)
    neurons = np.tanh(neurons*0.6 + syn*0.8 + noise)
    history.append(np.mean(neurons))
    if len(history) > 400:
        history.pop(0)
    draw()
    learn()
    root.after(STEP_DELAY,brain_step)

def draw():
    canvas.delete("all")
    if mode == "graph":
        draw_graph()
    if mode == "columns":
        draw_columns()

def draw_graph():

    max_connections = 3

    for i in range(N):

        strongest = np.argsort(np.abs(weights[i]))[-max_connections:]

        for j in strongest:

            w = weights[i][j]

            if abs(w) > 0.2:

                x1,y1 = pos[i]
                x2,y2 = pos[j]

                color = "green" if w>0 else "red"

                canvas.create_line(
                    x1,y1,x2,y2,
                    fill=color,
                    width=int(abs(w)*3)
                )

    for i in range(N):

        x,y = pos[i]

        a = neurons[i]

        r = 6 + abs(a)*10

        color = "cyan" if a>0 else "orange"

        canvas.create_oval(
            x-r,y-r,x+r,y+r,
            fill=color
        )
def draw_columns():
    if len(history) < 2:
        return
    step_x = 800/len(history)
    last_x = None
    last_y = None
    for i,val in enumerate(history):
        x = i*step_x
        y = 250 - val*200
        if last_x is not None:
            canvas.create_line(last_x,last_y,x,y,fill="cyan",width=2)
        last_x = x
        last_y = y

def set_graph():
    global mode
    mode = "graph"
    log("mode graph")

def set_columns():
    global mode
    mode = "columns"
    log("mode columns")

def rebuild():
    try:
        n = int(neuron_entry.get())
    except:
        return
    init_brain(n)
    log("brain rebuilt "+str(n))

root = tk.Tk()
root.title("Brain Lab")

canvas = tk.Canvas(root,width=800,height=500,bg="black")
canvas.pack()

controls = tk.Frame(root)
controls.pack()

tk.Button(controls,text="A reward",command=reward).pack(side="left")
tk.Button(controls,text="B pain",command=pain).pack(side="left")

tk.Button(controls,text="graph mode",command=set_graph).pack(side="left")
tk.Button(controls,text="column mode",command=set_columns).pack(side="left")

config = tk.Frame(root)
config.pack()

tk.Label(config,text="neurons").pack(side="left")

neuron_entry = tk.Entry(config,width=5)
neuron_entry.insert(0,"30")
neuron_entry.pack(side="left")

tk.Button(config,text="rebuild brain",command=rebuild).pack(side="left")

logbox = tk.Text(root,height=6)
logbox.pack(fill="both")

init_brain(30)

brain_step()

root.mainloop()
