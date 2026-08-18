import random
import sys

# Seed the generator (like srandom)
random.seed()

# Generate a random number
random_num = (random.randint(1,100))

if random_num % 2 == 0:
    sys.exit(0)
else:    
    sys.exit(1)