import breezycreate2
import os
import time
from multiprocessing import Process, Queue
import signal


robot = breezycreate2.Robot(port='/dev/ttyUSB1')

speed = lambda value: robot.setForwardSpeed(value)
turn = lambda value: robot.setTurnSpeed(value)
sleep = lambda value: time.sleep(value)
direction = 1

def u_turn(direction):
	if direction > 0:
        	print "turn clockwise"
		step(0, 200, 1)
		step(100, 0, 2)
		step(0, 200, 1)
	else:
        	print "turn counter-clockwise"
		step(0, -200, 1)
		step(100, 0, 2)
		step(0, -200, 1)

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
	#while True:
	   print "=========================="
    	   print "Bumper center left value: %s" % robot.getLightBumperCenterLeft()
    	   #print "Bumper front left value: %s" % robot.getLightBumperFrontLeft()
    	   #print "Bumper left value: %s" %  robot.getLightBumperLeft()
    	   #print "=========================="
    	   print "Bumper center right value: %s" % robot.getLightBumperCenterRight()
    	   #print "Bumper front right value: %s" % robot.getLightBumperFrontRight()
    	   #print "Bumper right value: %s" %  robot.getLightBumperRight()
    	   print "=========================="
           	        
	   if robot.getLightBumperCenterLeft() > 80 or robot.getLightBumperCenterRight() > 80:
		q.put("stop")
		#speed(0)
	   else:
		q.put("move")
		#step(50, 0, 2)

   	except KeyboardInterrupt:
        	speed(0)
		break
   	except Exception, e:
		print e

def move(q):
   sleep(1)
   while True:
	try:
	   if q.get() == "stop":
		print "stop irobot"
		#speed(0)
		print "back away from the wall"
		#step(-50, 0, 3)
		speed(-200)
	   elif q.get() == "move":
		print "move forward"
		#step(50, 0, 3)
		speed(100)
	   else:
		print "OH NO! Stoppping"
		print "What is in the queue: %s" % q.get()
		speed(0)
	except KeyboardInterrupt:
		speed(0)
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
	process_one.terminate()
	process_two.terminate()
	while process_one.is_alive() and process_two.is_alive():
		print process_one.is_alive()
		print process_two.is_alive()
    except Exception, e:
  	print e
