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

    # @MyProperty desugars to:  age = MyProperty(age)
    @property  # type: ignore[reportRedeclaration]
    def age(self):
        return self.__x - 2

    # @age.setter desugars to:  age = age.setter(age)
    @age.setter  # type: ignore[reportRedeclaration]
    def age(self, value):
        if value > 30:
            self.__x = 30
        else:
            self.__x = value

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
print(person.get_fullname())
print(person)
print(type(person))
print(isinstance(person, Person))
print(isinstance(person, object))
