# cse210-final

# Tetris
Tetris is a game where the player completes lines by placing falling colored bricks that have letters' squared shapes. When one line is correctly filled, the player wins one point per line. If the player misses completely filling a line and the bricks reach the top of the screen, the player loses 1 point. If all the points get to 0, the player loses 1 life. 


Rules
Tetris is played according to the following rules:

Move the falling brick left or right, depending on where you want to place it.
Rotate the shape so it can fit the empty sapce and fill at least one line.
When a line is filled, it disappears and the player wins & point per line. 
The game is over if the pieces reach the top of the screen and there is no way to return the falling bricks back up to the top. So, try to avoid 

So, you should avoid stacking the bricks trying to fill the empty spaces and thus reduce the size of the wall, so that it does not reach the top of the screen. 

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
  +-- game 
    +-- casting
        +-- actor           (specific classes)
        +-- cast            (specific classes)
        +-- gem             (specific classes)
        +-- rock            (specific classes)
    +-- directing
        +-- director        (specific classes) 
    +-- services
       +-- keyboard_service (specific classes)
       +-- video_service    (specific classes)
    +-- shared
        +-- color           (specific classes)
        +-- point           (specific classes) 
  +-- __main__.py       (program entry point)
+-- README.md           (general info)
```

## Required Technologies
* Python 3.8.0
* Pygame

# Features
(2) Main Scene
·        (2) Play button
·        (3) Help button
(1) Game Scene
·        (1) User-controlled paddle
·        (1) Falling bricks rotation
·        (1) Falling bricks bricks
·        (1) Locked position detection
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

## Authors
* Baron Tshibasu