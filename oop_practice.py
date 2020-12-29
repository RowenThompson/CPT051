class Card:
    def  __init__(self, title, origin):
        self.title = title
        self.origin = origin

    def get_title(self):
        return self.title

    def get_origin(self):
        return self.origin

    def report_flag(self):
        print("this is not functional")

class Player:
    numer_of_players = 0

    @classmethod
    def count_number_of_players(cls):
        return cls.number_of_players

    @classmethod
    def add_player(cls):
        cls.number_of_players += 1
    
    def __init__(self, name, identity):
        self.name = name
        self.identity = identity

    def get_name(self):
        return name

    def get_identity():
        return identity

    def kick_me(self):
        print("You have attempted to kick a player. Function not coded")

class Mod_player(Player):
    def  __init__(self, title, origin):
        super().__init__(self, name, identity)
        
    def kick_player(player):
        print("You have tried to kick " + player.get_name())



c = Card("Title!", "Onion")

print(c.get_title() + " | " + c.get_origin())

