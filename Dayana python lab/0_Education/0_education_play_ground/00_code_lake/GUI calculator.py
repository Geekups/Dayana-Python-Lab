#A library for building graphical interfaces
from tkinter import *

# The value displayed in the text entry box
expression = "" 


# To update expression in the text entry box
def press(item):
    
    # 'global' to change the variable throughout the code
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# To evaluate the final expression
def Equal_press():

    try:
        global expression
        
        # 'eval' is for parsing strings
        analyze = str(eval(expression))
        input_text.set(analyze)

        expression = ""
    
    except:
 
        input_text.set(" error ")
        expression = ""
 
# To clear values in the text entry box
def clear():
    global expression
    expression = ""
    input_text.set("")


if __name__ == "__main__":

    # create a GUI windows
    root = Tk()

    root.title("GUI calculator")

    root.geometry("300x400")

    root.configure(background="#eef4f8")
    # StringVar() is a varible class we create an instance of this class
    input_text = StringVar()

    entry_box = Entry(root, textvariable = input_text)
    entry_box.grid(columnspan= 4, ipadx= 100,ipady= 5,pady=4)
    
    # "Buttons 1 to 9" represent calculator numbers

    button1 = Button(root, text = " 1 ", fg = "black", bg = "#6dbfb8", command = lambda: press(1), height = 3, width = 10 )
    button1.grid(row = 2, column = 0 )
    
    button2 = Button(root, text = " 2 ", fg = "black", bg = "#6dbfb8", command = lambda: press(2), height = 3, width = 10 )
    button2.grid(row = 2, column = 1 )

    button3 = Button(root, text = " 3 ", fg = "black", bg = "#6dbfb8", command = lambda: press(3), height = 3, width = 10 )
    button3.grid(row = 2, column = 2 )

    button4 = Button(root, text = " 4 ", fg = "black", bg = "#6dbfb8", command = lambda: press(4), height = 3, width = 10 )
    button4.grid(row = 3, column = 0 )

    button5 = Button(root, text = " 5 ", fg = "black", bg = "#6dbfb8", command = lambda: press(5), height = 3, width = 10 )
    button5.grid(row = 3, column = 1 )

    button6 = Button(root, text = " 6 ", fg = "black", bg = "#6dbfb8", command = lambda: press(6), height = 3, width = 10 )
    button6.grid(row = 3, column = 2 )

    button7 = Button(root, text = " 7 ", fg = "black", bg = "#6dbfb8", command = lambda: press(7), height = 3, width = 10 )
    button7.grid(row = 4, column = 0 )

    button8 = Button(root, text = " 8 ", fg = "black", bg = "#6dbfb8", command = lambda: press(8), height = 3, width = 10 )
    button8.grid(row = 4, column = 1 )

    button9 = Button(root, text = " 9 ", fg = "black", bg = "#6dbfb8", command = lambda: press(9), height = 3, width = 10 )
    button9.grid(row = 4, column = 2 )

    button0 = Button(root, text = " 0 ", fg = "black", bg = "#6dbfb8", command = lambda: press(0), height = 3, width = 10 )
    button0.grid(row = 5, column = 0 )
    
    # Four operation buttons

    plus = Button(root, text = " + ", fg = "black", bg = "#f5f200", command = lambda: press("+"), height = 3, width = 10 )
    plus.grid(row = 5, column = 1 )
    
    minus = Button(root, text = " - ", fg = "black", bg = "#f5f200", command = lambda: press("-"), height = 3, width = 10 )
    minus.grid(row = 5, column = 2 )
    
    mult = Button(root, text = " * ", fg = "black", bg = "#f5f200", command = lambda: press("*"), height = 3, width = 10 )
    mult.grid(row = 6, column = 0 )
    
    divid = Button(root, text = " / ", fg = "black", bg = "#f5f200", command = lambda: press("/"), height = 3, width = 10 )
    divid.grid(row = 6, column = 1 )

    equal = Button(root, text = " = ", fg = "black", bg = "#75ba75", command = Equal_press, height = 3, width = 10 )
    equal.grid(row = 6, column = 2 )
    
    # 'cl' is to clear values in the text entry box
    cl = Button(root, text = " clear ", fg = "black", bg = "#eef4f8", command = clear, height = 3, width = 10 )
    cl.grid(row = 7, column = 2 )

    # auditor button
    decimal = Button(root, text = " . ", fg = "black", bg = "#f5f200", command = lambda: press("."), height = 3, width = 10 )
    decimal.grid(row = 7, column = 1 )
    
    # start the GUI
    root.mainloop()
