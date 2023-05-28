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
        print('=' * 36)
        print('')


# Editar empleados
def editar_empleados(empleados):
    if len(empleados) > 0:
        pass
    else:
        print('No se han ingresado empleados al sistema.')
    
    
# Eliminar Empleado
def eliminar_empleado(empleados):
    if len(empleados) > 0:
        cedula = input('Cedula a eliminar: ')
        print('')
        for i in range(len(empleados)):
            if empleados[i].get_cedula() == cedula:
                empleados.remove(empleados[i])
                print('Empleado eliminado correctamente.')
                break
            else:
                print('No se han encontrado resultados.')
    else:
        print('No se han ingresado empleados al sistema.')
    

# Buscar empleado
def buscar_empleado(empleados):
    if len(empleados) > 0:
        cedula = input('Cedula a buscar: ')
        print('')
        for i in range(len(empleados)):
            if empleados[i].get_cedula() == cedula:
                print(empleados[i])
                break
            else:
                print('No se han encontrado resultados.')
    else:
        print('No se han ingresado empleados al sistema.')
    


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

                input('Enter para continuar...')
            
            case 2:
                header('Crear Empleado.')
                empleado.crear_empleado()
                empleados.append(empleado)
                input('Enter para continuar...')
            
            case 3:
                header('Mostrar Empleados')
                
                mostrar_empleados(empleados)
                input('Enter para continuar...')
                
            case 4:
                header('Buscar Empleados')
                buscar_empleado(empleados)
                input('Enter para continuar...')
            case 5:
                header('Editar Datos de Empleado')

                input('Enter para continuar...')
            
            case 6:
                header('Eliminar Empleado')
                eliminar_empleado(empleados)
                input('Enter para continuar...')

            case 7:
                print('Gracias por utilizar el sistema...')
                break
            
            case _:
                print('Ingrese una opción correcta.')
                input('Enter para continuar...')
                

if __name__ == '__main__':
    main()