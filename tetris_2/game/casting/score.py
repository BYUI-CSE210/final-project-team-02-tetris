class Score:
    """Handles the player's scores"""
    
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
        with open('assets/scores.txt', 'r') as f:
            lines = f.readlines()
            score = lines[0].strip()

        return score