class estudiante():



    def __init__(self, nombre, apellido1, apellido2, curso, clase):
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.curso = curso
        self.clase = clase

    def __str__(self):
        atributos = list(vars(self).items())
        atributos_valor = [f"{nombre} = {valor}" for nombre, valor in atributos]
        return "\n".join(atributos_valor)



a = estudiante('Pablo', 'Lopez', 'Fernandez', 2, '2ºA')
b = estudiante('Ricardo', 'Barrio', 'Perez', 1, '1ºB')

estudiantes = [a, b]

print(a)

