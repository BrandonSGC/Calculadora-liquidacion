from Empleado import Empleado
from datetime import datetime
from dateutil.relativedelta import relativedelta

import os
     
# Methods

# Limpia pantalla e imprime el titulo dentro de los "=".
def header(titulo = ""):
    os.system('cls')
    print('=' * int(len(titulo)))
    print(titulo)
    print('=' * int(len(titulo)))

# Mostrar empleados
def mostrar_empleados(empleados): 
    for i in range(len(empleados)):
        print(f"{empleados[i]}")
    print('=' * 30)
    print('')

# Editar empleados
def editar_empleados(empleados):
    for i in range(len(empleados)):
        print(f"{i}- {empleados[i]}")
    
    seleccionar_empleado()
    
# Eliminar Empleado
def eliminar_empleado():
    pass

# Seleccionar empleado
def seleccionar_empleado(self):
    pass


def main():
    # En esta lista almacenaremos los empleados.
    empleados = []
    continuar = True
    while continuar:        
        
        header('Grupo Diez - Menú')
        print('\n1- Calcular Liquidación')
        print('2- Mostrar Empleados') 
        print('3- Editar Datos de Empleado') 
        print('4- Salir')        

        try:
            opcion = int(input('\nIngrese una opción: '))
        except:
            opcion = -1   
        
        empleado = Empleado()
        match opcion:
            case 1:
                header('Calcular Liquidación')
                empleado.ingresar_empleado() 
                empleados.append(empleado) 
                os.system('cls')
                print('\nResultado: \n')              
                print(empleado)
                
                input('Enter para continuar...')
                
            case 2:
                header('Mostrar Empleados')
                if len(empleados) > 0:
                    mostrar_empleados(empleados)
                else:
                    print('No se han ingresado empleados al sistema.')
                input('Enter para continuar...')
                
            case 3:
                header('Editar Datos de Empleado')
                mostrar_empleados()
                input('Enter para continuar...')
            
            case 4:
                print('Gracias por utilizar el sistema...')
                break
            
            case _:
                print('Ingrese una opción correcta.')
                input('Enter para continuar...')
                

if __name__ == '__main__':
    main()