class MyProperty:
    def __init__(self, fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def getter(self, fget):
        return MyProperty(fget, self.fset, self.fdel)

    def setter(self, fset):
        return MyProperty(self.fget, fset, self.fdel)

    def deleter(self, fdel):
        return MyProperty(self.fget, self.fset, fdel)

    def __get__(self, instance, owner):
        if instance is None:          # accessed on the class, not an instance
            return self

        if self.fget is None:
            raise AttributeError("can't get attribute")

        return self.fget(instance)

    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")

        self.fset(instance, value)

    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")

        self.fdel(instance)


class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.__x = age

    def _age_get(self):
        return self.__x - 2

    def _age_set(self, value):
        if value > 30:
            self.__x = 30
        else:
            self.__x = value

    age = MyProperty(_age_get, _age_set)

    def greet(self, message):
        self.has_greet = True
        print(f"{self.firstname} {self.lastname} says {message}!")
    
    def get_fullname(self):
        return f"{self.firstname} {self.lastname}"
    
    def __str__(self):
        return f"A person named {self.get_fullname()} aged {self.age}"

person = Person("Federico", "Bolelli", 20)  # What do you mean I don't look 20? 😅
person.greet("I love Beer 🍺🍺!")
print(person.age)

person.age += 54
# person.set_age(person.get_age() + 54)
print(person.get_fullname())
print(person)
print(type(person))
print(isinstance(person, Person))
print(isinstance(person, object))

# "Federico" in [person1, person2]

# class GameCharacter:

#     def __init__(self, name, health=50, strength=30, defence=20):
#         self.name = name
#         self.health = health
#         self.strength = strength
#         self.defence = defence


#     def attack(self, victim):
#         victim.health = victim.health - self.strength
#         print(f"Bam! {self.name} attacked {victim.name}.", 
#              f"{victim.name}'s health is now {victim.health}")


#     def defend(self, attacker):
#         self.health = self.health - attacker.strength * 0.25
#         print(f"{self.name} defended against {attacker.name}.",
#              f"{self.name}'s health is now {self.health}")

#     def __str__(self):
#         return (f"{self.name} is a GameCharacter (health: {self.health}, "
#                 f"strength: {self.strength}, defence: {self.defence})")

# class Enemy(GameCharacter, ):

#     def __init__(self, name, health=50, strength=30, defence=20, evilness=50):
#         # call the constructor of the superclass
#         super().__init__(name, health, strength, defence)
#         self.evilness = evilness


#     def evil_laugh(self):
#         print("Heheheheheeeeee!!")    


#     def __str__(self):
#         return (super().__str__().replace("GameCharacter", "Enemy").replace(")", ",") 
#                 + f" evilness: {self.evilness})")


# boy = GameCharacter("Boy", 100, 20, 10)
# evilman = Enemy("Voldemort", 30, 50, 40, 100)
# print(boy)
# print(evilman)
# evilman.attack(boy)
# boy.defend(evilman)
# boy.evil_laugh()  # You should get an error here.

