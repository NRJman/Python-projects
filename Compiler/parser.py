from tree import *
from analyser import *

tree = Tree()
print()
print()
print()

print(lexems)
error_table={"Wrong delimiter":-1, "Wrong key_word":-2, "No such identifier":-3, "Wrong integer":-4, "Dot expected, but end of array found":-5}


def takeWord(where, what):
    for key, value in where.items():
        if value == what:
            return key

def fail(fail_value):
    tree.add(fail_value)
    tree.current_element = tree.current_element.parent_element
    print(takeWord(error_table, fail_value))

def procedureIdentifier(i):
    tree.add('procedure-identifier')
    tree.add('identifier')
    if int(lexems[i]) >= 1000:
        tree.add(takeWord(identifierCodes, int(lexems[i])))
        tree.current_element = tree.current_element.parent_element
    else:
        print("ERROR:: THERE IS NO SUCH IDENTIFIER.")
        exit()
    tree.current_element = tree.current_element.parent_element
    tree.current_element = tree.current_element.parent_element


def variableIdentifier(i):
    tree.add('variable-identifier')
    tree.add('identifier')
    if 1001 <= int(lexems[i]) <= 1007:
        tree.add(takeWord(identifierCodes, int(lexems[i])))
        tree.current_element = tree.current_element.parent_element
        tree.current_element = tree.current_element.parent_element
        tree.current_element = tree.current_element.parent_element
        i += 1
    else:
        print("ERROR:: variable name can not be such as key word!")
        exit()
        print("ERROR:: THERE IS NO SUCH IDENTIFIER.")
        exit()
        i += 1
        tree.current_element = tree.current_element.parent_element
        tree.current_element = tree.current_element.parent_element
    return i


def rangesList():
    tree.add('range-list')
    tree.add('<empty>')
    tree.current_element = tree.current_element.parent_element
    tree.current_element = tree.current_element.parent_element


def range(i):
    tree.add('range')
    tree.add('unsigned-integer')
    tree.add(takeWord(constantsCodes, int(lexems[i])))
    tree.current_element = tree.current_element.parent_element
    tree.current_element = tree.current_element.parent_element
    i += 1
    if int(lexems[i]) == 46:
        tree.add(takeWord(delimitersCodes, int(lexems[i])))
        tree.current_element = tree.current_element.parent_element
        i += 1
        if int(lexems[i]) == 46:
            tree.add(takeWord(delimitersCodes, int(lexems[i])))
            tree.current_element = tree.current_element.parent_element
            i += 1
            tree.add('unsigned-integer')
            tree.add(takeWord(constantsCodes, int(lexems[i])))
            tree.current_element = tree.current_element.parent_element
            tree.current_element = tree.current_element.parent_element
            tree.current_element = tree.current_element.parent_element
        else:
            print("ERROR:: WRONG DELIMITER.")
            exit()
            tree.current_element = tree.current_element.parent_element
    else:
        print("ERROR:: WRONG DELIMITER.")
        exit()
        tree.current_element = tree.current_element.parent_element
    return i


def attribute(i):
    tree.add('attribute')
    if 1001 <= int(lexems[i]) <= 1007:
        tree.add(takeWord(identifierCodes, int(lexems[i])))
        tree.current_element = tree.current_element.parent_element
        tree.current_element = tree.current_element.parent_element
        i += 1
    elif int(lexems[i]) == 91:
        tree.add(takeWord(delimitersCodes, int(lexems[i])))
        tree.current_element = tree.current_element.parent_element
        i += 1
        i = range(i)
        i += 1
        rangesList()
        if int(lexems[i]) == 93:
            tree.add(takeWord(delimitersCodes, int(lexems[i])))
            tree.current_element = tree.current_element.parent_element
            tree.current_element = tree.current_element.parent_element
            i += 1
        else:
            print("ERROR:: WRONG DELIMITER.")
            exit()
            tree.current_element = tree.current_element.parent_element
            i += 1
    else:
        print("ERROR:: THERE IS NO SUCH IDENTIFIER.")
        exit()
        tree.current_element = tree.current_element.parent_element
        i += 1
    return i


def identifiersList(i):
    tree.add('identifiers-list')
    while int(lexems[i]) != 58:
        if int(lexems[i]) == 44:
            tree.add(takeWord(delimitersCodes, int(lexems[i])))
            tree.current_element = tree.current_element.parent_element
            i += 1
        else:
            i = variableIdentifier(i)
    tree.add('<empty>')
    tree.current_element = tree.current_element.parent_element
    tree.current_element = tree.current_element.parent_element
    return i


def attributesList(i):
    tree.add('attributes-list')
    while int(lexems[i]) != 59:
        if int(lexems[i]) == 44:
            i += 1
        else:
            i = attribute(i)
    tree.add('<empty>')
    tree.current_element = tree.current_element.parent_element
    tree.current_element = tree.current_element.parent_element
    return i


def declaration(i):
    tree.add('declaration')
    i = variableIdentifier(i)
    i = identifiersList(i)
    if int(lexems[i]) == 58:
        tree.add(takeWord(delimitersCodes, int(lexems[i])))
        tree.current_element = tree.current_element.parent_element
        i += 1
        attribute(i)
        i += 1
        i = attributesList(i)
        if int(lexems[i]) == 59:
            tree.add(takeWord(delimitersCodes, int(lexems[i])))
            tree.current_element = tree.current_element.parent_element
            tree.current_element = tree.current_element.parent_element
        else:
            print("ERROR:: WRONG DELIMITER.")
            exit()
            tree.current_element = tree.current_element.parent_element
            i += 1
    else:
        print("ERROR:: WRONG DELIMITER.")
        exit()
        tree.current_element = tree.current_element.parent_element
        i += 1
    return i


