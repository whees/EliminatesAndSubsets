# Eliminates and Subsets

## Definitions

Given two problems, Alpha and Beta

**eliminate:** Alpha is an eliminate of Beta if and only if:

1. Alpha has the same start AND finish as Beta.
2. Alpha's middle is a subset\* of Beta's middle.
3. Alpha's feet are a subset of Beta's feet.

**subset:** Alpha is a subset of Beta if and only if:

1. Alpha has the same start OR finish as Beta.
2. Alpha's middle is a subset of Beta's middle.
3. Alpha's feet are a subset of Beta's feet.
4. Alpha's start or finish is a subset of Beta's middle.

*\*Subset can also denote a set theoretic subset, depending on the context.  
    Set theoretic subsets apply to sets, board theoretic subsets apply to problems.*

## Table of Contents

**main.py:** Implementation of the main process

1. Creates a librarian and a sieve.  
2. Feeds the librarian's climbs through the sieve to sort by start, finish.  
3. Uses sieve to find eliminates and subsets.  
4. Saves eliminates and subsets to a .txt file at 'txt/eliminates_and_subsets.txt'.  

**librarian.py:** Implementation of Librarian object to parse 'txt/climbs.txt' for climb data.  

**climb.py:** Implementation of Climb and Holds objects to store climb data.

**sieve.py:** Implementation of Sieve object to sort climbs and find eliminates and subsets.
