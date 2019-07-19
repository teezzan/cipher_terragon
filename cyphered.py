            
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
Ui_MainWindow, QtBaseClass = uic.loadUiType("cypherUI.ui")

lis= {'a':[3,3,2],'b':[2,3,2],'c':[1,2,3],'d':[1,2,1],'e':[1,1,1],'f':[3,1,1],'g':[3,1,2],'h':[3,3,1],'i':[3,2,2],'j':[3,2,3],'h':[3,3,1],'i':[3,2,2],'j':[3,2,3],'k':[2,2,2],'l':[2,2,1],'m':[2,1,1],'n':[2,3,1],'o':[3,1,3],'p':[1,1,2],'q':[3,3,3],'r':[3,2,1],'s':[1,1,3],'t':[2,3,3],'u':[1,2,2],'v':[1,3,1],'w':[1,3,2],'x':[2,2,3],'y':[1,3,3],'z':[2,1,3],' ':[2,1,2]}


class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.encypher_btn.clicked.connect(self.enc)
        self.ui.decypher_btn.clicked.connect(self.dec)
#        self.ui.confirm.clicked.connect(self.encode_input)
#        self.ui.connect.clicked.connect(self.decode_key)
        

    def enc(self):
        print(self.encode_input(self.ui.input.toPlainText()))
        self.ui.output.setText(self.encode_input(self.ui.input.toPlainText()))
        
    def dec(self):
        print(self.decode_input(self.ui.input.toPlainText()))
        self.ui.output.setText(self.decode_input(self.ui.input.toPlainText()))
    
    def encode_input(self,text,key=5):
        encoded=""
        for i in range(0,len(text),key):
            encoded+=self.encode_key(text[i:i+key])
        return encoded

    def encode_key(self,inp):
        cyp=""
        out=""
        for i in range(3):
            for j in inp:
                cyp+=str(lis[j][i])
        for k in range(0,len(cyp),3):
            out+=str(list(lis.keys())[list(lis.values()).index([int(cyp[k]),int(cyp[k+1]),int(cyp[k+2])])])
        return out
        
    #print(list(lis.keys())[list(lis.values()).index([3,3,2])])
    
    def decode_input(self,text,key=5):
        decoded=""
        for i in range(0,len(text),key):
            decoded+=self.decode_key(text[i:i+key])
        return decoded

        
    def decode_key(self,enc,key=5):
        print(enc)
        cyp=""
        dec=""
        for i in enc:
            for j in range(3):
                cyp+= str(lis[i][j])
        print(cyp)
        itr=int(len(cyp)/3)
        for i in range(0,itr):
    #        for k in range(i,(2*i)+1,itr):
            dec+=str(list(lis.keys())[list(lis.values()).index([int(cyp[i]),int(cyp[i+itr]),int(cyp[i+(2*itr)])])])
        print (dec)
        return dec 

        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

