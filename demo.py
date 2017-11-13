import breezycreate2
import os
import time
from multiprocessing import Process, Queue
import signal


robot = breezycreate2.Robot(port='/dev/ttyUSB1')

speed = lambda value: robot.setForwardSpeed(value)
turn = lambda value: robot.setTurnSpeed(value)
sleep = lambda value: time.sleep(value)

def u_turn(d):
	if d > 0:
        	print "u-turn clockwise"
		step(0, 190, 1)
		step(80, 0, 2)
		step(0, 100, 0.5)
	else:
        	print "u-turn counter-clockwise"
		step(0, -190, 1)
		step(80, 0, 2)
		step(0, -100, 0.5)

def step(speed_val, turn_val, time_val):
  if speed_val:
    turn(0)
    speed(speed_val)
  else:
    speed(0)
    turn(turn_val)
  sleep(time_val)

def sensewalls(q):
   while True:
   	try:
		#print "robot.getLightBumperLeft(): %s | robot.getLightBumperRight(): %s" % (robot.getLightBumperLeft(), robot.getLightBumperRight())
	    	#print "robot.getLightBumperFrontLeft(): %s | robot.getLightBumperFrontRight(): %s" % (robot.getLightBumperFrontLeft(), robot.getLightBumperFrontRight())
	    	#print "robot.getLightBumperCenterLeft(): %s | robot.getLightBumperCenterRight(): %s" % (robot.getLightBumperCenterLeft(), robot.getLightBumperCenterRight())
	    	print "robot.getLightBumper() - right  %s" % robot.getLightBumper()[0]
        	print "robot.getLightBumper() - center right  %s" % robot.getLightBumper()[1]
        	print "robot.getLightBumper() - front right  %s" % robot.getLightBumper()[2]
        	print "robot.getLightBumper() - front left  %s" % robot.getLightBumper()[3]
        	print "robot.getLightBumper() - center left  %s" % robot.getLightBumper()[4]
        	print "robot.getLightBumper() - left  %s" % robot.getLightBumper()[5]
		print "-----------------------------------------"

		if(robot.getWallSeen() and robot.getLightBumper()[0] and robot.getLightBumper()[2]):
			#print "Stop at a corner. Wall front and right" 
			q.put("stop_turn_anticlockwise")
			speed(0)
			sleep(3.5)
		elif(robot.getLightBumper()[5] and robot.getLightBumper()[4] and robot.getLightBumper()[3] and not robot.getWallSeen()):
			#print "Stop at a corner. Wall front and Left"
			q.put("stop_turn_clockwise")
			speed(0)
			sleep(3.5)
	   	elif (robot.getLightBumper()[4] or robot.getLightBumper()[1]):
			#print "Stop. Wall front."
			q.put("stop")
			speed(0)
			sleep(3.5)
	   	else:
			#print "move!!!"
			q.put("move")
   	except KeyboardInterrupt:
		break
   	except Exception, e:
		print e

def move(q):
   direction = -1
   while True:
	try:
	   if q.get() == "stop":
		print "Detected wall in front. Ready to make an u-turn.."
		u_turn(direction)
		direction = direction * -1
	   elif q.get() == "stop_turn_clockwise":
		print "At a corner. Detected walls in front and left. Ready to make an u-turn clockwise"		
		u_turn(1)
		direction = -1
	   elif q.get() == "stop_turn_anticlockwise":
                print "At a corner. Detected walls in front and right. Ready to make an u-turn anti-clockwise"
                u_turn(-1)
                direction = 1
	   elif q.get() == "move":
		print "move forward"
		speed(100)
		#speed(0)
		# take an image
		# sleep (x)
	   else:
		print "in else statement..."
		continue
	except KeyboardInterrupt:
		break
   	except Exception, e:
        	print e

if __name__ == '__main__':
    try:
    	q = Queue()
    	process_one = Process(target=sensewalls, args=(q,))
    	process_two = Process(target=move, args=(q,))
    	process_one.start()
    	process_two.start()

    	q.close()
    	q.join_thread()

    	process_one.join()
    	process_two.join()

    except KeyboardInterrupt:
	print "exiting......."
	speed(0)
	turn(0)
	process_one.terminate()
	process_two.terminate()
	while process_one.is_alive() and process_two.is_alive():
		speed(0)
		turn(0)
		print process_one.is_alive()
		print process_two.is_alive()
    except Exception, e:
  	print e
