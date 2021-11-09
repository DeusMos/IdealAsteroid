from os import error
import random
import numpy as np

def generate_new_data(count = 3000):
    generate_data_file2D("data/data2D.txt",count)
    generate_data_file3D("data/data3D.txt",count)

def rngNormal(mean=0, std=100):
    return np.random.normal(mean, std,1)[0]

def generate_data_file2D(filename,count):
    with open(filename, "w") as the_file:       
        the_file.write(f"{count}\n")
        for _ in range(0, count):
            the_file.write(f"{rngNormal(0, 100)} {rngNormal(0,100)}")
            the_file.write("\n")

def generate_data_file3D(filename,count):
    with open(filename, "w") as the_file:       
        the_file.write(f"{count}\n")
        for _ in range(0, count):
            the_file.write(f"{rngNormal(0, 100)} {rngNormal(0,100)} {rngNormal(0,100)}")
            the_file.write("\n")

def add_axis(data):
    mymin, mymax = data.min()/100, data.max()/100 # the new axis will be 1% the magnitude of the original axis
    zs = np.random.normal(mymin, mymax, (len(data),1))# this should make a disk of points
    data = np.concatenate((data, zs), axis=1)
    return data

def conver_2D_to_3D(data):
    data = add_axis(data)
    return data

def find3DAngle(a,b,c):
    ba = a - b
    bc = c - b
    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    return np.arccos(cosine_angle)

def findKeyForMinValue(myDict):
    listofkeys = list(myDict.keys())
    listofvalues = list(myDict.values())
    minvalue = min(listofvalues)
    index = listofvalues.index(minvalue)
    key = listofkeys[index]
    return key

def loadData(filename):
    with open(filename) as f:
        content = f.readlines()
    content.pop(0)
    colCount = int(len(content[0].split(" ")))
    data = np.zeros((len(content),colCount))
    for i in range(0, len(content)):
        try:
            data[i] = np.array(content[i].split(" "))
        except error as e:
            print(f"Error at line {i} {e}")
            data[i] = np.zeros(colCount)
    if data[0,:].shape[0] == 2:
        data = conver_2D_to_3D(data)
    return data

if __name__ == "__main__":


    generate_data_file2D("data2D.txt",1000)
    generate_data_file3D("data3D.txt",1000)
