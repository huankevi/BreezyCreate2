#!/usr/bin/env bash

dir_robot="robot/"
if test -d "$dir_robot";
then
    cd $dir_robot
fi

python servode.py to_goal --sg 1 512 --sg 2 600 --sg 3 600 --sg 4 150 --sg 5 333
