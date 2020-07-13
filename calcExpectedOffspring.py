#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 11:38:19 2020

@author: bram
"""

# Import modules needed
import sys

# Dictionary of parental pairs and odds of having offspring with dominant phenotype
oddsChildDominant = {'AA-AA': 1,
                     'AA-Aa': 1,
                     'AA-aa': 1,
                     'Aa-Aa': 0.75,
                     'Aa-aa': 0.5,
                     'aa-aa': 0}

genotype = ['AA-AA', 'AA-Aa', 'AA-aa', 'Aa-Aa', 'Aa-aa', 'aa-aa']
genotypeCounts = []

# Read in file and collect numbers 
with open(sys.argv[1]) as f:
    # Save integers in file as a list 
    for line in f:
        for char in line:
            if char == ' ' or char == '\n':
                pass
            else:
                genotypeCounts.append(char)

Res = 0

for types, counts in zip(genotype, genotypeCounts):
    if types in oddsChildDominant:
        Res += oddsChildDominant[types] * int(counts)

Res *= 2
print(f"Expected offspring displaying dominant phenotype: {Res}")