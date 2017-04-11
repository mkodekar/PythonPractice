# making a default dictionary
exDict = {'Rehan': 26, 'Pritesh': 24, 'Akash': 21}
print(exDict)

# adding a key to dictionary
exDict['Santosh'] = 25
print(exDict)

# deleting a key from a dictionary
del exDict['Santosh']
print(exDict)

# lets add a list to the dictionary

exDict = {'Rehan': [26, 'Bms'], 'Pritesh': [24, 'BE'], 'Akash': [21, 'BSCIT']}
print(exDict)

# printing only the content of 'Rehan from the dictionary'
print(exDict['Rehan'])

# print only the age of pritesh
print(exDict['Pritesh'][0])

# print only the course of akash
print(exDict['Akash'][1])

# editing elements of the dic
exDict['Rehan'] = 'BMS'
print(exDict)


def addfunctodict(arg):
    return 'Func , [1]'.format(arg)
 

def anotherfucn(arg):
    return 'Pong, [0]'.format(arg)


def do_ls(arg):
    return 'Do, [2]'.format(arg)


# adding functions to dictionary
funDic = {'pong': anotherfucn, 'func': addfunctodict, 'do': do_ls}

print(funDic)
print(funDic['pong'])
