from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

import os

class Empleado:    
    # Constructores.
    def __init__(self, cedula = 0, nombre = "", apellidos = "", 
    telefono = 0, puesto = "", fecha_entrada = "", fecha_salida = "",
    total_aguinaldo = 0, total_preaviso = 0, total_cesantia = 0, 
    total_liquidacion = 0):
        self.__cedula = cedula
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__telefono = telefono
        self.__puesto = puesto
        self.__fecha_entrada = fecha_entrada
        self.__fecha_salida = fecha_salida
        self.__total_preaviso = total_preaviso
        self.__total_aguinaldo = total_aguinaldo
        self.__total_cesantia = total_cesantia
        self.__total_liquidacion = total_liquidacion
    
    # Getters & Setters
    def get_cedula(self):
        return self.__cedula    
    def set_cedula(self, cedula):
        self.__cedula = cedula
    
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def get_apellidos(self):
        return self.__apellidos
    def set_apellidos(self, apellidos):
        self.__apellidos = apellidos
              
    def get_telefono(self):
        return self.__telefono
    def set_telefono(self, telefono):
        self.__telefono = telefono        
        
    def get_puesto(self):
        return self.__puesto
    def set_puesto(self, puesto):
        self.__puesto = puesto        
    
    def get_fecha_entrada(self):
        return self.__fecha_entrada
    def set_fecha_entrada(self, fecha_entrada):
        self.__fecha_entrada = fecha_entrada
        
    def get_fecha_salida(self):
        return self.__fecha_salida
    def set_fecha_salida(self, fecha_salida):
        self.__fecha_salida = fecha_salida
        
    def get_total_preaviso(self):
        return self.__total_preaviso
    def set_total_preaviso(self, total_preaviso):
        self.__total_preaviso = total_preaviso
       
    def get_total_aguinaldo(self):
        return self.__total_aguinaldo
    def set_total_aguinaldo(self, total_aguinaldo):
        self.__total_aguinaldo = total_aguinaldo   
        
    def get_total_cesantia(self):
        return self.__total_cesantia
    def set_total_cesantia(self, total_cesantia):
        self.__total_cesantia = total_cesantia
    
    def get_total_liquidacion(self):
        return self.__total_liquidacion
    def set_total_liquidacion(self, total_liquidacion):
        self.__total_liquidacion = total_liquidacion
        
        
    # Metodos

    # Crear nuevo empleado.
    def crear_empleado(self):
        self.set_cedula(input('\nCedula ejemplo "123427893": ')) #validar
        self.set_nombre(input('Nombre (Solo el nombre): '))
        self.set_apellidos(input('Apellidos: '))
        self.set_telefono = int(input('Telefono ejemplo "71234567": ')) #validar
        self.set_puesto(input('Puesto: '))
        
        # Obtener fechas
        fecha_entrada = input('Fecha de entrada ejemplo 2022-01-01: ')
        fecha_salida = input('Fecha de salida ejemplo 2022-01-01: ')
   
        # Asignamos las fechas ya en su formato corecto.
        self.set_fecha_entrada(self.formatear_fecha(fecha_entrada))
        self.set_fecha_salida(self.formatear_fecha(fecha_salida))



        # Arreglar lo de pedir los salarios.

        print('\nCalcular el preaviso:\n')
        self.set_total_preaviso(self.calcular_preaviso())
        print(self.get_total_preaviso())

        print('\nCalcular Cesantía')
        self.set_total_cesantia(self.calcular_cesantia())
        print(self.get_total_cesantia())

        
    def seleccionar_motivo_salida(self):
        continuar = True
        while continuar:
            os.system('cls')
            print('Motivo de salida: ')
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
                    self.set_responsabilidad_patronal(True)
                    break
                case 2:
                    self.set_responsabilidad_patronal(False)
                    break
                case 3:
                    self.set_responsabilidad_patronal(False)
                    break
                case _:
                    print('Ingrese una opcion correcta.')
                    input('Enter para continuar...')
        

    
    def calcular_preaviso(self):
        # Sacamos los años, meses y dias que trabajo el empleado a partir
        # de la fecha de entrada y salida.
        years, meses, dias = self.obtener_tiempo_laborado(self.get_fecha_entrada(), self.get_fecha_salida())

        # Obtenemos el salario total de los ultimos 6 meses para el calculo del preaviso y cesantia. 
        print('Por favor ingrese el ingreso bruto / neto de los ultimos 6 salarios.')
        salario_total = 0        
        for i in range(6):
            salario = int(input(f'Salario # {i+1}: '))
            salario_total += salario

        # Una vez tenemos el salario total de esos meses lo tenemos
        # que dividir entre 6.        
        salario_total = salario_total / 6     
        
        # Ahora ese promedio lo debemos de dividir entre los 30 dias del
        # mes para sacar el salario por dia.
        salario_dia = salario_total / 30
        print(f'Salario por dia: {salario_dia}')
        
        # Dependiendo de esos dias entonces de acuerdo a la tabla
        # verificamos cuantos dias de preaviso le tocan.
        if years < 1 and meses < 3:
            return 0
        
        # De 3 a menos de 6 meses: 1 semana.
        elif years < 1 and meses >= 3 and meses < 6:
            dias_preaviso = 7
            total_preaviso = salario_dia * dias_preaviso
            return total_preaviso
        
        # De 6 meses a menos de 1 año: 15 días.
        elif years < 1 and meses >= 6:
            dias_preaviso = 15
            total_preaviso = salario_dia * dias_preaviso
            return total_preaviso
        
        # Más de 1 año: 1 mes de preaviso
        else:
            dias_preaviso = 30
            total_preaviso = salario_dia * dias_preaviso
            return total_preaviso


    def calcular_cesantia(self): 
        # Sacamos los años, meses y dias que trabajo el empleado a partir
        # de la fecha de entrada y salida.
        years, meses, dias = self.obtener_tiempo_laborado(self.get_fecha_entrada(), self.get_fecha_salida())

        # Obtenemos el salario total de los ultimos 6 meses para el calculo del preaviso y cesantia. 
        print('Por favor ingrese el ingreso bruto / neto de los ultimos 6 salarios.')
        salario_total = 0        
        for i in range(6):
            salario = int(input(f'Salario # {i+1}: '))
            salario_total += salario

        # Una vez tenemos el salario total de esos meses lo tenemos
        # que dividir entre 6.        
        salario_total = salario_total / 6     
        
        # Ahora ese promedio lo debemos de dividir entre los 30 dias del
        # mes para sacar el salario por dia.
        salario_dia = salario_total / 30
        print(f'Salario por dia: {salario_dia}')
        

        if years == 1:
            dias_cesantia = 19.5
            cesantia = salario_dia * dias_cesantia
            return cesantia

        elif years == 2:
            dias_cesantia = 20
            cesantia = salario_dia * dias_cesantia
            return cesantia

        elif years == 3:
            dias_cesantia = 20.5
            cesantia = salario_dia * dias_cesantia
            return cesantia
        
        elif years == 4:
            dias_cesantia = 21
            cesantia = salario_dia * dias_cesantia
            return cesantia
        
        elif years == 5:
            dias_cesantia = 21.24
            cesantia = salario_dia * dias_cesantia
            return cesantia

        elif years == 6:
            dias_cesantia = 21.5
            cesantia = salario_dia * dias_cesantia
            return cesantia

        elif years == 7:
            dias_cesantia = 22
            cesantia = salario_dia * dias_cesantia
            return cesantia
        
        else:
            pass



        # Se multiplican esos dias por cada año.
        # Ejemplo si el trabajador duro 2 años entonces digamos
        # que la tabla le dice 20 dias. Enotonces lo que 
        # hacemos es multiplcar 20 por cada año laborado
        # Osea : 20 * años trabajados = 40

        # Luego multiplicamos 40 * salario por dia 



        pass

    def calcular_aguinaldo(self):
        pass

    def calcular_liquidacion(self):        
        pass

    # Metodo para dar convertir string a fecha.
    def formatear_fecha(self, fecha):
        # Convertimos a fechas con el formato correcto.
        fecha = datetime.strptime(fecha, "%Y-%m-%d")
        return fecha    
    
    # Metodo para...
    def obtener_tiempo_laborado(self, fecha1, fecha2):
        diferencia = fecha2 - fecha1

        #Obtenemos la diferencia en años, meses y dias.
        years = diferencia.days // 365
        meses = (diferencia.days % 365) // 30
        dias = (diferencia.days % 365) % 30

        return years, meses, dias
    
    def obtnener_salarios(self):
        pass
        
    def obtener_salario_dia(self):
        pass

    
        
    
    def __str__(self):
        return f"Cédula: {self.get_cedula()} \nEmpleado: {self.get_nombre()} {self.get_apellidos()}\nPuesto: {self.get_puesto()} \nTelefono: {self.get_telefono()} \nFecha de entrada: {self.get_fecha_entrada()} \nFecha de salida: {self.get_fecha_salida()}\nAguinaldo: {self.get_total_aguinaldo()} \nCesantía: {self.get_total_cesantia()} \nPreaviso: {self.get_total_preaviso()} \nTotal Liquidacion: {self.get_total_liquidacion()}"