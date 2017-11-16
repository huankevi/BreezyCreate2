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
		if sys.argv[1] == "left":
			
			step(0,-200,1)
		else:
			step(0,200,1)

except KeyboardInterrupt:
  pass
except Exception, e:
  print e

speed(0)
turn(0)

robot.close()
