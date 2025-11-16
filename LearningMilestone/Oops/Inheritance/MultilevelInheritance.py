class state:
    def __init__(self, name, code):
        self.statename = name
        self.statecode = code
    def stateInfo(self):
        print(f"State name - {self.statename} and state code - {self.statecode}")
class district(state):
    def __init__(self, name, code, dname, dcode):
        super().__init__(name, code)
        self.districtename = dname
        self.districtcode = dcode
    def districtInfo(self):
        print(f"District name - {self.districtename} and District code - {self.districtcode}")
class city(district):
    def __init__(self, name, code, dname, dcode, cname, ccode):
        super().__init__(name, code, dname, dcode)
        self.cityname = cname
        self.citycode = ccode

    def cityInfo(self):
        print(f"city name - {self.cityname} and city code - {self.citycode}")

c = city("Karnata", 2143, "Belgaum", 590001, "Belagavi", 590001)
c.stateInfo()
c.districtInfo()
c.cityInfo()