#puzzle based on riddles
from four_puzzle import Puzzle
class Riddle_puzzle(Puzzle):
    def __init__(self):
        self.question="Question\nI speak without a mouth\nand hear without ears.\nI have no body,\nbut I come alive with wind.\n\nWhat am I?\n" #contains question
        self.__answer=["Echo","Whistle","Flute","Wind itself"]   #contains answer

    #Display Question
    def display_question(self):
        return self.question

    #check Answer
    def check_answer(self,User_Answer):
        if User_Answer in self.__answer:
            return "\nAnswer is "+"True\n"
        else:
            return "\nAnswer is "+"False\n"

player_1=Riddle_puzzle()
question=player_1.display_question() 
print(question)
print(player_1.check_answer('Echo'))
