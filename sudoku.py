def printGrid(grid):
	print("")
	for row in grid:
		rowstring=""
		for square in row:
			rowstring+=square+" "
		print(rowstring)
	print("")

def finished(grid):
	for row in grid:
		for square in row:
			if square=="-":
				return False
	return True

def removeGhosts(grid):
	for i in range(0,9):
		for j in range(0,9):
			if grid[i][j][0]=="N":
				grid[i][j]="-"

def elimNumsInGrid(row,col,grid,options):
	zonei=int(row/3)*3
	zonej=int(col/3)*3
	for i in range(zonei,zonei+3):
		for j in range(zonej,zonej+3):
			num=grid[i][j]
			if num!="-":
				print("removed: "+num)
				options.remove(num)

def findOptions(row,col,grid):
	options=["1","2","3","4","5","6","7","8","9"]
	elimNumsInGrid(row,col,grid,options)
	if len(options)==1:
		grid[row][col]=options[0]
	print(options)

def fillNumber(num,row,col,grid):
	print("Fill "+num+" in Row "+str(row)+", Col "+str(col))
	grid[row][col]=num

def scanZone(i,j,num,grid):
	count=0
	rowpos=-1
	colpos=-1
	for row in range(i,i+3):
		for col in range(j,j+3):
			if grid[row][col]==num:
				return
			if grid[row][col]=="-":
				rowpos=row
				colpos=col
				count+=1
	if count==1:
		fillNumber(num,rowpos,colpos,grid)

def scanGrid(num,grid):
	for i in range(0,3):
		for j in range(0,3):
			zonei=i*3
			zonej=j*3
			scanZone(zonei,zonej,num,grid)

def fillHoriVert(row,col,num,grid):
	for i in range(0,9):
		if grid[row][i]=="-":
			grid[row][i]="N"+num
		if grid[i][col]=="-":
			grid[i][col]="N"+num

def expandGrid(num,grid):
	for i in range(0,9):
		for j in range(0,9):
			if grid[i][j]==num:
				fillHoriVert(i,j,num,grid)

grid=[]

for i in range(0,9):
	row=[]
	for j in range(0,9):
		row=row+["-"]
	grid=grid+[row]

grid[0][0]="7"
grid[0][3]="5"
grid[0][5]="8"

grid[1][2]="9"
grid[1][3]="7"
grid[1][5]="1"
grid[1][6]="3"

grid[2][1]="8"
grid[2][6]="4"
grid[2][8]="1"

grid[3][0]="8"
grid[3][4]="6"
grid[3][7]="1"
grid[3][8]="4"

grid[4][1]="3"
grid[4][2]="7"
grid[4][4]="1"
grid[4][7]="9"

grid[5][1]="9"
grid[5][5]="2"
grid[5][6]="8"

grid[6][1]="2"
grid[6][3]="9"
grid[6][4]="5"
grid[6][7]="4"

grid[7][0]="9"
grid[7][2]="1"
grid[7][5]="7"
grid[7][8]="8"

grid[8][2]="5"
grid[8][3]="1"
grid[8][8]="2"

printGrid(grid)

iterations=0

while not finished(grid) and iterations<100:
	for i in range(1,10):
		expandGrid(str(i),grid)
		scanGrid(str(i),grid)
		removeGhosts(grid)
	iterations+=1

printGrid(grid)
print("Finished in "+str(iterations)+" iterations")
















