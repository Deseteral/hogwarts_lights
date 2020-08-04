import network

cred_f = open('wifi_credentials.txt')
wifi_credentials = cred_f.read().split('\n');

sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
    print('connecting to network...')
    sta_if.active(True)
    sta_if.connect(wifi_credentials[0], wifi_credentials[1])
    while not sta_if.isconnected():
        pass
print('network config: ', sta_if.ifconfig())
