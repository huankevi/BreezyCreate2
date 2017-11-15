# Open the EF
#python servode.py to_goal --sg 5 600
python servode.py to_goal --sg 1 594 --sg 2 405 --sg 3 405
sleep 1
python servode.py to_goal --sg 4 256
sleep 1
# Close the EF
python servode.py to_goal --sg 5 600
# Allow the EF to close
sleep 1
# Move to ready position
python servode.py to_goal --sg 1 450 --sg 2 575 --sg 3 575 --sg 4 330 --sg 5 600
