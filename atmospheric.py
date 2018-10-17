import constants
import math


def minimum_mass(age, temp, radius, mass):
    return (math.log(age/9)*3*constants.universal_gas*temp*radius)/(2 * constants.gravitional * mass)
