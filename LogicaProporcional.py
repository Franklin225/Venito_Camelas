import ttg

proposiciones = ['p', 'q', 'r']

expresionLogica = ['(p implies q)', '(not q and r)', '(r implies q)']

tablita = ttg.Truths(proposiciones, expresionLogica)

print(tablita)
