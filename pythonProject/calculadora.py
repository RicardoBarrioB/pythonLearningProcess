
class calculadora:

    def suma(*args):
        resul = 0
        for num in args:
            if type(num) == int or type(num) == float:
                resul += num
        print('La suma de los numeros es ', resul)

    def resta(x, *args):
        resul = x
        for num in args:
            if type(num) == int or type(num) == float:
                resul -= num
        print('El resultado es ', resul)

    def multi(*args):
        resul = 1
        for num in args:
            if type(num) == int or type(num) == float:
                resul *= num
        print('La multiplicacion de los numeros es ', resul)

    def div(x, *args):
        resul = x
        for num in args:
            if type(num) == int or type(num) == float:
                resul /= num
        print('El resultado es ', resul)

x = 20
y = 10
z = 5
t = 2.0

array = [1,2,4,5,6,7,8]

calculadora.suma(x, y, z, t)
print(type(x), type(y), type(z), type(t))
calculadora.resta(x, y, z, t)
print(type(x), type(y), type(z), type(t))
calculadora.multi(x, y, z, t)
print(type(x), type(y), type(z), type(t))
calculadora.div(x, y, z, t)
print(type(x), type(y), type(z), type(t))

calculadora.suma(*array)