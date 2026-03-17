#control room acsess
class Door:
    def __init__(self):
        self.__is_lock="Lock" #Lock/Unlock
    
    #open door 
    def unlock(self):
        self.__is_lock="Unlock"
        

    #close door 
    def lock(self):
        self.__is_lock="Lock"
        
    
    # return locked/unlocked -> After solving puzzle
    def check_status(self):
        return "Door is "+self.__is_lock
player=Door()
print(player.check_status()) 
player.unlock()
print(player.check_status())   

