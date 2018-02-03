#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 17:05:49 2018

@author: mitchellyoung
"""
name='Mercury'

words=[]
#http://interactivepython.org/runestone/static/pip/Files/files.html
with open("planet_data.dat","r") as doc:
    data=doc.readlines()
    
for line in data:
    words=(line.split())
    #if name in words:
    print words


"""
list_locs=[]

for line in data:   
    location=line.find(name)
    list_locs.append(location)
    testing=line[location:len(name)+location]
    
    print testing
    
    
#location=data.index(name)



 
  #  if words==name+";":
#data=open("planet_data.dat","r")
"""


