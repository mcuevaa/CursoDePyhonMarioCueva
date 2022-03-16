# Métodos de clase y métodos estáticos

# Métodos estáticos: son aquellos métodos que no requieren una instancia de la clase
class Carro:
    def __init__(self, placa='ABC-123', color='rojo'):
        self.placa = placa,
        self.color = color

    def rodar(self):
        print(f'Soy el auto de placas {self.placas} y soy de color {self.color}')


carro1 = Carro()
carro2 = Carro(placa='BDC-567', color='azul')

carro1.rodar()
