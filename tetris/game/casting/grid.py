class Grid:
    """A multidimensional list that helps locate the falling blocks as they move down"""

    def create_grid(locked_spots={}):
        """Creates a mutlidimensional list with 20 rows and 10 columns to keep track of the bricks in the falling blocks. 
        
        Arg: locked_spots

        Returns: 
            A grid (multidimensional list)
        """
        grid = [[(0,0,0) for x in range(10)] for x in range(20)]
        
        # loop through the locked positions and modify our blank grid to show these pieces.
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (j,i) in locked_spots:
                    c = locked_spots[(j,i)]
                    grid[i][j] = c
        return grid