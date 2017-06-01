keyWords = {'BEGIN', 'END', 'FOR', 'PROGRAM', 'VAR', 'CONST'}
delimiters = {',', ';', '/', '+', '[', ']', ':', '.', '='}
numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}

keyWordsCodes = {}
delimitersCodes = {}
constantsCodes = {}
identifierCodes = {}

kWCode = 401
cCode = 501
iCode = 1001

dArray = []
kWArray = []
cArray = []
iArray = []
mistakes = []

lengthOfMistake = 0
countLines = 0

def isKeyWord(word):
    return word in keyWords

def isDelimiter(word):
    return word in delimiters

def isNumber(word):
    return word in numbers

file = open('signal-program.txt')
i = 0
lexem = ''
newFileString = ""
comment = ""
buf = file.read(1)

while buf != '':
    if isNumber(buf):
        lexem = ''
        while isNumber(buf):
            lexem = lexem + buf
            buf = file.read(1)
        if lexem not in cArray:
            cArray.append(lexem)
            constantsCodes[lexem] = cCode
            cCode += 1
        newFileString += str(cCode - 1) + ' '
        if isDelimiter(buf):
            if buf not in dArray:
                dArray.append(buf)
                delimitersCodes[buf] = ord(buf)
            newFileString += str(ord(buf)) + ' '
        buf = file.read(1)
    elif 65 <= ord(buf) <= 90 or 97 <= ord(buf) <= 122:
        lexem = ''
        while True:
            if buf != ' ':
                lexem = lexem + buf
            buf = file.read(1)
            if buf != '':
                if not 65 <= ord(buf) <= 90 or 97 <= ord(buf) <= 122 or isNumber(buf):
                    break
            else:
                break
        if isKeyWord(lexem):
            if lexem not in kWArray:
                kWArray.append(lexem)
                keyWordsCodes[lexem] = kWCode
                kWCode += 1
            newFileString += str(kWCode - 1) + ' '
        else:
            if lexem not in iArray:
                iArray.append(lexem)
                identifierCodes[lexem] = iCode
                iCode += 1
            newFileString += str(iCode - 1) + ' '
    elif buf == '(':
        buf = file.read(1)
        if buf == '':
            break
        else:
            if buf == '*':
                buf = file.read(1)
                if buf == '':
                    print('Unexpected end of file on' + countLines + 1 + 'line.')
                else:
                    while True:
                        buf = file.read(1)
                        while buf != '' and buf != '*':
                            buf = file.read(1)
                        if buf == '':
                            print('Unexpected end of file on', countLines + 1, 'line.')
                            break
                        else:
                            buf = file.read(1)
                        if buf == ')':
                            buf = file.read(1)
                            break
    elif isDelimiter(buf):
        if buf not in dArray:
            dArray.append(buf)
            delimitersCodes[buf] = ord(buf)
        newFileString += str(ord(buf)) + ' '
        buf = file.read(1)
    elif 9 <= ord(buf) <= 13 or ord(buf) == 32:
        newFileString += str(ord(buf)) + ' '
        if buf == '\n':
            countLines += 1
        buf = file.read(1)
    elif not (65 <= ord(buf) <= 90 or 97 <= ord(buf) <= 122):
        mistakes.append(i)

print(constantsCodes)
print(identifierCodes)
print(keyWordsCodes)
print(delimitersCodes)

lexem_line = newFileString.split(' ')
lexems = []
for i in lexem_line:
    if i != '9' and i != '10' and i != '32':
        lexems.append(i)
print(lexems)

newFile = open('result.txt', 'w')
newFile.write(newFileString)