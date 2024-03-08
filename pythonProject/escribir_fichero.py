
import estudiante

a = estudiante.estudiante('Pablo', 'Lopez', 'Fernandez', 2, '2ºA')
b = estudiante.estudiante('Ricardo', 'Barrio', 'Perez', 1, '1ºB')

estudiantes = [a, b]


f = open("pruebas.txt","w",encoding="utf8")
f.write(b.__str__())







