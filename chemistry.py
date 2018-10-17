class Element:
    mass = 0.0

    def __init__(self, params):
        self.mass = params["mass"]

    def molar_mass_kilograms(self):
        return self.mass / 1000

hydrogen = Element({"mass": 1.00794})
