# Mitchell Young
import math as ma


data=open("planet_data.dat","r")

#Planet name
name=str.capitalize(str.lower(raw_input("What is the name of the planet? Type help for options: ")))
if name=="Help":
    print "Mercury, Venus, Earth, Mars, Ceres, Jupiter, Saturn, Uranus, Neptune, Pluto, Eris, Comet, Proxima Centuari b, or Kepler-37b"
    name=str.capitalize(str.lower(raw_input("What is the name of the planet? See above list: ")))

#print data.line[0]

"""
#Other inputs
alt=int(raw_input("What is your altitude?"))

if line[0]==name:


#4/3*pi*R^3*P

print "Planet:",name
"""
