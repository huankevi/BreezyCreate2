import robotarm
import time

irobot = robotarm.Robot(5,1023,400,400,100,1,1)
irobot.set_ready_position(450,575,575,330,600)
time.sleep(5)
irobot.reset(5)
#robotarm.main()
