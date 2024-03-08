

def comprobar(cadena):
    primero = id(cadena)
    nombre_variable = [nombre for nombre, valor in locals().items() if valor is cadena][0]
    print('variable ' + nombre_variable, id(cadena), type(cadena))
    cadena = 1
    print('variable ' + nombre_variable + ':', id(cadena), type(cadena))
    segundo = id(cadena)

    if primero != segundo:
        print('Los ids son diferentes ya que el tipo es inmutable')

comprobar('cadena')









