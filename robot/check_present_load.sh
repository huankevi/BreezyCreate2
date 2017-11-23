#!/usr/bin/env bash

dir_robot="robot/"
if test -d "$dir_robot";
then
    cd $dir_robot
fi

python servode.py all_registers 5 2> present_load.out
cat present_load.out | awk '/present_load/ {print $NF}'
