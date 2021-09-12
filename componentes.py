from helpers import gotoxy
import time
class Menu:
    def __init__(self, titulo="", opciones=[], col=6, fila=1):
        self.titulo = titulo
        self.opciones = opciones
        self.col = col
        self.fila = fila
    def menu(self):
        gotoxy(self.col, self.fila); print(self.titulo)
        self.col -=5
        for opciones in self.opciones:
            self.fila += 1
            gotoxy(self.col, self.fila); print(opcion)
        gotoxy(self.col+5, self.fila+2)
        opc = input("Elija opcion[1...{}]:".format(len(self.opciones)))
        return opc

class Valida:
    def solo_numero(self, mensaje_Error, col, fila):
        while True:
            gotoxy(col, fila)
            valor = input()
            try:
                if int(valor) > 0:
                    break
            except:
                gotoxy(col+10, fila):print(mensaje_Error)
                time.sleep(1)
                gotoxy(col+10, fila);print(" "*len(mensaje_Error))
        return valor
    
    def solo_letras(self, mensaje, mensaje_Error):
        while True:
            valor = str(input("        ----->            |  {} ".format(mensaje)))
            if valor.isalpha():
                break
            else:
                print("         --------><  |  {}".format(mensaje_Error))
        return valor

    def solo_decimales(self, mensaje, mensaje_Error):
        while True:
            valor = str(input("         ----->  | {} ".format(mensaje)))
            try:
                valor = float(valor)
                if valor > float(0):
                    break
            except:
                print("         -------><  | {} ".format(mensaje_Error))
        return valor 