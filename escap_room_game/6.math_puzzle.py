# Math based puzzle
from four_puzzle import Puzzle
class Math_puzzle(Puzzle):
    def __init__(self):
        self.question="If\n3 + 3 = 10\n4 + 4 = 16\n5 + 5 = 26\n\nWhat is\n6 + 6 = ?\n" #contains question
        self.__answer=40   #contains answer
    
    #for dispaly question
    def display_question(self):
        return self.question

    #verify answer
    def check_answer(self,User_Answer):
        if User_Answer is self.__answer:
            return "\nAnswer is True\n"
        else:
            return "\nAnswer is False\n"

player_1=Math_puzzle()
question=player_1.display_question() 
print(question)
print(player_1.check_answer('Echo'))
