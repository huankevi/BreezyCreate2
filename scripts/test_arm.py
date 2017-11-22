import boto3
import os
import breezycreate2
import time
import picamera

IMG_FILENAME = "image.jpg"
reko_client = boto3.client('rekognition')

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

#os.system("robot/torque_disable.sh")
#os.system("robot/load_gg_profile_maker_studio.sh")
#sleep(2)
os.system("robot/move_position.sh")
sleep(2)
os.system("robot/wed_image_pos.sh")
#sleep(1)

#print os.path.join(os.path.dirname(__file__), "robot", "pick_position.sh")
#os.system(os.path.join(os.path.dirname(__file__), "robot", "pick_position.sh"))



