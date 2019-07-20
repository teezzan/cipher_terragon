# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 15:21:27 2019

@author: TEEE
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 14:29:31 2019

@author: TEEE
"""

from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
import base64
lis= {'a':[3,3,2],'b':[2,3,2],'c':[1,2,3],'d':[1,2,1],'e':[1,1,1],'f':[3,1,1],'g':[3,1,2],'h':[3,3,1],'i':[3,2,2],'j':[3,2,3],'h':[3,3,1],'i':[3,2,2],'j':[3,2,3],'k':[2,2,2],'l':[2,2,1],'m':[2,1,1],'n':[2,3,1],'o':[3,1,3],'p':[1,1,2],'q':[3,3,3],'r':[3,2,1],'s':[1,1,3],'t':[2,3,3],'u':[1,2,2],'v':[1,3,1],'w':[1,3,2],'x':[2,2,3],'y':[1,3,3],'z':[2,1,3],' ':[2,1,2]}

window = Tk()
window.title("Ciphering app")
window.geometry('300x100')
lbl = Label(window, text="Input your word")
lbl.grid(column=0, row=0)
txt = Entry(window,width=20)
txt.grid(column=1, row=0)


out = Label(window, text="")
out.grid(column=1, row=4)
out_label = Label(window, text="Output: ")
out_label.grid(column=0, row=4)



def clicked():
    if (selected.get()==0):
        res=encode_input(txt.get().lower())
        out.configure(text= res)
#        txt.insert(INSERT,res)
    elif(selected.get()==1):
        res=decode_input(txt.get())
        out.configure(text= res)
#        txt.insert(INSERT,res)
def encode_input(text,key=5):
        encoded=""
        text=text.lower()
        for i in range(0,len(text),key):
            encoded+=encode_key(text[i:i+key])
        print("bse64:"+str(base64.b64encode(str.encode(encoded))))
        te=str(base64.b64encode(str.encode(encoded)))
        return te[2:len(te)-1]

def encode_key(inp):
    cyp=""
    out=""
    
    for i in range(3):
        for j in inp:
            cyp+=str(lis[j][i])
    for k in range(0,len(cyp),3):
        out+=str(list(lis.keys())[list(lis.values()).index([int(cyp[k]),int(cyp[k+1]),int(cyp[k+2])])])
    #return base64.b64encode(str.encode(out))#out
    return out

def decode_input(text,key=5):
#    print("init",text)
    te=str(text)
    te=str(base64.b64decode(str.encode(te)))
#    print("")
#    print("te real:"+te)
    te=str(te)
    te=te[2:len(te)-1]
    text=te
#    print("TXT:",text)
    decoded=""
    
    for i in range(0,len(text),key):
        decoded+=decode_key(text[i:i+key])
    return decoded

    
def decode_key(enc,key=5):
#    print(enc)
    cyp=""
    dec=""
    for i in enc:
        for j in range(3):
            cyp+= str(lis[i][j])
#    print(cyp)
    itr=int(len(cyp)/3)
    for i in range(0,itr):
#        for k in range(i,(2*i)+1,itr):
        dec+=str(list(lis.keys())[list(lis.values()).index([int(cyp[i]),int(cyp[i+itr]),int(cyp[i+(2*itr)])])])
#    print (dec)
    return dec 
     
btn = Button(window, text="GO", command=clicked)
btn.grid(column=3, row=0)
#txt = scrolledtext.ScrolledText(window,width=20,height=5)
#txt.grid(column=0,row=0)
selected = IntVar()
rad1 = Radiobutton(window,text='Cipher', value=0, variable=selected)
rad2 = Radiobutton(window,text='Decipher', value=1, variable=selected)
rad1.grid(column=0, row=3)
rad2.grid(column=1, row=3)
window.mainloop()