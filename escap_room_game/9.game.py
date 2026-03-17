#controls the entire gameplay
#this is the main controller
class Game:
    def __init__(self):
        self.player=None #player object
        self.rooms=None #List of rooms
        self.current_room_index=None #track current level
        self.score_manager=None #manage score

    #start_game
    def start_game(self):
        pass

    #create_puzzle_and_rooms
    def setup_rooms(self):
        pass

    #main game loop
    def play(self):
        pass

    #go to next level
    def move_to_next_room(self):
        pass
    
    #show final score
    def end_game(self):
        pass
