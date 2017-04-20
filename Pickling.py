import pickle as pic

exampleDict = {1: "a", 2: "b", 3: "c", 4: "d"}

pickle_out = open('dict.pickle', 'wb')
pic.dump(exampleDict, pickle_out)
pickle_out.close()


