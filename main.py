# Bibliotecas
import os
from xml.dom import minidom

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
    if len(empleados) > 0:
        for i in range(len(empleados)):
            print(f"{empleados[i]}")
            print('=' * 36)
            print('')
    else:
        print('No se han ingresado empleados al sistema.')

# Modificar empleados
def modificar_empleados(empleados):
    if len(empleados) > 0:
        cedula = input('Cedula del empleado a modificar: ')
        print('')
        for i in range(len(empleados)):
            if empleados[i].get_cedula() == cedula:
                                
                print('Que desea modificar?\n')
                print(f'1- Nombre: {empleados[i].get_nombre()}')
                print(f'2- Apellidos: {empleados[i].get_apellidos()}')
                print(f'3- Telefono: {empleados[i].get_telefono()}')
                print(f'4- Puesto: {empleados[i].get_puesto()}')
                print(f'5- Fecha de entrada: {empleados[i].get_fecha_entrada()}')
                print(f'6- Fecha de salida: {empleados[i].get_fecha_salida()}')
                print(f'7- Calcular nuevamente la liquidacion')
                print('8- Cancelar')
                try:
                    opcion = int(input('\nSeleccione una opcion: '))
                except:
                    opcion = -1

                match opcion:
                    case 1:
                        print(f'\nNombre: {empleados[i].get_nombre()}')
                        empleados[i].set_nombre(input('Nuevo nombre: '))
                        print('El nombre se ha actualizado correctamente.')
                        break
                    case 2:
                        print(f'\nApellidos: {empleados[i].get_apellidos()}')
                        empleados[i].set_apellidos(input('Nuevos apellidos: '))
                        print('Los apellidos se ha actualizado correctamente.')
                        break
                    case 3:
                        print(f'\nTelefono: {empleados[i].get_telefono()}')
                        # Mientras el telefono no sea valido le preguntamos su telefono.
                        telefono_valido = False
                        while not telefono_valido:
                            telefono = input('Ingresa tu nuevo teléfono, ejemplo "8888-8888": ')
                            telefono_valido = empleados[i].validar_telefono(telefono)
                            if telefono_valido:
                                empleados[i].set_telefono(telefono)
                                break

                        print('El Telefono se ha actualizado correctamente.')
                        break
                    case 4:
                        print(f'\nPuesto: {empleados[i].get_puesto()}')
                        empleados[i].set_puesto(input('Nuevo Puesto: '))
                        print('El Puesto se ha actualizado correctamente.')
                        break
                    case 5:
                        print(f'\nFecha de entrada: {empleados[i].get_fecha_entrada()}')
                        fecha_valida = False
                        while not fecha_valida:
                            fecha_entrada = input('Nueva fecha de entrada ejemplo 2022-01-01: ')
                            fecha_valida = empleados[i].validar_fecha(fecha_entrada)
                            if fecha_valida:
                                empleados[i].set_fecha_entrada(empleados[i].formatear_fecha(fecha_entrada))
                                break

                        print('La fecha de entrada se ha actualizado correctamente.')
                        break
                    case 6:
                        print(f'\nFecha de salida: {empleados[i].get_fecha_salida()}')

                        fecha_valida = False
                        while not fecha_valida:
                            fecha_salida = input('Nueva fecha de salida ejemplo 2023-01-01: ')
                            fecha_valida = empleados[i].validar_fecha(fecha_salida)
                            if fecha_valida:
                                empleados[i].set_fecha_salida(empleados[i].formatear_fecha(fecha_salida))
                                break

                        print('La fecha de salida se ha actualizado correctamente.')
                        break
                    case 7:
                        calcular_liquidacion(empleados)
                    case 8:
                        break
                    case _:
                        print('No es una opcion valida.')
            else:
                print('No se han encontrado resultados.')
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
    

