# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 20:57:31 2024

@author: lcuev
"""
from librarian import Librarian
from sieve import Sieve

librarian = Librarian()
sieve = Sieve()

sieve.fill_dictionaries_with(librarian.climbs)

eliminates = sieve.get_eliminates()
subsets = sieve.get_subsets()


with open('txt/eliminates_and_subsets.txt', mode='w') as file:
    file.write('ELIMINATES:\n')
    for original_name, eliminate_names in eliminates.items():
        file.write(f'{original_name}:\n')
        for name in eliminate_names:
            file.write(f' ---- {name}\n')
        
    file.write('\n')
    file.write('\n')
    file.write('SUBSETS:\n')
    for original_name, subset_names in subsets.items():
        file.write(f'{original_name}:\n')
        for name in subset_names:
            file.write(f' ---- {name}\n')

print()
print()
print('Success!')        






































