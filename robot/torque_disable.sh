#!/usr/bin/env bash

dir_robot="robot/"
if test -d "$dir_robot";
then
    cd $dir_robot
fi

python servode.py write_register torque_enable 0 --sid 1
python servode.py write_register torque_enable 0 --sid 2
python servode.py write_register torque_enable 0 --sid 3
python servode.py write_register torque_enable 0 --sid 4
python servode.py write_register torque_enable 0 --sid 5
