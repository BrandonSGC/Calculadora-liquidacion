from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

import os

class Empleado:    
    # Constructores.
    def __init__(self, cedula = 0, nombre = "", apellidos = "", 
    telefono = 0, puesto = "", sueldo = "", responsabilidad_patronal = False, 
    renuncia = False, fecha_entrada = "", fecha_salida = "",
    aguinaldo = 0, preaviso = False, cesantia = 0, total_liquidacion = 0):
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
        self.__aguinaldo = aguinaldo
        self.__cesantia = cesantia
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
       
    def get_aguinaldo(self):
        return self.__aguinaldo
    def set_aguinaldo(self, aguinaldo):
        self.__aguinaldo = aguinaldo   
        
    def get_cesantia(self):
        return self.__cesantia
    def set_cesantia(self, cesantia):
        self.__cesantia = cesantia
    
    def get_total_liquidacion(self):
        return self.__total_liquidacion
    def set_total_liquidacion(self, total_liquidacion):
        self.__total_liquidacion = total_liquidacion
        
        
    # Metodos
    def ingresar_empleado(self):
        self.set_cedula(input('\nCedula: ')) #validar
        self.set_nombre(input('Nombre (Solo el nombre): '))
        self.set_apellidos(input('Apellidos: '))
        self.set_telefono = input('Telefono: ') #validar
        self.set_puesto(input('Puesto: '))
        self.set_sueldo(int(input('Sueldo mensual: '))) #validar
        
        os.system('cls')
        # Obtener fechas
        fecha_entrada = input('Fecha de entrada ejemplo 2022/01/01: ')
        fecha_salida = input('Fecha de salida ejemplo 2022/01/01: ')
                
                
                
        # Asignamos la fecha ya en su formato al atributo.
        self.set_fecha_salida(self.formato_fecha(fecha_salida))
                
        
        
        
        self.seleccionar_motivo_salida()
        if self.get_responsabilidad_patronal == True:        
            # Calcular cesantia
            self.set_cesantia(self.calcular_cesantia())
            print(f"Total cesantia: {self.get_cesantia()}")
            
            # Calcular aguinaldo.
            self.set_aguinaldo(self.calcular_aguinaldo(self.get_fecha_salida()))
            
            # Pagar peraviso.
            
            # Calcular Total de la Liquidacion.
            self.set_total_liquidacion(self.calcular_liquidacion())
            
        else:
            # Calcular aguinaldo.
            self.set_aguinaldo(self.calcular_aguinaldo(self.get_fecha_salida()))
            
            
        respuesta = input("¿Se ha ejercido el preaviso? (Si / No): ")
        if respuesta == 'Si' or 'si' or 'SI' or 's':
            self.set_preaviso(True)
        else:
            self.set_preaviso(False)
            
            
    # Metodo para dar convertir string a fecha.
    def formato_fecha(self, fecha):
        # Convertimos a fechas con el formato correcot.
        fecha = datetime.strptime(fecha, "%Y/%m/%d")
        return fecha
        
        
    def obtener_ultimos_meses(self, fecha_salida):
        # Obtén la fecha actual
        fecha_salida = datetime.now()

        # Calcula la fecha hace 6 meses
        fecha_6_meses_atras = fecha_salida - timedelta(days=6*30)  # Asumiendo que un mes tiene 30 días.

        # Imprime los últimos 6 meses
        for i in range(6):
            fecha = fecha_6_meses_atras + timedelta(days=i*30)
            print(fecha.strftime("%Y-%m"))

        
        
    def seleccionar_motivo_salida(self):
        continuar = True
        while continuar:
            os.system('cls')
            print('Motivo de salida: ')
            print('1- Despido con responsabilidad patronal')
            print('2- Despido sin responsabilidad patronal')
            print('3- Renuncia')
            
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

                 
    # Debe tener responsabilidad patronal.
    def calcular_cesantia(self): 
        total_cesantia = 0
        
        print('Ingrese los ultimos 6 salarios recibidos.\n')
        for i in range(6):
            total_cesantia += int(input(f'Salario # {i}: '))
        
        # Se suman los salarios de los últimos seis meses y se divide entre seis para obtener el monto mensual.
        return total_cesantia / 6
        
        
    
    def preaviso(self): 
        pass
    
    
    def calcular_liquidacion(self):        
        liquidacion = self.get_cesantia() + self.get_aguinaldo()
        return liquidacion
    
    
    
    def __str__(self):
        return f"Cédula: {self.get_cedula()} \nEmpleado: {self.get_nombre()} {self.get_apellidos()}\nPuesto: {self.get_puesto()} \nFecha de entrada: {self.get_fecha_entrada()} \nFecha de salida: {self.get_fecha_salida()}\nAguinaldo: {self.get_aguinaldo()} \nCesantía: {self.get_cesantia()} \nPreaviso: {self.get_preaviso()} \nResponsabilidad Patronal: {self.get_responsabilidad_patronal()}"