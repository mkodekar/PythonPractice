appendME = '\n New data to be inserted into the file'

appendFile = open('exampleText.ged', 'a')
appendFile.write(appendME)
appendFile.close()
