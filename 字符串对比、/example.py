import difflib

a = 'hello'

b = 'hell'

print(difflib.SequenceMatcher(None, a, b).quick_ratio())