def declarationsList(i):
    tree.add('declarations-list')
    i = declaration(i)
    tree.add('<empty>')
    tree.current_element = tree.current_element.parent_element
    tree.current_element = tree.current_element.parent_element
    return i


def variableDeclarations(i):
    tree.add('variable-declarations')
    if int(lexems[i]) == 402:
        tree.add(takeWord(keyWordsCodes, int(lexems[i])))
        tree.current_element = tree.current_element.parent_element
        i += 1
        i = declarationsList(i)
        tree.add('<empty>')
        tree.current_element = tree.current_element.parent_element
    else:
        print("ERROR:: WRONG KEYWORD.")
        exit()
        tree.current_element = tree.current_element.parent_element
        i += 1
    return i


def constantIdentifier(i):
    tree.add('constant-identifier')
    tree.add('identifier')
    tree.add(takeWord(identifierCodes, int(lexems[i])))
    tree.current_element = tree.current_element.parent_element
    tree.current_element = tree.current_element.parent_element
    return i


def constant(i):
    tree.add('constant')
    tree.add('unsigned-integer')
    tree.add(takeWord(constantsCodes, int(lexems[i])))
    tree.current_element = tree.current_element.parent_element
    tree.current_element = tree.current_element.parent_element
    tree.current_element = tree.current_element.parent_element
    return i



def constantDeclaration(i):
    tree.add('constant-declaration')
    i += 1
    i = constantIdentifier(i)
    i += 1
    if(int(lexems[i]) == 61):
        tree.add(takeWord(delimitersCodes, int(lexems[i])))
        tree.current_element = tree.current_element.parent_element
        i += 1
        i = constant(i)
        i += 1
        if(int(lexems[i]) == 59):
            tree.add(takeWord(delimitersCodes, int(lexems[i])))
            tree.current_element = tree.current_element.parent_element
            tree.current_element = tree.current_element.parent_element
            tree.current_element = tree.current_element.parent_element
        else:
            print("ERROR:: WRONG DELIMITER.")
            exit()
            i += 1
    else:
        print("ERROR:: WRONG DELIMITER.")
        exit()
        i += 1
    return i



def constantDeclarationsList(i):
    tree.add('constant-declarations-list')
    while int(lexems[i + 1]) != 404:
        i = constantDeclaration(i)
    tree.add('<empty>')
    tree.current_element = tree.current_element.parent_element
    tree.current_element = tree.current_element.parent_element
    tree.current_element = tree.current_element.parent_element
    tree.current_element = tree.current_element.parent_element
    return i


def constantDeclarations(i):
    tree.add('constant-declarations')
    tree.add('CONST')
    tree.current_element = tree.current_element.parent_element
    i = constantDeclarationsList(i);
    i += 1
    return i

def declarations(i):
    tree.add('declarations')
    i = variableDeclarations(i)
    tree.current_element = tree.current_element.parent_element
    i += 1
    i = constantDeclarations(i)
    return i


def statementsList():
    tree.add('statements-list')
    tree.add('<empty>')
    tree.current_element = tree.current_element.parent_element
    tree.current_element = tree.current_element.parent_element
    tree.current_element = tree.current_element.parent_element


def block(i):
    tree.add('block')
    i = declarations(i)
    if int(lexems[i]) == 404:
        tree.add(takeWord(keyWordsCodes, int(lexems[i])))
        i += 1
        statementsList()
        if int(lexems[i]) == 405:
            tree.add(takeWord(keyWordsCodes, int(lexems[i])))
            tree.current_element = tree.current_element.parent_element
            tree.current_element = tree.current_element.parent_element
        else:
            print("ERROR:: WRONG KEYWORD.")
            exit()
            tree.current_element = tree.current_element.parent_element
            i += 1
    else:
        print("ERROR:: WRONG KEYWORD.")
        exit()
        tree.current_element = tree.current_element.parent_element
        i += 1
    return i


def program():
    tree.add('program')
    i = 0
    if int(lexems[i]) == 401:
        tree.add(takeWord(keyWordsCodes, int(lexems[i])))
        print("-------", tree.current_element, "-----------")
        tree.current_element = tree.current_element.parent_element
        i += 1
        procedureIdentifier(i)
        i += 1
        if int(lexems[i]) == 59:
            tree.add(takeWord(delimitersCodes, int(lexems[i])))
            tree.current_element = tree.current_element.parent_element
            i += 1
            i = block(i)
            i += 1
            print(len(lexems))
            if i == len(lexems) - 1:
                print("ERROR:: DOT EXPECTED, BUT END OF ARRAY FOUND.")
                exit()
            else:
                if int(lexems[i]) == 46:
                    tree.add(takeWord(delimitersCodes, int(lexems[i])))
                elif int(lexems[i]) == '':
                    print("ERROR:: WRONG DELIMITER.")
                    exit()
                    tree.current_element = tree.current_element.parent_element
                    i += 1
                else:
                    print("ERROR:: WRONG DELIMITER.")
                    exit()
                    tree.current_element = tree.current_element.parent_element
                    i += 1
        else:
            print("ERROR:: WRONG DELIMITER.")
            exit()
            tree.current_element = tree.current_element.parent_element
            i += 1
    else:
        print("ERROR:: WRONG KEYWORD.")
        exit()
        tree.current_element = tree.current_element.parent_element
        i += 1
    return tree


program()
tree.print_tree()