#!/usr/bin/python3 
import sys
import data
import math
import graph
import numpy as np
from scipy.spatial import ConvexHull
data.generate_new_data()
def FindBestAsteroid(fileName = "data/data.txt", debug = False):
    pts = data.loadData(fileName)
    hull = ConvexHull(pts)
    cx, cy, cz = np.average(pts.T[0]), np.average(pts.T[1]), np.average(pts.T[2])# find the center of the cloud
    center = (cx,cy,cz)
    angles = {}
    for v in hull.vertices:#for each vertices
        angles[v]=[]   
        for vv in hull.vertices: #check eacher vertices        
            if v == vv: continue#unless they are the same
            angle = data.find3DAngle(center,pts[v],pts[vv])        
            angles[v].append(angle)#append angle to list of angles

    maxes = {}#find the max angle for each vertices
    for v in hull.vertices:
        maxes[v] = max(angles[v])
    indexOfSmallestAngles = data.findKeyForMinValue(maxes)#find the smallest maximum anlge
    if debug:
        print("The smallest possible field of view is: ", math.degrees(maxes[indexOfSmallestAngles]), "degrees")
        print("The index of the asteroid with the smallest field of view is: ", indexOfSmallestAngles)
        print("The coordinates to the asteroid with the smallest field of view are: ", pts[indexOfSmallestAngles])
        graph.graphIt(pts,hull,indexOfSmallestAngles,center)
    return pts[indexOfSmallestAngles]

if __name__ == '__main__':
    try:
        debug = False
        if len(sys.argv) > 1: 
            if len(sys.argv)>2 and sys.argv[2] == "debug": debug = True
            result = FindBestAsteroid(sys.argv[1],debug=debug)
            print(f"{result[0]} {result[1]}")
        else:            
            result = FindBestAsteroid("data/data3D.txt",debug=True)
            print(result)
    except Exception as e:
        print(e)
        print("Usage: ./main.py <filename> [debug]")
    