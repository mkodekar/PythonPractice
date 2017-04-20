import pickle as pick

pickle_in = open('dict.pickle', 'rb')
example_dict = pick.load(pickle_in)
print(example_dict)
pickle_in.close()