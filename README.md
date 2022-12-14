# finalProjectFall2022

This videogame is intented to be a continuously more difficult and exciting game of racing the clock. With further development, this

## Description

An in-depth paragraph about your project and overview of use.

## Getting Started

Ensure that window dimensions found in settings are accomodated by your device

### Dependencies

Requires libraries Random and Pygame

### Installing

Only required files are main.py and settings.py in the 'game' folder
No modifications to files needed

### Executing program

Program will run on run command
Program runs in a windowed screen with easy access to 'close application' button
Pressing the escape button will also close the program


## Help

Within spawn block, if changing the score requirements for each threshold:
   'kill' will run through the entire spawn block, regardless of current score. What this means:
      When crossing from one score threshold to the next, both will run.
      My original files have the first score threshold set to 15, which means when you kill an enemy at SCORE = 14, the spawn block will add 1 to your score, summon
      another enemy, then see that your score is 15, continue to run 'kill', add 1 to your score, then summon another enemy. This is the basis of the game in its
      alpha version, but it is also fundamentally an error in the code. Because of this, SCORE will never = 15, 25, 35, or 45. Any changes to the spawn block must be         made with this knowledge in mind.
   


## Authors

Brayton Arthur
braypo80@gmail.com

## Version History

* 0.2
    * Fixed collisions, working enemy counter, semi-implemented sweep function. Final Project submission
* 0.1
    * Initial Release during videogame project

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [w3Schools](https://www.w3schools.com/python/default.asp)
* [PyGame](https://www.pygame.org/docs/)
* Andrew Perevoztchikov
* Roman Moralez
