"""Study of author repetitions in data"""

from data import data
from pprint import pprint
from operator import itemgetter
from collections import Counter

per_author = {}
for date, author, message in data:
    per_author.setdefault(author, []).append(message)

def print_msg_counts(counts:Counter, amount:int=20, start:str='\t') -> print:
    for author, nb_msg in sorted(tuple(counts.most_common(amount)), key=itemgetter(0)):
        print(f'{start}{author}: {nb_msg}')

print("Nombre de message pour les auteurs les plus prolifiques:")
nb_per_author = Counter({author: len(messages) for author, messages in per_author.items()})
print_msg_counts(nb_per_author)

print("Nombre de message UNIQUE pour les auteurs les plus prolifiques:")
nb_unique_per_author = Counter({author: len(set(messages)) for author, messages in per_author.items()})
print_msg_counts(nb_unique_per_author)


