import atmospheric
import orbital
import constants

import physical
import chemistry


def vec_to_rgb(r,g,b):
    return [int(255*r), int(255*g), int(255*b)]

Mk = 8.991 * constants.earth_mass
Rk = 1.808 * constants.earth_radius
Tk = 1227

#Mk = 4.861 * constants.earth_mass
#Rk = 1.817 * constants.earth_radius
#Tk = 1227

# print(orbital.calculate_period(1206.03 * constants.kilo, 1.32 * constants.solar_mass)/constants.year)

print(atmospheric.minimum_mass(1 * constants.billion, 1000, constants.earth_radius, constants.earth_mass))
print(atmospheric.minimum_mass(5.6112 * constants.billion, Tk, Rk, Mk))

print(physical.gravity_pull(Mk, Rk)/constants.earth_gravity)

print(atmospheric.minimum_mass(4.562 * constants.billion, 1000, constants.jupiter_radius, constants.jupiter_mass))
print(atmospheric.minimum_mass(5.6112 * constants.billion, Tk, Rk,
                               chemistry.hydrogen.molar_mass_kilograms()) / constants.earth_mass)

print(physical.gravity_distance(2.8328 * constants.earth_gravity, Mk)/constants.kilo)
print(physical.gravity_distance(2.7505 * constants.earth_gravity, Mk)/constants.kilo)
print(physical.gravity_distance(2.709 * constants.earth_gravity, Mk)/constants.kilo)

