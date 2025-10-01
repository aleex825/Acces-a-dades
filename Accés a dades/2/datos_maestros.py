import os
import unicodedata

class datos_maestros:
    TXT = "reservas_maestro.txt"

    def __init__(self, num_asiento, nombre_pasajero, clase, destino):
        self.num_asiento = num_asiento
        self.nombre_pasajero = nombre_pasajero
        self.clase = clase
        self.destino = destino

    def creacion_datos_maestros(self):
        with open(datos_maestros.TXT, "a", encoding="utf-8") as f:
            f.write(f"{self.num_asiento},{self.nombre_pasajero},{self.clase},{self.destino}\n")

    # normaliza nombres de archivo: sin acentos, minúsculas, espacios->_
    def _normalizar(self, texto):
        t = unicodedata.normalize("NFKD", texto)
        t = "".join(c for c in t if not unicodedata.combining(c))
        t = t.strip().lower().replace(" ", "_")
        return t

    def destinos(self):
        conteo = {}  # archivo_destino -> cantidad
        with open(datos_maestros.TXT, "r", encoding="utf-8") as fr:
            for linea in fr:
                partes = [p.strip() for p in linea.strip().split(",")]
                if len(partes) < 4:
                    continue
                # OJO: usar el destino de la línea, no self.destino
                destino_linea = partes[3]
                destino_norm = self._normalizar(destino_linea)
                archivo_destino = f"reservas_{destino_norm}.txt"

                with open(archivo_destino, "a", encoding="utf-8") as fw:
                    fw.write(",".join(partes) + "\n")

                conteo[archivo_destino] = conteo.get(archivo_destino, 0) + 1

        for nombre, n in conteo.items():
            print(f"{nombre}: {n} reservas")


# Ejemplo
r1 = datos_maestros("12A", "Juan Pérez", "Economy", "Madrid")
r2 = datos_maestros("14B", "María López", "Business", "París")
r3 = datos_maestros("21C", "Carlos García", "Economy", "Madrid")
r4 = datos_maestros("05D", "Ana Sánchez", "Business", "Londres")
r5 = datos_maestros("19E", "Luis Gómez", "Economy", "París")
r6 = datos_maestros("08F", "Sofía Vargas", "Economy", "Londres")

for r in (r1, r2, r3, r4, r5, r6):
    r.creacion_datos_maestros()

r1.destinos()
