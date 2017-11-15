import breezycreate2
import os
import time
import sys
sys.setrecursionlimit(1500)
from multiprocessing import Process, Queue

robot = breezycreate2.Robot(port='/dev/ttyUSB1')

speed = lambda value: robot.setForwardSpeed(value)
turn = lambda value: robot.setTurnSpeed(value)
sleep = lambda value: time.sleep(value)

direction = -1

def u_turn(d):
	if d > 0:
        	print "u-turn clockwise"
		step(0, 200, 1)
		while robot.getLightBumper()[3] or robot.getLightBumper()[4]:
			step(0, 100, 1)			
		step(80, 0, 2)
		step(0, 150, 1)
	else:
        	print "u-turn counter-clockwise"
		step(0, -200, 1)
		while robot.getLightBumper()[1] or robot.getLightBumper()[2]:
                        step(0, -100, 1)
		step(80, 0, 2)
		step(0, -150, 1)

def step(speed_val, turn_val, time_val):
  if speed_val:
    turn(0)
    speed(speed_val)
  else:
    speed(0)
    turn(turn_val)
  sleep(time_val)

def sensewalls():

	if(robot.getWallSeen() and robot.getLightBumper()[0] and robot.getLightBumper()[2]):
                speed(0)
		move(True, -1)
        elif(robot.getLightBumper()[5] and (robot.getLightBumper()[4] or robot.getLightBumper()[3]) and not robot.getWallSeen()):
                speed(0)
                move(True, 1)
        elif (robot.getLightBumper()[4] or robot.getLightBumper()[1]):
                speed(0)
                move(True, 0)
        else:
                move(False,0)
	sensewalls()

   
def move(uturn, rotation):
	# direction: 0 - turn around, 1 - clockwise turn, -1 - anticlockwise turn
	global direction

	if not uturn:
		print "move forward"
        	speed(100)
	else:
		if rotation == 0:
			print "Detected wall in front. Ready to make an u-turn.."
                	u_turn(direction)
			direction = direction * -1	
		elif rotation == 1:
			print "At a corner. Detected walls in front and left. Ready to make an u-turn clockwise"
                	u_turn(rotation)
			direction = rotation * -1
		else:
			print "At a corner. Detected walls in front and right. Ready to make an u-turn anti-clockwise"
                	u_turn(rotation)
			direction = rotation * -1


if __name__ == '__main__':
	try:
		sensewalls()

	except KeyboardInterrupt:
		print "exiting......."
		speed(0)
		turn(0)
	except Exception, e:
		print e
