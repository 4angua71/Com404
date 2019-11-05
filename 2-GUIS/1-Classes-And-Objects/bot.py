class Bot:
    def __init__(self, name, age, energy, shieldlevel):
        self.name = name
        self.age = age
        self.energy= energy
        self.shieldlevel= shieldlevel

    def display_name(self):
        print("*" + "*"*(len(self.name))+"*")
        print("*"+ str(self.name) + "*")
        print("*" + "*"*(len(self.name))+"*")


    def display_age(self):
        print(" * "*int(self.age))
        print(" * "*int(self.age))
        print(" | "*int(self.age))
        print(" | "*int(self.age))
        print("*" + "*"*(int(self.age)*3)+"*")
        print("*" + " "*(int(self.age)*3)+"*")
        print("*" + " "*(int(self.age)*3)+"*")
        print("*" + "*"*(int(self.age)*3)+"*")
        print("*" + " "*(int(self.age)*3)+"*")
        print("*" + " "*(int(self.age)*3)+"*")
        print("*" + "*"*(int(self.age)*3)+"*")


    def display_energy(self):
        print(" Energy: " + int(self.energy)*('|'))

    def display_shield(self):
        print(" Shields: (( " + str(self.shieldlevel)+ " ))")

    def display_summary(self):
        print(" Name: "+ (len(self.name))*('*'))
        print(" Age: "+ int(self.age)*('♦'))
        print(" Energy: "+ int(self.energy)*('♥'))
        print(" Shields: " + int(self.shieldlevel)*('♦'))

    def  __str__ (self):
        print("{} is {} years old and has an energy level of {} and a shield level of {}".format(self.name, self.age, self.energy, self.shieldlevel))

nono = Bot("NoNo", 10, 5, 5)

nono.display_name()
nono.display_age()
nono.display_energy()
nono.display_shield()
nono.display_summary()
nono.__str__()

