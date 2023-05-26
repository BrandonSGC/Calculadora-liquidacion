from datetime import datetime
from dateutil.relativedelta import relativedelta

import os

class Empleado:    
    # Constructores.
    def __init__(self, cedula = 0, nombre = "", apellidos = "", 
    telefono = 0, puesto = "", sueldo = "", responsabilidad_patronal = False, 
    renuncia = False, fecha_entrada = "", fecha_salida = "",
    aguinaldo = 0, preaviso = False, cesantia = False):
        self.__cedula = cedula
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__telefono = telefono
        self.__puesto = puesto
        self.__sueldo = sueldo
        self.__responsabilidad_patronal = responsabilidad_patronal
        self.__renuncia = renuncia
        self.__fecha_entrada = fecha_entrada
        self.__fecha_salida = fecha_salida
        self.__preaviso = preaviso
    
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
        
    def get_sueldo(self):
        return self.__sueldo
    def set_sueldo(self, sueldo):
        self.__sueldo = sueldo
        
    def get_responsabilidad_patronal(self):
        return self.__responsabilidad_patronal
    def set_responsabilidad_patronal(self, responsabilidad_patronal):
        self.__responsabilidad_patronal = responsabilidad_patronal    
        
    def get_renuncia(self):
        return self.__renuncia
    def set_reuncia(self, renuncia):
        self.__renuncia = renuncia
    
    def get_fecha_entrada(self):
        return self.__fecha_entrada
    def set_fecha_entrada(self, fecha_entrada):
        self.__fecha_entrada = fecha_entrada
        
    def get_fecha_salida(self):
        return self.__fecha_salida
    def set_fecha_salida(self, fecha_salida):
        self.__fecha_salida = fecha_salida
        
    def get_responsabilidad_patronal(self):
        return self.__responsabilidad_patronal
    def set_responsabilidad_patronal(self, responsabilidad_patronal):
        self.__responsabilidad_patronal = responsabilidad_patronal
        
    def get_preaviso(self):
        return self.__preaviso
    def set_preaviso(self, preaviso):
        self.__preaviso = preaviso
        
        
    # Metodos
    def ingresar_empleado(self):
        self.set_cedula(input('Cedula: ')) #validar
        self.set_nombre(input('Nombre: '))
        self.set_apellidos(input('Apellidos: '))
        self.set_telefono = input('Telefono: ') #validar
        self.set_puesto(input('Puesto: '))
        self.set_sueldo(int(input('Sueldo: '))) #validar
        
        os.system('cls')
        self.seleccionar_motivo_salida()
        if self.get_responsabilidad_patronal == True:
            # Calcular cesantia, aguinaldo y pagar preaviso.
            pass
        else:
            # Calcular aguinaldo.
            pass
        
        respuesta = input("¿Se ha ejercido el preaviso? (Si / No): ")
        if respuesta == 'Si' or 'si' or 'SI' or 's':
            self.set_preaviso(True)
        else:
            self.set_preaviso(False)
            
            
       
    def seleccionar_motivo_salida(self):
        continuar = True
        while continuar:
            print('1- Despido con responsabilidad patronal')
            print('2- Despido sin responsabilidad patronal')
            print('3- Renuncia')
            
            opcion = int(input('Seleccione una opción: '))

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
        

    # Promedio mensual de las ganancias de todo el año.
    def calcular_aguinaldo(self, fecha_entrada, fecha_salida, salario):
        pass
            
    # Debe tener responsabilidad patronal.
    def calcular_cesantia(self): 
        pass
    
    # Sacar cuanto tiempo ha trabajado.
    def preaviso(self): 
        pass
    
    def __str__(self):
        return f"Cédula: {self.get_cedula()} \nEmpleado: {self.get_nombre()} {self.get_apellidos()}\nPuesto: {self.get_puesto()} \nFecha de entrada: {self.get_fecha_entrada()} \nFecha de salida: {self.get_fecha_salida()}"