print("---Add Quiz---")
qName = input("Please enter the quiz name")
numQ = int(input("Please enter the number of questions"))
qList = {}
questString = ""
for qSet in range(numQ):
    q = input("Please enter question {0}".format(qSet+1))
    questString = q + "   "
    numAns = int(input("Please enter the number of answers."))
    answerVar = 'A'
    for aSet in range(numAns):
        answer = input("Please enter answer {0}".format(answerVar))
        questString += " {0}:{1} ".format(answerVar, answer)
        answerVar = ord(answerVar)
        answerVar +=1
        answerVar = chr(answerVar)
    print(questString)
    correct = input("Which answer is correct?")
    qList[qSet] = {'question':questString}, {'answer':correct}
print(qList)