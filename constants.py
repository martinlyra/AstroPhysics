import physical

# physical
gravitional = 6.674 * pow(10,-11) # (m/kg)^2
universal_gas = 8.3144621

# time constants in seconds
minute = 60
hour = 60 * minute
day = 24 * hour
year = 365 * day

# quantity
kilo = pow(10,3)
million = mega = pow(10,6)
billion = giga = pow(10,9)

# stellar distances
au = 149597871 * kilo

# stellar masses
earth_mass = 5.972 * pow(10, 24)
jupiter_mass = 1.898 * pow(10, 27)
solar_mass = 1.9891 * pow(10, 30)

# stellar radii
earth_radius = 6371 * kilo
jupiter_radius = 69911 * kilo
solar_radius = 695700 * kilo

# known gravity pulls
earth_gravity = physical.gravity_pull(earth_mass, earth_radius)
