class SingletonInit:
    __uniquInstance = None

    @staticmethod
    def createInstance():
        if SingletonInit.__uniquInstance == None:
            print("Singleton object is created")
            SingletonInit()
        return SingletonInit.__uniquInstance

    def __init__(self):
        if SingletonInit.__uniquInstance != None:
            raise Exception('Object exists!')
        else:
            SingletonInit.__uniquInstance = self

s1 = SingletonInit()          # __init__ called → __uniquInstance = s1
s1.createInstance()           # __uniquInstance already set, returns s1
print(s1)                     # prints object reference

s2 = SingletonInit()          # __init__ called → raises Exception('Object exists!')
s2.createInstance()           # never reached
print(s2)                     # never reached