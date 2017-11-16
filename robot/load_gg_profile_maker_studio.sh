#!/usr/bin/env bash

dir_robot="robot/"
if test -d "$dir_robot";
then
    cd $dir_robot
fi

python servode.py write_register torque_enable 1 --sid 1
python servode.py write_register torque_enable 1 --sid 2
python servode.py write_register torque_enable 1 --sid 3
python servode.py write_register torque_enable 1 --sid 4
python servode.py write_register torque_enable 1 --sid 5
python servode.py write_register torque_limit 1023 --sid 1
python servode.py write_register torque_limit 1023 --sid 2
python servode.py write_register torque_limit 1023 --sid 3
python servode.py write_register torque_limit 1023 --sid 4
python servode.py write_register torque_limit 1023 --sid 5
python servode.py write_register cw_compliance_slope 400 --sid 1
python servode.py write_register cw_compliance_slope 400 --sid 2
python servode.py write_register cw_compliance_slope 400 --sid 3
python servode.py write_register cw_compliance_slope 400 --sid 4
python servode.py write_register cw_compliance_slope 400 --sid 5
python servode.py write_register ccw_compliance_slope 400 --sid 1
python servode.py write_register ccw_compliance_slope 400 --sid 2
python servode.py write_register ccw_compliance_slope 400 --sid 3
python servode.py write_register ccw_compliance_slope 400 --sid 4
python servode.py write_register ccw_compliance_slope 400 --sid 5
python servode.py write_register moving_speed 100 --sid 1
python servode.py write_register moving_speed 100 --sid 2
python servode.py write_register moving_speed 100 --sid 3
python servode.py write_register moving_speed 100 --sid 4
python servode.py write_register moving_speed 100 --sid 5
python servode.py write_register cw_compliance_margin 1 --sid 1
python servode.py write_register cw_compliance_margin 1 --sid 2
python servode.py write_register cw_compliance_margin 1 --sid 3
python servode.py write_register cw_compliance_margin 1 --sid 4
python servode.py write_register cw_compliance_margin 1 --sid 5
python servode.py write_register ccw_compliance_margin 1 --sid 1
python servode.py write_register ccw_compliance_margin 1 --sid 2
python servode.py write_register ccw_compliance_margin 1 --sid 3
python servode.py write_register ccw_compliance_margin 1 --sid 4
python servode.py write_register ccw_compliance_margin 1 --sid 5
