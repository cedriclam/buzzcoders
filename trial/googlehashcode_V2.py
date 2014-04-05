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

    MatrixInput = [[0] * height for _ in range(width)]
    Matrixtmp = [[0] * height for _ in range(width)]
    MatrixOutput = [['.'] * height for _ in range(width)]
    
    isFirst = True
    i = 0
    for line in lines:
        if isFirst:
            isFirst = False
            continue
        
        j = 0
        while j < height:
            MatrixInput[i][j] = str(line[j])
            Matrixtmp[i][j] = str(line[j])
            j = j + 1
        i = i + 1
    
    i = 0
    j = 0
    while i < width:
        j = 0
        while j < height:
            
            if MatrixInput[i][j] == "#":
                
                iNext = 0
                iNext = i
                jNext = 0
                jNext = j
                #check on the right it's also a X
                while iNext < width:
                    if MatrixInput[iNext][j] != "#": 
                        break
                    iNext = iNext + 1
                
                while jNext < height:
                    if MatrixInput[i][jNext] != "#": 
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
                    
                # check if it is good todo an array
                nbX = 0
                nb0 = 0
                for arrayX in range(i,i+size):
                    for arrayY in range(j,j+size):
                        if (arrayX >= width) or (arrayY >= height) :
                            continue
                        
                        
                        if MatrixInput[arrayX][arrayY] == "#":
                            nbX = nbX + 1
                        else: 
                            nb0 = nb0 + 1
                            
                # add command only if it is relevant to print            
                if nbX > nb0:
                    centerX = i + (size/2) + 1
                    centerY = j + (size/2) + 1
                    S = int(size/2)
                    command = "PAINTSQ "+ str(centerY)+ " "+ str(centerX)+ " "+str(S)+ "\n"
                    print command
                    outputInstruction.append(command)
                    # add in the outputMatrix the point printed
                    for arrayX in range(i,i+size):
                        for arrayY in range(j,j+size):
                            if (arrayX >= width) or (arrayY >= height) :
                                continue
                            
                            MatrixOutput[arrayX][arrayY] = "#"
                            MatrixInput[arrayX][arrayY] = "."
                                
                
            j = j + 1
        i = i + 1
    
    # compare the input and ouput
    i = 0
    j = 0
    while i < width:
        j = 0
        while j < height:
            if Matrixtmp[i][j] != MatrixOutput[i][j]:
                if Matrixtmp[i][j] == '.':
                    command = "ERASECELL "+ str(j)+ " "+ str(i)+ "\n"
                if MatrixInput[i][j] == '.':
                    command = "PAINTSQ "+ str(j)+ " "+ str(i)+ " 0\n"
            
            j =j + 1
        i = i + 1
                
    
    nbInstruction = str(len(outputInstruction))
    outputFile.write(nbInstruction+ "\n")
    for instruction in outputInstruction:
        outputFile.write(instruction)
            
                
                
            
            

    # Close opend file
    inputFile.close()
    pass