#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 15:47:47 2020

@author: hemma
"""
import math

# Class name -- Note that there is no explicit inheritance here
class MyFraction:
    # Constructor
    def __init__(self, num, den):
        # Attributes
        self.num = num
        self.den = den
        self.normalize()
    
    # Methods
    def normalize(self):
        gcd = math.gcd(self.num, self.den)
        self.num = int(self.num / gcd)
        self.den = int(self.den / gcd)
    
    def eval(self):
        return(self.num / self.den)
    
    # Overriding of functions
    def __float__(self):
        return(self.num / self.den)
    
    def __str__(self):
        return (" " + str(self.num) + "\n---\n" + " " + str(self.den) + "\n")
    
    def __add__(self, other):
        cd = self.den * other.den
        cn = self.num*other.den + other.num*self.den
        return( MyFraction(cn, cd) )


if __name__ == '__main__':
    fractionA = MyFraction(3,4)
    fractionB = MyFraction(4,3)
    added = fractionA + fractionB
    print(added)
