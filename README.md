
## MakerSpace iRobot Create2 Project

#### Operating Instructions:

1. Clone the entire repo to your Raspberry Pi
2. Verify you have the following device files: `/dev/ttyUSB0` (USB to Serial iRobot interface) and `/dev/ttyACM0` (USB to TTL Dynamixel Servo Interface). If they appear to be different on your system, then update `search.py`, `rekog.py` and `robot/servode.py` to reflect the correct device filename.
3. Place the iRobot Create2 in the **center of the demo area**.
4. Run `ssh robot/load_gg_profile_maker_studio.sh` to set the initial configurations for Servos.
5. Run `python search.py "celebrity name"` e.g. `python search.py "Angelina Jolie"`

---

## BreezyCreate2
BreezyCreate2 provides a simple abstraction layer on top of the
<a href="https://github.com/pomeroyb/Create2Control">Create2API</a>
library by Brandon Pomeroy, suitable for use by beginning Python programmers.
BreezyCreate2 uses the standard Python distutils
to install the Python module breezycreate2 and the JSON file required by
Create2API.  I have tested it with Python 2.7 and 3.5.

Once you've installed BreezyCreate2, you can access its sole
class, the <tt>Robot</tt> class, which has easy methods for interacting with the robot: <tt>setForwardSpeed</tt>,
<tt>playNote</tt>,  <tt>getBumpers</tt>, etc. (See the <tt>robotest.py</tt> script for an example.)

#### More interacting methods:

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
