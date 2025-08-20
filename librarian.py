# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 20:58:08 2024

@author: lcuev
"""
from climb import Climb
    
class Librarian:
    def __init__(self):
        self.climbs = self.get_climbs()

    def get_climbs(self):
        climbs = []
        
        with open('txt/climbs.txt', 'r') as file:
            for string in file:
                climbs.append(Climb.from_string(string))
                
        return climbs

    
    
    
    
    
    
    



