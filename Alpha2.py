'''
Created on Mar 22, 2019

@author: s271486
'''
from tkinter import *

import time 

root = Tk()

root.title("Alphabet")

Letters = Label(root)

for outerCounter in range(65, 91):
    for innerCounter in range(97, 123):
        
        #create the letters
        upper = chr(outerCounter)
        
        lower = chr(innerCounter)
        
        Letters = Label(text= str(upper) +"=>" + str(lower))
        
        #pack and refresh
        Letters.pack()
        time.sleep(.8)
        root.update_idletasks()
        root.update()
        Letters.pack_forget()

root.mainloop() 