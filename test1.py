import os
import argparse
from pprint import pprint
from Sudoku.Sudoku import SudokuPuzzle

def main(args):
    puzzle = SudokuPuzzle()
    puzzle.read_puzzle(args.input)
    puzzle.update_pvalues()
    puzzle.deduce_row_pvalues()
    puzzle.deduce_col_pvalues()
    puzzle.deduce_block_pvalues()

    pprint(puzzle.pvalues)

def cli():
    """Command line interface for search algorithm."""
    parser = argparse.ArgumentParser(description="search start")
    parser.add_argument('-i', '--input', type=str)
    args = parser.parse_args()
    main(args)

if __name__ == '__main__':
    cli()
