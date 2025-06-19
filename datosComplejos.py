empleados = [{"nombre":"Pepe", "edad":22, "departamento":"DAM", "salario":1200},
             {"nombre":"Juan", "edad":45, "departamento":"DAW", "salario":1890},
             {"nombre":"Maria", "edad":19, "departamento":"DAM", "salario":1230},
             {"nombre":"Alex", "edad":28, "departamento":"DAW", "salario":1740},
             {"nombre":"Ana", "edad":26, "departamento":"ASIR", "salario":1460},
             {"nombre":"Felipe", "edad":36, "departamento":"DAM", "salario":1150},
             {"nombre":"Jaime", "edad":40, "departamento":"DAW", "salario":1100},
             {"nombre":"Maribel", "edad":32, "departamento":"ASIR", "salario":1450}
             ]

def filtrarDepartamento(empleados):
    departamento = input("Dime el nombre del departamento: ")
    empleados_filtrados = []
    for empleado in empleados:
        if empleado["departamento"] == departamento:
            empleados_filtrados.append(empleado)
    return empleados_filtrados
        
# print("Empleados del departamento:")
# empleados_DAM = filtrarDepartamento(empleados)
# for empleado in empleados_DAM:
#     print(empleado)
    
def calcularSalarioTotal(empleados):
    salarioTotal = 0
    for empleado in empleados:
        salarioTotal += empleado["salario"]
    return salarioTotal

#print(f"El salario total de la empresa es: {calcularSalarioTotal(empleados)}")

def salarioMasAlto(empleados):
    empleadoMaspagado = 0
    max = 0
    for empleado in empleados:
        if empleado["salario"] > max:
            max = empleado["salario"]
            empleadoMaspagado = empleado
    return empleadoMaspagado

# Mostrar el empleado mejor pagado
empleado_mejor_pagado = salarioMasAlto(empleados)
print(f"El empleado mejor pagado es: {empleado_mejor_pagado['nombre']} con un salario de {empleado_mejor_pagado['salario']}")

# Ordenar empleados por edad
def ordenaPorEdad(empleados):
    return sorted(empleados, key=lambda empleado: empleado["edad"])

masjoven = ordenaPorEdad(empleados)
print("los empleados de menor a mayor son:")
for empleado in masjoven:
    print(f"{empleado['nombre']} - {empleado['edad']} años")
        
