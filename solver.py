import time
def solver(grid):
    start = time.process_time() #start timer
    lastPrint = start
    toSolve=[] #list of values to modify
    for y in range(9):
        for x in range(9):
            if(grid[y][x]==0): 
                toSolve.append([y,x]) #add values to solve for
    toSolve = tuple(toSolve)
    solveIndex = 0 #coordinate from the toSolve to start guessing
    while 1:
        if(time.process_time()-lastPrint>printTimer):
            lastPrint=time.clock()
            printGrid(grid)
            print("Solving...")
        current = toSolve[solveIndex]
        if(grid[current[0]][current[1]]<9):
            grid[current[0]][current[1]]+=1 #increment value
            """--------------------------------------------------------------------"""
            """--------------------------------------------------------------------"""
            """--------------------------------------------------------------------"""
            ##########
            #scan row#
            ##########
            count=0 #counts how many times the value guessed appears in the row
            for val in grid[current[0]]: #scan row
                if(val==grid[current[0]][current[1]]): #if found value in row
                    count+=1 
            if(count!=1): #if value appears more than once (should appear once in its own row)
                continue #continue to loop to increment value

            #############
            #scan column#
            #############
            count = 0 #reset counter
            for x in range(9): #scan column
                if(grid[x][current[1]]==grid[current[0]][current[1]]): #if found value in column
                    count+=1 
            if(count!=1): #if value appears more than once (should appear once in its own column)
                continue #continue to loop to increment value

            ##########
            #scan box#
            ##########
            count = 0 #reset counter
            boxY = int(current[0]/3) #gets the box Y index from 0,1,2
            boxX = int(current[1]/3) #gets the box X index from 0,1,2
            for y in range(3):
                for x in range(3):
                    if(grid[boxY*3+y][boxX*3+x] == grid[current[0]][current[1]]):
                        count+=1
            if(count!=1): #if value appears more than once (should appear once in its own box)
                continue #continue to loop to increment value

            #############
            #scan knight#
            #############
            count = 0 #reset counter
            possibleMoves=[[-2,1],[-2,-1],
                           [2,1],[2,-1],
                           [1,2],[1,-2],
                           [-1,2],[-1,-2]]
            for move in possibleMoves:
                #ignore index out of bounds moves
                    #check if y is between and including 0-8          check if x is between and including 0-8
                if(move[0]+current[0]>=0 and move[0]+current[0]<9 and move[1]+current[1]>=0 and move[1]+current[1]<9):
                    if(grid[current[0]+move[0]][current[1]+move[1]]==grid[current[0]][current[1]]): #if found value in move
                        count+=1 
            if(count>0): #if value appears, not doing 1 since the tiles checked doesnt include the tile in question
                continue #continue to loop to increment value
                
            ###############
            #scan diagonal#
            ###############
            count = 0 #reset counter
            if(current[0]==current[1]):#see if the coordinate is on the diagonal
                diagonal0= [[0,0],
                            [1,1],
                            [2,2],
                            [3,3],
                            [4,4],
                            [5,5],
                            [6,6],
                            [7,7],
                            [8,8]]
                for coord in diagonal0:
                    if(grid[current[0]][current[1]] == grid[coord[0]][coord[1]]):
                        count+=1
                if(count!=1): #if value appears, not doing 1 since the tiles checked doesnt include the tile in question
                    continue #continue to loop to increment value
            count = 0 #reset counter
            #the condition "current[0]==8-current[1]" takes a whole crap ton of time to run for some reason
            #as of Python 3.7.4
            if(current[0]==8-current[1]):#see if the coordinate is on the diagonal
                diagonal1= [[0,8],
                            [1,7],
                            [2,6],
                            [3,5],
                            [4,4],
                            [5,3],
                            [6,2],
                            [7,1],
                            [8,0]]
                for coord in diagonal1:
                    if(grid[current[0]][current[1]] == grid[coord[0]][coord[1]]):
                        count+=1
                if(count!=1): #if value appears, not doing 1 since the tiles checked doesnt include the tile in question
                    continue #continue to loop to increment value
            """--------------------------------------------------------------------"""
            """--------------------------------------------------------------------"""
            """--------------------------------------------------------------------"""
            
            #if succeeded all checks
            solveIndex+=1 #move to next index
            backTrack=0 #reset backtrack counter
            if(solveIndex>=len(toSolve)): #finished solving
                timeMs = (time.process_time()-start)*1000 
                printGrid(grid)
                print(f"Done in {timeMs:.5f} milliseconds")
                return
        else:
            if(solveIndex==0):
                timeMs = (time.process_time()-start)*1000 
                printGrid(grid)
                print(f"No solution found in {timeMs:.5f} milliseconds")
                break;
            grid[current[0]][current[1]] = 0
            solveIndex-=1
            backTrack+=1 #how many times needed to backtrack
                
def printGrid(grid):
    for y in range(9):
        for x in range(9):
            if(x==3 or x==6):
                print("|",end="")
            if(x==0 and (y==3 or y==6)):
                print("\n-----------")
            elif(x==0):
                print("")
            print(grid[y][x],end="")
    print("")



printTimer = 10

grid=[[0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0]]


    
solver(grid)
