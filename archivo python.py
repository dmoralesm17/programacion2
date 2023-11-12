
def ingresar_informacion():
    print("(1) Ingresar mascota al registro")
    print("(2) Ingresar registro de ultima vacunacion")
    print("(3) Estado de extraviado")
def ingresar_mascota():
    input("Nombre de la mascota:")
    input("N° de chip:")
    input("Nombr del tutor:")
    input("Fecha ultima vacuna:")


datos_guardados = {
    21738: {"Nombre de la mascota": "Hercules", "Nombre del tutor": "Braian Inostroza", "N° de chip": "21738", "UltimaVacuna": "10/10/2023", "Estado de vacunacion": "Vigente", "Alerta de extravio": "No extraviado"},
    45637: {"Nombre de la mascota": "Chop", "Nombre del tutor": "Martin Rubilar", "N° de chip": "45637", "UltimaVacuna": "7/8/2023", "Estado de vacunacion": "Vigente", "Alerta de extravio": "No extraviado"},
    32468: {"Nombre de la mascota": "Ares", "Nombre del tutor": "Benjamin Caroca", "N° de chip": "32468", "UltimaVacuna": "6/11/2022", "Estado de vacunacion": "No vigente", "Alerta de extravio": "No extraviado"},
    21463: {"Nombre de la mascota": "Limon", "Nombre del tutor": "Claudio Villagran", "N° de chip": "21463", "UltimaVacuna": "9/4/2023", "Estado de vacunacion": "Vigente", "Alerta de extravio": "Extraviado"}
}

def mostrar_datos(numero):
    if numero in datos_guardados:
        datos = datos_guardados[numero]
        print(f"datos asociados al numero {numero}:")
        for clave, valor in datos.items():
            print(f"{clave}: {valor}")
    else:
        print(f"No hay datos asociados al numero {numero}.")


def ingresar_ultima_vacuna():
    datos_mascotas = {
        "21738": {"Nombre Mascota": "Hercules", "UltimaVacuna": "10/10/2023"},
        "45637": {"Nombre Mascota": "Chop", "UltimaVacuna": "07/08/2023"},
        "32468": {"Nombre Mascota": "Ares", "UltimaVacuna": "06/11/2023"},
        "21643": {"Nombre Macota": "limon", "UltimaVacuna": "09/04/2023"},
    }

    numero_chip = input("Ingrese N° de chip de la mascota:")

    if numero_chip in datos_mascotas:
        nueva_fecha_vacuna = input("Ingrese la última fecha de vacunación (DD/MM/AAAA): ")
        datos_mascotas[numero_chip]["UltimaVacuna"] = nueva_fecha_vacuna
        print("La fecha de vacunación ha sido actualizada.")
    else:
        print("No se encontró ninguna mascota con el N° de chip proporcionado.")

datos_mascotas = {
    "21738": {"Nombre": "Hercules", "UltimaVacuna": "10/10/2023", "Extraviado": False},
    "45637": {"Nombre": "Ares", "UltimaVacuna": "07/08/2023", "Extraviado": False},
    "32468": {"Nombre": "Ares", "UltimaVacuna": "06/11/2023", "Extraviado":False},
    "21643": {"Nombre": "Limon", "UltimaVacuna": "09/04/2023", "Extraviado": True}
}


user1 = "Daniel Schmidt"
user2 = "Jayden Rogers"
psw1 = "tigre54lunes"
psw2 = "leon79martes"
intentos_limite = 3
intentos = 0
while intentos < intentos_limite:
 print("- Ingrese sus datos.")
 print("Usuario: ")
 user = input()
 print("Contraseña: ")
 psw = input()
 if user==user1 and psw==psw1:
    print("Bienvenido al sistema, Doctor Schmidt.")
    intentos = 4
 elif user==user2 and psw==psw2:
    print("Bienvenido al sistema, Doctor Rogers.")
    intentos = 4
 else: 
    print("El usuario o la contraseña no son válidos. ")
    intentos += 1
if intentos == intentos_limite:
    print("Demasiados intentos. Acceso Bloqueado.")
print("Bienvenido a Veterinaria PetHealthy")
print("Menu de servicios:")
print("(1) Ingresar informacion")
print("(2) Consultar informacion")

opcion_principal = input("Seleccione una opcion:")
if opcion_principal == "1":
    usr = input("Ingrese su usuario:")
    psw = input("Ingrese su contraseña:")
    ingresar_informacion()

elif opcion_principal =="2":
    usr = input("ingrese su usuario:")
    psw = input("Ingrese su contraseña:")
    numero_ingresado = int(input("Ingrese el N° de chip:"))
    mostrar_datos(numero_ingresado)
input()

sub_opcion_1 = input("Seleccione una opcion:")
if sub_opcion_1 =="1":
    ingresar_mascota()
elif sub_opcion_1 =="2":
    ingresar_ultima_vacuna()
elif sub_opcion_1 =="3":
    numero_chip = input("Ingrese N° de chip de la mascota:")
    if numero_chip in datos_mascotas:
        confirmacion = input(f"¿Está seguro de marcar como extraviada a la mascota con N° de chip {numero_chip}? (Sí/No): ").lower()
        
        if confirmacion == "si":
            datos_mascotas[numero_chip]["Extraviado"] = True
            print(f"La mascota con N° de chip {numero_chip} ha sido marcada como extraviada.")
        else:
            print("Operación cancelada.")
    else:
        print("No se encontró ninguna mascota con el N° de chip proporcionado.")

# Mostrar datos después de la operación
print("Datos de las mascotas después de la operación:")
print(datos_mascotas)
    









