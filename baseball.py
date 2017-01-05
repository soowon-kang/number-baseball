# -*- coding: utf-8 -*-
import random


class Baseball:
    def __init__(self, _max=9, _chance=10):
        """
        Main flow for the number baseball game
        
        :param _max:    [int] max number of the game input
        :param _chance: [int] max chances to play the game
        """
        
        self.num = []
        self.upper_bound = _max
        self.chance = _chance
        self.game_count = 0
        self.strike_count = 0
        self.ball_count = 0
        pass

    def initialize(self):
        """
        We must call this function before the game starts.
        We can also use re-initialize the game.
        """
        self.num = list(range(10))
        random.shuffle(self.num)
        self.num = self.num[:3]
        self.game_count = 0
        pass

    def check(self, *user):
        """
        Check the game result by using the user input
        
        :param user:    [list of int]       the user input
        :return:        [tuple of two ints] the game result,
                                            the number of strikes and balls
        """
        assert len(user) == 3, "The length of user input should be 3."

        self.game_count += 1
        
        # check the remained chances to play the game
        if self.game_count > self.chance:
            return -1, -1

        self.strike_count = 0
        self.ball_count = 0
        for i in range(3):
            assert isinstance(user[i], int), "Wrong type found"
            assert 0 <= user[i] <= self.upper_bound, "Out of bound."
            
            # calculate the number of strikes
            if self.num[i] == user[i]:
                self.strike_count += 1
                
            # calculate the number of balls
            if user[i] in self.num:
                self.ball_count += 1
        self.ball_count -= self.strike_count

        return self.strike_count, self.ball_count

    pass

