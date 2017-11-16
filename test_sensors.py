import breezycreate2
import time

robot = breezycreate2.Robot(port='/dev/ttyUSB1')

speed = lambda value: robot.setForwardSpeed(value)
turn = lambda value: robot.setTurnSpeed(value)
sleep = lambda value: time.sleep(value)

def step(speed_val, turn_val, time_val):
  if speed_val:
    turn(0)
    speed(speed_val)
  else:
    speed(0)
    turn(turn_val)
  sleep(time_val)
  
try:
  i = 0
  while True:
	print "robot.getLightBumperLeft(): %s | robot.getLightBumperRight(): %s" % (robot.getLightBumperLeft(), robot.getLightBumperRight())
	print "robot.getLightBumperFrontLeft(): %s | robot.getLightBumperFrontRight(): %s" % (robot.getLightBumperFrontLeft(), robot.getLightBumperFrontRight())
	print "robot.getLightBumperCenterLeft(): %s | robot.getLightBumperCenterRight(): %s" % (robot.getLightBumperCenterLeft(), robot.getLightBumperCenterRight())
	print "-----------------------------------------"

	print "robot.getWallSensor(): %s" % robot.getWallSensor()
	print "robot.getWallSeen(): %s" % robot.getWallSeen()
	#print robot.getLightBumper()
#	print "robot.getLightBumper() - right  %s" % robot.getLightBumper()[0]
#	print "robot.getLightBumper() - center right  %s" % robot.getLightBumper()[1]
#	print "robot.getLightBumper() - front right  %s" % robot.getLightBumper()[2]
#	print "robot.getLightBumper() - front left  %s" % robot.getLightBumper()[3]
#	print "robot.getLightBumper() - center left  %s" % robot.getLightBumper()[4]
#	print "robot.getLightBumper() - left  %s" % robot.getLightBumper()[5]

	print "robot.getBumpers() - left %s" % robot.getBumpers()[0]
	print "robot.getBumpers() - right %s" % robot.getBumpers()[1]

#	
	sleep(3)
except KeyboardInterrupt:
  pass
except Exception, e:
  print e

speed(0)
#turn(0)

robot.close()
