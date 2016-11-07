import os
import argparse
from pprint import pprint
from Sudoku.Sudoku import SudokuPuzzle

def main(args):
    puzzle = SudokuPuzzle()
    puzzle.read_puzzle(args.input)
    puzzle.update_pvalues()

    for _ in range(9):
        puzzle.deduce_row_pvalues()
        puzzle.deduce_col_pvalues()
        puzzle.deduce_block_pvalues()
        puzzle.assign_singles()
    puzzle.print_pvalues()
    comb_list = [len(ss) for ss in puzzle.pvalues.values()]
    comb = 1
    for num in comb_list:
        comb *= num
    print('{:,}'.format(comb))

def cli():
    """Command line interface for search algorithm."""
    parser = argparse.ArgumentParser(description="search start")
    parser.add_argument('-i', '--input', type=str)
    args = parser.parse_args()
    main(args)

if __name__ == '__main__':
    cli()
