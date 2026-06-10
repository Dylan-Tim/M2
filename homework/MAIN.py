from abc import ABC, abstractmethod


# ── ABSTRACT BASE CLASS (Parent) ──────────────────────────────────────────────
# Animal inherits from ABC — this makes it an abstract class (Abstraction)
class Instrument(ABC):

    # Parent constructor — stores attributes shared by ALL animals
    def __init__(self, name, noise):
        self.name = name
        self.noise = noise

    # Concrete method — all child classes inherit this for free
    def display(self):
        print(f"Name: {self.name}  |  noise: {self.noise}")

    # Abstract method — every child class MUST implement this
    @abstractmethod
    def speak(self):
        pass


# ── CHILD CLASS 1 ─────────────────────────────────────────────────────────────
class Drums(Instrument):

    def __init__(self, name, noise, breed):
        super().__init__(name, noise)   # calls Animal's constructor
        self.breed = breed

    def speak(self):
        print(f"{self.name} ({self.breed}) says: da dum!")


# ── CHILD CLASS 2 ─────────────────────────────────────────────────────────────
class Guitar(Instrument):

    def __init__(self, name, noise, phrase):
        super().__init__(name, noise)
        self.phrase = phrase

    def speak(self):
        print(f"{self.name} says: {self.phrase}! {self.phrase}!")


# ── CHILD CLASS 3 ─────────────────────────────────────────────────────────────
class Ukelele(Instrument):

    def __init__(self, name, noise, pride):
        super().__init__(name, noise)
        self.pride = pride

    def speak(self):
        print(f"{self.name} (Pride: {self.pride}) says: sttt!")


# ── CREATE OBJECTS & RUN THE SHOW ─────────────────────────────────────────────
Drums    = Drums("Drums",  "da dum!",      "bass family")
Guitar = Guitar("Guitar",  "sttt!",    "string family")
Ukelele   = Ukelele("Ukelele",  "lololo!",  "string family")

print("=== music Sound Show ===\n")
for music in [Drums, Guitar, Ukelele]:
    music.display()
    music.speak()
    print()