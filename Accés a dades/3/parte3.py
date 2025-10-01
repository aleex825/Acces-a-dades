from datetime import datetime

MAESTRO_ERR = "reservas_maestro_con_errores.txt"
LOG = "registro_errores.log"

with open(MAESTRO_ERR, "w", encoding="utf-8") as f:
    f.write("12A, Juan Pérez, Economy, Madrid\n")        # válida
    f.write("14B, María López, Business\n")              # falta destino
    f.write("\n")                                        # línea vacía
    f.write("21C; Carlos García; Economy; Madrid\n")     # separador incorrecto
    f.write("[2025-09-20 23:54:00]\n")                   # basura
    f.write("05D, Ana Sánchez, Business, Londres\n")     # válida
    f.write("19E, , Economy, París\n")                   # nombre vacío
    f.write("08F, Sofía Vargas, Economy, Londres, EXTRA\n")  # campo de más

# limpiar / crear log
with open(LOG, "w", encoding="utf-8") as _:
    pass

def log_error(linea_original, descripcion):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG, "a", encoding="utf-8") as s:
        s.write(f"{ts}, {linea_original}, {descripcion}\n")

conteo = {}  # archivo_destino a cantidad

with open(MAESTRO_ERR, "r", encoding="utf-8") as fr:
    for linea in fr:
        original = linea.rstrip("\n")
        linea = linea.strip()
        if linea == "":
            log_error(original, "Línea vacía")
            continue

        partes = [p.strip() for p in linea.split(",")]

        if len(partes) != 4:
            log_error(original, "Formato incorrecto: se esperaban 4 campos separados por comas")
            continue

        asiento, nombre, clase, destino = partes

        # No debe haber campos vacíos
        if asiento == "" or nombre == "" or clase == "" or destino == "":
            log_error(original, "Campos vacíos")
            continue

        archivo_destino = f"reservas_{destino}.txt"
        with open(archivo_destino, "a", encoding="utf-8") as fw:
            fw.write(f"{asiento}, {nombre}, {clase}, {destino}\n")

        conteo[archivo_destino] = conteo.get(archivo_destino, 0) + 1



for nombre_archivo, n in conteo.items():
    print(f"{nombre_archivo}: {n} reservas válidas")

print("\n--- Contenido de registro_errores.log ---")
with open(LOG, "r", encoding="utf-8") as flog:
    contenido = flog.read().strip()
    if contenido == "":
        print("(Sin errores)")
    else:
        print(contenido)
