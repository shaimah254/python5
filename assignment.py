from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Abstract base class representing an animal.
    """
    
    def __init__(self, name: str, habitat: str):
        """
        Initialize an Animal instance.
        
        Args:
            name (str): The animal's common name
            habitat (str): Primary habitat of the animal
        """
        self.name = name
        self.habitat = habitat
        
    @abstractmethod
    def move(self) -> str:
        """
        Abstract method defining how the animal moves.
        To be implemented by concrete subclasses.
        """
        pass
    
    def describe(self) -> str:
        """
        Provide a basic description of the animal.
        """
        return f"A {self.name} that lives in {self.habitat}."


class Bird(Animal):
    """
    A class representing birds that can fly.
    """
    
    def move(self) -> str:
        """
        Birds move by flying.
        """
        return "🦅 Flying through the air with wings!"
    
    def describe(self) -> str:
        """
        Enhanced description including bird-specific info.
        """
        return f"{super().describe()} It's a bird that can fly."


class Fish(Animal):
    """
    A class representing fish that swim.
    """
    
    def move(self) -> str:
        """
        Fish move by swimming.
        """
        return "🐠 Swimming gracefully through the water!"
    
    def describe(self) -> str:
        """
        Enhanced description including fish-specific info.
        """
        return f"{super().describe()} It's a fish that can swim."


class Snake(Animal):
    """
    A class representing snakes that slither.
    """
    
    def move(self) -> str:
        """
        Snakes move by slithering.
        """
        return "🐍 Slithering smoothly across surfaces!"
    
    def describe(self) -> str:
        """
        Enhanced description including snake-specific info.
        """
        return f"{super().describe()} It's a snake that can slither."


class Kangaroo(Animal):
    """
    A class representing kangaroos that hop.
    """
    
    def move(self) -> str:
        """
        Kangaroos move by hopping.
        """
        return "🦘 Hopping powerfully with strong hind legs!"
    
    def describe(self) -> str:
        """
        Enhanced description including kangaroo-specific info.
        """
        return f"{super().describe()} It's a marsupial that can hop."


# Demonstration of polymorphism
if __name__ == "__main__":
    animals = [
        Bird("Eagle", "mountains"),
        Fish("Clownfish", "coral reefs"),
        Snake("Python", "jungles"),
        Kangaroo("Red Kangaroo", "Australian outback")
    ]
    
    for animal in animals:
        print("\n" + animal.describe())
        print(animal.move())