# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 23:50:13 2019

@author: TEEE
"""
key=5
#list={'a':[3,3,2],'b':[2,3,2],'c'=[1,2,3],'d'=[1,2,1],'e'=[1,1,1],'f'=[3,1,1],'g'=[3,1,2],'h'=[3,3,1],'i'=[3,2,2],'j'=[3,2,3],'h'=[3,3,1],'i'=[3,2,2],'j'=[3,2,3],'k'=[2,2,2],'l'=[2,2,1],'m'=[2,1,1],'n'=[2,3,1],'o'=[3,1,3],'p'=[1,1,2],'q'=[3,3,3],'r'=[3,2,1],'s'=[1,1,3],'t'=[2,3,3],'u'=[1,2,2],'v'=[1,3,1],'w'=[1,3,2],'x'=[2,2,3],'y'=[1,3,3],'z'=[2,1,3],'.'=[2,1,2]}
lis= {'a':[3,3,2],'b':[2,3,2],'c':[1,2,3],'d':[1,2,1],'e':[1,1,1],'f':[3,1,1],'g':[3,1,2],'h':[3,3,1],'i':[3,2,2],'j':[3,2,3],'h':[3,3,1],'i':[3,2,2],'j':[3,2,3],'k':[2,2,2],'l':[2,2,1],'m':[2,1,1],'n':[2,3,1],'o':[3,1,3],'p':[1,1,2],'q':[3,3,3],'r':[3,2,1],'s':[1,1,3],'t':[2,3,3],'u':[1,2,2],'v':[1,3,1],'w':[1,3,2],'x':[2,2,3],'y':[1,3,3],'z':[2,1,3],'.':[2,1,2]}
def encode_input(text,key):
    encoded=""
    for i in range(0,len(text),key):
        encoded+=parse_key(text[i:i+key])
    print(encoded)

def parse_key(inp):
    cyp=""
    out=""
    for i in range(3):
        for j in inp:
            cyp+=str(lis[j][i])
    for k in range(0,len(cyp),3):
        out+=str(list(lis.keys())[list(lis.values()).index([int(cyp[k]),int(cyp[k+1]),int(cyp[k+2])])])
    return out
        
#print(list(lis.keys())[list(lis.values()).index([3,3,2])])
    
def decode_key(enc,key):
    intermediate=""
    for i in enc:
        for j in range(3):
            intermediate+= str(lis[i][j])
    print(intermediate)
    

