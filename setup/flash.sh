#!/bin/sh
set -e

PORT='/dev/tty.usbserial-1430'
BAUD='115200'

echo '    [performing erase_flash]'
esptool.py --port $PORT erase_flash
echo ''

echo '    [flashing micropython]'
esptool.py --port $PORT --baud $BAUD write_flash --flash_size=detect 0 ./setup/micropython_esp8266-20191220-v1.12.bin
echo ''

echo '    [setting up WiFi connection]'
ampy -p $PORT -b $BAUD -d 2 put ./boot.py
ampy -p $PORT -b $BAUD -d 2 put ./wifi_credentials.txt
echo ''

echo '    [installing picoweb]'
ampy -p $PORT -b $BAUD -d 2 put ./setup/picoweb
echo ''

echo '    [installing picoweb deps]'
echo "    [press ctrl+X after installation is done]\n"
rshell -f ./setup/install_micropython_deps.rshell
echo ''

echo '    [flashing app code]'
ampy -p $PORT -b $BAUD -d 2 put ./main.py
echo ''

echo '    [reseting board]'
rshell -f ./setup/reset_board.rshell

echo "DONE."
