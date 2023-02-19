class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        if color in ["rojo", "verde", "amarillo", "negro", "blanco"]:
            self.color = color
        else:
            pass

class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos,marca,motor,registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        Auto.cantidadCreados += 1
    
    def cantidadAsientos(self):
        cantidad = 0
        for asiento in self.asientos:
            if isinstance(asiento, Asiento):
                cantidad += 1
        return cantidad

    def verificarIntegridad(self):
        registro_auto = self.registro
        registro_motor = self.motor.registro
        registro_asientos = [asiento.registro for asiento in self.asientos]
        
        if registro_auto == registro_motor and all(registro == registro_auto for registro in registro_asientos):
            return "Auto original"
        else:
            return "Las piezas no son originales"