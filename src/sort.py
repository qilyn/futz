"""
The apprentice wizard Escalenor has inherited a great library from his
predecessor. Score! The problem is, all the books are in a strange order.

The arcane disturbances caused by incompatible magical fields around the
books have been a terrible nuisance.

Through experimentation, he has figured out how to arrange the types of magical
books which fixes the magical interference (and now his slippers have stopped
turning into comical fruit-adorned hats).

Figure out the rules of the sorting system and implement them so that Merlot
always knows where to shelve his books.

- Some of these 'experiments' had no stable configuration; these cases return
  None.
- He has included one test that has more than one solution.

- E = enchantment
- A = abjuration
- D = divination
- N = evocation

- E (enchantment) needs to be stored next to at least one abjuration book
- A (abjuration) must be on the outside (edges) of the shelf.
- D (divination) must be to the right of any enchantment books
- N (evocation) must be to the left of any enchantment books

"""

assert sort_spellbooks('E') == None
assert sort_spellbooks('N') == 'N'
assert sort_spellbooks('A') == 'A'
assert sort_spellbooks('D') == 'D'

assert sort_spellbooks('AEN') == 'NEA'
assert sort_spellbooks('AED') == 'AED'
assert sort_spellbooks('AAE') == 'AEA'
assert sort_spellbooks('EDN') == None

assert sort_spellbooks('AAAEE') == None

assert sort_spellbooks('DDNN') == ['DDNN', 'NNDD', 'DNDN', 'NDND']

"""
Extra:
What is the solution for each of these shelves?

AA
AAED
AAEN
ANNNNE
"""
