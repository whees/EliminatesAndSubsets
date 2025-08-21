# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 16:54:04 2025

@author: Luis
"""
class Holds:
    def __init__(self, holds):
        self.feet, self.start, self.middle, self.finish = holds
        
    @staticmethod
    def from_splits(splits):
        holds = (set(), set(), set(), set())

        for i in range(4):
            if len(splits[i]):
                for hold in splits[i].split(','):
                    holds[i].add(int(hold))
                    
        return Holds(holds)

class Climb:
    def __init__(self, name, grade, holds):
        self.name = name 
        self.grade = grade
        self.holds = holds
        self.start_key = Climb.get_start_key(holds)
        self.finish_key = Climb.get_finish_key(holds)
    
    def string(self):
        return f'{self.name} ({self.grade})'
        
    def is_eliminate_of(self, climb):
        if self.holds.start != climb.holds.start or self.holds.finish != climb.holds.finish:
            return False 
        
        if self.holds.feet.issubset(climb.holds.feet) and self.holds.middle.issubset(climb.holds.middle):
            return True
        
        return False
    
    def is_subset_of(self, climb):
        if self.holds.start != climb.holds.start and self.holds.finish != climb.holds.finish:
            return False 
        
        if self.holds.feet.issubset(climb.holds.feet) and self.holds.middle.issubset(climb.holds.middle): 
            if self.holds.finish.issubset(climb.holds.middle):
                return True
            
            if self.holds.start.issubset(climb.holds.middle):
                return True
        
        return False
    
    @staticmethod
    def get_start_key(holds):
        start_key = [hold for hold in holds.start]
        start_key.sort()
        
        if len(start_key) < 2:
            start_key.extend(start_key)
        
        return tuple(start_key)
    
    @staticmethod
    def get_finish_key(holds):
        finish_key = [hold for hold in holds.finish]
        finish_key.sort()       
        
        if len(finish_key) < 2:
            finish_key.extend(finish_key)
                    
        return tuple(finish_key)
    
    @staticmethod
    def from_string(string):
        splits = string.split('|')
        name = splits[0]
        grade = float(splits[1])
        holds = Holds.from_splits(splits[2:6])
        
        return Climb(name, grade, holds)
