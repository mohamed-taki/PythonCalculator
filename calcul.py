from tkinter import *
import sys 

#creat the window and its title
root = Tk()
root.title("Calcul herbaaaaaana")

#Set a canvas and its dimensions within the window
canvas = Canvas(root,height=685, width=445, bg="white")
canvas.pack() 

#make the size of the window unchangable
root.resizable(width=False, height=False)

#set the result's frame within the window (as a label for the text)
result = Frame(root,bg="#ffa1b3")
result.place(relwidth=0.98,relheight=0.25, rely = 0.01, relx=0.01)

#Creat an empty variable that'll store the selected buttons's values and one that'll store the last one's length
text_numbers = str()
txt_len= IntVar()

#Creat an array that'll store the buttons's value as numbers and operations
nums = ['1','2','3','4','5','6','7','8','9']
ops = ['-','+','x','÷']
#This is the main function which we'll know via it which button is being pressed, and add take action based on that button's value
def take_action(n):
    global text_numbers
    global txt_len
    txt_len = len(text_numbers)
    #txt_len = len(text_numbers)
    #check if the pressed button is a text that containes a number or an operation
    if n in nums or n in ops: 
        if txt_len == 28 or txt_len==57 or txt_len == 86:
            text_numbers+="\n"+n
            change_nums(text_numbers)   
        #to check if the user has passed the limits of possible text
        elif txt_len >=115:
            return    
        else:
            text_numbers += str(n)
            change_nums(text_numbers)       
            print(len(text_numbers))
    elif n == "<":
        text_numbers = text_numbers[:-1] #remove the last number from the text
        clear_text()
        change_nums(text_numbers)

    elif n =="ac":
        text_numbers=""
        clear_text()
    
    elif n == "=":
        Equal()

#This fucntion will change the text in the text label
def change_nums(tn):
    global txt_len
    #To avoid bugs, we should use a fresh and clean text label
    clear_text()
    if tn != "" or len(tn) > 0:
        if txt_len <28:
            text_label = Label(result, text=tn, height=2, font=("Arial",20), padx=10, bg = "black", fg="white", justify=LEFT)
        if txt_len >= 28 and txt_len < 57: 
            text_label = Label(result, text=tn, height=3, font=("Arial",20), padx=10, bg = "black", fg="white", justify=LEFT)
        elif txt_len >= 57 and txt_len <86: 
            text_label = Label(result, text=tn, height=4, font=("Arial",20), padx=10, bg = "black", fg="white", justify=LEFT)
        elif txt_len >= 86: 
            text_label = Label(result, text=tn, height=5, font=("Arial",20), padx=10, bg = "black", fg="white", justify=LEFT)
        text_label.place(x=0, y = 0) 
    else:
        clear_text()

#This function will clear the preior data/text in the text label
def clear_text():
    for widget in result.winfo_children():
        widget.destroy()

#An equal function to calculate the result of the text in the text area
#Also note that the name is diffrent from the var's name which has a small "e" but the function has a capitale one
def Equal():
    global text_numbers
    #Verify that the text has at least one possible operation in it
    for i in range(len(str(text_numbers))):
        if not(text_numbers[i] in ops) and not(text_numbers[i] in nums):
            return
    #to change the uncountable characters
    text_numbers = text_numbers.replace('÷', '/')
    text_numbers = text_numbers.replace('x', '*')
    change_nums(eval(text_numbers)) #the eval function helps us with calculating the given text from "text_numbers" and stored in "res"
    text_numbers = ""

#set buttons

    #Numbers

num1 = Button(root, text="1", padx=25, pady=10, font=("Arial", 30),bg="#B2B5DB",
                                    command=lambda m="1": take_action(m))
num1.place(x=0,y=282)

num2 = Button(root, text="2", padx=25, pady=10, font=("Arial", 30),bg="#B2B5DB",
                                    command=lambda m="2": take_action(m))
num2.place(x=110,y=282)

num3 = Button(root, text="3", padx=25, pady=10, font=("Arial", 30),bg="#B2B5DB",
                                    command=lambda m="3": take_action(m))
num3.place(x=220,y=282)

num4 = Button(root, text="4", padx=25, pady=10, font=("Arial", 30),bg="#B2B5DB",
                                    command=lambda m="4": take_action(m))
num4.place(x=0,y=382)

num5 = Button(root, text="5", padx=25, pady=10, font=("Arial", 30),bg="#B2B5DB",
                                    command=lambda m="5": take_action(m))
num5.place(x=110,y=382)

num6 = Button(root, text="6", padx=25, pady=10, font=("Arial", 30),bg="#B2B5DB",
                                    command=lambda m="6": take_action(m))
num6.place(x=220,y=382)

num7 = Button(root, text="7", padx=25, pady=10, font=("Arial", 30),bg="#B2B5DB",
                                    command=lambda m="7": take_action(m))
num7.place(x=0,y=482)

num8 = Button(root, text="8", padx=25, pady=10, font=("Arial", 30),bg="#B2B5DB",
                                    command=lambda m="8": take_action(m))
num8.place(x=110,y=482)

num9 = Button(root, text="9", padx=25, pady=10, font=("Arial", 30),bg="#B2B5DB",
                                    command=lambda m="9": take_action(m))
num9.place(x=220,y=482)

num0 = Button(root, text="0", padx=75, pady=10, font=("Arial", 30),bg="#B2B5DB",
                                    command=lambda m="0": take_action(m))
num0.place(x=0,y=582)

    #Operations

equal = Button(root, text="=", padx=91, pady=10, font=("Arial", 30),bg="#E8C341",
                                    command=lambda m="=": take_action(m))
equal.place(x=210,y=582)

plus = Button(root, text="+", padx=30, pady=10, font=("Arial", 30),bg="#E8C341",
                                    command=lambda m="+": take_action(m))
plus.place(x=330,y=382)

div = Button(root, text="÷", padx=30, pady=10, font=("Arial", 30),bg="#E8C341",
                                    command=lambda m="÷": take_action(m))
div.place(x=330,y=282)

minus = Button(root, text="-", padx=35, pady=10, font=("Arial", 30),bg="#E8C341",
                                    command=lambda m="-": take_action(m))
minus.place(x=330,y=482)

mult = Button(root, text="x", padx=37, pady=15, font=("Arial", 25),bg="#E8C341",
                                    command=lambda m="x": take_action(m))
mult.place(x=330,y=182)

delete = Button(root, text="<==", padx=11, pady=15, font=("Arial", 25),bg="#e36464",
                                    command=lambda m="<": take_action(m))
delete.place(x=220,y=182)

ac = Button(root, text="AC", padx=70, pady=15, font=("Arial", 25),bg="#e36464",
                                    command=lambda m="ac": take_action(m))
ac.place(x=0,y=182)


#load the app icone from the same path as the script file
root.iconbitmap(default=sys.path[0]+"/app_icone.ico")

#Keep the app running untill the user closes it
root.mainloop()

#2021/09/21 7:27 AM
#DONE by Mohamed Taki
#insta : @itsmeyukki