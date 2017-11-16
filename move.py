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
	step(float(sys.argv[1]),0,float(sys.argv[2]))


except KeyboardInterrupt:
  pass
except Exception, e:
  print e

speed(0)
turn(0)

robot.close()
