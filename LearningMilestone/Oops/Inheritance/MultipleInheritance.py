class division:
    def __init__(self, a, b):
        self.n = a
        self.d = b

    def divide(self):
        return self.n / self.d


class modulus:
    def __init__(self, a, b):
        self.n = a
        self.d = b

    def mod_divide(self):
        return self.n % self.d


class div_mod(division, modulus):
    def __init__(self, a, b):
        self.n = a
        self.d = b

    def div_and_mod(self):
        divval = division.divide(self)
        modval = modulus.mod_divide(self)
        return (divval, modval)

dmod = div_mod(10,4)
print(f'dmod.divide() - {dmod.divide()}')
print(f'dmod.mod_divide() - {dmod.mod_divide()}')
print(f'dmod.div_and_mod() - {dmod.div_and_mod()}')