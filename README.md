# Hogwarts lights controller

## Setup

### Flashing micropython
```bash
esptool.py --port /dev/tty.usbserial-1430 erase_flash
esptool.py --port /dev/tty.usbserial-1430 --baud 460800 write_flash --flash_size=detect 0 ./setup/esp8266-20191220-v1.12.bin
```

### Installing picoweb
On PC execute:
```bash
ampy -p /dev/tty.usbserial-1430 -b 115200 -d 2 put ./setup/picoweb
```

Then on device (in micropython REPL):
```python
upip.install('micropython-uasyncio')
upip.install('micropython-ulogging')
upip.install('micropython-pkg_resources')
upip.install('utemplate')
```

### Installing controller software
```bash
ampy -p /dev/tty.usbserial-1430 -b 115200 -d 2 put ./boot.py
ampy -p /dev/tty.usbserial-1430 -b 115200 -d 2 put ./main.py
ampy -p /dev/tty.usbserial-1430 -b 115200 -d 2 put ./wifi_credentials.txt
```

where `wifi_credentials.txt` is a text file containing your WiFi SSID and password each in new line.
