import sqlite3
import os
import argparse

def main(args):
    path = os.path.abspath(args.input)
    if os.path.isfile(path):
        os.remove(path)
    conn = sqlite3.connect(path)
    cur = conn.cursor()

    # Create decision table
    cur.execute("""
    create table
        decision
            (row, column, value)
    """)

    # Create cell decisions
    all_dec = []
    for row in range(9):
        for col in range(9):
            for val in range(1, 10):
                all_dec.append((row, col, val))
    cur.executemany(
        """insert into decision values (?, ?, ?)""", all_dec)

    # Create constraint table
    cur.execute("""
    create table
        constraints
            (
                description text,
                type text,
                row int,
                column int,
                block int,
                amount int,
                value int)
    """)

    # A cell must have a minimum of 1 value
    cell_cons = []
    amount = 1
    _type = 'min'
    desc = 'Cell {row},{col} must have a {type} of {amount} value'
    for row in range(9):
        for col in range(9):
            cell_cons.append(
                (
                    desc.format(row=row, col=col, type=_type, amount=amount),
                    _type,
                    row,
                    col,
                    None, # block num
                    amount,
                    None # value
                )
            )
    cur.executemany(
        """insert into constraints values (?, ?, ?, ?, ?, ?, ?)""", cell_cons)

    # A row must have a single value X
    row_val_con = []
    amount = 1
    _type = 'min'
    desc ='Row {row} must have a {type} of {amount} {value}'
    for row in range(9):
        for val in range(1, 10):
            row_val_con.append(
                (
                    desc.format(row=row, type=_type, amount=amount, value=val),
                    _type,
                    row,
                    None, # col
                    None, # block num
                    amount,
                    val
                )
            )

    cur.executemany(
        """insert into constraints values (?, ?, ?, ?, ?, ?, ?)""",
        row_val_con)

    # A column must have a single value X
    col_val_con = []
    amount = 1
    _type = 'min'
    desc = 'Column {row} must have a {type} of {amount} {value}'
    for col in range(9):
        for val in range(1, 10):
            col_val_con.append(
                (
                    desc.format(row=row, type=_type, amount=amount, value=val),
                    _type,
                    None,  # row
                    col,   # col
                    None,  # block num
                    amount,
                    val
                )
            )

    cur.executemany(
        """insert into constraints values (?, ?, ?, ?, ?, ?, ?)""",
        col_val_con)

    # A column must have a single value X
    block_val_con = []
    amount = 1
    _type = 'min'
    desc = 'Block {block} must have a {type} of {amount} {value}'
    for block in range(9):
        for val in range(1, 10):
            block_val_con.append(
                (
                    desc.format(block=block, type=_type, amount=amount, value=val),
                    _type,
                    None,   # row
                    None,   # col
                    block,  # block num
                    amount,
                    val
                )
            )
    cur.executemany(
        """insert into constraints values (?, ?, ?, ?, ?, ?, ?)""",
        block_val_con)


    conn.commit()
    conn.close()


def cli():
    parser = argparse.ArgumentParser(description="search start")
    parser.add_argument('-i', '--input', type=str)
    args = parser.parse_args()
    main(args)

if __name__ == '__main__':
    cli()

