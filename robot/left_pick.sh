#Ready position
#python servode.py to_goal --sg 1 450 --sg 2 575 --sg 3 575 --sg 4 330 --sg 5 600
# Goto desired location with EF open
# Offset = (1 @ +70) (2 & 3 @ -20) (4 @ +30)
#python servode.py to_goal --sg 1 572 --sg 2 397 --sg 3 397 --sg 4 229 --sg 5 600
python servode.py to_goal --sg 1 594 --sg 2 405 --sg 3 405 --sg 5 564
sleep 1
python servode.py to_goal --sg 4 256
sleep 1
# Close the EF
python servode.py to_goal --sg 5 700
# Allow the EF to close
sleep 1
# Move to ready position and not change the EF grip
python servode.py to_goal --sg 1 450 --sg 2 575 --sg 3 575 --sg 4 330
