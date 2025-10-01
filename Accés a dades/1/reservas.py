class reserva:
    TXT = "reservas.txt"

    def __init__(self, num_asiento, nombre_pasajero, clase):
        self.num_asiento = num_asiento
        self.nombre_pasajero = nombre_pasajero
        self.clase = clase

    def creacion_reserva(self):
        with open(reserva.TXT, "a", encoding="utf-8") as f:
            f.write(f"{self.num_asiento},{self.nombre_pasajero},{self.clase}\n")

    def procesar_reserva(self):
        total = 0
        business = 0
        with open(reserva.TXT, "r", encoding="utf-8") as f:
            for linea in f:
                partes = [p.strip() for p in linea.strip().split(",")]
                if len(partes) != 3:
                    continue
                asiento, nombre, clase = partes
                print(f"Asiento {asiento} | Pasajero: {nombre} | Clase: {clase}")
                total += 1
                if clase.lower() == "business":
                    business += 1
        print(f"\nTotal de reservas realizadas: {total}")
        print(f"Hay un total de {business} reservas en Business")


r1 = reserva("12A", "Juan Pérez", "Economy")
r2 = reserva("14B", "María López", "Business")
r3 = reserva("21C", "Carlos García", "Economy")
r1.creacion_reserva(); r2.creacion_reserva(); r3.creacion_reserva()

r1.procesar_reserva()
