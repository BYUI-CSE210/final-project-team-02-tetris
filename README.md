# cse210-final

# Tetris
Tetris is a game where the player completes bricks' lines by placing falling a set of bricks that have letters' squared shapes. Each set of bricks has its own color depending on the letter it represents (J, L, I, T, S, Z, or O). 

When one line is completely filled, the wall collapses and any full line disappears. The player wins one point for each full line. If the player fails to fill a line, they can catch up and fill the next line as soon as possible. Otherwise, the blocks pile up until they reach the top of the screen. That way, the player loses 1 point. If all the points get down to 0, the player loses 1 life. The game starts with 3 lives.  


# Rules
Tetris is played according to the following rules:

1. Start the game by pressing Enter or Space key, and then move the falling block left and right using the arrow keys to position in the empty spot, depending on where it will fit.
2. Use the down arrow key to accelerate the falling of the block, and the space key to pause and resume the game. 
3. Rotate the shape by pressing the space key or the up direction arrow key as many times as needed until the block's position fits to the empty spot when possible.
4. When a row is filled, it disappears and the player wins & point per line. 
5. The player loses 1 life at a time until the game is over, when the blocks reach the top of the screen. 


## Getting Started
Make sure you have Python 3.8.0 or newer installed and running on your machine. Open a terminal and browse to the project's root folder. Start the program by running the following command.

You also to have pygame installed on your computer to use the module. To install pygame on your computer, run the following command in your terminal: pip install pygame.

```
python3 tetris 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure
The project files and folders are organized as follows:
```
root                     (project root folder)
+-- tetris               (source code for game)
  +-- assests
  +-- game 
    +-- casting
        +-- actor           (specific classes)
        +-- cast            (specific classes)
        +-- block             (specific classes)        
    +-- directing
        +-- director        (specific classes) 
    +-- services
        +-- keyboard_service (specific classes)
        +-- video_service    (specific classes)
    +-- __main__.py       (program entry point)
    +-- constants.py           (all the program's constants)
+-- README.md           (general info)

## Project Structure
## Required Technologies
* Python 3.8.0
* Pygame

# Features
(2) Main Scene
·        (2) Play button
·        (3) Help button
(1) Game Scene
·        (1) User-controlled paddle
·        (1) Falling blocks 
·        (1) Blocks rotation
·        (1) Locked spots detection
·        (2) Life display
·        (2) Score display
·        (2) Sound effects
(3) Help Scene
·        (3) Help text
·        (3) Back button
(2) Win Scene
·        (2) Announcement
(2) Lose Scene
·        (2) Announcement
·        (2) Restart button

# Extra point comment
Because of all the features above, we believe that we deserve the extra bonus point. Other than that, we used most of the principles of programming with classes learned in class, including maintainability. We understand that the program not perfect and easily be improved
because it was built following the principles of maintainability. 

## Authors
* Baron Tshibasu (tshibasubaron@yahoo.fr)
* Camden Chadsey