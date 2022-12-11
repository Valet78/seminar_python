pathFile = '.\\sem_7\\file_7.txt'

def SaveFile(strSave: str):
    with open(pathFile, "a") as fileTxt:
        fileTxt.write(strSave + '\n') 

def OpenFile():
    with open(pathFile, "r") as fileTxt:
        return fileTxt.readlines()


# SaveFile('dtdtdtd dtdtdtdt')
print(OpenFile())