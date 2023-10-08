#print('HelloWorld')

#a = int(input('Введите первое значение: '))
#b = int(input('Введите второе значение:'))
#c = a + b
#print (c, "Сумма введенных чисел")

class Robot:
    population = 0
    
    def __init__(self, name):
        self.name = name
        print("init {0}".format(self.name))

    population +=1

    def __del__(self):
        print("{0} delleted".format(self.name))

    population -=1
    
    if population == 0:
        print('Robotov nety')
    else:
        print("We have {0:d} robots".format(population))


    def sayHi(self):
        print("Hello! my name is {0}".format(self.name))


droid1 = Robot("C3PO")
droid1.__init__("C3PO")
droid1.sayHi()
droid1.__del__()

class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age
