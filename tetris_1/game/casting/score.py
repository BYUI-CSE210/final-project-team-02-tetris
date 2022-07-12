class Score:
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def update_score(nscore):
        """Creates a file to save score
        Arg: nscore
        """
        score = max_score()

        with open('scores.txt', 'w') as f:
            if int(score) > nscore:
                f.write(str(score))
            else:
                f.write(str(nscore))

    def max_score():
        """Saves maximum scores earned by the player
        
        Returns: score (integer)
        """
        with open('tetris/assets/scores.txt', 'r') as f:
            lines = f.readlines()
            score = lines[0].strip()

        return score