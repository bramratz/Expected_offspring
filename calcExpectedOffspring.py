#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 11:38:19 2020

@author: bram
"""

# Import modules needed
import sys

# Read in file and collect numbers 
with open(sys.argv[1]) as f:
    # Save integers in file as a list 
    line = [item.strip() for item in f.readlines()]
    for i in line:
        print(i)
