'''
Created on Apr 2, 2014

@author: clamoriniere
'''

import sys


if __name__ == '__main__':
    
    # Open a file
    inputFile = open("doodle.txt", "r")
    
    outputInstruction = list()
 
    lines = inputFile.readlines()
    
    size = lines[0].split(" ")
    width = int(size[0])
    height = int(size[1])

    MatrixInput = width*[height*['0']]
    MatrixInput = [[0] * height for _ in range(width)]
    MatrixOutput = width*[height*['0']]
    
    isFirst = True
    i = 0
    for line in lines:
        if isFirst:
            isFirst = False
            continue
        
        j = 0
        while j < height:
            MatrixInput[i][j] = str(line[j])
            j = j + 1
        i = i + 1
    i = 0
    j = 0
    o = 0
    mstr = ""
    while i < width:
	j = 0;
        while j < height:
	    if MatrixInput[i][j] == '#':
		if (o != 0):
		    mstr += '\n'	
            	mstr += "PAINTSQ " + str(i) + " " + str(j) + " 0"
		o += 1
	    j += 1
	i += 1
    print(o)
    print(mstr)
            

    # Close opend file
    inputFile.close()
    pass
