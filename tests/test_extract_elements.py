import matplotlib.pyplot as plt
from matplotlib_extract import extract_elements

import numpy as np
from os import path


def test_extract_elements():
    # build
    x = np.linspace(0, 2*np.pi)
    y1 = 2*x
    y2 = 6 + 2*np.sin(x)

    plt.plot(x, y1, label="1")
    plt.plot(x, y2)
    plt.legend(loc="lower right")

    # run
    extract_elements()

    # test
    assert path.exists("axes.png")
    assert path.exists("legend_0.png")
    assert path.exists("line_0.png")
    assert path.exists("line_1.png")