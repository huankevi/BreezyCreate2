#!/usr/bin/env bash
echo $PATH
echo $PYTHONPATH

python -m servode write_register torque_enable 1 --sid 1
#python -m servode write_register torque_enable 1 --sid 2
#python -m servode write_register torque_enable 1 --sid 3
#python -m servode write_register torque_enable 1 --sid 4
#python -m servode write_register torque_enable 1 --sid 5
#python -m servode write_register torque_limit 1023 --sid 1
#python -m servode write_register torque_limit 1023 --sid 2
#python -m servode write_register torque_limit 1023 --sid 3
#python -m servode write_register torque_limit 1023 --sid 4
#python -m servode write_register torque_limit 1023 --sid 5
#python -m servode write_register cw_compliance_slope 400 --sid 1
#python -m servode write_register cw_compliance_slope 400 --sid 2
#python -m servode write_register cw_compliance_slope 400 --sid 3
#python -m servode write_register cw_compliance_slope 400 --sid 4
#python -m servode write_register cw_compliance_slope 400 --sid 5
#python -m servode write_register ccw_compliance_slope 400 --sid 1
#python -m servode write_register ccw_compliance_slope 400 --sid 2
#python -m servode write_register ccw_compliance_slope 400 --sid 3
#python -m servode write_register ccw_compliance_slope 400 --sid 4
#python -m servode write_register ccw_compliance_slope 400 --sid 5
#python -m servode write_register moving_speed 100 --sid 1
#python -m servode write_register moving_speed 100 --sid 2
#python -m servode write_register moving_speed 100 --sid 3
#python -m servode write_register moving_speed 100 --sid 4
#python -m servode write_register moving_speed 100 --sid 5
#python -m servode write_register cw_compliance_margin 1 --sid 1
#python -m servode write_register cw_compliance_margin 1 --sid 2
#python -m servode write_register cw_compliance_margin 1 --sid 3
#python -m servode write_register cw_compliance_margin 1 --sid 4
#python -m servode write_register cw_compliance_margin 1 --sid 5
#python -m servode write_register ccw_compliance_margin 1 --sid 1
#python -m servode write_register ccw_compliance_margin 1 --sid 2
#python -m servode write_register ccw_compliance_margin 1 --sid 3
#python -m servode write_register ccw_compliance_margin 1 --sid 4
#python -m servode write_register ccw_compliance_margin 1 --sid 5
