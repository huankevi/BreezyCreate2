
## MakerSpace iRobot Create2 Project

#### Operating Instructions:

1. Clone the entire repo to your Raspberry Pi
2. Verify you have the following device files: `/dev/ttyUSB0` (USB to Serial iRobot interface) and `/dev/ttyACM0` (USB to TTL Dynamixel Servo Interface). If they appear to be different on your system, then update `search.py`, `rekog.py` and `robot/servode.py` to reflect the correct device filename.
3. Run `ssh robot/load_gg_profile_maker_studio.sh` to set the initial configurations for Servos.

Testing Rekognition capability:
4. Run `python rekog.py "celebrity name"` e.g. `python rekog.py "Angelina Jolie"`

Testing Roomba + Rekognition capability: 
5. Place the iRobot Create2 in the **center of the demo area**.
6. Run `python search.py "celebrity name"` e.g. `python search.py "Angelina Jolie"`

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
