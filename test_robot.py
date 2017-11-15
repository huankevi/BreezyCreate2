import breezycreate2
import time
import sys, os
from robot import robotarm

try:
  #while True:
  robot_arm = robotarm.Robot()
  robot_arm.load_robot_profile(5,1023,400,400,100,1,1)
  robot_arm.set_arm_position(450,575,575,330,500)
  #time.sleep(5)
  #robot_arm.reset(5)
  robotarm.main()

except KeyboardInterrupt:
  pass
except Exception, e:
  print e

