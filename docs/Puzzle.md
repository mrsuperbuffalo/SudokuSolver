## Puzzle

The puzzle is represented by the Sudoku objectin the Sudoku folder. This puzzle
will be used to interact with solving the puzzle.


### How it should work

I expect to have an array of arrays indexed by row and column starting from
the top left that stores the values in the puzzle. I wish to use this double
array(list) to hold the values that are specified or deduced. There will be
another object that holds the possible values of a cell.


### Issues

#### 11-6-16

I believe I have been creating the puzzle incorrectly. It should represent the
solution to the puzzle. I've been attempting to push the search and ability to
solve the puzzle into the same package. I think I need to pull some of the it
out or I need to used the read puzzle as the base for the search.