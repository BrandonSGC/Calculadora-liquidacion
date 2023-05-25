from datetime import datetime
from dateutil.relativedelta import relativedelta

import os

class Empleado:    
    # Constructores.
    def __init__(self, cedula = 0, nombre = "", apellidos = "", 
    telefono = 0, puesto = "", responsabilidad_patronal = False, 
    renuncia = False, fecha_entrada = "", fecha_salida = "",
    aguinaldo = 0, preaviso = False, cesantia = False):
        self.__cedula = cedula
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__telefono = telefono
        self.__puesto = puesto
        self.__responsabilidad_patronal = responsabilidad_patronal
        self.__renuncia = renuncia
        self.__fecha_entrada = fecha_entrada
        self.__fecha_salida = fecha_salida
    
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
        
        
    # Metodos
    def ingresar_empleado(self):
        self.set_cedula(input('Cedula: '))
        self.set_nombre(input('Nombre: '))
        self.set_apellidos(input('Apellidos: '))
        self.set_telefono = int(input('Telefono: '))
        self.set_puesto(input('Puesto: ')) 
        #self.obtener_fechas()
        self.seleccionar_motivo_salida()        
        if self.get_responsabilidad_patronal():
            # Calcular cesantia, aguinaldo y pagar preaviso.
            pass
        else:
            self.calcular_aguinaldo()
            pass
        
        
        
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
            
   
    # Obtenemos una lista con los meses desde que inicio y salio del trabajo.
    def obtener_meses_entre_fechas(self, fecha_entrada, fecha_salida):
        meses = []
        fecha_actual = fecha_entrada
        while fecha_actual <= fecha_salida:
            meses.append(fecha_actual.strftime("%B %Y"))
            fecha_actual += relativedelta(months=1)
        return meses
            

    def obtener_fechas(self):
        fecha_entrada = input('Fecha de entrada (Ejemplo: 2022/01/01): ')
        fecha_salida = input('Fecha de salida (Ejemplo: 2023/01/01): ')

        # Obtenemos una lista con los valores individuales del año, mes y día.
        datos_fecha_entrada = fecha_entrada.split('/')
        datos_fecha_salida = fecha_salida.split('/')

        # Asignamos la fecha a los atributos ya con el formato correcto.
        self.set_fecha_entrada(datetime(int(datos_fecha_entrada[0]), int(datos_fecha_entrada[1]), int(datos_fecha_entrada[2])))
        self.set_fecha_salida(datetime(int(datos_fecha_salida[0]), int(datos_fecha_salida[1]), int(datos_fecha_salida[2])))

        meses = self.obtener_meses_entre_fechas(self.get_fecha_entrada(), self.get_fecha_salida())

        salario_total = 0
        for mes in range(len(meses) - 1):
            salario = int(input(f'Salario de {meses[mes]}: '))
            salario_total += salario

        print(f'Salario total: {salario_total}')
        
        
    
    
    # Promedio mensual de las ganancias de todo el año.
    def calcular_aguinaldo(self): 
        fecha_entrada = input('Fecha de entrada (Ejemplo: 2022/01/01): ')
        fecha_salida = input('Fecha de salida (Ejemplo: 2023/01/01): ')

        # Obtenemos una lista con los valores individuales del año, mes y día.
        datos_fecha_entrada = fecha_entrada.split('/')
        datos_fecha_salida = fecha_salida.split('/')

        # Asignamos la fecha a los atributos ya con el formato correcto.
        self.set_fecha_entrada(datetime(int(datos_fecha_entrada[0]), int(datos_fecha_entrada[1]), int(datos_fecha_entrada[2])))
        self.set_fecha_salida(datetime(int(datos_fecha_salida[0]), int(datos_fecha_salida[1]), int(datos_fecha_salida[2])))

        meses = self.obtener_meses_entre_fechas(self.get_fecha_entrada(), self.get_fecha_salida())

        salario_total = 0
        for mes in range(len(meses) - 1):
            salario = int(input(f'Salario de {meses[mes]}: '))
            salario_total += salario
        
        # Calculo aguinaldo.
        aguinaldo = (salario_total / len(meses)) / 12

        print(f'Aguinaldo: {aguinaldo}')
        
          
    # Debe tener responsabilidad patronal.
    def calcular_cesantia(self): 
        pass
    
    # Sacar cuanto tiempo ha trabajado.
    def preaviso(self): 
        pass
    
    def __str__(self):
        return f"Cédula: {self.get_cedula()} \nEmpleado: {self.get_nombre()} {self.get_apellidos()}\nPuesto: {self.get_puesto()} \nFecha de entrada: {self.get_fecha_entrada()} \nFecha de salida: {self.get_fecha_salida()}"