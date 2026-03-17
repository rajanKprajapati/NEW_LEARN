#present class for all puzzle 
"""This class is inherited by other puzzle"""
class Puzzle:
    def __init__(self):
        self.question=None
        self.answer=None

    #show puzzle text
    def diaplay_question(self):
        pass

    #check if currect
    def check_answer(self):
        pass

