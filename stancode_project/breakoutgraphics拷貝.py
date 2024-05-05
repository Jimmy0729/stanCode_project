"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10  # Number of rows of bricks
BRICK_COLS = 10    # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7   # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        self.ball = GOval(2*BALL_RADIUS, 2*BALL_RADIUS)
        self.ball.filled = True
        self.ball.fill_color = '#BEBEBE'
        self.ball.color = '#BEBEBE'
        self.window.add(self.ball, x=(self.window.width-self.ball.width)/2, y=(self.window.height-self.ball.height)/2)
        self.paddle = GRect(PADDLE_WIDTH, PADDLE_HEIGHT)
        self.paddle.fill_color = True
        self.paddle.filled = 'black'
        self.paddle.color = 'black'
        self.window.add(self.paddle, x=(self.window.width-self.paddle.width)/2, y=self.window.height-PADDLE_OFFSET)
        self.brick_num = BRICK_COLS * BRICK_COLS
        self.score = 0
        self.label = GLabel('Score==' + str(self.score))
        # the score board
        self.label.font = '-25'
        self.window.add(self.label, x=0, y=self.window.height)
        self.__dx = 0
        self.__dy = 0
        self.test = 0
        # it is a switch to pass dx and dy to user
        onmousemoved(self.drag)
        onmouseclicked(self.start)
        self.game = False
        self.win_slogan = GLabel('You win:)')
        self.win_slogan.font = '-40'
        self.lose_slogan = GLabel('You lose:(')
        self.lose_slogan.font = '-40'
        '''
        Use for loop to product brick. According to the proportion of length of BRICK_COLS to choose brick's color
        '''

        for i in range(BRICK_COLS):
            for j in range(BRICK_ROWS):
                self.brick = GRect(BRICK_WIDTH, BRICK_HEIGHT)
                if i <= BRICK_COLS/5:
                    self.brick.filled = True
                    self.brick.fill_color = '	#272727'
                    self.brick.color = '	#272727'
                if BRICK_COLS/5 < i <= 2*BRICK_COLS/5:
                    self.brick.filled = True
                    self.brick.fill_color = '#5B5B5B'
                    self.brick.color = '#5B5B5B'
                if 2*BRICK_COLS/5 < i <= 3*BRICK_COLS/5:
                    self.brick.filled = True
                    self.brick.fill_color = '#8E8E8E'
                    self.brick.color = '#8E8E8E'
                if 3*BRICK_COLS/5 < i <= 4*BRICK_COLS/5:
                    self.brick.filled = True
                    self.brick.fill_color = '	#BEBEBE'
                    self.brick.color = '	#BEBEBE'
                if i > 4*BRICK_COLS/5:
                    self.brick.filled = True
                    self.brick.fill_color = '	#D0D0D0'
                    self.brick.color = '	#D0D0D0'
                self.window.add(self.brick, x=0 + j*(self.brick.width+BRICK_SPACING), y=BRICK_OFFSET+i*(self.brick.height + BRICK_SPACING))
    '''
    Let mouse move the paddle on it's central location. When mouse out of the border let whole paddle stay inside
    '''
    def drag(self, mouse):
        self.paddle.x = mouse.x-self.paddle.width/2
        if 0 >= mouse.x-self.paddle.width/2:
            self.paddle.x = 0
        if mouse.x + self.paddle.width/2 >= self.window.width:
            self.paddle.x = self.window.width-self.paddle.width
    '''
    When mouse click, give it a initial dx and dy, when user detect self.test ==1, it will use get_dx and get_dy to 
    find  initial dx and dy
    '''
    def start(self, event):
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.test += 1

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def set_dx(self):
        self.__dx = random.randint(4, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        return self.__dx

        # it is a function let ball have random dx

    def reflection(self):
        if self.game:
            self.window.add(self.win_slogan, x=(self.window.width-self.lose_slogan.width)/2, y=(self.window.height-self.win_slogan.height)/2)
        else:
            self.window.add(self.lose_slogan, x=(self.window.width-self.lose_slogan.width)/2, y=(self.window.height-self.lose_slogan.height)/2)
    # it is a function when game over and then will reflect their relative slogan

        # Create a paddle
        # Center a filled ball in the graphical window
        # Default initial velocity for the ball
        # Initialize our mouse listeners
        # Draw bricks
