class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def mostrar_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}"

class Auto(Vehiculo):
    def __init__(self, marca, modelo, año, numero_puertas, es_automatico):
        super().__init__(marca, modelo, año)
        self.numero_puertas = numero_puertas
        self.es_automatico = es_automatico

    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"{info_base}, Número de Puertas: {self.numero_puertas}, Es Automático: {self.es_automatico}"

class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, cilindraje, tipo):
        super().__init__(marca, modelo, año)
        self.cilindraje = cilindraje
        self.tipo = tipo

    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"{info_base}, Cilindraje: {self.cilindraje}, Tipo: {self.tipo}"

def main():
    vehiculos = [
        Auto("Toyota", "Corolla", 2020, 4, True),
        Auto("Ford", "Fiesta", 2018, 5, False),
        Moto("Yamaha", "MT-07", 2021, 689, "Deportiva"),
        Moto("Honda", "PCX", 2022, 150, "Scooter"),
    ]

    for vehiculo in vehiculos:
        print(vehiculo.mostrar_info())

if __name__ == "__main__":
    main()
