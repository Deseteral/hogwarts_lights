#!/bin/sh
set -e

source ./setup/set_vars.sh

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

source ./setup/flash_app_code.sh

echo "DONE."