def calcular_liquidacion(empleados):
    if len(empleados) > 0:
        cedula = input('Cedula del empleado a calcular la liquidación: ')
        print('')
        for i in range(len(empleados)):
            if empleados[i].get_cedula() == cedula:
                print(empleados[i])
                continuar = True
                while continuar:
                    print('\nPor favor ingrese el motivo de salida: ')
                    print('1- Despido con responsabilidad patronal')
                    print('2- Despido sin responsabilidad patronal')
                    print('3- Renuncia')
                    
                    # Validamos que la opcion sea correcta.
                    try:
                        opcion = int(input('\nIngrese una opción: '))
                    except:
                        opcion = -1

                    match opcion:
                        case 1:
                            os.system('cls')
                            header('Calculo Aguinaldo')
                            empleados[i].set_total_aguinaldo(empleados[i].calcular_aguinaldo())
                            print(f'\nEl Aguinaldo de {empleados[i].get_nombre()} es de: {empleados[i].get_total_aguinaldo()}')
                            input('Pulse una tecla para continuar...')
                            
                            os.system('cls')                                                        

                            header('Calculo de Preaviso y Cesantía')
                            # Obtenemos el salario por dia a partir de los ultimos 6 salarios.
                            salario_dia = empleados[i].obtener_salario_dia()

                            # Calculamos el preaviso
                            empleados[i].set_total_preaviso(empleados[i].calcular_preaviso(salario_dia))
                            print(f'\nEl monto del Preaviso de {empleados[i].get_nombre()} es de: {empleados[i].get_total_preaviso()}')

                            # Calculamos la cesantia.
                            empleados[i].set_total_cesantia(empleados[i].calcular_cesantia(salario_dia))
                            print(f'\nEl monto de la Cesantía de {empleados[i].get_nombre()} es de: {empleados[i].get_total_cesantia()}')

                            # Calculamos la liquidación.
                            empleados[i].set_total_liquidacion(empleados[i].calcular_liquidacion())
                            print(f'\nEl monto de la Liquidación de {empleados[i].get_nombre()} es de: {empleados[i].get_total_liquidacion()}')
                            break

                        case 2:
                            os.system('cls')
                            header('Calculo Aguinaldo')
                            empleados[i].set_total_aguinaldo(empleados[i].calcular_aguinaldo())
                            print(f'\nEl Aguinaldo de {empleados[i].get_nombre()} es de: {empleados[i].get_total_aguinaldo()}')
                            input('Pulse una tecla para continuar...')

                            # Calculamos la liquidación.
                            empleados[i].set_total_liquidacion(empleados[i].calcular_liquidacion())
                            print(f'\nEl monto de la Liquidación de {empleados[i].get_nombre()} es de: {empleados[i].get_total_liquidacion()}')
                            
                            break

                        case 3:
                            os.system('cls')
                            header('Calculo Aguinaldo')
                            empleados[i].set_total_aguinaldo(empleados[i].calcular_aguinaldo())
                            print(f'\nEl Aguinaldo de {empleados[i].get_nombre()} es de: {empleados[i].get_total_aguinaldo()}')
                            input('Pulse una tecla para continuar...')                            

                            # Preguntar si realizo el preaviso
                            continuar2 = True
                            while continuar2:
                                print('\nSe ha ejercido el preaviso?\n')
                                print('1- Si')
                                print('2- No')
                                
                                try:
                                    opcion = int(input('\nOpción: '))
                                except:
                                    opcion = -1
                                
                                match opcion:
                                    case 1:
                                        # Calculamos el preaviso
                                        empleados[i].set_total_preaviso(empleados[i].calcular_preaviso(salario_dia))
                                        print(f'\nEl monto del Preaviso de {empleados[i].get_nombre()} es de: {empleados[i].get_total_preaviso()}')                                        
                            # Calculamos la liquidación.
                            empleados[i].set_total_liquidacion(empleados[i].calcular_liquidacion())
                            print(f'\nEl monto de la Liquidación de {empleados[i].get_nombre()} es de: {empleados[i].get_total_liquidacion()}')
                            break

                        case _:
                            print('Ingrese una opcion correcta.')
                            input('Enter para continuar...')                
                break
            else:
                print('No se han encontrado resultados.')
    else:
        print('Primero debe de ingrear el empleado al sistema.')


