import snowboydecoder
import subprocess
import os.path
import pyaudio
import wave
import time
import boto3
import servode

IMG_FILENAME = "/home/pi/image.jpg"
reko_client = boto3.client('rekognition')
polly_client = boto3.client('polly')

import apa102
import time
import threading
try:
    import queue as Queue
except ImportError:
    import Queue as Queue


DETECTOR_STATE = 0
FILENAME = "hello.wav"

def pickup_left():
	robotarm = Robot()
	robotarm.set_arm_position(594, 405, 405, 330, 500)
        time.sleep(1)
        robotarm.set_arm_position(594, 405, 405, 244, 500)
        time.sleep(1)
        # Close the EF
        robotarm.set_arm_position(594, 405, 405, 244, 330)
        time.sleep(2)
        # move back to ready position
        robotarm.set_arm_position(450, 575, 575, 330, 330)

def pickup_right():
	robotarm = Robot()
        robotarm.set_arm_position(470, 412, 412, 330, 500)
        time.sleep(1)
        robotarm.set_arm_position(470, 412, 412, 244, 500)
        time.sleep(1)
        # Close the EF
        robotarm.set_arm_position(470, 412, 412, 244, 340)
        time.sleep(2)
        # move back to ready position
        robotarm.set_arm_position(457, 575, 575, 330, 330)

def drop(direction):
    robotarm = Robot()
    if direction == "left":
        #os.system('./drop_left.sh')
        robotarm.set_arm_position(594, 405, 405, 330, 330)
        time.sleep(1)
        robotarm.set_arm_position(594, 405, 405, 244, 330)
        time.sleep(1)
        # open the EF
        robotarm.set_arm_position(594, 405, 405, 244, 500)
        time.sleep(2)
        # move back to ready position
        robotarm.set_arm_position(450, 575, 575, 330, 500)
    else:
        #os.system('./drop_right.sh')
        robotarm.set_arm_position(470, 412, 412, 330, 330)
        time.sleep(1)
        robotarm.set_arm_position(470, 412, 412, 244, 500)
        time.sleep(1)
        # Open the EF
        robotarm.set_arm_position(470, 412, 412, 244, 500)
        time.sleep(2)
        # move back to ready position
        robotarm.set_arm_position(457, 575, 575, 330, 500)	

#Records an audio snippet and sends to Lex, returns the matching slot value
def call_lex():
    os.system('sox -d -c 1 -r 16000 -e signed -b 16 hello.wav trim 0 5')

    lex = boto3.client('lex-runtime')
    recording = open(FILENAME, 'rb')
    resp = lex.post_content(botName="CelebrityPickupBot",botAlias="test", userId="anupam", contentType="audio/l16; rate=16000; channels=1", inputStream=recording)
    print(resp)
    if 'name' in resp['slots']:
        return resp['slots']['name']
    elif 'direction' in resp['slots']:
        return resp['slots']['direction']
    else:
        return None

def polly_speak(ssml_data):
    polly_response = polly_client.synthesize_speech(
        OutputFormat='mp3',
        Text= ssml_data,
        TextType='ssml',
        VoiceId='Justin',
    )
    audioFile = open('/home/pi/sound.mp3', 'w')
    audioFile.write(polly_response['AudioStream'].read())
    audioFile.close()
    os.system('madplay /home/pi/sound.mp3')

def find_nose_position(all_face_data, name):
    for face_data in all_face_data:
        if face_data['Name'] == name:
            for landmark in face_data['Face']['Landmarks']:
                if landmark['Type'] == "nose":
                    return landmark
    # If given name was not found return None
    return None

def get_celebrity_names(all_face_data):
    celebrity_names = []
    for face_data in all_face_data:
        celebrity_names.append(face_data['Name'])
    return celebrity_names


