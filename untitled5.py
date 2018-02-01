#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 17:05:49 2018

@author: mitchellyoung
"""
#http://interactivepython.org/runestone/static/pip/Files/files.html
data=open("planet_data.dat","r")
for row in data:
    values = row.split()
    print(values[0])
for 