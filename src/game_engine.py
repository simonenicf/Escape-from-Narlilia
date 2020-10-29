class Console():
    def check_answer(self, question, answers=None):
        print(question)

        while True:
            userInput = input('Answer: ')

            if (not answers == None):

                for answer in answers:
                    if(userInput == answer):
                        return answer
            else:
                return userInput
        
            print('This is a invalid answer! Please put in a valid answer!\n')

class Player():
    def set_name(self, name):
        self.name = name
    
    def get_name(self, name):
        return self.name
    

    