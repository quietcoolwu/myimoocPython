L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in zip(list(range(1, len(L)+1)), L):
    print((index, '-', name))