# #!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]


class Dog:
    def __init__(self, name = "", breed = ""):
            self._name = name
            self._breed = breed
    
    def get_name(self):
         return self._name

    def set_name(self, name):
        if isinstance(name,str) and 1 <= len(name) <= 25:
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")

    def get_breed(self):
         return self._breed
    
    def set_breed(self, breed):
        if isinstance(breed, str) and breed in APPROVED_BREEDS:
             self._breed = breed
        else:
             print("Breed must be in list of approved breeds.")

    name = property(get_name, set_name,)
    breed = property( get_breed, set_breed,)

fido = Dog()
fido.name = "scooby"
print(fido.name)

fido.breed = "Corgi"
print(fido.breed)

# class Human:
#     species = "Homo sapiens"
#     def __init__(self, name):
#         self.name = name
#         self._age = 0

#     def get_age(self):
#         print("Retrieving age.")
#         return self._age

#     def set_age(self, age):
#         if (type(age) in (int, float)) and (0 <= age <= 120):
#             print(f"Setting age to { age }.")
#             self._age = age

#         else:
#             print("Age must be a number between 0 and 120.")

#     age = property(get_age, set_age,)


# abdi = Human("abdi")
# abdi.age = 121
