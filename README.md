# the-game-of-life
Dead simple ***Conway's** game of life*

## The rules are simple
1. if a cell has 2 or 3 living neighbours, the cell survive
2. if a dead cell has 3 neighbours, the cell become alive
3. if a cell has less than 2 neighbours, the cell dies
4. if a cell has more than 3 neighbours, the cell dies

## Usage
    drawing.py [-h] [-g N] [-s N] [-t {cli,gui}]

    Conway's game of life

    optional arguments:
  
    -h, --help            
                       show this help message and exit
  
    -g N, --generations N
  
                        number of generation to loop over
  
    -s N, --size N        
                        size of the board
  
    -t {cli,gui}, --type {cli,gui}
  
                        type of display

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
_note:procedural code_

## Licence
[WTFPL](https://wikipedia.org/wiki/WTFPL)
