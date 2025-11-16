from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def draw(self):
        "Abrstract Method"
        return
class Circle(Shape):
    def draw(self):
        print("Drawing cIrcle")
        return
class Rectangle(Shape):
    def draw(self):
        print("Drawing Rectangle")
        return

shape = [Circle(),Rectangle()]
for sp in shape:
    sp.draw()