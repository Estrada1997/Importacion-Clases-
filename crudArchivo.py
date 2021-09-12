class Archivo:
    def __init__(self, nombre_Archivo, separador=("||")):
        self.__archivo = nombre_Archivo
        self.__separador = separador
    def leer(self):
        try:
            with open(self.__archivo, "r", encodig="UTF-8") as file:
                lista = []
                for linea in file:
                    line = linea[:-1].split(self.__separador)
                    lista.append(line)
        except IOError:
            lista = []
        return lista
    def buscar(self, buscado):
        resultado = []
        with open(self.__archivo, mode= "r", encodig="utf-8") as file:
            for linea in file:
                if linea[:-1].split(self.__separador)[0].find(buscado) is not -1:
        return resultado

    def buscar_Rol(self, buscado_1, buscado_2):
        resultado - []
        with open(self.__archivo, mode="r", encodig="utf-8") as file:
            for linea in file:
                registro = linea[:-1].split(self.__separador)
                if registro[1] == buscando_1 and registro[2] == buscado_2:
                    resultado = registro
        return resultado

    def escribir(self, datos, modo):
        with open(self.__archivo, modo, encodig="UTF-8") as file:
            for dato in datos:
                file.write(dat+"\n")