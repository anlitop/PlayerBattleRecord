import numpy as np
import numpy as np 
from matplotlib import pyplot as plt


def draw(x,y,title="图表"):
    plt.title(title)
    plt.plot(x,y,"ob")
    plt.show()
