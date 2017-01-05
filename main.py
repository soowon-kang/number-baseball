# -*- coding: utf-8 -*-
import cs1graphics as cg
import baseball
import time


class KeyHandler(cg.EventHandler):
    def __init__(self, _canvas, _status, _chance, _s, _b):
        """
        [API] for cs1graphics
        UI definitions
        
        :param _canvas: [cs1graphics.Canvas]            graphic background
        :param _status: [cs1graphics.Text]              indicate status
        :param _chance: [cs1graphics.Text]              indicate chances
        :param _s:      [list of cs1graphics.Circle]    visualize # of strikes
        :param _b:      [list of cs1graphics.Circle]    visualize # of balls
        """
        
        # setting parameters
        cg.EventHandler.__init__(self)
        self.canvas = _canvas
        self.msg = _status
        self.text = ''
        self.num = ''
        self.chance = _chance
        self.game = baseball.Baseball()
        self.game.initialize()
        self.s_circle = _s
        self.b_circle = _b
        
        # setting initial status
        self.set_chance()
        self.msg.setMessage("Game starts!")
        pass
    
    def handle(self, event):
        """
        [API] for cs1graphics
        Handle the keyboard and mouse events in some proper ways
        
        :param event:   handling event
        """
        if event.getDescription() == 'keyboard':
            # handle keyboard events
            key = event.getKey()
            key_num = ord(key)
            
            """ helpful ascii
            del:    127
            0:      48
            9:      57
            A:      65
            a:      97
            esc:    27
            enter:  13
            space:  32
            ,:      44
            ctrl+H: 8
            """
            
            # use above ascii numbers
            if key_num == 127 or key_num == 8:
                self.num = self.num[:-1]
                self.text = self.num
            elif key_num == 13:
                try:
                    # cast numbers (+ error handling)
                    a, b, c = map(int, self.text.strip().split())
                except ValueError:
                    self.text = ''
                    self.msg.setMessage("Not enough numbers.")
                    return
                
                # re-initialize status of parameters
                self.num = ''
                self.reset()
                
                # calculate strike and ball
                strike, ball = self.game.check(a, b, c)
                
                # check there is no remained chance to play the game
                if strike < 0:
                    a, b, c = self.game.num
                    self.msg.setMessage('The answer was %d %d %d.' % (a, b, c))
                    self.game.initialize()
                    return
                
                # post the remained chances
                self.set_chance()
                
                # update status text
                self.text = '%d strike(s) %d ball(s)' % (strike, ball)
                
                # update status (+ check the game ends)
                self.set_result(strike, ball)
            elif key_num == 27:
                # exit the game
                self.msg.setMessage("Bye bye~")
                time.sleep(3)
                self.canvas.close()
            elif 48 <= key_num <= 57 or key_num == 32:
                # input numbers handling
                self.num += key
                self.text = self.num
            
            # set the status text
            self.msg.setMessage(self.text)
        
        elif event.getDescription() == 'mouse click':
            # handle mouse click events
            # self.msg.setMessage('mouse click')
            pass
        
        elif event.getDescription() == 'mouse release':
            # handle mouse release events
            # self.msg.setMessage('mouse release')
            pass
        
        elif event.getDescription() == 'mouse drag':
            # handle mouse drag events
            # self.msg.setMessage('mouse drag')
            pass
    
    def set_result(self, _strike, _ball):
        """
        Visualize the result of a turn
        If the number of strikes is 3, the user wins.
        
        :param _strike: [int] the number of strikes
        :param _ball:   [int] the number of balls
        :return:
        """
        for i in range(_strike):
            self.s_circle[i].setFillColor('dark green')
        for i in range(_ball):
            self.b_circle[i].setFillColor('yellow')
        
        # check the game ends
        if _strike == 3:
            self.text = "Congratulations!"
            self.game.initialize()
            self.set_chance()
        pass
    
    def set_chance(self):
        """
        Wrapper function to set the remained chances
        """
        self.chance.setMessage("%d" % (self.game.chance-self.game.game_count))
        pass
    
    def reset(self):
        """
        Wrapper function to reset the visualized objects
        """
        for i in range(3):
            self.s_circle[i].setFillColor('white')
            self.b_circle[i].setFillColor('white')
        pass
    
    pass


if __name__ == "__main__":
    # Background
    canvas = cg.Canvas(800, 600, bgColor='skyblue')
    
    # Title msg
    intro = cg.Text(message="Number Baseball Game", fontsize=37)
    intro.moveTo(400, 50)
    canvas.add(intro)
    
    # "Strike" msg
    s_text = cg.Text(message="Strike", fontsize=23)
    s_text.moveTo(100, 149)
    canvas.add(s_text)
    
    # "Ball" msg
    b_text = cg.Text(message="Ball", fontsize=23)
    b_text.moveTo(100, 299)
    canvas.add(b_text)
    
    # Remained chances msg
    chance_text = cg.Text("", 23)
    chance_text.moveTo(100, 450)
    canvas.add(chance_text)
    
    # Status msg
    status_text = cg.Text("", 31)
    status_text.moveTo(400, 450)
    canvas.add(status_text)
    
    # Underline for status msg
    line = cg.Path(cg.Point(200, 470), cg.Point(600, 470))
    line.setBorderColor((90, 90, 90))
    line.setBorderWidth(5)
    line.setDepth(200)
    canvas.add(line)
    
    # Circles for strike
    cs1 = cg.Circle(50)
    cs1.setBorderColor('white')
    cs1.setFillColor('white')
    cs1.setBorderWidth(7)
    cs1.moveTo(350, 150)
    cs2 = cs1.clone()
    cs2.move(150, 0)
    cs3 = cs2.clone()
    cs3.move(150, 0)
    strike_circle = [cs1, cs2, cs3]
    canvas.add(cs1)
    canvas.add(cs2)
    canvas.add(cs3)
    
    # Circles for ball
    cb1 = cs1.clone()
    cb2 = cs2.clone()
    cb3 = cs3.clone()
    cb1.move(0, 150)
    cb2.move(0, 150)
    cb3.move(0, 150)
    ball_circle = [cb1, cb2, cb3]
    canvas.add(cb1)
    canvas.add(cb2)
    canvas.add(cb3)
    
    # Event handler
    key_handler = KeyHandler(canvas, status_text, chance_text,
                             strike_circle, ball_circle)
    canvas.addHandler(key_handler)