def generar_XML(empleados):
    # Crear el documento XML
    doc = minidom.Document()

    # Crear la etiqueta raíz
    root = doc.createElement("root")
    doc.appendChild(root)

    for i in range(len(empleados)):

        # Crear el elemento 'empleado'
        empleado = doc.createElement("empleado")
        root.appendChild(empleado)

        # Crear el elemento dentro de 'empleado'
        nombre = doc.createElement("nombre")
        empleado.appendChild(nombre)
        # Agregar el texto dentro de la etiqueta
        nombre_texto = doc.createTextNode(empleados[i].get_nombre())
        nombre.appendChild(nombre_texto)

        apellidos = doc.createElement('apellidos')
        empleado.appendChild(apellidos)
        apellidos_texto = doc.createTextNode(empleados[i].get_apellidos())
        apellidos.appendChild(apellidos_texto)

        telefono = doc.createElement('telefono')
        empleado.appendChild(telefono)
        telefono_texto = doc.createTextNode(empleados[i].get_telefono())
        telefono.appendChild(telefono_texto)

        puesto = doc.createElement('puesto')
        empleado.appendChild(puesto)
        puesto_texto = doc.createTextNode(empleados[i].get_puesto())
        puesto.appendChild(puesto_texto)
        
        fechaEntrada = doc.createElement('fechaEntrada')
        empleado.appendChild(fechaEntrada)
        # Convertimos la fecha en string.
        fecha_entrada = empleados[i].get_fecha_entrada()
        fecha_entrada_string = fecha_entrada.strftime('%Y-%m-%d')        
        fechaEntrada_texto = doc.createTextNode(fecha_entrada_string)
        fechaEntrada.appendChild(fechaEntrada_texto)

        fechaSalida = doc.createElement('fechaSalida')
        empleado.appendChild(fechaSalida)
        # Convertimos la fecha en string.
        fecha_salida = empleados[i].get_fecha_salida()
        fecha_salida_string = fecha_salida.strftime('%Y-%m-%d')
        fechaSalida_texto = doc.createTextNode(fecha_salida_string)
        fechaSalida.appendChild(fechaSalida_texto)

        totalPreaviso = doc.createElement('totalPreaviso')
        empleado.appendChild(totalPreaviso)
        totalPreaviso_texto = doc.createTextNode(str(empleados[i].get_total_preaviso()))
        totalPreaviso.appendChild(totalPreaviso_texto)

        totalAguinaldo = doc.createElement('totalAguinaldo')
        empleado.appendChild(totalAguinaldo)
        totalAguinaldo_texto = doc.createTextNode(str(empleados[i].get_total_aguinaldo()))
        totalAguinaldo.appendChild(totalAguinaldo_texto) 
        
        totalCesantia = doc.createElement('totalCesantia')
        empleado.appendChild(totalCesantia)
        totalCesantia_texto = doc.createTextNode(str(empleados[i].get_total_cesantia()))
        totalCesantia.appendChild(totalCesantia_texto)
        
        totalLiquidacion = doc.createElement('totalLiquidacion')
        empleado.appendChild(totalLiquidacion)
        totalLiquidacion_texto = doc.createTextNode(str(empleados[i].get_total_liquidacion()))
        totalLiquidacion.appendChild(totalLiquidacion_texto)

    # Guardar el documento XML en un archivo
    xml_file = open("output.xml", "w")
    xml_file.write(doc.toprettyxml(indent="\t"))
    xml_file.close()

def leer_XML(empleados):
    pass

def actualizar_XML(empleados):
    pass

def eliminar_XML(empleados):
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
        print('5- Modificar Datos de Empleado')
        print('6- Eliminar Empleado')
        print('7- Generar Archivo XML')
        print('8- Leer Archivo XML')
        print('9- Actualizar Archivo XML')
        print('10- Eliminar Archivo XML')        
        print('11- Salir')


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
                calcular_liquidacion(empleados)
                                
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
                header('Modificar Datos de Empleado')
                modificar_empleados(empleados)
                input('Enter para continuar...')
            
            case 6:
                header('Eliminar Empleado')
                eliminar_empleado(empleados)
                input('Enter para continuar...')

            case 7:
                header('Generar Archivo XML')
                generar_XML(empleados)
                input('Enter para continuar... ')

            case 8:
                header('Leer Archivo XML')
                
                input('Enter para continuar... ')

            case 9:
                header('Actualizar Archivo XML')
                
                input('Enter para continuar... ')

            case 10:
                header('Eliminar Archivo XML')
                
                input('Enter para continuar... ')
            
            case 11:
                print('Gracias por utilizar el sistema...')
                break
            
            case _:
                print('Ingrese una opción correcta.')
                input('Enter para continuar...')
                

if __name__ == '__main__':
    main()