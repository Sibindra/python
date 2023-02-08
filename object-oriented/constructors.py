class Person:
    def __init__(self,name,occ):
        self.name = name
        self.occ = occ


    def info(self):
        print('Name: ', self.name)
        print('Occ: ', self.occ)

hari = Person('Hari','Developer')
ram = Person('Ram','HR')

c = Person(1,2)

hari.info()
c.info()