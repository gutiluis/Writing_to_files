#!/bin/python
import sqlite3
# script for running db
import logging

logging.basicConfig(level=logging.INFO)

logging.debug("""
target (Connection) - The database connection to save the backup to.
pages (int) - The number of pages to copy at a time. If equal to or less than 0, the entire database is copied in a single step. Defaults to -1.
progress (callback | None) - If set to a callable, it is invoked with three integer arguments for every backup iteration: the status of the last iteration, the remaining number of pages still to be copied, and the total number of pages. Defaults to None.
name (str) - The name of the database to back up. Either "main" (the default) for the main database, "temp" for the temporary database, or the name of a custom database as attached using the ATTACH DATABASE SQL statement.
sleep (float) - The number of seconds to sleep between successive attempts to back up remaining pages.
""")


def progress(status, remaining, total):
    print(f'Copied {total-remaining} of {total} pages...')

src = sqlite3.connect('example.db')
dst = sqlite3.connect('backup.db')
with dst:
    src.backup(dst, pages=1, progress=progress)
dst.close()
src.close()
