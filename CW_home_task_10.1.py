# codewars task1 - 'Ball, super Ball' - SoftServe10 - Lesson10
'''
	Create a class Ball.

	Ball objects should accept one argument for 
	"ball type" when instantiated. # 

	If no arguments are given, ball objects should instantiate with a "ball type" 
	of "regular."
'''


# VAR1 - NON-RELEWANT WITH CODEWARS
class Ball(object):

    def __init__(self, ball_type = 'regular'):
        self.ball_type = ball_type


ball1 = Ball()
print(ball1.ball_type)

ball2 = Ball('super')
print(ball2.ball_type)


# VAR2 - NON-RELEWANT WITH CODEWARS
# solution through the instance of the class
# not using constructor
class Ball(object):

    def ball_type(self, ball_type = 'regular'):
        self.ball_type = ball_type
    
        return self.ball_type


ball1 = Ball()
s = ball1.ball_type() # функція без виклику - тільки звернення
print(s)

# s = ball1.ball_type # утворення bound-method
# print(s.__func__) # <function Ball.ball_type at 0x7f9955782160>

ball2 = Ball()
print(ball2.ball_type('super')) # функція без виклику

# або через метод getattr
print(getattr(ball1, 'ball_type'))
print(getattr(ball2, 'ball_type'))

