import math
import constants


def calculate_period(semi_major, parent_mass):
    gm = constants.gravitional * parent_mass
    t = 2 * math.pi * pow(pow(semi_major, 3)/gm, 0.5)
    return t
