############################################################
#Name : Sathi.Ranganathan
#Porject : SSH autnentication manager
#date : Feburay,22.2018
############################################################
import os
import sys
import Tkinter as tk

root = tk.Tk()
t = tk.Text(root, height = 10, width = 50,borderwidth=2, relief="groove")
t2 = tk.Text(root, height = 10, width = 50,borderwidth=2, relief="groove")
foo = 1

def countlines(event):
    c = event.widget.index("end-1c")
    a = []
    a = c.split(".")
    labelTwo=tk.Label(root, text = "Number of text in this SMS :" +a[1] + "maximum is 918")
    if (int(a[1]) == 918):
        t.configure(state='disabled')
    labelTwo.place(x=5,y=215)

def action():
    input_text = t.get("1.0","end-1c")
    t2.configure(state='normal')
    n = 160
    g = 0
    a = [input_text[i:i+n] for i in range(0, len(input_text), n)]
    for i in range(0,len(a)):
        g = g+1
        print ("this is your message id : " + str(g) + "\n")
        print ("this is your message: " + a[i] + "\n\n")
        t2.insert("end",("this is your message id : " + str(g) + "\n"))
        t2.insert("end",("this is your message: " + a[i] + "\n\n"))
    t2.configure(state='disabled')

def main():
    #root = tk.Tk()
    root.geometry("525x525")
    root.resizable(False, False)
    menu = tk.Menu(root)
    root.config(menu=menu)

    labelOne=tk.Label(root, text = "Enter the SMS text message:")
    #scroll_1 = Scrollbar(root)
    #t.config(yscrollcommand=scroll_1.set)
    labelOne.place(x=5,y=25)

    t.place(x = 5,y = 50)
    t2.place(x = 5,y = 300)
    t2.configure(state='disabled')
    quote = """Please enter a message"""
    t.insert(tk.END,"")
    t.bind("<KeyRelease>", countlines)
    button = tk.Button(root, height=3,width=12,text='Parse txt Message', command=action)
    button.place(x = 5,y = 225)

    root.mainloop()


if __name__ == '__main__':
  main()
