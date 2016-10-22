import os
import argparse
from pprint import pprint
from Sudoku.Sudoku import SudokuPuzzle


def main(args):
    puzzle = SudokuPuzzle()
    puzzle.read_puzzle(args.input)
    print(puzzle.check_puzzle())

def cli():
    """Command line interface for search algorithm."""
    parser = argparse.ArgumentParser(description="search start")
    parser.add_argument('-i', '--input', type=str)
    args = parser.parse_args()
    main(args)

if __name__ == '__main__':
    cli()
