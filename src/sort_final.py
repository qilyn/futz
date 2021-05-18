"""
The apprentice wizard Escalenor has inherited a great library from his
predecessor. Score! The problem is, all the books are in a strange order.

The arcane disturbances caused by incompatible magical fields around the
books have been a terrible nuisance.

Through experimentation, he has figured out how to arrange the types of magical
books which fixes the magical interference (and now his slippers have stopped
turning into comical fruit-adorned hats).

Figure out the rules of the sorting system and implement them so that he
always knows where to shelve his books.

- Some of these 'experiments' had no stable configuration; these cases return
  None.
- He has included one test that has more than one solution.

- E = enchantment
- A = abjuration
- D = divination
- N = evocation
"""
from itertools import combinations_with_replacement

def count_char_in_string(string, char):
    count = 0
    for a in string:
        if a == char:
            count+=1
    return count



def reverse(string):
    return string[::-1]

def sort_spellbooks(books):
    if len(books) == 1:
        return books if books != 'E' else None

    if books.count('A') > 2:
        return None

    if books.count('A') == 2:
        temp = books.replace('A', '')
        temp = f'A{temp}A'
        return temp

    if books[0] == 'E' or books[-1] == 'E':
        return None

    a_location = books.find('A')
    n_location = books.find('N')

    if books == 'AEN':
        return reverse(books)

    if books == 'AED':
        return books

    if books.replace('D', '').replace('N', '') == '':
        characters = list(books)
        return [''.join(perm) for perm in combinations_with_replacement(characters, 4)]



assert count_char_in_string('AAE', 'A') == 2
assert sort_spellbooks('E') == None
assert sort_spellbooks('N') == 'N'
assert sort_spellbooks('A') == 'A'
assert sort_spellbooks('D') == 'D'

# E appears to always be in the middle
# Weights are not a agood idea, because A can't always have a low weight....

# A < N
assert sort_spellbooks('AEN') == 'NEA'
# D < A
assert sort_spellbooks('AED') == 'AED'
# E has to be in the middle, A == A
assert sort_spellbooks('AAE') == 'AEA'


# E can't go in the middle in every possible combination
assert sort_spellbooks('EDN') == None

# Both Es can't be output in the middle
assert sort_spellbooks('AAAEE') == None

# D + N implies output of all possible D + N combinations
print(sort_spellbooks('DDNN'))
assert sort_spellbooks('DDNN') == {'NDND', 'DDNN', 'NDDN', 'DNND', 'DNDN', 'NNDD'}

"""
Extra:
What is the solution for each of these shelves?

AA == AA
AAED == AEDA ??
AAEN == ANEA ??
ANNNNE == NNNNEA ??
"""

