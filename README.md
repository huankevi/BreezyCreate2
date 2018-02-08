
## MakerSpace iRobot Create2 Project

#### Operating Instructions:

1. Clone the entire repo to your Raspberry Pi
2. Verify you have the following device files: `/dev/ttyUSB0` (USB to Serial iRobot interface) and `/dev/ttyACM0` (USB to TTL Dynamixel Servo Interface). If they appear to be different on your system, then update `search.py`, `rekog.py` and `robot/servode.py` to reflect the correct device filename.
3. From the command line, run `sh robot/load_gg_profile_maker_studio.sh` to set the initial configurations for Servos.

###### Testing Rekognition capability:
4. From the command line, run `sh robot/wed_image_pos.sh` to prepare the robotic arm for taking an image
5. Place the celebrity face object beneath the camera to the left as shown in the image below:

![Optional Text](../master/image_taking_pos.jpg)

6. From the command line, run `python rekog.py "celebrity name"` e.g. `python rekog.py "Angelina Jolie"`

###### Testing iRobot Create2 unit + Rekognition capability:

7. Place the roomba unit in the **center of the demo area**.
8. From the command line, run `python search.py "celebrity name"` e.g. `python search.py "Angelina Jolie"`
9. The roomba unit will travel a fixed distance before it came to a stop. The robotic arm will then be extended out and ready to take an image
10. Place the celebrity face object beneath the camera to the left as shown in the image above.

---

#### BreezyCreate2 - Added functions:

`getWallSeen` - returns a boolean (true | false) when wall sensor value reaches above certain value

`getBatteryTemperature` - returns the temperature of Roomba’s battery in degrees Celsius.   

`getLightBumper` - returns a boolean (true | false) when one or more light bumper sensors reaches above certain value

`getLightBumperFrontLeft` - returns the strength of the light bump front left signal.

`getLightBumperCenterLeft` - returns the strength of the light bump center left signal.

`getLightBumperLeft` - returns the strength of the light bump left signal.

`getLightBumperFrontRight` - returns the strength of the light bump front right signal.

`getLightBumperCenterRight` - returns the strength of the light bump center right signal.

`getLightBumperRight` - returns the strength of the light bump right signal.

`getBatteryCharge` - returns the current charge of Roomba’s battery in milliamp-hours (mAh). The charge value decreases as the battery is depleted during running and increases when the battery is charged.

`getDistance` - Returns the distance that Roomba has traveled in millimeters since the distance it was last requested is sent as a signed 16-bit value, high byte first
