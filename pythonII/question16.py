# Imagine you are creating a Super Mario game. You need to define
# a class to represent Mario. What would it look like? If you aren't
# familiar with SuperMario, use your own favorite video or board game
# to model a player.

class mario:
    def __init__(self, avatar_name, coins, level, time, live):
        self.name = avatar_name
        self.coins = coins
        self.level = level
        self.time = time
        self.live = live