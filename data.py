"""import of raw data"""

import csv


def load_data():
    "Return iterable of (date, author, message)"
    with open('data/messages-leetchi-fdo - source.tsv') as fd:
        yield from csv.reader(fd, delimiter='\t')

data = tuple(load_data())
