class quiz:
    question = {
        0:{'question':'What is 5+4?   A:7   B:54   C:9   D:11', 'answer':'C'},
        1:{'question':'What is 12 / 3?   A:3   B:4   C:9   D:2', 'answer':'B'},
        2:{'question':'What is 6-5?   A:0   B:3   C:2   D:1', 'answer':'C'},
        3:{'question':'What is 3*7?   A:21   B:14   C:23   D:19', 'answer':'A'},
        4:{'question':'What is 8+7?   A:15   B:14   C:17   D:13', 'answer':'A'}
    }

    def __init__ (self):
        self.questNum = 0
        self.numCorrectAns = 0

    def checkAns(self, ans):
        if quiz.question [self.questNum]['answer'] == ans.upper():
            self.numCorrectAns+=1
        self.questNum+=1
        if self.questNum == 5:
            return True
        return False

    def askQuestion(self):
        return self.question[self.questNum]['question']

