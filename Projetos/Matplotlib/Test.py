import matplotlib.pyplot as plt
import numpy as np

fig,ax = plt.subplots()

x = np.arange(0,100.0)

functions = [
    ('Cosine', np.cos(2*np.pi*x/50.0), 'b-'),
    ('Sine',   np.sin(2*np.pi*x/50.0), 'r--'),
]


plt.show(block = False)


for label, y, style in functions:

    ax.plot(x, y, style, label = label)
    ax.legend()
    fig.canvas.draw()
    plt.pause(5)