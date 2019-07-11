import os, math
import matplotlib.pyplot as plt

def createTriangle():
    plt.figure()
    plt.autoscale(enable=True)
    print([firstPoint(), secondPoint(45,12), thirdPoint(14)])

    t1 = plt.Polygon([firstPoint(), secondPoint(45,12), thirdPoint(14)], closed=False,
                           color="blue", alpha=0.3, fill=True, edgecolor=None)
    plt.gca().add_patch(t1)
    plt.gca().relim()
    plt.gca().autoscale_view()
# update ax.viewLim using the new dataLim

    plt.show()

def firstPoint():
    return (0,0)

def secondPoint(angle, length):
    y = length*math.sin(math.radians(angle))
    x = length*math.cos(math.radians(angle))
    return (x, y)

def thirdPoint(length):
    x = length
    y = 0
    return (x,y)

createTriangle()