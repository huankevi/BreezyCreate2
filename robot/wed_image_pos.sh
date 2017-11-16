#!/usr/bin/env bash

dir_robot="robot/"
if test -d "$dir_robot";
then
    cd $dir_robot
fi

python servode.py to_goal --sg 1 442 --sg 2 429 --sg 3 425 --sg 4 536 --sg 5 400
