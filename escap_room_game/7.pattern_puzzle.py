# Sequence/pattern based puzzle
from four_puzzle import Puzzle
class Pattern_puzzle(Puzzle):
    def __init__(self):
        self.question="Find the missing number: \n2 → 6 → 12 → 20 → 30 → ?\n" #contains question
        self.__answer=42   #contains answer
    
    #for dispaly question
    def display_question(self):
        return self.question

    #verify answer
    def check_answer(self,User_Answer):
        if User_Answer is self.__answer:
            return "Answer is True\n"
        else:
            return "Answer is False\n"
        
  
player_1=Pattern_puzzle()
question=player_1.display_question() 
print(question)
print(player_1.check_answer('Echo'))
