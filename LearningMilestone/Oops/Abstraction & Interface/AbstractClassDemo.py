from abc import ABC, abstractmethod


class Abclass(ABC):
    @abstractmethod
    def abmethod(self):
        print("Abstract Method")
        #return

    def fullMethod(self):
        print("Concrete method")
        #return
#ab = Abclass() #Not allowed to instatiate the Abstract class
#ab.abmethod()

class SubClass(Abclass):
    def abmethod(self):
        super().abmethod()
        #return

sc = SubClass()
sc.abmethod()
sc.fullMethod()