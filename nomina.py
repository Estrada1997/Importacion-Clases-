from componentes import Meu, Valida
from helpers import borrar_Pantalla, gotoxy
from crudArchvos import Archivo
from entidades_Rol import *
from datetime import date
import time
# Menu Mantenimiento
def emp_Administrativo():
    pass
def emp_Obrero():
    pass
def cargos():
    borrar_Pantalla()
    gotoxy(20,2);print("Mantenimento de Cargos")
    gotoxy(15,4);print("Codigo: ")
    gotoxy(15,5);print("Descripcion Cargos: ")
    gotoxy(33,5)
    desCargo = input()
    archiCargo = Archivo("./archivos/cargo.txt","||")
    cargos = archiCargo.leer()
    if cargos: id_Sig = int(cargos[-1][9])+1
    else: id_Sig = 1
    cargo = Cargo(desCargo, id_Sig)
    datos = cargo.getCargo()
    datos = "||".join(datos)
    archiCargo.escribir([datos], "a")
    #...................
    #Opciones del Menu Novedades
def sobre_tiempo():
    borrar_Pantalla()
    gotoxy(20,2);print("Ingreso de Horas Extras")
    empleado, entEmpleado = [], None
    aamm, h50, h100 = 0, 0, 0
    while not empleado:
        gotoxy(15,5);print("Empleado ID [ ]: ")
        gotoxy(27,5);id = input().upper()
        archi_Empleado = Archivo(",/archivo/obrero.txt","||")
        empleado = archi_Empleado.buscar(id)
        if empleado:
            entEmpleado =Obrero(empledo[1], empleado[2], empleado[3], empleado[4])
            gotoxy(35,5);print(entEmpleado.nombre)
        else:
            gotoxy(27,6);print("No existe Empleado con ese codigo[{}]:".format(id))
            time.sleep(2);gotoxy(27,6);print(" "*40)
    gotoxy(15,6);print("Periodo[aaaamm]")
    gotoxy(15,7);print("Horas 50: ")
    gotoxy(15,8);print("Horas 100: ")
    validar = Valida()
    aamm = validar.solo_numero("Error: Solo numeros", 23,6)
    
    gotoxy(23,7);h50 = input()
    gotoxy(24,8);h100 = input()
    gotoxy(15,9);print("Esta seguro de graba el Registro(s/n):")
    gotoxy(54,9);grabar = input().lower()
    if grabar == "s":
        archiSobre_tiempo = Archivo("./archivo/sobretiempo.txt","||")
        SobreTiempo = archiSobre_tiempo.leer()
        if sobre_tiempo: id_Sig = int(sobre_tiempo[-1][0])+1
        else: id_Sig = 1 
        sobre_tiempo = SobreTiempo(entEmpleado, aamm, h50, h100, True, id_Sig)
        datos = sobre_tiempo.get_Sobre_Tiempo()
        datos ="||".join(datos)
        archiSobre_tiempo.escribr([datos],"a")
        gotoxy(10,10);input("Regstro Grabado SatisFactoriamente\nPresione una tecla para contiuar:")
    else:
        gotoxy(10,10);input("Registro No fue Grabado\n Presione una tecla para contiuar")
def prestamos():
    pass
def rolAdministrativo():
    borrar_Pantalla()
    gotoxy(20,2);print("Rol Administrativo")
    aamm = 0
    gotoxy(15,6);print("Periodo[aaaamm]")
    validar = Valida()
    aamm = validar.solo_numero("Error: Solo numeros", 23,6)
    gotoxy(15,7);print("Esta seguro de Procesar el Rol(s/n):")
    gotoxy(54,7);grabar =input().lower()
    entEmpAdm = None 
    if grabar == "s":
        archiRol = Archivo("./archivos/rolCabAdm.txt","||")
        rolesAdm = archiRol.leer()
        if rolesAdm : id_Sig = nt(rolesAdm[-1][0])+1
        else: id_Sig = 1
        archiEmp = Archivo("./archivos/administratvo.ttxt", "||")
        empAdm = archiEmp.leer()
        if empAdm:
            nomina = Nomina(date.today(), aamm, "OBREROS")
            for empleado in empAdm:
                entEmpAdm = Administrativo(empleado[1], empleado[2], empleado[3], empleado[4]. empleado[5])
                print(entEmpAdm.nombre, entEmpAdm.Sueldo)
                nomina.calcular_NominaDetalle(empleado)
    else:
        gotoxy(10,10);input("Rol no fue Procesado\n presione una tecla par continuar...")
        input("Presione una tecla contiuar....")
def rolObrero():
    pass
opc=""
while opc != "5":
    borrar_Pantalla()
    menu =Menu("Menu Principal",["1) Mantenimeto","2) Novedades","3) Rol de Pago","4) Consultas","5) Salir"])
    opc = menu.menu()
    if opc == "1":
        opc_1 = ""
        while opc_1 !="7"
        borrar_Pantalla()
        menu_1 = Menu("Menu Mantenimiento",["1) Empleado Administrativo","2) Empleado Obrero", "3) Cargos","4) Departamento","5) Empresa","6) Parametros","7) Salir"])
        if opc_1 ="1":
            emp_Administrativo()
        elif opc_1 =="3":
            cargos()
    elif opc == "2":
        opc_1 = ""
        while opc_1 !="7"
        borrar_Pantalla()
        menu_1 = Menu("Menu Mantenimiento",["1) Empleado Administrativo","2)Empleado Obrero", "3) Cargos","4) "])
        if opc_2 ="1":
            Sobre_Tiempo()
        elif opc_2 =="2":
            prestamo()
    elif opc =="3":
        borrar_Pantalla()
        menu_3 = Menu("Menu Rol",["1) Rol Administrativo","2) Rol Obrero", "3) Cargos","4) "])
        if opc_3 ="1":
            rolAdministrativo()
        elif opc_3 =="2":
            rolObrero()
    elif opc =="4":
        borrar_Pantalla()
        menu_4 = Menu("Menu Consulta",["1) Empleados","2) Cargos", "3) Departamento","4) "])
        opc_4 = menu.menu()
    elif opc =="5":
        borrar_Pantalla()
            print("Gracias por su vsita...")
    else:
        print("Opcion no Valida")
input("Presione una tecla para salir")
borrar_Pantalla()