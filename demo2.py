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
		step(0, 250, 1)
		step(100, 0, 1.5)
		step(0, 155, 1)
	else:
        	print "u-turn counter-clockwise"
		step(0, -200, 1)
		step(100, 0, 1.5)
		step(0, -165, 1)

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
		print "robot.getLightBumperLeft(): %s | robot.getLightBumperRight(): %s" % (robot.getLightBumperLeft(), robot.getLightBumperRight())
	    	print "robot.getLightBumperFrontLeft(): %s | robot.getLightBumperFrontRight(): %s" % (robot.getLightBumperFrontLeft(), robot.getLightBumperFrontRight())
	    	print "robot.getLightBumperCenterLeft(): %s | robot.getLightBumperCenterRight(): %s" % (robot.getLightBumperCenterLeft(), robot.getLightBumperCenterRight())
	    	print "-----------------------------------------"

	   	if (robot.getLightBumperCenterLeft() > 90 or robot.getLightBumperCenterRight() > 90):
			print "stop!!!"
			q.put("stop")
			sleep(3.5)
	   	else:
			print "move!!!"
			q.put("move")
   	except KeyboardInterrupt:
		break
   	except Exception, e:
		print e

def move(q):
   #sleep(1)
   direction = -1
   while True:
	try:
	   if q.get() == "stop":
		speed(0)
		print "stop irobot"
		u_turn(direction)
		direction = direction * -1
	   elif q.get() == "move":
		print "move forward"
		speed(100)
		#speed(0)
		# take an image
		# sleep (x)
	   else:
		speed(0)
		print "STOP!!!! Turn around..."
		if q.get() == "stop":
			u_turn(direction)
                	direction = direction * -1
		else:
			print "what is in queue 1: %s" % q.get()
			print "What is in the queue 2: %s" % q.get()
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
	process_one.terminate()
	process_two.terminate()
	while process_one.is_alive() and process_two.is_alive():
		speed(0)
		turn(0)
		print process_one.is_alive()
		print process_two.is_alive()
    except Exception, e:
  	print e
