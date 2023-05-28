# Bibliotecas
import os

from Empleado import Empleado
from datetime import datetime
from dateutil.relativedelta import relativedelta
     

# Metodos

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
    pass
    
    
# Eliminar Empleado
def eliminar_empleado(empleados):
    pass


# Buscar empleado
def buscar_empleado(empleados):
    pass


# Metodo Principal (Donde empezamos a ejecutar todo el codigo).
def main():
    # En esta lista almacenaremos los empleados.
    empleados = []
    continuar = True
    while continuar:        
        
        header('Grupo Diez - Menú')
        print('\n1- Calcular Liquidación')
        print('2- Crear Empleado')
        print('3- Mostrar Empleados') 
        print('4- Buscar Empleados') 
        print('5- Editar Datos de Empleado')
        print('6- Eliminar Empleado')
        print('7- Salir')


        # Validamos que solo se ingresen numeros.
        try:
            opcion = int(input('\nIngrese una opción: '))
        except:
            opcion = -1                   
            
        empleado = Empleado()

        # Ingresa el usuario a la funcionalidad escogida.
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
                header('Crear Empleado.')

                input('Enter para continuar...')
            
            case 3:
                header('Mostrar Empleados')
                if len(empleados) > 0:
                    mostrar_empleados(empleados)
                else:
                    print('No se han ingresado empleados al sistema.')
                input('Enter para continuar...')
                
            case 4:
                header('Buscar Empleados')
                
                input('Enter para continuar...')
            case 5:
                header('Editar Datos de Empleado')

                input('Enter para continuar...')
            
            case 6:
                header('Eliminar Empleado')

                input('Enter para continuar...')

            case 7:
                print('Gracias por utilizar el sistema...')
                break
            
            case _:
                print('Ingrese una opción correcta.')
                input('Enter para continuar...')
                

if __name__ == '__main__':
    main()