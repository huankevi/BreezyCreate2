import breezycreate2
import os
import time
from multiprocessing import Process, Queue
import rekog
import sys

robot = breezycreate2.Robot(port='/dev/ttyUSB0')

speed = lambda value: robot.setForwardSpeed(value)
turn = lambda value: robot.setTurnSpeed(value)
sleep = lambda value: time.sleep(value)

CELEB_NAME = "Andy Jassy"
WAKEUP_MELODY = [('A4',15,0.3),
         ('C5',45,2.2)]

BOWOUT_MELODY = [('C4',11,0.3),
            ('C4',11,0.3),
            ('C4',11,0.3),
            ('C4',32,0.7),
            ('G4',32,0.7),
            ('F4',11,0.3),
            ('E4',11,0.3),
            ('D4',11,0.3),
            ('C5',64,1.2),
            ('G4',40,0.7),
            ('F4',11,0.3),
            ('E4',11,0.3),
            ('D4',11,0.3),
            ('C5',64,1.2),
            ('G4',40,0.7),
            ('F4',11,0.3),
            ('E4',11,0.3),
            ('F4',11,0.3),
            ('D4',64,2) ]

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


def enterserach():
        step(100, 0, 3)
        speed(0)
        step(0, 50, 3.55)
        turn(0)

def exitsearch():
        step(0, 50, 2.35)
        turn(0)
        step(100, 0, 2.3)
        speed(0)
	os.system(os.path.join(os.path.dirname(__file__), "robot", "mic_drop.sh"))
        for triple in BOWOUT_MELODY:
                robot.playNote(triple[0], triple[1])
                time.sleep(triple[2])
	os.system(os.path.join(os.path.dirname(__file__), "robot", "move_position.sh"))
	
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
	    	#print "robot.getLightBumper() - right  %s" % robot.getLightBumper()[0]
        	#print "robot.getLightBumper() - center right  %s" % robot.getLightBumper()[1]
        	#print "robot.getLightBumper() - front right  %s" % robot.getLightBumper()[2]
        	#print "robot.getLightBumper() - front left  %s" % robot.getLightBumper()[3]
        	#print "robot.getLightBumper() - center left  %s" % robot.getLightBumper()[4]
        	#print "robot.getLightBumper() - left  %s" % robot.getLightBumper()[5]
		#print "-----------------------------------------"
		
		if robot.getBumpers()[0] or robot.getBumpers()[1]:
			q.put("stop")
                        speed(0)
			turn(0)
		elif(robot.getWallSeen() and robot.getLightBumper()[0] and robot.getLightBumper()[2]):
			q.put("stop")
			speed(0)
			turn(0)
		elif(robot.getLightBumper()[5] and robot.getLightBumper()[4] and robot.getLightBumper()[3] and not robot.getWallSeen()):
			q.put("stop")
			speed(0)
			turn(0)
	   	elif (robot.getLightBumper()[4] or robot.getLightBumper()[1]):
			q.put("stop")
			speed(0)
			turn(0)
	   	else:
			q.put("move")
			
   	except KeyboardInterrupt:
		break
   	except Exception, e:
		print e
		break

def move(q):
   while True:
	try:
		if q.get() == "stop":
                	print "Detected obstacle.."
                	speed(0)
			turn(0)
           	elif q.get() == "move":
                	print "searching..."
			step(65, 0, 2.9)
        		speed(0)
        		step(0, 11, 1.8)
        		turn(0)
			# read to take an image
        		print("Taking an image")
        		os.system(os.path.join(os.path.dirname(__file__), "robot", "wed_image_pos.sh"))
        		grab_status = rekog.align_X(CELEB_NAME)
        		if grab_status is None:
                		os.system(os.path.join(os.path.dirname(__file__), "robot", "move_position.sh"))
			else:
                		os.system(os.path.join(os.path.dirname(__file__), "robot", "move_position_grab.sh"))
				sleep(2)
				exitsearch()
				print "Done! Press Ctrl-C to quit the program"
				break
        		sleep(2)
		else:
			print "in else statement..."
                	continue
	except KeyboardInterrupt:
		break
   	except Exception, e:
		print e
		break

if __name__ == '__main__':
    try:

	for triple in WAKEUP_MELODY:
        	robot.playNote(triple[0], triple[1])
               	time.sleep(triple[2])
       	print "iRobot activated..."
        
	try:
        	CELEB_NAME = sys.argv[1]
        except IndexError:
                print "Usage: search.py \"<celebrity_name>\""
               	print "Default celebrity is Andy Jassy"
        
	print "Celerity Target: %s " % CELEB_NAME
        os.system(os.path.join(os.path.dirname(__file__), "robot", "move_position.sh"))
        sleep(2)
        enterserach()

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
