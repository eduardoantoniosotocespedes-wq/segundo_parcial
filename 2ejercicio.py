temperaturas = []

print("Ingresa la temperatura máxima de cada día de la semana:")
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

for dia in dias:
    temp = float(input(f"{dia}: "))
    temperaturas.append(temp)

print(f"\nTemperaturas registradas: {temperaturas}")

temp_alta = temperaturas[0]
temp_baja = temperaturas[0]

for t in temperaturas:
    if t > temp_alta:
        temp_alta = t
    if t < temp_baja:
        temp_baja = t

print(f"\nTemperatura más alta de la semana: {temp_alta}°C")
print(f"Temperatura más baja de la semana: {temp_baja}°C")

contador_calor = 0
for t in temperaturas:
    if t > 25:
        contador_calor += 1

print(f"\nDías que superaron los 25°C: {contador_calor}")