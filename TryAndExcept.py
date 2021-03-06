import csv as c

with open('demo.csv') as csvfile:
    readCsv = c.reader(csvfile, delimiter=",")
    print(readCsv)
    names = []
    dates = []
    ranks = []
    for row in readCsv:
        date = row[0]
        name = row[2]
        rank = row[1]
        names.append(name)
        dates.append(date)
        ranks.append(rank)

print(names)
print(dates)
print(ranks)

try:
    whoseRank = input('Whose rank you want to know?\n')
    if whoseRank in names:
        rank = names.index(whoseRank)
        theRank = ranks[rank]
        print('The Rank of', whoseRank, 'is', theRank)
    else:
        print(whoseRank, 'is not in the list')
except NameError as e:
    print(e)
finally:
    print('continue')
