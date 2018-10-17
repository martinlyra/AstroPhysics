import constants


def escape_velocity(m, r):
    e1 = pow(constants.gravitional*m/r, 0.5)/constants.kilo
    e2 = e1 * pow(2, 0.5)
    return [e1, e2]


def gravity_pull(mass, radius):
    return (constants.gravitional * mass) / pow(radius, 2)


def gravity_distance(gravity, mass):
    return pow((constants.gravitional * mass) / gravity, 0.5)
