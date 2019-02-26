def valInput(input):
    #Checks for valid integer input.
    try:
        val = int(input)
        return True
    except ValueError:
        return False

def valAnswer(input, numAns):
    #checks to ensure correct answer is an available answer
    answerCheck = 'A'
    for check in range(numAns):
        if(input == answerCheck):
            return True
        answerCheck = chr(ord(answerCheck)+1)
    return False

def addQuiz():
    print("---Add Quiz---")
    qName = input("Please enter the quiz name")
    numQ = input("Please enter the number of questions")
    #check for valid input
    while(valInput(numQ) == False or int(numQ) <= 0):
        #invalid input
        numQ = input("Please enter valid input for the number of questions (int greater than 0)")
    numQ = int(numQ)
    #empty list for questions and answers
    qList = {}
    for qSet in range(numQ):
        q = input("Please enter question {0}".format(qSet+1))
        questString = q + "   "
        numAns = input("Please enter the number of answers.")
        #checks for valid int input for number of answers
        while(valInput(numAns) == False or int(numAns) <= 0):
            #invalid input
            numAns = int(input("Please enter valid input for the number of answers (int greater than 0)"))
        numAns = int(numAns)
        answerVar = 'A'
        for aSet in range(numAns):
            answer = input("Please enter answer {0}".format(answerVar))
            questString += " {0}:{1} ".format(answerVar, answer)
            answerVar = chr(ord(answerVar)+1)
        print(questString)
        correct = input("Which answer is correct?")
        #checks to ensure valid answer is entered from answer list
        while(valAnswer(correct, numAns) == False):
            #invalid input
            correct = input("Please select one of the entered answers")
        #enters entry into dictionary to be read by bot
        qList[qSet] = {'question':questString}, {'answer':correct}
    return qList