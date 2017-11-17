import boto3
import os
import breezycreate2
import time
import picamera
import sys

IMG_FILENAME = "image.jpg"
reko_client = boto3.client('rekognition')
robot = breezycreate2.Robot(port='/dev/ttyUSB1')

speed = lambda value: robot.setForwardSpeed(value)
turn = lambda value: robot.setTurnSpeed(value)
sleep = lambda value: time.sleep(value)

X_LOWER = 0.38
X_UPPER = 0.43
Y_LOWER = 0.69
Y_UPPER = 0.73

def step(speed_val, turn_val, time_val):
  if speed_val:
    turn(0)
    speed(speed_val)
  else:
    speed(0)
    turn(turn_val)
  sleep(time_val)

def find_nose_position(all_face_data, name):
    for face_data in all_face_data:
        if face_data['Name'] == name:
            for landmark in face_data['Face']['Landmarks']:
                if landmark['Type'] == "nose":
                    return landmark
    # If given name was not found return None
    return None

def take_image():
	print("Taking an image using Pycam now ")
	with picamera.PiCamera() as camera:
		camera.flash_mode = 'on'
		camera.resolution = (1296, 972)
		camera.capture('image.jpg')
		camera.close()
		

def call_rekog(celeb_name):
	location = 0
	take_image()
	image_data = open("./image.jpg", 'rb')
	print("Celebrity %s image taken, sending it to Rekognition now" % celeb_name)
	resp = reko_client.recognize_celebrities(Image={'Bytes' : image_data.read()})
	print resp
	celeb_nose = find_nose_position(resp['CelebrityFaces'],celeb_name)
	print('Nose location is', celeb_nose)
	return celeb_nose

def align_X(celeb_name):
	while True:
		try:
            		object_loc = call_rekog(celeb_name)
			#return None
			if object_loc is None:
				object_loc = call_rekog(celeb_name)
			print (object_loc['X'] )
                	print (object_loc['Y'] )
                	x_val = float(object_loc['X'])
                	#if x_val > 0.32 and x_val < 0.39:
                	if x_val > X_LOWER and x_val < X_UPPER:
                        	print "X is aligned"
                        	break
                	print('calculating x delta')
                	x_delta = x_val - 0.3
                	print x_delta
                	if abs(x_delta) < 0.05:
                        	break;
                	if x_delta > 0:
                        	step(0,100,x_delta)
                        	turn(0)
                	else:
                        	step(0,-100,(x_delta * -1))
                        	turn(0)
                except (RuntimeError, TypeError, NameError):
                        print "failed to identify the celebrity..."
                        return None

	print "--x is located--"
	while True:
		try:
			object_loc = call_rekog(celeb_name)
			if object_loc is None:
				object_loc = call_rekog(celeb_name)

			print (object_loc['X'] )
			print (object_loc['Y'] )
			y_val = float(object_loc['Y'])
			if y_val > Y_LOWER and y_val < Y_UPPER:
				print "Y is aligned"
				break
			print('calculating y delta')
			y_delta = y_val - 0.6
			print y_delta
			if abs(y_delta) < 0.05:
				break;
			if y_delta > 0:
				step(-100,0,y_delta*1)
				speed(0)
			else:
				step(100,0,y_delta * -1.8)
				speed(0)
		except Exception, e:
                        print "failed to identify the celebrity..."
                        return None

	print "--y is located--"
	while True:
		try:
            		object_loc = call_rekog(celeb_name)
			if object_loc is None:
				object_loc = call_rekog(celeb_name)
			print (object_loc['X'] )
			print (object_loc['Y'] )
			x_val = float(object_loc['X'])
			if x_val > X_LOWER and x_val < X_UPPER:
				print "X is aligned"
				break
			print('calculating x delta')
			x_delta = x_val - 0.3
			print x_delta
			if abs(x_delta) < 0.05:
				break;
			if x_delta > 0:
				step(0,100,x_delta)
				turn(0)
			else:
				step(0,-100,(x_delta * -1))
				turn(0)
		except Exception, e:
                        print "failed to identify the celebrity..."
                        return None

	final_location = call_rekog(celeb_name)
	print " -------- "
	print final_location
	print "done"
	step(100,0,0.25)
	speed(0)
	turn(0)
	os.system(os.path.join(os.path.dirname(__file__), "robot", "pick_position.sh"))

    # we need to detect if we have failed to pick up the object and action to take next

if __name__ == '__main__':
	align_X(sys.argv[1])
