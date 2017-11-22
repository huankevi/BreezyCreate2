import breezycreate2
import time

robot = breezycreate2.Robot(port='/dev/ttyUSB1')

speed = lambda value: robot.setForwardSpeed(value)
turn = lambda value: robot.setTurnSpeed(value)
sleep = lambda value: time.sleep(value)

def u_turn(direction):
	if direction > 0:
                print "trying to turn clockwise"
		step(0, 200, 1)
		step(100, 0, 3)
		step(0, 200, 1)
	else:
                print "trying to turn anti-clockwise"
		step(0, -200, 1)
		step(100, 0, 3)
		step(0, -200, 1)
		


def step(speed_val, turn_val, time_val):
  if speed_val:
    turn(0)
    speed(speed_val)
  else:
    speed(0)
    turn(turn_val)
  sleep(time_val)
  
#u_turn(1)
try:
  direction = 1
  is_turn = 0;
  while True:
    step(100, 0, 3)
    print "Ready to take a photo"
    sleep(1)
    print robot.getWallSensor() 
    
    step(0, -100, 1)
    print "turned to see sensor value"
    if robot.getWallSensor() > 0:
        print "detected a wall"
        print robot.getWallSensor() 
        step(0, 100, 1)
	direction = direction * -1	
        u_turn(direction)
	is_turn = 1
    if is_turn == 0:
    	step(0, 100, 1)
        print "turning back to normal path"
    else:
	is_turn = 0
    #step(0, 100, 1)
    #step(0, -100, 2)
    #step(0, 100, 1)
    #step(-200, 0, 1.5)
    #step(0, 0, .5)
except KeyboardInterrupt:
  pass
except Exception, e:
  print e

speed(0)
turn(0)

robot.close()
