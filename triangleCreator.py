import os, math
import matplotlib.pyplot as plt
import random

def createTriangle(data):
    plt.figure()
    plt.autoscale(enable=True)
    print([firstPoint(), secondPoint(float(data[2]),float(data[3])), thirdPoint(float(data[5]))])

    t1 = plt.Polygon([firstPoint(), secondPoint(float(data[2]),float(data[3])), thirdPoint(float(data[5]))], closed=False,
                           color="black", alpha=0.3, fill=False, edgecolor='black')
    t2 = plt.Polygon([firstPoint(),thirdPoint(float(data[5]))], closed=False,
                           color="black", alpha=0.3, fill=False, edgecolor='black')
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

