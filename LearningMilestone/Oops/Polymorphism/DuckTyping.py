class Duck:
    def sound(self):
        return "Quack, quack"
class OtherBird:
    def sound(self):
        return "Koo, koo"

def makesound(bird):
    print(bird.sound())

dk = Duck()
ob = OtherBird()
makesound(dk)
makesound(ob)
