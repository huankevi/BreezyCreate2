import breezycreate2
import time
import sys
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
	print sys.argv[1]
	distance = float(sys.argv[1]) * 1.5
	#step(100,0,1.25)
	step(100,0,distance)


except KeyboardInterrupt:
  pass
except Exception, e:
  print e

speed(0)
turn(0)

robot.close()
