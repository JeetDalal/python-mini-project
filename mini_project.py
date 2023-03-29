from tkinter import *

root = Tk()
root.configure(background='light green')
root.title("Registration Form")
root.geometry("1000x700")



#Suduko Algorithm 


'''0 means the cells where no value is assigned'''
grid = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
        [0, 1, 0, 0, 0, 4, 0, 0, 0],
	[4, 0, 7, 0, 0, 0, 2, 0, 8],
	[0, 0, 5, 2, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 9, 8, 1, 0, 0],
	[0, 4, 0, 0, 0, 3, 0, 0, 0],
	[0, 0, 0, 3, 6, 0, 0, 7, 2],
	[0, 7, 0, 0, 0, 0, 0, 0, 3],
	[9, 0, 3, 0, 0, 0, 6, 0, 4]]





	
# else:
# 	print("Solution does not exist:(")

#Button Functionality
def onPressed():
    M = 9
    def puzzle(a):
        for i in range(M):
            for j in range(M):
                print(a[i][j],end = " ")
            print()
    def solve(grid, row, col, num):
        for x in range(9):
            if grid[row][x] == num:
                return False
             
        for x in range(9):
            if grid[x][col] == num:
                return False
 
 
        startRow = row - row % 3
        startCol = col - col % 3
        for i in range(3):
            for j in range(3):
                if grid[i + startRow][j + startCol] == num:
                    return False
        return True 
    def Suduko(grid, row, col):
 
        if (row == M - 1 and col == M):
            return True
        if col == M:
            row += 1
            col = 0
        if grid[row][col] > 0:
            return Suduko(grid, row, col + 1)
        for num in range(1, M + 1, 1): 
     
            if solve(grid, row, col, num):
         
                grid[row][col] = num
                if Suduko(grid, row, col + 1):
                    return True
            grid[row][col] = 0
        return False
    
    if (Suduko(grid, 0, 0)):
        puzzle(grid)
    else:
        print("Solution does not exist:(")
    for i in range(11,20):
	    for j in range(11,20):
		    label[grid_table[f'{i}{j}']].config(text=f'{grid[i-11][j-11]}',font=('20'),borderwidth=3,background='WHITE',highlightthickness=3)
                    


# UI of the App

heading = Label(text='Suduko Solver',font=('times',24))
heading.grid(row=0,column=10,pady=50)

grid_table={}
label={}

for i in range(11,20):
    for j in range(11,20):
        grid_table[f'{i}{j}'] = Canvas(height=50,width=50,bg='WHITE',borderwidth=3,background='WHITE')
        # grid_table[f'{i}{j}'].place_text(text)
#placing on root
button = Button(root,bg='WHITE',text="Solve",borderwidth=5,command=onPressed)
button.grid(row=35,column=10)
for i in range(11,20):
    for j in range(11,20):
        grid_table[f'{i}{j}'].grid(row=i,column=j)


text=""
for i in range(11,20):
	    for j in range(11,20):
                 label[grid_table[f'{i}{j}']]=Label(grid_table[f'{i}{j}'],height=2,width=5, text=f'{grid[i-11][j-11]}' if grid[i-11][j-11] != 0 else "",font=('20'),borderwidth=3,background='WHITE',highlightthickness=3)
                 label[grid_table[f'{i}{j}']].pack()
# can01.grid(row=10,column=10)
			
root.mainloop()
