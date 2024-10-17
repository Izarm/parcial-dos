from operator import truediv

Salario_base_mensual = int(input ("Salario base mensual $: "))
Cargo_empleado = input("Cargo empleado: ").lower()
Nivel_de_desempeño = input("Nivel de desempeño: ").lower()
desempeño_alto_directivo = 0.2
desempeño_medio_directivo = 0.1
desempeño_bajo_directivo = 0.0
desempeño_alto_operativo = 0.15
desempeño_medio_operativo = 0.05
desempeño_bajo_operativo = 0.0
bonificacion_auxiliar = 0.0





if Cargo_empleado == "directivo" and Nivel_de_desempeño == "alto":
    Bonificacion = Salario_base_mensual * desempeño_alto_directivo
    resultado = Bonificacion + Salario_base_mensual
    print(f"-----Resumen del Pago-----\n"
          f"Cargo: {Cargo_empleado.capitalize()}\n"
          f"Nivel De Desempeño: {Nivel_de_desempeño.capitalize()}\n"
          f"Salario Base: ${Salario_base_mensual}\n"
          f"Bonificación: ${Bonificacion}\n"
          f"Total a Recibir: ${resultado}\n"
          f"------------------------------------")

elif Nivel_de_desempeño == "medio" and Cargo_empleado == "directivo":

    Bonificacion = Salario_base_mensual * desempeño_medio_directivo
    resultado = Bonificacion + Salario_base_mensual
    print(f"-----Resumen del Pago-----\n"
          f"Cargo: {Cargo_empleado.capitalize()}\n"
          f"Nivel De Desempeño: {Nivel_de_desempeño.capitalize()}\n"
          f"Salario Base: ${Salario_base_mensual}\n"
          f"Bonificación: ${Bonificacion}\n"
          f"Total a Recibir: ${resultado}\n"
          f"------------------------------------")
elif Nivel_de_desempeño == "bajo" and Cargo_empleado == "directivo":

    Bonificacion = Salario_base_mensual * desempeño_bajo_directivo
    resultado = Bonificacion + Salario_base_mensual
    print(f"-----Resumen del Pago-----\n"
          f"Cargo: {Cargo_empleado.capitalize()}\n"
          f"Nivel De Desempeño: {Nivel_de_desempeño.capitalize()}\n"
          f"Salario Base: ${Salario_base_mensual}\n"
          f"Bonificación: ${Bonificacion}\n"
          f"Total a Recibir: ${resultado}\n"
          f"------------------------------------")

elif Nivel_de_desempeño == "alto" and Cargo_empleado == "operativo":

    Bonificacion = Salario_base_mensual * desempeño_alto_operativo
    resultado = Bonificacion + Salario_base_mensual
    print(f"-----Resumen del Pago-----\n"
          f"Cargo: {Cargo_empleado.capitalize()}\n"
          f"Nivel De Desempeño: {Nivel_de_desempeño.capitalize()}\n"
          f"Salario Base: ${Salario_base_mensual}\n"
          f"Bonificación: ${Bonificacion}\n"
          f"Total a Recibir: ${resultado}\n"
          f"------------------------------------")

elif Nivel_de_desempeño == "medio" and Cargo_empleado == "operativo":

    Bonificacion = Salario_base_mensual * desempeño_medio_operativo
    resultado = Bonificacion + Salario_base_mensual
    print(f"-----Resumen del Pago-----\n"
          f"Cargo: {Cargo_empleado.capitalize()}\n"
          f"Nivel De Desempeño: {Nivel_de_desempeño.capitalize()}\n"
          f"Salario Base: ${Salario_base_mensual}\n"
          f"Bonificación: ${Bonificacion}\n"
          f"Total a Recibir: ${resultado}\n"
          f"------------------------------------")
elif Nivel_de_desempeño == "bajo" and Cargo_empleado == "operativo":

    Bonificacion = Salario_base_mensual * desempeño_bajo_operativo
    resultado = Bonificacion + Salario_base_mensual
    print(f"-----Resumen del Pago-----\n"
          f"Cargo: {Cargo_empleado.capitalize()}\n"
          f"Nivel De Desempeño: {Nivel_de_desempeño.capitalize()}\n"
          f"Salario Base: ${Salario_base_mensual}\n"
          f"Bonificación: ${Bonificacion}\n"
          f"Total a Recibir: ${resultado}\n"
          f"------------------------------------")
elif Nivel_de_desempeño == "alto" and Cargo_empleado == "auxiliar":

    Bonificacion = Salario_base_mensual * bonificacion_auxiliar
    resultado = Bonificacion + Salario_base_mensual
    print(f"-----Resumen del Pago-----\n"
          f"Cargo: {Cargo_empleado.capitalize()}\n"
          f"Nivel De Desempeño: {Nivel_de_desempeño.capitalize()}\n"
          f"Salario Base: ${Salario_base_mensual}\n"
          f"Bonificación: ${Bonificacion}\n"
          f"Total a Recibir: ${resultado}\n"
          f"------------------------------------")

elif Nivel_de_desempeño == "medio" and Cargo_empleado == "auxiliar":

    Bonificacion = Salario_base_mensual * bonificacion_auxiliar
    resultado = Bonificacion + Salario_base_mensual
    print(f"-----Resumen del Pago-----\n"
          f"Cargo: {Cargo_empleado.capitalize()}\n"
          f"Nivel De Desempeño: {Nivel_de_desempeño.capitalize()}\n"
          f"Salario Base: ${Salario_base_mensual}\n"
          f"Bonificación: ${Bonificacion}\n"
          f"Total a Recibir: ${resultado}\n"
          f"------------------------------------")

elif Nivel_de_desempeño == "bajo" and Cargo_empleado == "auxiliar":

    Bonificacion = Salario_base_mensual * bonificacion_auxiliar
    resultado = Bonificacion + Salario_base_mensual
    print(f"-----Resumen del Pago-----\n"
          f"Cargo: {Cargo_empleado.capitalize()}\n"
          f"Nivel De Desempeño: {Nivel_de_desempeño.capitalize()}\n"
          f"Salario Base: ${Salario_base_mensual}\n"
          f"Bonificación: ${Bonificacion}\n"
          f"Total a Recibir: ${resultado}\n"
          f"------------------------------------")




