def detected_callback():
    detector.terminate()
    DETECTOR_STATE = 0
    print "yes, how may I help you"

    lex_result = call_lex()
    print("Name of celebrity detected as ", lex_result)

    print("Taking an image using Pycam now ")
    os.system('raspistill -o /home/pi/image.jpg')

    image_data = open(IMG_FILENAME, 'rb')
    print("Image taken, sending it to Rekognition now")
    resp = reko_client.recognize_celebrities(Image={'Bytes' : image_data.read()})
    print "======================================================================================="
    print resp

    jeff_nose = find_nose_position(resp['CelebrityFaces'],"Jeff Bezos")
    jassy_nose = find_nose_position(resp['CelebrityFaces'],"Andy Jassy")

    location = 0

    if lex_result.lower() == "Jeff Bezos".lower():
        location = jeff_nose
    else:
        location = jassy_nose

    print('location is', location)

    if location is None:
        response_not_found = "<speak><s>Could not find %s in the image </s></speak>" % (lex_result)
        print (response_not_found)
        main() 

    if jeff_nose is not None:
        print("Jeff nose is at X " , round(jeff_nose['X'],3), "and Y ", round(jeff_nose['Y'],3) )
    if jassy_nose is not None:
        print("Jassy nose is at X " , round(jassy_nose['X'],3), "and Y ", round(jassy_nose['Y'],3) )

    if(location['X']<0.5):
        pickup_left()
        print ("Trying to pickup Left object since location[X] is", location['X'] )
    else:
        pickup_right()
        print ("Trying to pickup Right object since location[X] is", location['X'] )

    print ("picked up")
    celebrity_names = get_celebrity_names(resp['CelebrityFaces'])
    celebrity_count = len(celebrity_names)
    generated_text = "<speak><s>I found %d celebrities in front of me </s> <s>Their names are </s><s> %s </s><s> I just picked %s as you asked me </s><s> Shall I put is back on left or right? </s> </speak> " % (celebrity_count, ", ".join(celebrity_names), lex_result)
    print generated_text
    polly_speak(generated_text)

    print ("tell the drop direction now...")
    #Call lex to check if the user says left or right
    lex_result = call_lex()
    if(lex_result == "left"):
        drop("left")
    else:
        drop("right")

    text_to_say = "<speak><s> That was fun, let's play again </s> </speak> "
    print text_to_say
    polly_speak(text_to_say)
    main()

#pixels = Pixels()
#detector = snowboydecoder.HotwordDetector("../MakerSpace/robot/Jarvis.pmdl", sensitivity=0.5, audio_gain=1)
detector = snowboydecoder.HotwordDetector(os.path.join(os.path.dirname(__file__), "Jarvis.pmdl"), sensitivity=0.5, audio_gain=1)

class Robot():
	
	def __init__(self):
		pass

	def load_robot_profile(self, sids, torque_limit, cw_slope, ccw_slope, speed, cw_margin, ccw_margin):
                self.sid = []
		for x in range(sids):
			self.sid.append(x+1)
		
                ## set torque to 1
                self.register = 'torque_enable'
		self.value = 1
                servode.write_register(self)
                
	        ## set torque_limit to 1023
                self.register = 'torque_limit'
                self.value = torque_limit
                servode.write_register(self)    
 
                ## set cw_compliance_slope to 400
                self.register = 'cw_compliance_slope'
		self.value = cw_slope 
		servode.write_register(self)    
    
		## set ccw_compliance_slope to 400
		self.register = 'ccw_compliance_slope'
		self.value = ccw_slope 
		servode.write_register(self)    
   
		## set moving_speed to 100
		self.register = 'moving_speed'
		self.value = speed
		servode.write_register(self)    
   
		## set cw_compliance_margin to 1
		self.register = 'cw_compliance_margin'
		self.value = cw_margin
		servode.write_register(self)    

		## set ccw_compliance_margin to 1
		self.register = 'ccw_compliance_margin'
		self.value = ccw_margin
		servode.write_register(self)    
	
	def set_arm_position(self, *argv):    

		# set ready position for robot arm
		self.sg = []
	        servox_pos = []
		array_pos = 0
		for arg in argv:
			servox_pos = [array_pos+1, arg]
                        self.sg.append(servox_pos)
			array_pos+=1
		servode.to_goal(self)
 
        def reset(self, sids):
		self.sid = []
		for x in range(sids):
			self.sid.append(x+1)
		self.register = 'torque_enable'
		self.value = 0
                servode.write_register(self)


def main():
	detector.start(detected_callback)
	main()

if __name__ == '__main__':

	# Initializing parameters (Note: servo2 and servo3 must have identical position)
 		
		robotarm = Robot()
		robotarm.load_robot_profile(5,1023,400,400,100,1,1)   
                robotarm.set_arm_position(450,575,575,330,500)
                
 
	# start program
		main()
   
