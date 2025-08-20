# Eliminates and Subsets

## Definitions

**eliminate:** Problem A is an eliminate of Problem B if and only if:

1. Problem A has the same start AND finish as Problem B.
2. Problem A's middle is a subset of Problem B's middle.
3. Problem A's feet are a subset of Problem B's feet.

**subset:** Problem A is a subset of Problem B if and only if:

1. Problem A has the same start OR finish as Problem B.
2. Problem A's middle is a subset of Problem B's middle.
3. Problem A's feet are a subset of Problem B's feet.
4. Problem A's start or finish is a subset of Problem B's middle.

*\* subset can also refer to a set theoretic subset, depending on the context.*

## Table of Contents

**main.py:** Implementation of the main process, which

1. Creates a librarian and a sieve.  
2. Feeds the librarian's climbs through the sieve to sort by start, finish.  
3. Uses sieve to find eliminates and subsets.  
4. Saves eliminates and subsets to a .txt file at 'txt/eliminates_and_subsets.txt'.  

**librarian.py:** Implementation of Librarian object to parse 'txt/climbs.txt' for climb data.  

**climb.py:** Implementation of Climb and Holds objects to store climb data.

**sieve.py:** Implementation of Sieve object to sort climbs and find eliminates and subsets.
