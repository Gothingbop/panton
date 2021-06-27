from matplotlib import pyplot as plt
from matplotlib.patches import PathPatch
from matplotlib.path import Path
import numpy as np
import json
import pathlib

with open(pathlib.Path(__file__).parent.absolute() / "colors" / "blues.json") as _:
    colors = np.array(json.load(_)[1:])


def half_circle(x_center, y_center, radius, flip: int = 0):
    x = np.linspace(x_center - radius, x_center + radius, 10000)
    y = (-1) ** flip * np.sqrt(radius ** 2 - (x - x_center) ** 2) + y_center
    return x, y


if __name__ == '__main__':
    fig, ax = plt.subplots()
    n_circles = len(colors)
    for i in range(4):
        for j in range(n_circles-1):
            x_0, y_0 = half_circle((n_circles+1)*i, 0, j+1, i % 2)
            x_1, y_1 = half_circle((n_circles+1)*i, 0, j+2, i % 2)
            x = np.hstack([x_0, x_1[::-1]])
            y = np.hstack([y_0, y_1[::-1]])
            vertices = np.array([x, y]).T

            codes = [Path.LINETO]*vertices.shape[0]
            codes[0] = Path.MOVETO

            path = Path(vertices, codes)
            ax.plot(x, y, alpha=0)
            ax.add_patch(PathPatch(
                path,
                facecolor=colors[abs((n_circles-2)*(i % 2) - j)],
                edgecolor='none',
                alpha=1,
                antialiased=False
            ))
    ax.set_facecolor(colors[len(colors)//2])
    ax.set_xlim(0, 20)
    ax.set_ylim(-10, 10)
    fig.set_size_inches(96, 96)
    plt.axis("off")
    fig.savefig(
        './results/blue',
        bbox_inches='tight',
        pad_inches=0,
        facecolor=colors[len(colors)//2],
        transparent=False
    )

