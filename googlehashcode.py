'''
Created on Apr 2, 2014

@author: clamoriniere
'''

import sys


if __name__ == '__main__':
    
    sys.stdout.write("start")
    # Open a file
    inputFile = open("doodle.txt", "r")
    outputFile = open("output.txt", "wr")
    print "Name of the file: ", inputFile.name
    
    outputInstruction = list()
 
    lines = inputFile.readlines()
    
    size = lines[0].split(" ")
    width = int(size[0])
    height = int(size[1])
    print "Picture size: " , size[0], "," ,size[1]

    MatrixInput = width*[height*[0]]
    MatrixOutput = width*[height*[0]]
    
    isFirst = True
    i = 0
    for line in lines:
        if isFirst:
            isFirst = False
            continue
        
        j = 0
        while j < height:
            MatrixInput[i][j] = line[j]
            j = j + 1
        i = i + 1
    
    i = 0
    j = 0
    while i < width:
        while j < height:
            if MatrixInput[i][j] == "X":
                iNext = i
                jNext = j
                #check on the right it's also a X
                while iNext < width:
                    if MatrixInput[iNext][j] != "X": 
                        break
                    iNext = iNext + 1
                
                while jNext < height:
                    if MatrixInput[i][jNext] != "X": 
                        break
                    jNext = jNext + 1
                
                zoneWidth = iNext - i
                zoneHeight = jNext - j
                
                if (zoneHeight % 2) == 0:
                    zoneHeight = zoneHeight -1
                    
                if (zoneWidth % 2) == 0:
                    zoneWidth = zoneWidth -1
                
                size = zoneWidth
                if zoneWidth <= zoneHeight:
                    size = zoneHeight
                    
                    # check if it good todo an array
                    nbX = 0
                    nb0 = 0
                    for arrayX in range(i,i+size):
                        for arrayY in range(j,j+size):
                            if MatrixInput[arrayX][arrayY] == "X":
                                nbX = nbX + 1
                            else: 
                                nb0 = nb0 + 1
                    if nbX > nb0:
                        centerX = i + (size/2) + 1
                        centerY = j + (size/2) + 1
                        S = int(size/2)
                        command = "PAINTSQ ", str(centerY), " ", str(centerX), " ",str(S), "\n"
                        outputInstruction.append(object)
                        
                                
                
            j = j + 1
        i = i + 1
    
    nbInstruction = str(len(outputInstruction))
    outputFile.write(nbInstruction+ "\n")
    for instruction in outputInstruction:
        outputFile.write(instruction)
            
                
                
            
            

    # Close opend file
    inputFile.close()
    pass