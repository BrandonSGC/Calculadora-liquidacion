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
        self.set_telefono = input('Telefono ejemplo "71234567": ') #validar
        self.set_puesto(input('Puesto: '))
        
        # Obtener fechas
        fecha_entrada = input('Fecha de entrada ejemplo 2022-01-01: ')
        fecha_salida = input('Fecha de salida ejemplo 2022-01-01: ')
   
        # Asignamos las fechas ya en su formato corecto.
        self.set_fecha_entrada(self.formatear_fecha(fecha_entrada))
        self.set_fecha_salida(self.formatear_fecha(fecha_salida))
  



    # Metodo para dar convertir string a fecha.
    def formatear_fecha(self, fecha):
        # Convertimos a fechas con el formato correcto.
        fecha = datetime.strptime(fecha, "%Y-%m-%d")
        return fecha
            
        
        
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
        

    def calcular_aguinaldo(self, fecha_salida):
        # Obtenemos el ultimo diciembre.
        ultimo_diciembre = datetime(fecha_salida.year - 1, 12, 1)
        
        # Obtenemos los meses de diferencia.
        diferencia = relativedelta(fecha_salida, ultimo_diciembre)
        cantidad_meses = (diferencia.years * 12 + diferencia.months) + 1 #+1 Para que me cuente diciembre.

        salario_mensual = self.get_sueldo()
        
        aguinaldo = ((salario_mensual * cantidad_meses - 1) / cantidad_meses - 1) / 12

        return aguinaldo

                 

    def calcular_cesantia(self): 
        pass
          
    
    def calcular_dias_preaviso(self): 
        pass
    
    
    def calcular_liquidacion(self):        
        pass
    
    
    def __str__(self):
        return f"Cédula: {self.get_cedula()} \nEmpleado: {self.get_nombre()} {self.get_apellidos()}\nPuesto: {self.get_puesto()} \nFecha de entrada: {self.get_fecha_entrada()} \nFecha de salida: {self.get_fecha_salida()}\nAguinaldo: {self.get_total_aguinaldo()} \nCesantía: {self.get_total_cesantia()} \nPreaviso: {self.get_total_preaviso()} \nTotal Liquidacion: {self.get_total_liquidacion()}"