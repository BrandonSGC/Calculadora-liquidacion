from Empleado import Empleado
from datetime import datetime
from dateutil.relativedelta import relativedelta

import os

def main():
    # En esta lista almacenaremos los empleados.
    empleados = []
    continuar = True
    while continuar:        
        
        header('Grupo Diez - Menú')
        print('\n1- Calcular Liquidación')
        print('2- Editar Datos de Empleado')        
        
        opcion = int(input('\nIngrese una opción: '))
        empleado = Empleado()
        match opcion:
            case 1:
                header('Calcular Liquidación')
                empleado.ingresar_empleado() 
                empleados.append(empleado) 
                print('\nResultado: \n')              
                print(empleados[0])
                
                input('Enter para continuar...')
                
            case 2:
                header('Editar Datos de Empleado')
                
                input('Enter para continuar...')
            
            case 5:
                print('Gracias por utilizar el sistema...')
                break
            
            case _:
                print('Ingrese una opción correcta.')
                input('Enter para continuar...')
                
     
# Methods

# Limpia pantalla e imprime el titulo dentro de los "=".
def header(titulo = ""):
    os.system('cls')
    print('=' * int(len(titulo)))
    print(titulo)
    print('=' * int(len(titulo)))
    


if __name__ == '__main__':
    main()