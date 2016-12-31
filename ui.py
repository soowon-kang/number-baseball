# -*- coding: utf-8 -*-
import cs1graphics as cg
import baseball
import time


class KeyHandler(cg.EventHandler):
    def __init__(self, _canvas, _text, _s_circle, _b_circle):
        cg.EventHandler.__init__(self)
        self.canvas = _canvas
        self.msg = _text
        self.text = ''
        self.game = baseball.Baseball()
        self.game.initialize()
        self.s_circle = _s_circle
        self.b_circle = _b_circle
        pass

    def handle(self, event):
        if event.getDescription() == 'keyboard':
            key = event.getKey()
            """
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
            ascii_key = ord(key)
            if ascii_key == 127 or ascii_key == 8:
                self.text = self.text[:-1]
            elif ascii_key == 13:
                self.reset()
                a, b, c = map(int, self.text.strip().split())
                self.text = ''
                strike, ball = self.game.check(a, b, c)
                if strike < 0:
                    a, b, c = self.game.num
                    self.msg.setMessage('The answer was %d %d %d.' % (a, b, c))
                    self.game.initialize()
                    return

                self.msg.setMessage('%d strike(s), %d ball(s)' % (strike, ball))
                self.set_result(strike, ball)
                return
            elif ascii_key == 27:
                self.msg.setMessage("Bye bye~")
                time.sleep(3)
                self.canvas.close()
            elif 48 <= ascii_key <= 57 or ascii_key == 32:
                self.text += key
            self.msg.setMessage(self.text)

        elif event.getDescription() == 'mouse click':
            # self.msg.setMessage('mouse click')
            pass

        elif event.getDescription() == 'mouse release':
            # self.msg.setMessage('mouse release')
            pass

        elif event.getDescription() == 'mouse drag':
            # self.msg.setMessage('mouse drag')
            pass

    def set_result(self, _strike, _ball):
        for i in range(_strike):
            self.s_circle[i].setFillColor('dark green')
        for i in range(_ball):
            self.b_circle[i].setFillColor('yellow')
        if _strike == 3:
            self.msg.setMessage("Congratulations!")
        pass

    def reset(self):
        for i in range(3):
            self.s_circle[i].setFillColor('white')
            self.b_circle[i].setFillColor('white')

    pass


canvas = cg.Canvas(800, 600, bgColor='skyblue')

s_text = cg.Text(message="Strike", fontsize=23)
s_text.moveTo(100, 149)
canvas.add(s_text)

b_text = cg.Text(message="Ball", fontsize=23)
b_text.moveTo(100, 299)
canvas.add(b_text)

intro = cg.Text(message="Number Baseball Game", fontsize=37)
intro.moveTo(400, 50)
canvas.add(intro)

k_text = cg.Text("", 31)
k_text.moveTo(400, 450)
canvas.add(k_text)

line = cg.Path(cg.Point(200, 470), cg.Point(600, 470))
line.setBorderColor((90, 90, 90))
line.setBorderWidth(5)
line.setDepth(200)
canvas.add(line)

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

k_handler = KeyHandler(canvas, k_text, strike_circle, ball_circle)
canvas.addHandler(k_handler)

