"""
The apprentice wizard Escalenor has inherited a great library from his
predecessor. Score! The problem is, all the books are in a strange order.

Through experimentation, he has figured out how to arrange the types of magical
books which fixes the magical interference.

Implement the rules of the sorting system so that Escalenor
always knows if his books are arranged correctly:
- E (enchantment) needs to be stored next to at least one abjuration book
- A (abjuration) must be on the outside (edges) of the shelf.
- D (divination) must be to the right of any enchantment books
- N (evocation) must be to the left of any enchantment books
"""

# Code here



assert sort_spellbooks('E') == False
assert sort_spellbooks('N') == True
assert sort_spellbooks('A') == True
assert sort_spellbooks('D') == True

assert sort_spellbooks('NEA') == True
assert sort_spellbooks('AED') == True
assert sort_spellbooks('AEA') == True
assert sort_spellbooks('EDN') == False

assert sort_spellbooks('AAAEE') == False

assert sort_spellbooks('DDNN') == True

"""
Extra:
What is the solution for each of these shelves?

AA
AAED
AAEN
ANNNNE
"""
