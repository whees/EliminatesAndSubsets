# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 02:49:44 2025

@author: Luis
"""
from tqdm import tqdm

class Sieve:
    def __init__(self):
        self.start_dictionary = {}
        self.finish_dictionary = {}
    
    def fill_dictionaries_with(self, climbs):
        for climb in climbs:
            if climb.start_key in self.start_dictionary.keys():
                self.start_dictionary[climb.start_key].append(climb)
            else:
                self.start_dictionary[climb.start_key] = [climb]
                
            if climb.finish_key in self.finish_dictionary.keys():
                self.finish_dictionary[climb.finish_key].append(climb)
            else:
                self.finish_dictionary[climb.finish_key] = [climb]
                        
    def get_eliminates(self):
        eliminates = {}
        
        for climbs in tqdm(self.start_dictionary.values()):
            climb_count = len(climbs)
            
            for i in range(climb_count):
                for j in range(i):
                    
                    if climbs[i].is_eliminate_of(climbs[j]):
                        if climbs[j].string() in eliminates.keys():
                            eliminates[climbs[j].string()].append(climbs[i].string())
                        else:
                            eliminates[climbs[j].string()] = [climbs[i].string()]
                            
                    if climbs[j].is_eliminate_of(climbs[i]):
                        if climbs[j].string() in eliminates.keys():
                            eliminates.pop(climbs[j].string())
                        else:
                            eliminates[climbs[i].string()] = [climbs[j].string()]
                            
        return eliminates
    
    def get_subsets(self):
        subsets = {}
        
        for climbs in tqdm(self.start_dictionary.values()):
            climb_count = len(climbs)
            
            for i in range(climb_count):
                for j in range(i):
                    
                    if climbs[i].is_subset_of(climbs[j]):
                        if climbs[j].string() in subsets.keys():
                            subsets[climbs[j].string()].append(climbs[i].string())
                        else:
                            subsets[climbs[j].string()] = [climbs[i].string()]
                            
                    if climbs[j].is_subset_of(climbs[i]):
                        if climbs[i].string() in subsets.keys():
                            subsets[climbs[i].string()].append(climbs[j].string())
                        else:
                            subsets[climbs[i].string()] = [climbs[j].string()]
                            
        for climbs in tqdm(self.finish_dictionary.values()):
            climb_count = len(climbs)
            
            for i in range(climb_count):
                for j in range(i):
                    
                    if climbs[i].is_subset_of(climbs[j]):
                        if climbs[j].string() in subsets.keys():
                            subsets[climbs[j].string()].append(climbs[i].string())
                        else:
                            subsets[climbs[j].string()] = [climbs[i].string()]
                            
                    if climbs[j].is_subset_of(climbs[i]):
                        if climbs[i].string() in subsets.keys():
                            subsets[climbs[i].string()].append(climbs[j].string())
                        else:
                            subsets[climbs[i].string()] = [climbs[j].string()]
                            
        return subsets
                            
                            
                            