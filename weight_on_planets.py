# Mitchell Young
import math as ma

with open("planet_data.dat","r") as doc:
    data=doc.readlines()

#defining lists and G
name_list=[]
r_list=[]
d_list=[]
G_constant=6.67*10**(-11)
    
for l in data:
    words=(l.split())

#name list  
    if words[0].strip("; ")== "Comet":
        name_list.append(words[0].strip("; ")+" "+words[1].strip("; "))
    elif words[0].strip("; ")== "Proxima":
        name_list.append(words[0].strip("; ")+" "+words[1].strip("; ")+" "+words[2].strip("; "))
    else:name_list.append(words[0].strip("; "))
   
#radii list    
    if words[0].strip("; ")== "Comet":
        r_list.append(words[2].strip("; "))
    elif words[0].strip("; ")== "Proxima":
        r_list.append(words[3].strip("; "))
    else:r_list.append(words[1].strip("; "))    

#density list    
    if words[0].strip("; ")== "Comet":
        d_list.append(words[4].strip("; "))
    elif words[0].strip("; ")== "Proxima":
        d_list.append(words[5].strip("; "))
    else:d_list.append(words[3].strip("; "))

#user_input of Planet name
name=str.title(str.lower(raw_input("What is the name of the planet? Type help for options: ")))
if name=="Help":
    print name_list
    name=str.title(str.lower(raw_input("What is the name of the planet? See above list: ")))

if name=="Proxima Centauri B":
    name="Proxima Centauri b"
elif name=="Kepler-37B":
    name="Kepler-37b"
else: name=name


#finding index of name
locale=int(name_list.index(name))

#user_input of altitude
r=float(raw_input("What is your altitude in meters from the planet's surface? "))
r=r+float(r_list[locale])*1000

#mass of planet
P=float(d_list[locale])*1000
mass_planet=P*4/3*ma.pi*r**3

#G acceleration
accel=G_constant*mass_planet/(r**2)

#g's converstion
r_earth=float(r_list[3])*1000
P_earth=float(d_list[3])*1000
mass_earth=P_earth*4/3*ma.pi*r_earth**3
g_earth=G_constant*mass_earth/(r_earth**2)

#accel in g's
accel_gs=accel/g_earth

#person's weight
mass_person=float(raw_input("What is your mass in kilograms? "))
weight=mass_person*accel

#prints
print ""
print "Planet:", name
print "Planet's mass:", mass_planet,"kg"
print "Acceleration:", accel_gs,"g's"
print ""
print "Your weight:", weight,"N"
if weight>(mass_person*g_earth):
    print "Ummm... It seems you have GAINED weight since leaving Earth!"
elif weight<(mass_person*g_earth):
    print "Wow! It seems you have LOST weight since leaving Earth!"
else: print "You are the same weight as you are on Earth."