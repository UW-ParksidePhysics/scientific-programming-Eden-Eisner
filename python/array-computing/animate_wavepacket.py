import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def f(x, t, alpha, k, v, omega):
    return np.exp(-alpha * (x - v * t)**2) * np.sin(k * x - omega * t)

if __name__ == '__main__':
    x_values = np.linspace(0, 4, 1001)
    t_values = np.linspace(0, 1, 61)
    alpha = 1
    k = 3 * np.pi
    v = 3
    omega = 3 * v

    fig, ax = plt.subplots()
    line, = ax.plot(x_values, f(x_values, t_values[0], alpha, k, v, omega))

    def update(t):
        line.set_ydata(f(x_values, t, alpha, k, v, omega))
        return line,

    ani = animation.FuncAnimation(fig, update, frames=t_values, blit=True)
    ani.save('animation.gif', writer='pillow', fps=6)

    plt.show()