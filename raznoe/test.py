pathFile = '.\\sem_7\\file_7.txt'

def SaveFile(strSave: str):
    with open(pathFile, "a") as fileTxt:
        fileTxt.write(strSave + '\n') 

def OpenFile():
    with open(pathFile, "r") as fileTxt:
        return fileTxt.readlines()


# SaveFile('dtdtdtd dtdtdtdt')
# print(OpenFile())

with open('.\\sem_7\\file_7b.txt', "wb") as fileTxt:
        text = 'qqqqq fhgfs  asefwae  wefwqe wwef Миру мир!'.encode("utf-8")
        fileTxt.write(text) 
        
with open('.\\sem_7\\file_7b.txt', "rb") as fileTxt:
    print(fileTxt.read().decode('utf-8'))