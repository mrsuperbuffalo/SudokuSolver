import os
import argparse
from pprint import pprint
from Sudoku.Sudoku import SudokuPuzzle


def main(args):
    puzzle = SudokuPuzzle()
    puzzle.read_puzzle(args.input)
    # pprint(puzzle.values)
    pprint(puzzle.get_block(6))

def cli():
    """Command line interface for search algorithm."""
    parser = argparse.ArgumentParser(description="search start")
    parser.add_argument('-i', '--input', type=str)
    args = parser.parse_args()
    main(args)

if __name__ == '__main__':
    cli()
