'''Starting in the top left corner of a 2×2 grid, and
only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?'''

import math

# Returns number of routes moving right and down provided a gridSizexgridSize grid
def numRoutes(gridSize):

    return math.factorial(gridSize * 2) / ( math.factorial(gridSize) ** 2 )


print(numRoutes(20))
