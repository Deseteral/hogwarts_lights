#!/bin/sh
set -e

source ./setup/set_vars.sh

echo '    [flashing app code]'
ampy -p $PORT -b $BAUD -d 2 put ./main.py
echo ''

echo '    [reseting board]'
rshell -f ./setup/reset_board.rshell
