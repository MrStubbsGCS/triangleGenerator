import os, math
import matplotlib.pyplot as plt
import random

def createTriangle(data, data_vars):
    plt.figure()
    plt.autoscale(enable=True)
    print([firstPoint(), secondPoint(float(data[2]),float(data[1])), thirdPoint(float(data[0]))])

    t1 = plt.Polygon([firstPoint(), secondPoint(float(data[2]),float(data[1])), thirdPoint(float(data[0]))], closed=False,
                           color="black", alpha=0.3, fill=False, edgecolor='black')
    t2 = plt.Polygon([firstPoint(),thirdPoint(float(data[0]))], closed=False,
                           color="black", alpha=0.3, fill=False, edgecolor='black')

    for i in range(0, len(data)):
        if data_vars[i] != 0:
            data[i] = data_vars[i]

    plt.annotate("A = " + data[0]+"°", (0.25, 0.25))
    ''' plt.annotate("a = " + data[1], (1, 0.5))
    plt.annotate("B = " + data[2], (1, 0.5))
    plt.annotate("b = " + data[3], (1, 0.5))
    plt.annotate("C = " + data[4], (1, 0.5))
    plt.annotate("c = " + data[5], (1, 0.5))'''
#TODO
    #fix annotate location and data
    #fix angle side combos when drawing

    plt.gca().add_patch(t1)
    plt.gca().add_patch(t2)
    plt.gca().relim()
    plt.gca().autoscale_view()
    plt.axis('off')
# update ax.viewLim using the new dataLim
    randomint = str(random.randint(0,10000))
    plt.savefig("static/temp_triangle_"+randomint+".png")
    file = open("static/temp_triangle_"+randomint+".png")
    #plt.show()

    return file

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

