class Person:
    name = None
    occupation = None
    net_worth = None

    def info(self):
        print('Name: ',self.name)
        print('Occupation: ',self.occupation)
        print('Net worth: ',self.net_worth)

# a is an instance of person
a = Person()
a.name = 'Hari'
a.occupation = 'Salesman'
a.net_worth = 1000


b = Person()
b.name = 'Rita'
b.occupation = 'HR'
b.net_worth = 100

c = Person()

# a.info()
# b.info()
c.info()



