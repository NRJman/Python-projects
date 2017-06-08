from parser import program

namesArr = []
typesArr = []
constNamesArr = []
constValuesArr = []
blockPoint = ""
declarationsPoint = ""
tree = program()
flag = False

def compile():
    print("\n====================CODE=========================")
    print("---" + tree.root.leaves[0].leaves[1].leaves[0].leaves[0].val + "---")
    generator(tree.root)

def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def generator(current):
    global namesArr
    global typesArr
    global constNamesArr
    global constValuesArr
    global blockPoint
    global declarationsPoint
    global flag
    includeFlag = False
    printerCount = 0
    sameVarsFlag = False
    sameVarAndConstantFlag = False
    sameConstantsFlag = False

    if current.val == "block":
        blockPoint = current
    if current.val == "declarations":
        declarationsPoint = current

    if current.val == "declarations":
        print("DATA SEGMENT")
        print()
    elif current.val == "variable-declarations":

        namesArr.append(current.leaves[1].leaves[0].leaves[0].leaves[0].leaves[0].val)
        for i in range(len(current.leaves[1].leaves[0].leaves[1].leaves)):
            if current.leaves[1].leaves[0].leaves[1].leaves[i].val == "variable-identifier":
                namesArr.append(current.leaves[1].leaves[0].leaves[1].leaves[i].leaves[0].leaves[0].val)

        if current.leaves[1].leaves[0].leaves[3].leaves[0].val == "[":
            typesArr.append(current.leaves[1].leaves[0].leaves[3].leaves[1].leaves[0].leaves[0].val + "-" +
                            current.leaves[1].leaves[0].leaves[3].leaves[1].leaves[3].leaves[0].val)
            for i in range(len(current.leaves[1].leaves[0].leaves[4].leaves)):
                if current.leaves[1].leaves[0].leaves[4].leaves[i].leaves[0].val == "[":
                    typesArr.append(current.leaves[1].leaves[0].leaves[4].leaves[i].leaves[1].leaves[0].leaves[0].val + "-" +
                                    current.leaves[1].leaves[0].leaves[4].leaves[i].leaves[1].leaves[3].leaves[0].val)
                else:
                    typesArr.append(current.leaves[1].leaves[0].leaves[4].leaves[i].leaves[0].val)
        else:
            typesArr.append(current.leaves[1].leaves[0].leaves[3].leaves[0].val)
            for i in range(len(current.leaves[1].leaves[0].leaves[4].leaves) - 1):
                if current.leaves[1].leaves[0].leaves[4].leaves[i].leaves[0].val == "[":
                    typesArr.append(current.leaves[1].leaves[0].leaves[4].leaves[i].leaves[1].leaves[0].leaves[0].val + "-" +
                                    current.leaves[1].leaves[0].leaves[4].leaves[i].leaves[1].leaves[3].leaves[0].val)
                else:
                    typesArr.append(current.leaves[1].leaves[0].leaves[4].leaves[i].leaves[0].val)
        generator(blockPoint.leaves[1])
    elif current.val == "constant-declarations":
        for i in range(len(current.leaves[1].leaves) - 1):
            constNamesArr.append(current.leaves[1].leaves[i].leaves[0].leaves[0].leaves[0].val)
            constValuesArr.append(current.leaves[1].leaves[i].leaves[0].leaves[2].leaves[0].leaves[0].val)
        generator(tree.root.leaves[0].leaves[3].leaves[1])
        return
    elif current.val == "BEGIN":
        if constNamesArr and constValuesArr != []:
            for i in namesArr:
                for j in range(len(namesArr)):
                    if i == namesArr[j]:
                        if namesArr.index(i) != j:
                            includeFlag = True
                            sameVarsFlag = True
                for j in range(len(constNamesArr)):
                    if i == constNamesArr[j]:
                        includeFlag = True
                        sameVarAndConstantFlag
                for j in range(len(typesArr)):
                    if i == typesArr[j]:
                        print("ERROR:: variable name is the same as variable type!")
                        return
                if i == tree.root.leaves[0].leaves[1].leaves[0].leaves[0].val:
                    print("ERROR:: variable name is the same as program name!")
                    return

            if includeFlag == True:
                if sameVarsFlag == True:
                    print("Error:: this variable name is already used!")
                else:
                    print("Error:: the variable name is the same as one of constants names!")
                return

            for i in typesArr:
                if isint(i[0]) == False:
                    if i in ["SIGNAL", "COMPLEX", "EXT"]:
                        print(namesArr[printerCount] + "    ?    ?")
                    else:
                        print(str(namesArr[printerCount]) + "    DW    ?")
                else:
                    start = int(i[0])
                    end = int(i[2])
                    myRange = start
                    for k in range(start + 1, end + 1):
                        myRange = str(myRange) + ", " + str(k)
                    print(namesArr[printerCount] + '        ' + myRange)
                printerCount += 1

            for i in constNamesArr:
                for j in range(len(constNamesArr)):
                    if i == constNamesArr[j]:
                        if constNamesArr.index(i) != j:
                            includeFlag = True
                            sameConstantsFlag = True
                for j in range(len(typesArr)):
                    if i == typesArr[j]:
                        print("ERROR:: constant name is the same as variable type!")
                        return
                if i == tree.root.leaves[0].leaves[1].leaves[0].leaves[0].val:
                    print("ERROR:: constant name is the same as program name!")
                    return

            if includeFlag == True:
                if sameVarsFlag == False and sameConstantsFlag == True:
                    print("Error:: this constant name is already used!")
                else:
                    print("Error:: the variable name is the same as one of constants names!")
                return

            printerCount = 0

            for i in constNamesArr:
                print(i + "      DW    " + constValuesArr[printerCount])
                printerCount += 1

            print()
            print("DATA ENDS")
            print()
            print("CODE SEGMENT")
            print("CODE ENDS")

        return

    for i in range(len(current.leaves)):
        if current.val == "variable-declarations":
            generator(declarationsPoint.leaves[1])
            flag = True
            return
        else:
            generator(current.leaves[i])
            if flag == True:
                return