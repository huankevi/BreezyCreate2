import breezycreate2
import os
import time
import sys
sys.setrecursionlimit(1500)
#from robot import robotarm
import rekog

robot = breezycreate2.Robot(port='/dev/ttyUSB1')

speed = lambda value: robot.setForwardSpeed(value)
turn = lambda value: robot.setTurnSpeed(value)
sleep = lambda value: time.sleep(value)

MELODY = [('A4',15,0.3),
         ('C5',45,2.2)]

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
        	step(100, 0, 1.7)
		if robot.getBumpers()[0] and robot.getBumpers()[1]:
			print "left and right bumpers on"
			step(-50, 0, 1.5)
		elif robot.getBumpers()[0]:
			print "left bumper on"
			step(-50, 0, 1.5)
			step(0, 50, 1.5)
		elif robot.getBumpers()[1]:
			print "right bumper on"	
			step(-50, 0, 1.5)
			step(0, -50, 1.5)
		else:
			pass
		speed(0)
		# read to take an image
		print("Taking an image")
	        #os.system(os.path.join(os.path.dirname(__file__), "robot", "wed_image_pos.sh"))	
		#sleep(10)
		#nose_location = rekog.call_rekog()
		#print "location of the nose is: %s" % nose_location
		# set arm to move position
                os.system(os.path.join(os.path.dirname(__file__), "robot", "move_position.sh"))
		#sleep(3)
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
		for triple in MELODY:
    			robot.playNote(triple[0], triple[1])
    			time.sleep(triple[2])	
		
		os.system(os.path.join(os.path.dirname(__file__), "robot", "move_position.sh"))
		sleep(0.9)
		sensewalls()

	except KeyboardInterrupt:
		print "exiting......."
		speed(0)
		turn(0)
	except Exception, e:
		print e
