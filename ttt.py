from tkinter import *
# to display message to user, e.g. "you won!"
from tkinter import messagebox
# to style tkinter widget 
from tkinter import ttk  

#creates main tkinter window
root = Tk()
root.title('Tic Tac Toe Game')


# Determines who goes first 
# If clicked is TRUE, X will go. 
# If clicked is FALSE, O will go. 
# clicked = True # X goes first 
#count = 0

# disable all the butttons 
def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

# Check to see if someone won 
def checkifwon():
    global winner 
    winner = False 

    # check for X wins 
    # Top Row 
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":    
        b1.config(highlightbackground="blue") #change color of buttons to highlight win
        b2.config(highlightbackground="blue")
        b3.config(highlightbackground="blue") 
        winner = True   
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X Wins")
        disable_all_buttons()
    
    # Midddle Row 
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(highlightbackground="blue") #change color of buttons to highlight win
        b5.config(highlightbackground="blue") 
        b6.config(highlightbackground="blue")       
        winner = True 
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X Wins")
        disable_all_buttons()
    # Last Row 
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(highlightbackground="blue")  #change color of buttons to highlight win
        b8.config(highlightbackground="blue") 
        b9.config(highlightbackground="blue")       
        winner = True 
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X Wins")
        disable_all_buttons()
    # First Col
    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(highlightbackground="blue")    #change color of buttons to highlight win
        b4.config(highlightbackground="blue")    
        b7.config(highlightbackground="blue")       
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X Wins")
        disable_all_buttons()
    # Middle Col
    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(highlightbackground="blue")   #change color of buttons to highlight win
        b5.config(highlightbackground="blue")    
        b8.config(highlightbackground="blue")         
        winner = True 
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X Wins")
        disable_all_buttons()
    # Last Col
    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(highlightbackground="blue")  #change color of buttons to highlight win
        b6.config(highlightbackground="blue")    
        b9.config(highlightbackground="blue")          
        winner = True 
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X Wins")
        disable_all_buttons()
    # Diagonal 1
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(highlightbackground="blue") #change color of buttons to highlight win
        b5.config(highlightbackground="blue")    
        b9.config(highlightbackground="blue")          
        winner = True 
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X Wins")
        disable_all_buttons()
    # Diagonal 2
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(highlightbackground="blue") #change color of buttons to highlight win
        b5.config(highlightbackground="blue")    
        b7.config(highlightbackground="blue")           
        winner = True 
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X Wins")
        disable_all_buttons()
    
    #Check for O wins 
    # Top Row 
    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(highlightbackground="blue") #change color of buttons to highlight win
        b2.config(highlightbackground="blue")    
        b3.config(highlightbackground="blue")           
        winner = True 
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O Wins")
        disable_all_buttons()
    # Midddle Row 
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(highlightbackground="blue") #change color of buttons to highlight win
        b5.config(highlightbackground="blue")    
        b6.config(highlightbackground="blue")           
        winner = True 
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O Wins")
        disable_all_buttons()
    # Last Row 
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(highlightbackground="blue") #change color of buttons to highlight win
        b8.config(highlightbackground="blue")    
        b9.config(highlightbackground="blue")        
        winner = True 
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O Wins")
        disable_all_buttons()
    # First Col
    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(highlightbackground="blue") #change color of buttons to highlight win
        b4.config(highlightbackground="blue")    
        b7.config(highlightbackground="blue")           
        winner = True 
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O Wins")
        disable_all_buttons()
    # Middle Col
    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(highlightbackground="blue") #change color of buttons to highlight win
        b5.config(highlightbackground="blue")    
        b8.config(highlightbackground="blue")         
        winner = True 
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O Wins")
        disable_all_buttons()
    # Last Col
    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(highlightbackground="blue") #change color of buttons to highlight win
        b6.config(highlightbackground="blue")    
        b9.config(highlightbackground="blue")       
        winner = True 
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O Wins")
        disable_all_buttons()
    # Diagonal 1
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(highlightbackground="blue") #change color of buttons to highlight win
        b5.config(highlightbackground="blue")    
        b9.config(highlightbackground="blue")    
        winner = True 
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O Wins")
        disable_all_buttons()
    # Diagonal 2
    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(highlightbackground="blue")  #change color of buttons to highlight win
        b5.config(highlightbackground="blue")    
        b7.config(highlightbackground="blue")        
        winner = True 
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O Wins")
        disable_all_buttons()
    # Check if tie 
    if count == 9 and winner == False:
        messagebox.showinfo("Tic Tac Toe", "It's A Tie!")
        disable_all_buttons()
    




# Check if button is clicked 
def b_click(b):
    # keeps track of variables above inside function
    global clicked, count 

    # If button is empty and it's X's turn 
    if b["text"] == " " and clicked == True: 
        b["text"] = "X"
        clicked = False # O's turn 
        count += 1 # keep track of moves 
        checkifwon()
    elif b["text"] == " " and clicked == False: 
        b["text"] = "O"
        clicked = True # X's turn 
        count += 1 # keep track of moves
        checkifwon() 
    else:
        messagebox.showerror("Tic Tac Toe", "That box has already been selected\nPick another Box...") 

#start game over 
def reset():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    global clicked, count 
    clicked = True
    count = 0
# Build Buttons 
    # Need 9 buttons for Grid 
    b1 = Button(root, text=" " , font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b1)) 
    b2 = Button(root, text=" " , font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b2)) 
    b3 = Button(root, text=" " , font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b3)) 
    b4 = Button(root, text=" " , font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b4)) 
    b5 = Button(root, text=" " , font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b5)) 
    b6 = Button(root, text=" " , font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b6)) 
    b7 = Button(root, text=" " , font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b7)) 
    b8 = Button(root, text=" " , font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b8)) 
    b9 = Button(root, text=" " , font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b9)) 
    # Grid our buttons to the screen 
    # grid() puts widgets in a 2-D table. Row, Column, Padding
    # COLUMN
    # 0  1  2 
    # b1 b2 b3 0 R 
    # b4 b5 b6 1 O 
    # b7 b8 b9 2 W
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)
    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)
    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)


#Create menu 
my_menu = Menu(root)
root.config(menu=my_menu)

#create options menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options",menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset)

reset()
# Puts everything on display 
# Infinate loop, responds to user input until the program terminates 
root.mainloop()
