"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
import random

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3      # Number of attempts


def main():
    graphics = BreakoutGraphics()
    dx = graphics.get_dx()
    dy = graphics.get_dy()
    figure = 0
    # is a variable to count how many times you die
    num = 0
    # is a variable to count how many bricks you break
    while True:
        '''
        graphics.test is a variable from class. It's original value is 0. When user click the mouse, graphics test  
        plus 1 and the class will return dx and dy to the user. And then it plus one again in order to pretend get new
        dx and dy.
        '''
        if graphics.test == 1:
            dx = graphics.get_dx()
            dy = graphics.get_dy()
            # dx and dy are the speed that ball move.
            graphics.test += 1
        graphics.ball.move(dx, dy)

        '''
        If ball out of the screen border, it's dx and dy will be reverse until it go into the border.
        '''
        if graphics.ball.x <= 0:
            dx = abs(dx)
            # the ball dx is negative so give it a absolute value to let it reverse.
        if graphics.ball.x + graphics.ball.width >= graphics.window.width:
            dx = -abs(dx)
            # the ball dx is positive so give it a absolute value and negative sign to let it reverse.
        if graphics.ball.y <= 0:
            dy = abs(dy)
            # the ball dy is negative so give it a absolute value to let it reverse.
        '''
        When the ball out of the bottom border, let it go back to the the central of screen and let it's dx and dy go 
        back to 0, so it won't move. Moreover, graphics.test minus two so that next time we click it can have new dx
        and dy and move again.
        '''
        if graphics.ball.y + graphics.ball.height >= graphics.window.height:
            graphics.ball.x = (graphics.window.width-graphics.ball.width)/2
            graphics.ball.y = (graphics.window.height-graphics.ball.height)/2
            dx = 0
            dy = 0
            figure += 1
            graphics.test = 0
            if figure == NUM_LIVES:
                graphics.game = False
                graphics.reflection()

                break
            # When we out of the bottom border 3 times, this time you click, the ball won't move anymore
        '''
        Check if ball hit the object. If it done, classify witch object it hit. If it hit paddle, let dx have 50% to 
        choose left or right and let dy be reversed, if it hit label, let it's dx and dy be same so it wont have affect
        both and the rest object is brick, when hits brick, let dx have 50% to choose left or right and let dy be 
        reversed and window will remove brick. And how to classify if it hit object we need to inspect four angles
        of ball.
        
        '''
        if True:
            amount = True
            '''
            It is a switch. Classify the first corner to see if it hit object. If it does, we don't need to see other
            corners, but it don't, we need to check another corner instead.Every corner follow this rule.
            '''
            if amount:
                point1 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
                # the left top corner
                if point1 is not None:
                    if point1 == graphics.paddle:
                        # it is a function that can give a ball a random dx
                        graphics.set_dx()
                        dx = graphics.get_dx()
                        dy = -abs(dy)
                    elif point1 == graphics.label:
                        graphics.ball.x = graphics.ball.x
                        graphics.ball.y = graphics.ball.y
                    else:
                        num += 1
                        if random.random() > 0.5:
                            graphics.set_dx()
                            dx = graphics.get_dx()
                        # it is variable to count our score
                        dy = -dy
                        graphics.window.remove(point1)
                        graphics.label.text = 'Score==' + str(num)
                    amount = False
            if amount:
                point2 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball.height)
                # the left bottom corner
                if point2 is not None:
                    if point2 == graphics.paddle:
                        graphics.set_dx()
                        dx = graphics.get_dx()
                        dy = -abs(dy)
                    elif point2 == graphics.label:
                        graphics.ball.x = graphics.ball.x
                        graphics.ball.y = graphics.ball.y
                    else:
                        graphics.set_dx()
                        dx = graphics.get_dx()
                        num += 1
                        dy = -dy
                        graphics.window.remove(point2)
                        graphics.label.text = 'Score==' + str(num)
                    amount = False
            if amount:
                point3 = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y)
                # the right top corner
                if point3 is not None:
                    if point3 == graphics.paddle:
                        dy = -abs(dy)
                        graphics.set_dx()
                        dx = graphics.get_dx()
                    elif point3 == graphics.label:
                        graphics.ball.x = graphics.ball.x
                        graphics.ball.y = graphics.ball.y
                    else:
                        num += 1
                        graphics.set_dx()
                        dx = graphics.get_dx()
                        dy = -dy
                        graphics.window.remove(point3)
                        graphics.label.text = 'Score==' + str(num)
                    amount = False
            if amount:
                point4 = graphics.window.get_object_at(graphics.ball.x+graphics.ball.width, graphics.ball.y + graphics.ball.height)
                # the right bottom corner
                if point4 is not None:
                    if point4 == graphics.paddle:
                        dy = -abs(dy)
                        graphics.set_dx()
                        dx = graphics.get_dx()
                    elif point4 == graphics.label:
                        graphics.ball.x = graphics.ball.x
                        graphics.ball.y = graphics.ball.y
                    else:
                        graphics.set_dx()
                        dx = graphics.get_dx()
                        num += 1
                        dy = -dy
                        graphics.window.remove(point4)
                        graphics.label.text = 'Score==' + str(num)
                    amount = False
        if num == graphics.brick_num:
            # every brick be broken, so we let the game end, so let ball go to the point of central and let program stop
            graphics.ball.x = (graphics.window.width - graphics.ball.width) / 2
            graphics.ball.y = (graphics.window.height - graphics.ball.height) / 2
            graphics.game = True
            graphics.reflection()
            break

        pause(FRAME_RATE)

    # Add the animation loop here!


if __name__ == '__main__':
    main()
