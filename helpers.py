import os 
def gotoxy(x,y):
    print("%c[%d;%df"%(0x1B,y,x),end="")

def borrar_Pantalla():
    os.system("cls")

def mesaje(msg):
    pass