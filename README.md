# class-129-plantesdata
# https://spaceplace.nasa.gov/all-about-exoplanets/en/


# All of the planets in our solar system orbit around the Sun. Planets that orbit around other stars are called exoplanets. Exoplanets are very hard to see directly with telescopes. They are hidden by the bright glare of the stars they orbit.
# So, astronomers use other ways to detect and study these distant planets. They search for exoplanets by looking at the effects these planets have on the stars they orbit.
name - This is the name of the exo-planet.

light_years_from_earth - This is the distance of this planet from Earth in light years. 1
light year is the distance light can travel in one year, and light it super fast. It can travel
9.461 Trillion km in 1 year.


planet_mass - This is the mass of the planet with respect to Earth or Jupiter (Jupiter is
the metric for Gas Giants while Earth is the metric for all other types of planets).

stellar_magnitude - This is the brightness of the host star of the planet when observed
from Earth (just as the sun is our host star).

discovery_date - This is the year of discovery for the exo-planet.

hyperlink - This is just the hyperlink that we scraped.

planet_type - This is the type of the planet (Gas Giant, Super Earth, etc.).

temp_planet_date - This is a duplicate.

temp_planet_mass - This is another duplicate.

planet_radius - This is the radius of the exo-planet with respect to Earth or Jupiter.

orbital_radius - This is the average distance of this exo-planet from its sun. Just like our
solar system has 1 sun, there are multiple solar systems that contain many planets and
sun(s).

orbital_period - This is the time it takes to complete one orbit of it’s sun.

eccentricity - This denotes how circular the orbit is. It might be oval in shape too. The
lower the eccentricity, the more circular is the orbit.

pl_hostname - The name of the host solar system.

pl_letter - The letter given to this planet.

pl_name - The name of this planet (short version).

pl_discmethod - This is the discovery method which was used to find this exo-planet.

pl_controvflag - This is a boolean (0, 1) which says if the existence of this planet is
questioned or not.

pl_pnum - This is the number of planets that are there in its solar system.

pl_orbper - This is again, the orbital period in days.
Now since we are collecting data for planets that exist so far away from us, there is no
way for us to know the actual values of a planet, such as their orbital period, radius, etc.
so we do calculations for it. Each calculation is based on observation such as here, can
have a margin of error in the actual value. Thus, all the columns with err1 and err2 are
the scope of errors, and we will ignore them.

pl_orbperlim - This is again the radius of the orbit of the planet.

pl_orbeccen - This is again the eccentricity of the planet.

pl_orbincl - This is the orbital inclination, which means that it is the tilt of the exo-planet’s
orbit when it revolves around its sun.

pl_bmassj - This is again the mass of the planet.

pl_bmassprov - This is the unit to calculate the mass.

pl_radj - This is again, the radius of the planet.

pl_dens - This is the density of the planet.

pl_ttvflag - This is a flag that indicates if this planet's orbit exhibits any timing variations
from other planets in the system.

pl_kepflag - This is a flag that tells if the solar system exhibits a planetary system
(multiple planets) based on Kepler Field Mission.

pl_k2flag - This is a flag that tells if the solar system exhibits a planetary system based
on the K2 Mission.

pl_nnotes - This is just the number of notes associated with the planet.

ra_str - This is the right ascension of the planetary system, which is the east-west
coordinate by which the position of this planet is measured.

dec_str - This is the north-south coordinate by which the position of the planet is
measured.

st_dist - This is again the distance of the planet from Earth.

gaia_dist - This is again the distance of the planet from Earth in Gaia Parallax. Gaia
Parallax is the coordinate that is calculated with Trigonometry.

st_optmag - This is the Optical magnitude (discussed earlier).

st_optband - There are different bands in light. This is the band of the optical magnitude.

gaia_gmag - This is the magnitude of the host star of the planet measured in G-Band.

st_teff - This is the temperature of the host star in Kelvin.

st_mass - This is the amount of mass contained in the host star.

st_rad - This is the radius of the host star.

rowupdate - This is the date of last update for this exo-planet.

pl_facility - Facility at which the planet was discovered (There are many facilities that are
observing and looking for new planets/stars in our galaxy).












